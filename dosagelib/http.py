# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
import collections
import functools
import logging
import random
import time
from typing import Any
from urllib import parse, robotparser

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from . import configuration

# Default number of retries
MaxRetries = 3

# Factor for retry backoff (see urllib3.util.retry, this default means
# 2s, 4s, 8s)
RetryBackoffFactor = 2

# Default connection timeout
ConnectionTimeoutSecs = 60

logger = logging.getLogger(__name__)


class Session(requests.Session):
    """This session implements a very simple host-based throttling system: For
    each hostname we see, we keep a record on when is the earliest time we want
    to send the next request: If before sending a request this time isn't
    reached, we sleep a bit until the requirements are satisfied. By default,
    we only delay a random amount of at most 0.3sec - but some hosts might need
    longer delays.
    """
    def __init__(self) -> None:
        super().__init__()

        retry = Retry(MaxRetries, backoff_factor=RetryBackoffFactor)
        self.mount('http://', HTTPAdapter(max_retries=retry))
        self.mount('https://', HTTPAdapter(max_retries=retry))
        self.headers.update({'User-Agent': configuration.UserAgent})

        self.throttles: dict[str, RandomThrottle] = collections.defaultdict(
            lambda: RandomThrottle())
        self.host_options: dict[str, dict[Any, Any]] = {}

    def send(self, request, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = ConnectionTimeoutSecs

        hostname = parse.urlsplit(request.url).hostname
        self.throttles[hostname].delay()
        if hostname in self.host_options:
            kwargs.update(self.host_options[hostname])

        return super().send(request, **kwargs)

    def add_throttle(self, hostname: str, th_min, th_max):
        """Adds a new throttle for a host: Might overwrite the existing one.
        """
        self.throttles[hostname] = RandomThrottle(th_min, th_max)

    def add_host_options(self, hostname: str, options):
        """Adds custom options for a specific host: Might overwrite the existing one.
        """
        self.host_options[hostname] = options


class RandomThrottle:
    def __init__(self, th_min=0.0, th_max=0.3) -> None:
        self.th_min = th_min
        self.th_max = th_max
        self.next = time.time()

    def delay(self):
        d = self.next - time.time()
        if d > 0:
            time.sleep(d)
        self.next = time.time() + random.uniform(self.th_min, self.th_max)


def check_robotstxt(url: str, session: Session) -> None:
    """Check if robots.txt allows our user agent for the given URL.
    @raises: IOError if URL is not allowed
    """
    roboturl = _get_roboturl(url)
    rp = _get_robotstxt_parser(roboturl, session)
    if not rp.can_fetch(configuration.App, str(url)):
        raise IOError("%s is disallowed by %s" % (url, roboturl))


def _get_roboturl(url: str) -> str:
    """Get robots.txt URL from given URL."""
    pu = parse.urlsplit(url)
    return parse.urlunsplit((pu.scheme, pu.netloc, "/robots.txt", None, None))


@functools.lru_cache()
def _get_robotstxt_parser(url, session: Session) -> robotparser.RobotFileParser:
    """Get a RobotFileParser for the given robots.txt URL."""
    rp = robotparser.RobotFileParser()
    try:
        req = session.get(url)
    except Exception as e:
        # connect or timeout errors are treated as an absent robots.txt
        rp.allow_all = True
        logger.trace('GET %r caused exception: %s', url, e)
    else:
        if req.status_code >= 400:
            rp.allow_all = True
            logger.trace('GET %r caused HTTP error %i', url, req.status_code)
        elif req.status_code == 200:
            rp.parse(req.text.splitlines())
            logger.trace('GET %r successful, %i bytes', url, len(req.content))
            if rp.default_entry:
                # Filter default deny rules
                de = rp.default_entry
                de.rulelines = [rule for rule in de.rulelines if rule.allowance]
    return rp


# A default session for cookie and connection sharing
default_session = Session()

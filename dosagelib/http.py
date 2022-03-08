# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2020 Tobias Gruetzmacher
import collections
import random
import time

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.parse import urlparse

from .configuration import UserAgent

# Default number of retries
MaxRetries = 3

# Factor for retry backoff (see urllib3.util.retry, this default means
# 2s, 4s, 8s)
RetryBackoffFactor = 2

# Default connection timeout
ConnectionTimeoutSecs = 60


class Session(requests.Session):
    """This session implements a very simple host-based throttling system: For
    each hostname we see, we keep a record on when is the earliest time we want
    to send the next request: If before sending a request this time isn't
    reached, we sleep a bit until the requirements are satisfied. By default,
    we only delay a random amount of at most 0.3sec - but some hosts might need
    longer delays.
    """
    def __init__(self):
        super().__init__()

        retry = Retry(MaxRetries, backoff_factor=RetryBackoffFactor)
        self.mount('http://', HTTPAdapter(max_retries=retry))
        self.mount('https://', HTTPAdapter(max_retries=retry))
        self.headers.update({'User-Agent': UserAgent})

        self.throttles = collections.defaultdict(lambda: RandomThrottle())
        self.host_options = {}

    def send(self, request, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = ConnectionTimeoutSecs

        hostname = urlparse(request.url).hostname
        self.throttles[hostname].delay()
        if hostname in self.host_options:
            kwargs.update(self.host_options[hostname])

        return super(Session, self).send(request, **kwargs)

    def add_throttle(self, hostname, th_min, th_max):
        """Adds a new throttle for a host: Might overwrite the existing one.
        """
        self.throttles[hostname] = RandomThrottle(th_min, th_max)

    def add_host_options(self, hostname, options):
        """Adds custom options for a specific host: Might overwrite the existing one.
        """
        self.host_options[hostname] = options


class RandomThrottle(object):
    def __init__(self, th_min=0.0, th_max=0.3):
        self.th_min = th_min
        self.th_max = th_max
        self.next = time.time()

    def delay(self):
        d = self.next - time.time()
        if d > 0:
            time.sleep(d)
        self.next = time.time() + random.uniform(self.th_min, self.th_max)


# A default session for cookie and connection sharing
default_session = Session()

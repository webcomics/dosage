# -*- coding: utf-8 -*-
# Copyright (C) 2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .configuration import UserAgent

# Default number of retries
MaxRetries = 3

# Factor for retry backoff (see urllib3.util.retry, this default means
# 2s, 4s, 8s)
RetryBackoffFactor = 2

# Default connection timeout
ConnectionTimeoutSecs = 60


class Session(requests.Session):
    def __init__(self):
        super(Session, self).__init__()

        retry = Retry(MaxRetries, backoff_factor=RetryBackoffFactor)
        self.mount('http://', HTTPAdapter(max_retries=retry))
        self.mount('https://', HTTPAdapter(max_retries=retry))
        self.headers.update({'User-Agent': UserAgent})

    def send(self, request, **kwargs):
        if 'timeout' not in kwargs:
            kwargs['timeout'] = ConnectionTimeoutSecs
        return super(Session, self).send(request, **kwargs)


# A default session for cookie and connection sharing
default_session = Session()

# -*- coding: utf-8 -*-
# Copyright (C) 2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import gzip
import os.path
import re

try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache

from responses import add, GET, POST


_basedir = os.path.dirname(__file__)


def _file(name):
    return os.path.join(_basedir, 'responses', name)


@lru_cache()
def _content(name):
    with gzip.open(_file(name + '.html.gz'), 'r') as f:
        return f.read()


@lru_cache()
def _img():
    with open(_file('empty.png'), 'rb') as f:
        return f.read()


def xkcd():
    add(GET, 'https://xkcd.com/', _content('xkcd-1899'))
    for page in (302, 303, 1898, 1899):
        add(GET, 'https://xkcd.com/%i/' % page, _content('xkcd-%i' % page))
    add(GET, re.compile(r'https://imgs\.xkcd\.com/.*\.png'), _img(), content_type='image/png')


def bloomingfaeries():
    add(GET, 'http://www.bloomingfaeries.com/', _content('bf-home'))
    add(GET, 'http://www.bloomingfaeries.com/comic/public/bloomin-faeries-405/', _content('bf-405'))

    add(GET, re.compile(r'http://www\.bloomingfaeries\.com/.*\.jpg'), _img(), content_type='image/jpeg')

def zenpencils():
    add(GET, 'https://zenpencils.com/', _content('zp-home'))
    add(GET, 'https://zenpencils.com/comic/missing/', _content('zp-223'))
    add(GET, 'https://zenpencils.com/comic/lifejacket/', _content('zp-222'))
    add(GET, re.compile(r'https://cdn-zenpencils\.netdna-ssl\.com/wp-content/uploads/.*\.jpg'), _img(), content_type='image/jpeg')

def vote():
    add(POST, 'https://buildbox.23.gs/count/', '')

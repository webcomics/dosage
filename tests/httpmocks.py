# SPDX-License-Identifier: MIT
# Copyright (C) 2017-2019 Tobias Gruetzmacher
import gzip
import os.path
import re

from functools import lru_cache

from responses import add, GET


def _file(name):
    return os.path.join(os.path.dirname(__file__), 'responses', name)


@lru_cache()
def content(name):
    with gzip.open(_file(name + '.html.gz'), 'r') as f:
        return f.read()


@lru_cache()
def _img(name):
    with open(_file(name + '.png'), 'rb') as f:
        return f.read()


def page(url, pagename):
    add(GET, url, content(pagename))


def png(url, name='empty'):
    add(GET, url, _img(name), content_type='image/jpeg')


def jpeg(url, name='empty'):
    add(GET, url, _img(name), content_type='image/jpeg')


def xkcd():
    page('https://xkcd.com/', 'xkcd-1899')
    for num in (302, 303, 1898, 1899):
        page('https://xkcd.com/%i/' % num, 'xkcd-%i' % num)
    png(re.compile(r'https://imgs\.xkcd\.com/.*\.png'))

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2017 Tobias Gruetzmacher
import gzip
import os.path
import re
from functools import lru_cache

from responses import GET, add


def _file(name):
    return os.path.join(os.path.dirname(__file__), 'responses', name)


@lru_cache
def content(name, ext: str = 'html'):
    with gzip.open(_file(f'{name}.{ext}.gz'), 'r') as f:
        return f.read()


@lru_cache
def _img(name):
    with open(_file(name + '.png'), 'rb') as f:
        return f.read()


def page(url, pagename):
    add(GET, url, content(pagename))


def json(url, pagename):
    add(GET, url, content(pagename, 'json'))


def png(url, name='empty'):
    add(GET, url, _img(name), content_type='image/jpeg')


def jpeg(url, name='empty'):
    add(GET, url, _img(name), content_type='image/jpeg')


def xkcd():
    page('https://xkcd.com/', 'xkcd-1899')
    for num in (302, 303, 1898, 1899):
        page(f'https://xkcd.com/{num}/', f'xkcd-{num}')
    png(re.compile(r'https://imgs\.xkcd\.com/.*\.png'))

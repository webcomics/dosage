#!/usr/bin/env python
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get WebComicFactory comics and save the info in a JSON file for
further processing.
"""
from __future__ import absolute_import, division, print_function

import codecs
import sys
import os
import requests
from lxml import html

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa
from dosagelib.util import getPageContent
from scriptutil import (save_result, load_result, truncate_name, format_name)

json_file = __file__.replace(".py", ".json")


def find_first(session, url):
    try:
        data = html.document_fromstring(getPageContent(url, session))
        data.make_links_absolute(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return url
    firstlinks = data.cssselect('a.comic-nav-first')
    if not firstlinks:
        print("INFO No first link on »%s«, already first page?" % (url))
        return url
    return firstlinks[0].attrib['href']


def get_results():
    """Parse start page for supported comics."""
    res = {}
    url = 'http://www.thewebcomicfactory.com/'
    session = requests.Session()
    try:
        data = html.document_fromstring(getPageContent(url, session))
        data.make_links_absolute(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return {}

    for comicdiv in data.cssselect('div.ceo_thumbnail_widget'):
        comicname = comicdiv.cssselect('h2')[0]
        comiclink = comicdiv.cssselect('a')[0]
        comicurl = comiclink.attrib['href']
        name = format_name(comicname.text)
        if 'comic-color-key' in comicurl:
            continue
        comicurl = find_first(session, comicurl)
        res[name] = comicurl

    save_result(res, json_file)


def first_lower(x):
    return x[0].lower()


def print_results(args):
    """Print all comics."""
    min_comics, filename = args
    with codecs.open(filename, 'a', 'utf-8') as fp:
        data = load_result(json_file)
        for name, url in sorted(data.items(), key=first_lower):
            fp.write(u"\n\nclass %s(_WebcomicFactory):\n    firstStripUrl = %r\n" % (
                     truncate_name(name), str(url)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

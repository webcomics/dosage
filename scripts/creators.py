#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get a list of creators.com comics and save the info in a JSON file
for further processing.
"""
from __future__ import absolute_import, division, print_function

import codecs
import sys
import os

import requests
from lxml import html

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # noqa
from dosagelib.util import get_page
from dosagelib.scraper import get_scraperclasses
from scriptutil import (contains_case_insensitive, save_result, load_result,
                        truncate_name, format_name)

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
    'Doodles',  # no images
]


def handle_url(url, session, res):
    """Parse one listing page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = html.document_fromstring(get_page(url, session).text)
        data.make_links_absolute(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return

    for comicdiv in data.cssselect('ul.all-test li'):
        comiclink = comicdiv.cssselect('a')[0]
        comicurl = comiclink.attrib['href']
        name = format_name(comicdiv.cssselect('p strong')[0].text)
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name),
                  file=sys.stderr)
            continue

        res[name] = comicurl.rsplit('/', 1)[1]


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    sess = requests.Session()
    handle_url('https://www.creators.com/categories/comics/all', sess, res)
    handle_url('https://www.creators.com/categories/cartoons/all', sess, res)
    save_result(res, json_file)


def has_gocomics_comic(name):
    """Test if comic name already exists."""
    cname = "Gocomics/%s" % name
    for scraperclass in get_scraperclasses():
        lname = scraperclass.getName().lower()
        if lname == cname.lower():
            return True
    return False


def print_results(args):
    """Print comics."""
    min_comics, filename = args
    with codecs.open(filename, 'a', 'utf-8') as fp:
        for name, path in sorted(load_result(json_file).items()):
            lang = 'Es' if name.lower().endswith('spanish') else ''
            if has_gocomics_comic(name):
                fp.write(u'# %s has a duplicate in gocomics\n' %
                         truncate_name(name))
            else:
                fp.write(u"class %s(_Creators%s):\n    path = %r\n\n\n" %
                         (truncate_name(name), lang, path))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

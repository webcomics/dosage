#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get arcamax comics and save the info in a JSON file for further
processing.
"""
from __future__ import absolute_import, division, print_function

import codecs
import sys
import os

import requests
from lxml import html

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # noqa
from dosagelib.util import get_page
from dosagelib.scraper import get_scrapers
from scriptutil import (contains_case_insensitive, save_result, load_result,
                        truncate_name, format_name)

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
    "HagartheHorrible",  # better source available
]


def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = html.document_fromstring(get_page(url, session).text)
        data.make_links_absolute(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return

    for comiclink in data.cssselect('a.comic-icon'):
        path = comiclink.attrib['href']
        name = format_name(comiclink.attrib['title'])
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        res[name] = path.rsplit('/', 2)[1]
    if not res:
        print("ERROR:", "did not match any comics", file=sys.stderr)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    session = requests.Session()
    handle_url('http://www.arcamax.com/comics', session, res)
    save_result(res, json_file)


def find_dups(name):
    """Check if comic name already exists."""
    names = [
        ("Creators/%s" % name).lower(),
        ("DrunkDuck/%s" % name).lower(),
        ("GoComics/%s" % name).lower(),
        ("KeenSpot/%s" % name).lower(),
        ("ComicGenesis/%s" % name).lower(),
        ("SmackJeeves/%s" % name).lower(),
    ]
    for scraperobj in get_scrapers():
        lname = scraperobj.name.lower()
        if lname in names or lname == name.lower():
            return scraperobj.name
    return None


def first_lower(x):
    return x[0].lower()


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics, filename = args
    with codecs.open(filename, 'a', 'utf-8') as fp:
        data = load_result(json_file)
        for name, path in sorted(data.items(), key=first_lower):
            dup = find_dups(name)
            if dup is not None:
                fp.write(u"# %s has a duplicate in %s\n" % (name, dup))
            else:
                fp.write(u"\n\nclass %s(_Arcamax):\n    path = %r\n" % (
                    truncate_name(name), path))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

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
import re
import sys
import os

import requests

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))  # noqa
from dosagelib.util import get_page
from dosagelib.scraper import get_scraperclasses
from scriptutil import contains_case_insensitive, save_result, load_result, truncate_name, format_name

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(r'<li><a href="(/thefunnies/[^"]+)">([^<]+)</a>')

# names of comics to exclude
exclude_comics = [
    "HagartheHorrible",  # better source available
]


def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = get_page(url, session).text
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        shortname = match.group(1)
        name = format_name(match.group(2))
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        res[name] = shortname
    if not res:
        print("ERROR:", "did not match any comics", file=sys.stderr)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    session = requests.Session()
    handle_url('http://www.arcamax.com/comics', session, res)
    save_result(res, json_file)


def has_comic(name):
    """Check if comic name already exists."""
    names = [
        ("Creators/%s" % name).lower(),
        ("DrunkDuck/%s" % name).lower(),
        ("GoComics/%s" % name).lower(),
        ("KeenSpot/%s" % name).lower(),
        ("ComicGenesis/%s" % name).lower(),
        ("SmackJeeves/%s" % name).lower(),
    ]
    for scraperclass in get_scraperclasses():
        lname = scraperclass.getName().lower()
        if lname in names or lname == name.lower():
            return True
    return False


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics, filename = args
    with codecs.open(filename, 'a', 'utf-8') as fp:
        for name, shortname in sorted(load_result(json_file).items()):
            if name in exclude_comics:
                continue
            if has_comic(name):
                prefix = u'#'
            else:
                prefix = u''
            fp.write(u"%sadd(%r, %r)\n" % (prefix, str(truncate_name(name)),
                                           str(shortname)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

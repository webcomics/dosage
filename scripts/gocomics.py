#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get a list of gocomics and save the info in a JSON file for further
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
from scriptutil import contains_case_insensitive, format_name, save_result, load_result, truncate_name

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
        # "coming soon"
        "Angryprogrammer",
        "Guinness",
        "Jabberwoncky",
        "RandysRationale"
        "SignsOfOurTimes",
        "TheGagwriter",
        "Yaoyao",

        # duplicate
        "SaturdayMorningBreakfastCereal",
]


def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = html.document_fromstring(get_page(url, session).text)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return

    for comiclink in data.cssselect('a.alpha_list'):
        link = comiclink.attrib['href']
        name = format_name(comiclink.text)
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        res[name] = link


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> uri}
    res = {}
    session = requests.Session()
    handle_url('http://www.gocomics.com/features', session, res)
    handle_url('http://www.gocomics.com/explore/espanol', session, res)
    handle_url('http://www.gocomics.com/explore/editorial_list', session, res)
    handle_url('http://www.gocomics.com/explore/sherpa_list', session, res)
    save_result(res, json_file)


def first_lower(x):
    return x[0].lower()


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics, filename = args
    with codecs.open(filename, 'a', 'utf-8') as fp:
        data = load_result(json_file)
        for name, uri in sorted(data.items(), key=first_lower):
            if name in exclude_comics:
                print("Excluded " + name)
                continue
            fp.write(u"\n\nclass GC%s(_GoComics%s):\n    path = %r\n" % (
                truncate_name(name), 'Es' if 'espanol/' in uri else '',
                uri[1:]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

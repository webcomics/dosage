#!/usr/bin/env python
# Copyright (C) 2013 Bastian Kleineidam
"""
Script to get arcamax comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, asciify, unescape
from dosagelib.scraper import get_scrapers
from scriptutil import contains_case_insensitive, capfirst, save_result, load_result, truncate_name

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(r'<li><b><a href="(/thefunnies/[^"]+)">([^<]+)</a>')

# names of comics to exclude
exclude_comics = [
]


def handle_url(url, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data, baseUrl = getPageContent(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        shortname = match.group(1)
        name = unescape(match.group(2))
        name = asciify(name.replace('&', 'And').replace('@', 'At'))
        name = capfirst(name)
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", name, file=sys.stderr)
            continue
        res[name] = shortname
    if not res:
        print("ERROR:", "did not match any comics", file=sys.stderr)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    handle_url('http://www.arcamax.com/comics', res)
    save_result(res, json_file)


def has_comic(name):
    """Check if comic name already exists."""
    names = [
        ("Creators/%s" % name).lower(),
        ("DrunkDuck/%s" % name).lower(),
        ("GoComics/%s" % name).lower(),
        ("KeenSpot/%s" % name).lower(),
        ("SmackJeeves/%s" % name).lower(),
    ]
    for scraperclass in get_scrapers():
        lname = scraperclass.get_name().lower()
        if lname in names:
            return True
    return False


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    for name, shortname in sorted(load_result(json_file).items()):
        if name in exclude_comics:
            continue
        if has_comic(name):
            prefix = '#'
        else:
            prefix = ''
        print("%sadd(%r, %r)" % (prefix, str(truncate_name(name)), str(shortname)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

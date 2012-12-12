#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
"""
Script to get a list of creators.com comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, asciify, unescape, tagre
from scriptutil import contains_case_insensitive, capfirst

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(tagre("a", "href", r'(/comics/[^/]+)\.html') + r'<strong>([^<]+)</strong>')

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
        url = match.group(1)
        name = unescape(match.group(2))
        name = asciify(name.replace('&', 'And').replace('@', 'At'))
        name = capfirst(name)
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("WARN: skipping possible duplicate", name, file=sys.stderr)
            continue
        res[name] = url


def save_result(res):
    """Save result to file."""
    with open(json_file, 'wb') as f:
        json.dump(res, f, sort_keys=True)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    handle_url('http://www.creators.com/comics/cat-seeall.html', res)
    save_result(res)


def print_results(args):
    """Print comics."""
    with open(json_file, "rb") as f:
        comics = json.load(f)
    for name, url in sorted(comics.items()):
        if name in exclude_comics:
            continue
        print("add(%r, %r)" % (str(name), str(url)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

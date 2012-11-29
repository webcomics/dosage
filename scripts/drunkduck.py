#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
"""
Script to get drunkduck comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import tagre, getPageContent
from scriptutil import contains_case_insensitive

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
    "Twonks_and_Plonkers", # broken images, no real content
]


def handle_url(url, url_matcher, num_matcher, res):
    """Parse one search result page."""
    try:
        data, baseUrl = getPageContent(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        comicurl = match.group(1)
        name = comicurl[:-1].rsplit('/')[-1]
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("WARN: skipping possible duplicate", name, file=sys.stderr)
            continue
        if name in exclude_comics:
            continue
        # find out how many images this comic has
        end = match.end(1)
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR:", repr(data[end:end+300], file=sys.stderr))
            continue
        num = int(mo.group(1))
        res[name] = num


def save_result(res):
    """Save result to file."""
    with open(json_file, 'wb') as f:
        json.dump(res, f, sort_keys=True)


def get_results():
    """Parse all search result pages."""
    base = "http://www.drunkduck.com/search/?page=%d&search=&type=0&type=1&last_update="
    href = re.compile(tagre("a", "href", r'(/[^"]+/)', before="size24 yanone blue"))
    num = re.compile(r'(\d+) pages?</span>')
    # store info in a dictionary {name -> number of comics}
    res = {}
    # a search for an empty string returned 825 result pages
    result_pages = 825
    print("Parsing", result_pages, "search result pages...", file=sys.stderr)
    for i in range(1, result_pages + 1):
        print(i, file=sys.stderr, end=" ")
        handle_url(base % i, href, num, res)
    save_result(res)


def print_results(min_strips):
    """Print all comics that have at least the given number of minimum comic strips."""
    with open(json_file, "rb") as f:
        comics = json.load(f)
    for name, num in sorted(comics.items()):
        if name in exclude_comics:
            continue
        if num >= min_strips:
            print("add('%s')" % name)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(int(sys.argv[1]))
    else:
        get_results()

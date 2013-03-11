#!/usr/bin/env python
# Copyright (C) 2012-2013 Bastian Kleineidam
"""
Script to get a list of KeenSpot comics and save the info in a
JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, asciify, unescape, tagre
from dosagelib.scraper import get_scraperclasses
from scriptutil import contains_case_insensitive, capfirst, save_result, load_result, truncate_name, format_description

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(
  tagre("td", "onmouseover", r'([^"]+)') +
  tagre("a", "href", r'([^"]+\.keenspot\.com/)[^"]*') +
  r"(?:<b>)?([^<]+)(?:</b>)?</a>"
)
descurl_matcher = re.compile(r"(desc/[^']+\.html)")
desc_matcher = re.compile(r'</font><br>(.+)(?:</b>)?</td></tr>', re.DOTALL)

# names of comics to exclude
exclude_comics = [
]

# links to last valid strips
url_overrides = {
}

def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data, baseUrl = getPageContent(url, session)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        mo = descurl_matcher.search(match.group(1))
        desc = get_description(url + mo.group(1), session)
        comicurl = match.group(2)
        name = unescape(match.group(3))
        name = asciify(name.replace('&', 'And').replace('@', 'At'))
        name = capfirst(name)
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", name, file=sys.stderr)
            continue
        res[name] = (comicurl, desc)


def get_description(url, session):
    try:
        data, baseUrl = getPageContent(url, session)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return ""
    mo = desc_matcher.search(data)
    if not mo:
        print(data)
    return format_description(mo.group(1))


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    session = requests.Session()
    base = 'http://keenspot.com/'
    handle_url(base, session, res)
    save_result(res, json_file)


def has_comic(name):
    """Check if comic name already exists."""
    names = [
        ("Creators/%s" % name).lower(),
        ("GoComics/%s" % name).lower(),
        ("ComicGenesis/%s" % name).lower(),
    ]
    for scraperclass in get_scraperclasses():
        lname = scraperclass.getName().lower()
        if lname in names:
            return True
    return False


def print_results(args):
    """Print all comics."""
    for name, entry in sorted(load_result(json_file).items()):
        if name in exclude_comics:
            continue
        url, desc = entry
        if has_comic(name):
            prefix = '#'
        else:
            prefix = ''
        name = truncate_name(name).encode('utf-8')
        url = url.encode('utf-8')
        desc = desc.encode('utf-8')
        print("%sadd(%r, %r, %r)" % (prefix, name, url, desc))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

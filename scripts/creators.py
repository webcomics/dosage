#!/usr/bin/env python
# Copyright (C) 2012-2014 Bastian Kleineidam
"""
Script to get a list of creators.com comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import codecs
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, asciify, unescape, tagre
from dosagelib.scraper import get_scraperclasses
from scriptutil import contains_case_insensitive, capfirst, save_result, load_result, truncate_name

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(tagre("a", "href", r'(/comics/[^/]+)\.html') + r'<strong>([^<]+)</strong>')

# names of comics to exclude
exclude_comics = [
]

def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = getPageContent(url, session)
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
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        res[name] = url


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    session = requests.Session()
    handle_url('http://www.creators.com/comics/cat-seeall.html', session, res)
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
        for name, url in sorted(load_result(json_file).items()):
            if name in exclude_comics:
                continue
            if has_gocomics_comic(name):
                prefix = u'# duplicate of gocomics '
            else:
                prefix = u''
            fp.write(u"%sadd(%r, %r)\n" % (
              prefix, str(truncate_name(name)), str(url))
            )


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

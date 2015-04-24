#!/usr/bin/env python
# Copyright (C) 2012-2014 Bastian Kleineidam
"""
Script to get a list of gocomics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import codecs
import re
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import tagre, getPageContent, asciify, unescape
from scriptutil import contains_case_insensitive, capfirst, save_result, load_result, truncate_name

json_file = __file__.replace(".py", ".json")

#<a href="/shortname" class="alpha_list updated">name</a>
url_matcher = re.compile(tagre("a", "href", r'(/[^"]+)', after="alpha_list") + r"([^<]+)</a>")

# names of comics to exclude
exclude_comics = [
        "Angryprogrammer", # unavailable
        "Complex", # "coming soon"
        "Guinness", # "coming soon"
        "Jabberwoncky", # "coming soon"
        "KickyBrand", # unavailable
        "Penmanship", # unavailable
        "RandysRationale", # "coming soon"
        "SaturdayMorningBreakfastCereal", # duplicate
        "SignsOfOurTimes", # "coming soon"
        "TheGagwriter", # "coming soon"
        "Yaoyao", # "coming soon"
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
        shortname = match.group(1)
        name = unescape(match.group(2))
        name = asciify(name.replace('&', 'And').replace('@', 'At'))
        name = capfirst(name)
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        res[name] = shortname


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    session = requests.Session()
    handle_url('http://www.gocomics.com/features', session, res)
    handle_url('http://www.gocomics.com/explore/espanol', session, res)
    handle_url('http://www.gocomics.com/explore/editorial_list', session, res)
    handle_url('http://www.gocomics.com/explore/sherpa_list', session, res)
    save_result(res, json_file)


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics, filename = args
    with codecs.open(filename, 'a', 'utf-8') as fp:
        for name, shortname in sorted(load_result(json_file).items()):
            if name in exclude_comics:
                print("Excluded " + name)
                continue
            fp.write(u"add(%r, %r)\n" % (
              str(truncate_name(name)), str(shortname))
            )


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

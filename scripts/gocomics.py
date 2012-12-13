#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
"""
Script to get a list of gocomics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import tagre, getPageContent, asciify, unescape
from dosagelib.scraper import get_scrapers
from scriptutil import contains_case_insensitive, capfirst

json_file = __file__.replace(".py", ".json")

#<a href="/shortname" class="alpha_list updated">name</a>
url_matcher = re.compile(tagre("a", "href", r'(/[^"]+)', after="alpha_list") + r"([^<]+)</a>")

# names of comics to exclude
exclude_comics = [
    "FrikkFrakkAndFrank", # too few comics
    "Apocalypseharry", # too few comics
    "BatkidandBatrat", # too few comics
    "BETWEENTHELINES", # comic unavailable
    "Bonner", # missing page
    "Buster", # comic unavailabe
    "DALTONDOG", # comic unavailable
    "DellAndSteve", # too few comics
    "Dilbert", # redirect
    "InkeeDoodles", # comic unavailable
    "MaggiesComics", # too few comics
    "OfMiceandMud", # too few comics
    "OysterWar", # too few comics
    "PIGTIMES", # comic unavailable
    "PS", # comic unavailable
    "RichardsPoorAlmanac", # missing images
    "SherpaAid", # comic unavailable
    "SparComics", # comic unavailable
    "SurvivingSingle", # comic unavailable
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
            print("WARN: skipping possible duplicate", name, file=sys.stderr)
            continue
        res[name] = shortname


def save_result(res):
    """Save result to file."""
    with open(json_file, 'wb') as f:
        json.dump(res, f, sort_keys=True)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    handle_url('http://www.gocomics.com/features', res)
    handle_url('http://www.gocomics.com/explore/editorial_list', res)
    handle_url('http://www.gocomics.com/explore/sherpa_list', res)
    save_result(res)


def has_creators_comic(name):
    cname = "Creators/%s" % name
    for scraperclass in get_scrapers():
        lname = scraperclass.get_name().lower()
        if lname == cname.lower():
            return True
    return False


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    with open(json_file, "rb") as f:
        comics = json.load(f)
    for name, shortname in sorted(comics.items()):
        if name in exclude_comics:
            continue
        if has_creators_comic(name):
            prefix = '#'
        else:
            prefix = ''
        print("%sadd(%r, %r)" % (prefix, str(name), str(shortname)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
"""
Script to get keenspot comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import json
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, asciify, unescape, tagre
from dosagelib.scraper import get_scrapers
from scriptutil import contains_case_insensitive

json_file = __file__.replace(".py", ".json")

# <div class="comictitle"><strong><a target="_blank" onclick="pageTrackerCG._link('http://collegepros.comicgenesis.com'); return false;" href="http://collegepros.comicgenesis.com">Adventures of the College Pros</a>
url_matcher = re.compile(r'<div class="comictitle"><strong>' + tagre("a", "href", r'(http://[^"]+)') + r'([^<]+)</a>')
num_matcher = re.compile(r'Number of Days: (\d+)')

# names of comics to exclude
exclude_comics = [
    "JuvenileDiversion", # page moved
    "JustWeird", # page has 403 forbidden
    "MobileMadness", # page does not follow standard layout
    "KnightsOfTheNexus", # page does not follow standard layout
    "RogerAndDominic", # page does not follow standard layout
    "TheAvatar", # page does not follow standard layout
    "Michikomonogatari", # page does not follow standard layout
    "DungeonDamage", # page does not follow standard layout
    "SaveMeGebus", # page does not follow standard layout
    "BlueZombie", # broken page
    "BoomerExpress", # redirection to another page
    "FaultyLogic", # page does not follow standard layout
    "EarthRiser", # redirects to a new page
    "GoForIt", # page is gone
    "ACDeceptibotscomic", # no images

]

url_overrides = {
    # link to last valid strip
    "BallofYarn": "http://ballofyarn.comicgenesis.com/d/20020624.html",
}

def handle_url(url, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data, baseUrl = getPageContent(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        url = match.group(1) + '/'
        name = unescape(match.group(2))
        name = asciify(name.replace('&', 'And').replace('@', 'At'))
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("WARN: skipping possible duplicate", name, file=sys.stderr)
            continue
        # find out how many images this comic has
        end = match.end()
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR:", repr(data[end:end+300], file=sys.stderr))
            continue
        num = int(mo.group(1))
        res[name] = (url_overrides.get(name, url), num)


def save_result(res):
    """Save result to file."""
    with open(json_file, 'wb') as f:
        json.dump(res, f, sort_keys=True)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    base = 'http://guide.comicgenesis.com/Keenspace_%s.html'
    for c in '0ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        handle_url(base % c, res)
    save_result(res)


def has_comic(name):
    cname = ("Creators/%s" % name).lower()
    gname = ("GoComics/%s" % name).lower()
    for scraperclass in get_scrapers():
        lname = scraperclass.get_name().lower()
        if lname == cname or lname == gname:
            return True
    return False
 

def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics = int(args[0])
    with open(json_file, "rb") as f:
        comics = json.load(f)
    for name, entry in sorted(comics.items()):
        if name in exclude_comics:
            continue
        url, num = entry
        if num < min_comics:
            continue
        url = url.replace("comicgen.com", "comicgenesis.com")
        if has_comic(name):
            prefix = '#'
        else:
            prefix = ''
        print("%sadd(%r, %r)" % (prefix, str(name), str(url)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

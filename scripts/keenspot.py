#!/usr/bin/env python
# Copyright (C) 2012-2014 Bastian Kleineidam
"""
Script to get a list of KeenSpot comics and save the info in a
JSON file for further processing.
"""
from __future__ import print_function
import codecs
import re
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent, asciify, unescape, tagre, check_robotstxt
from dosagelib.scraper import get_scraperclasses
from scriptutil import contains_case_insensitive, capfirst, save_result, load_result, truncate_name

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(
  tagre("td", "onmouseover", r'([^"]+)') +
  tagre("a", "href", r'([^"]+\.keenspot\.com/)[^"]*') +
  r"(?:<b>)?([^<]+)(?:</b>)?</a>"
)

# names of comics to exclude
exclude_comics = [
    "BrawlintheFamily", # non-standard navigation
    "CrowScare", # non-standard navigation
    "Dreamless", # non-standard navigation
    "EV", # non-standard navigation
    "Exposure", # non-standard navigation
    "Flipside", # non-standard navigation
    "HerobyNight", # non-standard navigation
    "JadeWarriors", # non-standard navigation
    "LastBlood", # non-standard navigation
    "MysticRevolution", # non-standard navigation
    "NoRoomForMagic", # non-standard navigation
    "PunchanPie", # non-standard navigation
    "RoadWaffles", # non-standard navigation
    "Shadowbinders", # non-standard navigation
    "ShockwaveDarkside", # non-standard navigation
    "Supernovas", # non-standard navigation
    "Twokinds", # non-standard navigation
    "WisdomofMoo", # non-standard navigation
    "Yirmumah", # non-standard navigation
    "YouDamnKid", # non-standard navigation
]

# links to last valid strips
url_overrides = {
}

def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = getPageContent(url, session)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        comicurl = match.group(2)
        name = unescape(match.group(3))
        name = asciify(name.replace('&', 'And').replace('@', 'At'))
        name = capfirst(name)
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name), file=sys.stderr)
            continue
        try:
            if "/d/" not in comicurl:
                check_robotstxt(comicurl+"d/", session)
            else:
                check_robotstxt(comicurl, session)
        except IOError:
            print("INFO: robots.txt denied for keenspot", repr(name))
            continue
        res[name] = comicurl


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
    min_comics, filename = args
    with codecs.open(filename, 'a', 'utf-8') as fp:
        for name, entry in sorted(load_result(json_file).items()):
            if name in exclude_comics:
                continue
            url = entry
            if has_comic(name):
                prefix = u'#'
            else:
                prefix = u''
            name = truncate_name(name)
            fp.write(u"%sadd(%r, %r)\n" % (
              prefix, str(name), str(url))
            )


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

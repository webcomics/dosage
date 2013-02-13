#!/usr/bin/env python
# Copyright (C) 2013 Bastian Kleineidam
"""
Script to get arcamax comics and save the info in a JSON file for further processing.
"""
from __future__ import print_function
import re
import sys
import os
import requests
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from dosagelib.util import getPageContent
from dosagelib.scraper import get_scraperclasses
from scriptutil import contains_case_insensitive, save_result, load_result, truncate_name, format_name, format_description

json_file = __file__.replace(".py", ".json")

url_matcher = re.compile(r'<h3><a href="([^"]+)">')
desc_matcher = re.compile(r'<span class="subtext">(.*?)\[<a href', re.DOTALL)
num_matcher = re.compile(r'<b>Comics:</b> <span class="comicinfo">(\d+)</span>')
genre_matcher = re.compile(r'<b>Genre:</b> <span class="comicinfo">([^<]+)</span>')
activity_matcher = re.compile(r'<b>Activity status:</b> <span class="comicinfo">([^<]+)</span>')

# names of comics to exclude
exclude_comics = [
]


def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data, baseUrl = getPageContent(url, session)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return
    for match in url_matcher.finditer(data):
        comicurl = match.group(1)
        name = format_name(comicurl.split('.', 1)[0][7:])
        if name in exclude_comics:
            continue
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", name, file=sys.stderr)
            continue
        # find description
        end = match.end()
        mo = desc_matcher.search(data[end:])
        if not mo:
            print("ERROR matching description:", repr(data[end:end+300]), file=sys.stderr)
            continue
        desc = format_description(mo.group(1))
        # find out how many images this comic has
        mo = num_matcher.search(data[end:])
        if not mo:
            print("ERROR matching number:", repr(data[end:end+300]), file=sys.stderr)
            continue
        num = int(mo.group(1))
        # find genre
        mo = genre_matcher.search(data[end:])
        if not mo:
            print("ERROR matching genre:", repr(data[end:end+300]), file=sys.stderr)
            continue
        genre = mo.group(1)
        # find activity
        mo = activity_matcher.search(data[end:])
        if not mo:
            print("ERROR matching activity:", repr(data[end:end+300]), file=sys.stderr)
            continue
        active = mo.group(1).lower() == "active"
        res[name] = [
            comicurl, desc, num, genre, active
        ] 
    if not res:
        print("ERROR:", "did not match any comics", file=sys.stderr)


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    session = requests.Session()
    baseUrl = 'http://comicfury.com/search.php?search=1&webcomics=Search+for+webcomics&query=&worder=5&asc=1&incvi=1&incse=1&incnu=1&incla=1&all_ge=1&all_st=1&all_la=1&page='
    pages = 382
    for i in range(1, pages+1):
        url = baseUrl + str(i)
        handle_url(url, session, res)
    save_result(res, json_file)


def has_comic(name):
    """Check if comic name already exists."""
    names = [
        ("Creators/%s" % name).lower(),
        ("DrunkDuck/%s" % name).lower(),
        ("GoComics/%s" % name).lower(),
        ("KeenSpot/%s" % name).lower(),
        ("SmackJeeves/%s" % name).lower(),
        ("Arcamax/%s" % name).lower(),
    ]
    for scraperclass in get_scraperclasses():
        lname = scraperclass.get_name().lower()
        if lname in names:
            return True
    return False


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics = int(args[0])
    for name, entry in sorted(load_result(json_file).items()):
        if name in exclude_comics:
            continue
        url, desc, num, genre, active = entry
        if num < min_comics:
            continue
        if has_comic(name):
            prefix = '#'
        else:
            prefix = ''
        print("%sadd(%r, %r, %r) # %d" % (
          prefix, str(truncate_name(name)), str(url), desc, num
        ))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

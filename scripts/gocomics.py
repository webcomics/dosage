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
    "Adagio", # too few comics
    "AgentGates", # too few comics
    "Apocalypseharry", # too few comics
    "BatkidandBatrat", # too few comics
    "BETWEENTHELINES", # comic unavailable
    "Bonner", # missing page
    "Buster", # comic unavailabe
    "CarteBlanche", # missing images
    "Critterdoodles", # missing images
    "CountyLine", # too few comics
    "Crawdiddy", # comic unavailable
    "DALTONDOG", # comic unavailable
    "DellAndSteve", # too few comics
    "Dilbert", # redirect
    "DutchnPals", # too few comics
    "EclecticCartoons", # missing images
    "FlexandTone", # too few comics
    "FrikkFrakkAndFrank", # too few comics
    "GOODAndEVIL", # too few comics
    "GoodwithCoffee", # too few comics
    "InkeeDoodles", # comic unavailable
    "JoesBar", # missing images
    "KALEECHIKORNERS", # too few comics
    "LoveIs", # missing images
    "MaggiesComics", # too few comics
    "MagicCoffeeHair", # too few comics
    "NickGalifianakis", # too few comics
    "OfMiceandMud", # too few comics
    "OysterWar", # too few comics
    "Penguins", # too few comics
    "PIGTIMES", # comic unavailable
    "PS", # comic unavailable
    "Radiowave", # too few comics
    "RatchetAndSpin", # too few comics
    "RichardsPoorAlmanac", # missing images
    "SatchelandDuff", # too few comics
    "SherpaAid", # comic unavailable
    "Slowpoke", # comic moved
    "SpaghettiSandwich", # too few comics
    "SparComics", # comic unavailable
    "SurvivingSingle", # comic unavailable
    "TheBluckwells", # missing images
    "TheConjurers", # too few comics
    "TheDeadlys", # too few comics
    "TheNursesLockerRoom", # too few comics
    "Tomversation", # too few comics
    "VoicesInTheDark", # too few comics
    "WhatTheFrak", # too few comics
    "ZeekyZebraandCompany", # too few comics
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
    handle_url('http://www.gocomics.com/explore/editorial_list', session, res)
    handle_url('http://www.gocomics.com/explore/sherpa_list', session, res)
    save_result(res, json_file)


def print_results(args):
    """Print all comics that have at least the given number of minimum comic strips."""
    min_comics, filename = args
    with codecs.open(filename, 'a', 'utf-8') as fp:
        for name, shortname in sorted(load_result(json_file).items()):
            if name in exclude_comics:
                continue
            fp.write(u"add(%r, %r)\n" % (
              str(truncate_name(name)), str(shortname))
            )


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

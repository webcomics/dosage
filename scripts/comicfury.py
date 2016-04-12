#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get ComicFury comics and save the info in a JSON file for further
processing.
"""
from __future__ import absolute_import, division, print_function

import codecs
import sys
import os

import requests
from lxml import html

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # noqa
from dosagelib.util import get_page
from dosagelib.scraper import get_scraperclasses
from scriptutil import (contains_case_insensitive, save_result, load_result,
                        truncate_name, format_name)

# Absolute minumum number of pages a comic may have (restrict search space)
MIN_COMICS = 90

json_file = __file__.replace(".py", ".json")

# names of comics to exclude
exclude_comics = [
    # unsuitable navigation
    "AlfdisAndGunnora",
    "AnAmericanNerdinAnimatedTokyo",
    "AngryAlien",
    "BoozerAndStoner",
    "Bonejangles",
    "ConradStory",
    "Crossing",
    "ChristianHumberReloaded",
    "CorkandBlotto",
    "Democomix",
    "ErraticBeatComics",
    "EnergyWielders",
    "EvilBearorg",
    "Fiascos",
    "FateoftheBlueStar",
    "FPK",
    "Fanartgyle",
    "FrigginRandom",
    "GoodbyeKitty",
    "HighlyExperiMental",
    "IfAndCanBeFlowers",
    "JournalismStory",
    "JohnsonSuperior",
    "Keel",
    "JudgeDredBasset",
    "LomeathAndHuilii",
    "MNPB",
    "LucidsDream",
    "MadDog",
    "Minebreakers",
    "Moonlightvalley",
    "MyImmortalFool",
    "NATO",
    "NothingFits",
    "OptimisticFishermenandPessimisticFishermen",
    "Old2G",
    "NothingFitsArtBlog",
    "OutToLunchTheStingRayWhoreStory",
    "Pandemonium",
    "Pewfell",
    "ProjectX",
    "Ratantia",
    "RealLifeTrips",
    "Sandgate",
    "Secondpuberty",
    "Seconds",
    "SlightlyEccentricOrigins",
    "StardusttheCat",
    "StrangerthanFiction",
    "TalamakGreatAdventure",
    "TheBattalion",
    "TheDailyProblem",
    "TheMansionofE",
    "ThePainter",
    "TheSeekers",
    "TheTrialsofKlahadoftheAbyss",
    "TheStickmen",
    "ThornsInOurSide",
    "TopHeavyVeryBustyPinUpsForAdults",
    "USBUnlimitedsimulatedbody",
    "TylerHumanRecycler",
    "UAF",
    "WhenPigsFly",
    "YeOldeLegotimeTheatre",

    # no content
    "Angst",

    # images gone
    "BaseballCapsandTiaras",
    "CROSSWORLDSNEXUS",
    "Fathead",
    "KevinZombie",
    "KindergardenCrisIs",
    "NoSongsForTheDead",
    "RequiemShadowbornPariah",
    "TezzleandZeek",

    # broken HTML
    "CrossingOver",

    # unique html
    "IKilledtheHero",
    "PowerofPower",
    "Schizmatic",
    "WaketheSleepers",
    "WeightofEternity",
]


def handle_url(url, session, res):
    """Parse one search result page."""
    print("Parsing", url, file=sys.stderr)
    try:
        data = html.document_fromstring(get_page(url, session).text)
        data.make_links_absolute(url)
    except IOError as msg:
        print("ERROR:", msg, file=sys.stderr)
        return

    num = 999
    for comicdiv in data.cssselect('div.searchresult'):
        comiclink = comicdiv.cssselect('h3 a')[0]
        comicurl = comiclink.attrib['href']
        name = format_name(comiclink.text)
        if contains_case_insensitive(res, name):
            # we cannot handle two comics that only differ in case
            print("INFO: skipping possible duplicate", repr(name),
                  file=sys.stderr)
            continue

        info = comicdiv.cssselect('span.comicinfo')
        # find out how many images this comic has
        num = int(info[1].text.strip())
        # find activity
        active = info[6].text.strip().lower() == "active"
        lang = info[7].text.strip().lower()
        res[name] = [comicurl, num, active, lang]

    return num


def get_results():
    """Parse all search result pages."""
    # store info in a dictionary {name -> shortname}
    res = {}
    session = requests.Session()
    # Sort by page count, so we can abort when we get under some threshold.
    baseUrl = ('http://comicfury.com/search.php?search=1&webcomics=1&query=' +
               '&worder=1&asc=0&incvi=1&incse=1&incnu=1&incla=1&all_ge=1' +
               '&all_st=1&all_la=1&page=%d')
    last_count = 999
    page = 1
    print("Parsing search result pages...", file=sys.stderr)
    while last_count >= MIN_COMICS:
        last_count = handle_url(baseUrl % page, session, res)
        page += 1
        print(last_count, file=sys.stderr, end=" ")
    save_result(res, json_file)


def find_dups(name):
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
        lname = scraperclass.getName().lower()
        if lname in names:
            return scraperclass.getName().lower()
    return None


def first_lower(x):
    return x[0].lower()


def print_results(args):
    """Print all comics that have at least the given number of minimum
    comic strips."""
    min_comics, filename = args
    min_comics = int(min_comics)
    with codecs.open(filename, 'a', 'utf-8') as fp:
        data = load_result(json_file)
        for name, entry in sorted(data.items(), key=first_lower):
            url, num, active, lang = entry
            if name in exclude_comics:
                fp.write(u"# %s is excluded\n" % name)
                continue
            if num < min_comics:
                continue
            dup = find_dups(name)
            if dup is not None:
                fp.write(u"# %s has a duplicate in %s\n" % (name, dup))
            else:
                fp.write(u"class CF%s(_ComicFury):\n    url = %r\n\n\n" % (
                         truncate_name(name), str(url)))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_results(sys.argv[1:])
    else:
        get_results()

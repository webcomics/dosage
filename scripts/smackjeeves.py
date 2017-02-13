#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher
"""
Script to get a list of smackjeeves.com comics and save the info in a JSON file
for further processing.
"""
from __future__ import absolute_import, division, print_function

import sys
from six.moves.urllib.parse import urlsplit

from scriptutil import ComicListUpdater


class SmackJeevesUpdater(ComicListUpdater):
    # Absolute minumum number of pages a comic may have (restrict search space)
    MIN_COMICS = 90

    # names of comics to exclude
    excluded_comics = (
        # comic moved/we have a better module
        "Amya",
        "Footloose",
        "TitleUnrelated",

        # does not follow standard layout
        "300DaysOfSyao",
        "ADifferentPerspective",
        "Captor",
        "ClubLove",
        "Comatose",
        "DeSTRESS",
        "DreamCatcher",
        "Fumiko",
        "GART",
        "GarytheAlchemist",
        "ItoshiisCrazyNuzlockeAdventures",
        "JennyHaniver",
        "KiLAiLO",
        "LoudEra",
        "LunarHill",
        "Mafiagame",
        "MylifewithFel",
        "MyLifewithFelENESPANOL",
        "NegativeZen",
        "Nemutionpobae",
        "NightShot",
        "NormalIsBoring",
        "OpticalDisarray",
        "PicturesofYou",
        "Pornjunkiesstrip",
        "PrettyUgly",
        "Project217",
        "RemmyzRandomz",
        "Ribon",
        "RubysWorld",
        "ShinkaTheLastEevee",
        "SimplePixel",
        "SladesMansionofawesomeness",
        "SpaceSchool",
        "SushiGummy",
        "TC2KsPokemobians",
        "TheAfterSubtract",
        "ThePokemonArtBox",
        "THEVOIDWEBCOMIC",
        "ToDefeatThemAll",
        "TwoKeys",
        "Vbcomics",
        "WerewolfRichard",

        # has no previous comic link
        "ThreadCrashers",
        "AchievementStuck",

        # images are 403 forbidden
        "AngelJunkPileFelix",
        "AntavioussGenLab",
        "Harfang",
        "Okamirai",

        # missing images
        "AGirlAndHerShadow",
        "Carciphona",
        "CatboyattheCon",
        "ContraandtheSpamDump",
        "Darkkyosshorts",
        "DollarStoreCaviar",
        "EdgeofDecember",
        "EvD",
        "HAndJ",
        "HEARD",
        "IwillbenapoSpamDump",
        "KirbysoftheAlternateDimension",
        "Letsreviewshallwe",
        "MegaManSpriteExpo",
        "OmnisSpriteShowcase",
        "PiecesofBrokenGlass",
        "PlatonicManagementDilemma",
        "SecretSanta2011",
        "SerendipityAnEquestrianTale",
        "SJArtCollab",
        "SlightlyDifferent",
        "TheAttackoftheRecoloursSeason1",
        "ThroughTheWonkyEye",
        "TotallyKotor",
        "WinterMelody",
        "ZonowTheHedgehog",

        # missing previous link
        "BambooArmonicKnightsGuild",

        # broken host name
        "Razor",
    )

    def __init__(self, name):
        super(SmackJeevesUpdater, self).__init__(name)
        self.sleep = 1.5

    def handle_url(self, url):
        """Parse one search result page."""
        data = self.get_url(url)

        num = 999
        for comictag in data.cssselect('a.card'):
            page_url = comictag.attrib['href']
            name = comictag.cssselect('div.title')[0].text
            # search for url in extra page
            data2 = self.get_url(page_url)

            # find out how many images this comic has
            mo = data2.cssselect('div.num-pages div.value')
            num = int(mo[0].text.strip().replace(',', ''))

            mo = data2.cssselect('div.buttons a:last-child')
            comic_url = mo[0].attrib['href']
            # search for adult flag
            adult = data2.cssselect('div.mature')
            updates = data2.cssselect('div.updates div.value')[0].text_content()
            self.add_comic(name, (comic_url, len(adult) > 0, updates), num)

        next_url = data.cssselect("a.next")[0].attrib['href']
        return (next_url, num)

    def collect_results(self):
        """Parse all search result pages."""
        # Sort by number of comics, so we can abort when we get under some
        # threshold.
        next_url = "http://www.smackjeeves.com/search.php?last_update=6&sort_by=5"
        last_count = 999
        while last_count >= self.MIN_COMICS:
            print(last_count, file=sys.stderr)
            next_url, last_count = self.handle_url(next_url)

    def get_entry(self, name, data):
        sub, top = urlsplit(data[0]).hostname.split('.', 1)
        if top.lower() == "smackjeeves.com":
            opt = "sub='%s'" % sub
        else:
            opt = "host='%s.%s'" % (sub, top)
        if data[1]:
            opt += ", adult=True"
        if data[2] == 'Completed':
            opt += ", endOfLife=True"
        return u"cls('%s', %s)," % (name, opt)

if __name__ == '__main__':
    SmackJeevesUpdater(__file__).run()

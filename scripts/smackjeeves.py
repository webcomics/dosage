#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
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

    ADULT_IMG = 'http://www.smackjeeves.com/images/mature_content.png'

    # names of comics to exclude
    excluded_comics = (
        # comic moved/we have a better module
        "Amya",
        "Carciphona",
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
        "CatboyattheCon",
        "ContraandtheSpamDump",
        "Darkkyosshorts",
        "DollarStoreCaviar",
        "EdgeofDecember",
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
        "TotallyKotor",
        "WinterMelody",
        "ZonowTheHedgehog",

        # missing previous link
        "BambooArmonicKnightsGuild",

        # broken host name
        "Razor",
    )

    def handle_url(self, url):
        """Parse one search result page."""
        data = self.get_url(url)

        num = 999
        for comicdiv in data.cssselect(
                'div#webcomic_search_results div.full_banner_div'):
            page_url = comicdiv.cssselect('a:first-child')[0].attrib['href']
            name = comicdiv.cssselect('img.banny')
            if name:
                name = name[0].attrib['title']
            else:
                name = comicdiv.cssselect('h2')[0].text
            # find out how many images this comic has
            mo = comicdiv.cssselect('span.small-meter')
            if not mo:
                print("ERROR matching number of comics", file=sys.stderr)
                continue
            num = int(mo[0].text.strip())
            # search for url in extra page
            data2 = self.get_url(page_url)
            mo = data2.cssselect('div#quick_reading_links a:last-child')
            if not mo:
                print("ERROR matching comic URL", file=sys.stderr)
                continue
            comic_url = mo[0].attrib['href']
            # search for adult flag
            adult = data2.xpath('//img[@src="' + self.ADULT_IMG + '"]')
            self.add_comic(name, (comic_url, bool(adult)), num)

        next_url = data.cssselect(
            "div.search_nav td:last-child a")[0].attrib['href']
        return (next_url, num)

    def collect_results(self):
        """Parse all search result pages."""
        # Sort by number of comics, so we can abort when we get under some
        # threshold.
        next_url = (
            "http://www.smackjeeves.com/search.php?submit=1" +
            "&search_mode=webcomics&comic_title=&sort_by=4&special=all" +
            "&last_update=6&style_all=on&genre_all=on&format_all=on")
        last_count = 999
        while last_count >= self.MIN_COMICS:
            print(last_count, file=sys.stderr, end=" ")
            next_url, last_count = self.handle_url(next_url)

    def get_entry(self, name, data):
        sub, top = urlsplit(data[0]).hostname.split('.', 1)
        cl = u"class SJ%s(_SmackJeeves):" % name
        if top.lower() == "smackjeeves.com":
            cl += "\n    sub = '%s'" % sub
        else:
            cl += "\n    host = '%s.%s'" % (sub, top)
        if data[1]:
            cl += "\n    adult = True"
        return cl

if __name__ == '__main__':
    SmackJeevesUpdater(__file__).run()

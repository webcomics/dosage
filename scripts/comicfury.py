#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher
"""
Script to get ComicFury comics and save the info in a JSON file for further
processing.
"""

import sys
from urllib.parse import urlsplit

from scriptutil import ComicListUpdater


class ComicFuryUpdater(ComicListUpdater):
    # Absolute minumum number of pages a comic may have (restrict search space)
    MIN_COMICS = 90

    dup_templates = ('ComicSherpa/%s', 'Creators/%s', 'GoComics/%s',
                     'KeenSpot/%s', 'Arcamax/%s')

    langmap = {
        'german': 'de',
        'spanish': 'es',
        'italian': 'it',
        'japanese': 'ja',
        'french': 'fr',
        'portuguese': 'pt',
    }

    # names of comics to exclude
    excluded_comics = (
        # unsuitable navigation
        "AlfdisAndGunnora",
        "AnAmericanNerdInAnimatedTokyo",
        "AngryAlien",
        "BoozerAndStoner",
        "Bonejangles",
        "ConradStory",
        "Crossing",
        "ChristianHumberReloaded",
        "CorkAndBlotto",
        "Democomix",
        "ErraticBeatComics",
        "EnergyWielders",
        "EvilBearorg",
        "Fiascos",
        "FateOfTheBlueStar",
        "FPK",
        "Fanartgyle",
        "FrigginRandom",
        "GoodbyeKitty",
        "GoodSirICannotDraw",
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
        "MoonlightValley",
        "MyImmortalFool",
        "NATO",
        "NothingFits",
        "OptimisticFishermenAndPessimisticFishermen",
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
        "StardustTheCat",
        "StrangerThanFiction",
        "TalamakGreatAdventure",
        "TheBattalion",
        "TheBends",
        "TheDailyProblem",
        "TheMansionOfE",
        "ThePainter",
        "TheSeekers",
        "TheTrialsOfKlahadOfTheAbyss",
        "TheStickmen",
        "ThornsInOurSide",
        "TopHeavyVeryBustyPinUpsForAdults",
        "USBUnlimitedSimulatedBody",
        "TylerHumanRecycler",
        "UAF",
        "WhenPigsFly",
        "YeOldeLegotimeTheatre",

        # no content
        "Angst",
        "TheDevonLegacyPrologue",

        # images gone
        "BaseballCapsAndTiaras",
        "BiMorphon",
        "CROSSWORLDSNEXUS",
        "DevilSpy",
        "Fathead",
        "GOODBYEREPTILIANS",
        "KevinZombie",
        "KindergardenCrisIs",
        "NoSongsForTheDead",
        "RequiemShadowbornPariah",
        "SandboxDrama",
        "STICKFODDER",
        "TezzleAndZeek",
        "TheRealmOfKaerwyn",

        # broken HTML
        "CrossingOver",

        # unique html
        "IKilledTheHero",
        "PowerOfPower",
        "Schizmatic",
        "WakeTheSleepers",
        "WeightOfEternity",

        # moved
        "OopsComicAdventure",
    )

    def handle_url(self, url):
        """Parse one search result page."""
        data = self.get_url(url)

        count = 999
        for comicdiv in data.cssselect('div.searchresult'):
            comiclink = comicdiv.cssselect('h3 a')[0]
            comicurl = comiclink.attrib['href']
            name = comiclink.text

            info = comicdiv.cssselect('span.comicinfo')
            # find out how many images this comic has
            count = int(info[1].text.strip())
            # find activity
            active = info[6].text.strip().lower() == "active"
            lang = info[7].text.strip().lower()
            self.add_comic(name, (comicurl, active, lang), count)

        return count

    def collect_results(self):
        """Parse all search result pages."""
        # Sort by page count, so we can abort when we get under some threshold.
        baseUrl = ('https://comicfury.com/search.php?search=1&webcomics=1&' +
                   'query=&worder=1&asc=0&incvi=2&incnu=2&incla=2&incse=2&' +
                   'all_ge=1&all_st=1&all_la=1&page=%d')
        last_count = 999
        page = 1
        print("Parsing search result pages...", file=sys.stderr)
        while last_count >= self.MIN_COMICS:
            last_count = self.handle_url(baseUrl % page)
            page += 1
            print(last_count, file=sys.stderr, end=" ")

    def get_entry(self, name, entry):
        url, active, lang = entry
        langopt = ''
        if lang != "english":
            if lang in self.langmap:
                langopt = ", '%s'" % self.langmap[lang]
            else:
                print("WARNING:", "Unknown language:", lang)

        sub = urlsplit(url).hostname.split('.', 1)[0]
        return u"cls('%s', '%s'%s)," % (name, sub, langopt)


if __name__ == '__main__':
    ComicFuryUpdater(__file__).run()

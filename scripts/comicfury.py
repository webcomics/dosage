#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
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

        for comicdiv in data.cssselect('div.webcomic-result'):
            comiclink = comicdiv.cssselect('div.webcomic-result-title a')[0]
            comicurl = comiclink.attrib['href']
            name = comiclink.text

            info = comicdiv.cssselect('span.stat-value')
            # find out how many images this comic has
            count = int(info[0].text.strip())
            self.add_comic(name, comicurl, count)

        nextlink = data.cssselect('div.search-next-page a')
        if nextlink:
            return nextlink[0].attrib['href']
        else:
            return None

    def collect_results(self):
        """Parse all search result pages."""
        # Sort by page count, so we can abort when we get under some threshold.
        url = ('https://comicfury.com/search.php?query=&lastupdate=0&' +
          'completed=1&fn=2&fv=2&fs=2&fl=2&sort=0')

        print("Parsing search result pages...", file=sys.stderr)
        while url:
            url = self.handle_url(url)

    def get_entry(self, name, entry):
        url = entry
        sub = urlsplit(url).hostname.split('.', 1)[0]
        return f"cls('{name}', '{sub}'),"


if __name__ == '__main__':
    ComicFuryUpdater(__file__).run()

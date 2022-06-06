# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from .common import WordPressScraper
from ..helpers import indirectStarter


class WebcomicFactory(WordPressScraper):
    starter = indirectStarter

    def __init__(self, name, url):
        super(WebcomicFactory, self).__init__(name)
        self.url = url
        self.firstStripUrl = url

    @classmethod
    def getmodules(cls):
        return (
            # do not edit anything below since these entries are generated from
            # scripts/webcomicfactory.py
            # START AUTOUPDATE
            cls('AsTheMayoTurns',
                'http://www.thewebcomicfactory.com/comic/as-the-mayo-turns/'),
            cls('ComicBookMafia',
                'http://www.thewebcomicfactory.com/comic/comic-book-mafia/'),
            cls('Dealers',
                'http://www.thewebcomicfactory.com/comic/dealers-1-1998-was-the-year/'),
            cls('DigitalHobo',
                'http://www.thewebcomicfactory.com/comic/digital-hobo-1-its-a-living-kinda/'),
            cls('ECoastVsWCoast',
                'http://www.thewebcomicfactory.com/comic/east-coast-vs-west-coast-greetings-from-the-coasts/'),
            cls('GunCulture',
                'http://www.thewebcomicfactory.com/comic/gun-culture/'),
            cls('IHateMyKids',
                'http://www.thewebcomicfactory.com/comic/i-hate-my-kids/'),
            cls('InARelationship',
                'http://www.thewebcomicfactory.com/comic/in-a-relationship-3/'),
            cls('IntergalacticMedicalDoctor',
                'http://www.thewebcomicfactory.com/comic/intergalactic-medical-doctor/'),
            cls('JSchoolgirlsInLove',
                'http://www.thewebcomicfactory.com/comic/japanese-schoolgirls-in-love-1/'),
            cls('KingdomOfTheDwarves',
                'http://www.thewebcomicfactory.com/comic/kingdom-of-the-dwarves/'),
            cls('LesterCrenshawIsDead',
                'http://www.thewebcomicfactory.com/comic/lester-crenshaw-is-dead/'),
            cls('Millennials',
                'http://www.thewebcomicfactory.com/comic/millennials/'),
            cls('MiserableComedians',
                'http://www.thewebcomicfactory.com/comic/miserable-comedians-1-funny-because-its-sad/'),
            cls('OldeTymeGamer',
                'http://www.thewebcomicfactory.com/comic/olde-tyme-gamer-playing-injured/'),
            cls('PinJunkies',
                'http://www.thewebcomicfactory.com/comic/pin-junkies/'),
            cls('PostApocalypticNick',
                'http://www.thewebcomicfactory.com/comic/post-apocalyptic-nick/'),
            cls('RealTalk',
                'http://www.thewebcomicfactory.com/comic/real-talk-people-who-cut-in-line/'),
            cls('SoManyNightmares',
                'http://www.thewebcomicfactory.com/comic/so-many-nightmares-freedom-nightmare/'),
            cls('SportsGuys',
                'http://www.thewebcomicfactory.com/comic/sports-guys/'),
            cls('TalesOfPizza',
                'http://www.thewebcomicfactory.com/comic/tales-of-pizza-bad-tipper/'),
            cls('TAndA',
                'http://www.thewebcomicfactory.com/comic/the-webcomic-factory-premiere-t-and-a/'),
            cls('TheAntiwarComic',
                'http://www.thewebcomicfactory.com/comic/the-antiwar-comic-the-party/'),
            cls('TheGentlemensClub',
                'http://www.thewebcomicfactory.com/comic/the-gentlemens-club/'),
            cls('TheHorrorOfColony6',
                'http://www.thewebcomicfactory.com/comic/the-horror-of-colony-6-page-1/'),
            cls('TheKingsOfViralVideo',
                'http://www.thewebcomicfactory.com/comic/the-kings-of-viral-video-premiere/'),
            cls('TheSharonAndTonyExperiment',
                'http://www.thewebcomicfactory.com/comic/the-sharon-and-tony-experiment/'),
            cls('TonyDestructo',
                'http://www.thewebcomicfactory.com/comic/tony-destructo/'),
            cls('WeirdBikerTales',
                'http://www.thewebcomicfactory.com/comic/weird-biker-tales-the-last-outlaw/'),
            cls('WillysSpaceDive',
                'http://www.thewebcomicfactory.com/comic/willys-space-dive/'),
            # END AUTOUPDATE
        )

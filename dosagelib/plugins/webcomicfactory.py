# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from .common import _WordPressScraper


class _WebcomicFactory(_WordPressScraper):
    latestSearch = '//a[contains(concat(" ", @class, " "), " comic-nav-last ")]'

    @classmethod
    def starter(cls):
        """this is basically helpers.indirectStarter, but dynamically selecting
        the right parameters."""
        data = cls.getPage(cls.firstStripUrl)
        return cls.fetchUrl(cls.firstStripUrl, data, cls.latestSearch)


# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# DO NOT REMOVE


class AsTheMayoTurns(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/as-the-mayo-turns/'


class ComicBookMafia(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/comic-book-mafia/'


class Dealers(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/dealers-1-1998-was-the-year/'


class DigitalHobo(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/digital-hobo-1-its-a-living-kinda/'


class ECoastVsWCoast(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/east-coast-vs-west-coast-greetings-from-the-coasts/'


class GunCulture(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/gun-culture/'


class IHateMyKids(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/i-hate-my-kids/'


class InARelationship(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/in-a-relationship-3/'


class IntergalacticMedicalDoctor(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/intergalactic-medical-doctor/'


class JSchoolgirlsInLove(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/japanese-schoolgirls-in-love-1/'


class KingdomOfTheDwarves(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/kingdom-of-the-dwarves/'


class LesterCrenshawIsDead(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/lester-crenshaw-is-dead/'


class Millennials(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/millennials/'


class MiserableComedians(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/miserable-comedians-1-funny-because-its-sad/'


class OldeTymeGamer(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/olde-tyme-gamer-playing-injured/'


class PinJunkies(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/pin-junkies/'


class PostApocalypticNick(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/post-apocalyptic-nick/'


class RealTalk(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/real-talk-people-who-cut-in-line/'


class SoManyNightmares(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/so-many-nightmares-freedom-nightmare/'


class SportsGuys(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/sports-guys/'


class TalesOfPizza(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/tales-of-pizza-bad-tipper/'


class TAndA(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/the-webcomic-factory-premiere-t-and-a/'


class TheAntiwarComic(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/the-antiwar-comic-the-party/'


class TheGentlemensClub(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/the-gentlemens-club/'


class TheHorrorOfColony6(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/the-horror-of-colony-6-page-1/'


class TheKingsOfViralVideo(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/the-kings-of-viral-video-premiere/'


class TheSharonAndTonyExperiment(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/the-sharon-and-tony-experiment/'


class TonyDestructo(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/tony-destructo/'


class WeirdBikerTales(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/weird-biker-tales-the-last-outlaw/'


class WillysSpaceDive(_WebcomicFactory):
    firstStripUrl = 'http://www.thewebcomicfactory.com/comic/willys-space-dive/'

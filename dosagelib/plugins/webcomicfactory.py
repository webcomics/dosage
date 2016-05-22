# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from .common import _WordPressScraper, WP_LATEST_SEARCH
from ..helpers import indirectStarter


class _WebcomicFactory(_WordPressScraper):
    starter = indirectStarter
    latestSearch = WP_LATEST_SEARCH


# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# START AUTOUPDATE


class AsTheMayoTurns(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/as-the-mayo-turns/'
    firstStripUrl = url


class ComicBookMafia(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/comic-book-mafia/'
    firstStripUrl = url


class Dealers(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/dealers-1-1998-was-the-year/'
    firstStripUrl = url


class DigitalHobo(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/digital-hobo-1-its-a-living-kinda/'
    firstStripUrl = url


class ECoastVsWCoast(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/east-coast-vs-west-coast-greetings-from-the-coasts/'
    firstStripUrl = url


class GunCulture(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/gun-culture/'
    firstStripUrl = url


class IHateMyKids(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/i-hate-my-kids/'
    firstStripUrl = url


class InARelationship(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/in-a-relationship-3/'
    firstStripUrl = url


class IntergalacticMedicalDoctor(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/intergalactic-medical-doctor/'
    firstStripUrl = url


class JSchoolgirlsInLove(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/japanese-schoolgirls-in-love-1/'
    firstStripUrl = url


class KingdomOfTheDwarves(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/kingdom-of-the-dwarves/'
    firstStripUrl = url


class LesterCrenshawIsDead(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/lester-crenshaw-is-dead/'
    firstStripUrl = url


class Millennials(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/millennials/'
    firstStripUrl = url


class MiserableComedians(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/miserable-comedians-1-funny-because-its-sad/'
    firstStripUrl = url


class OldeTymeGamer(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/olde-tyme-gamer-playing-injured/'
    firstStripUrl = url


class PinJunkies(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/pin-junkies/'
    firstStripUrl = url


class PostApocalypticNick(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/post-apocalyptic-nick/'
    firstStripUrl = url


class RealTalk(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/real-talk-people-who-cut-in-line/'
    firstStripUrl = url


class SoManyNightmares(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/so-many-nightmares-freedom-nightmare/'
    firstStripUrl = url


class SportsGuys(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/sports-guys/'
    firstStripUrl = url


class TalesOfPizza(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/tales-of-pizza-bad-tipper/'
    firstStripUrl = url


class TAndA(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/the-webcomic-factory-premiere-t-and-a/'
    firstStripUrl = url


class TheAntiwarComic(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/the-antiwar-comic-the-party/'
    firstStripUrl = url


class TheGentlemensClub(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/the-gentlemens-club/'
    firstStripUrl = url


class TheHorrorOfColony6(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/the-horror-of-colony-6-page-1/'
    firstStripUrl = url


class TheKingsOfViralVideo(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/the-kings-of-viral-video-premiere/'
    firstStripUrl = url


class TheSharonAndTonyExperiment(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/the-sharon-and-tony-experiment/'
    firstStripUrl = url


class TonyDestructo(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/tony-destructo/'
    firstStripUrl = url


class WeirdBikerTales(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/weird-biker-tales-the-last-outlaw/'
    firstStripUrl = url


class WillysSpaceDive(_WebcomicFactory):
    url = 'http://www.thewebcomicfactory.com/comic/willys-space-dive/'
    firstStripUrl = url
# END AUTOUPDATE

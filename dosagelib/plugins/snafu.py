# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper
from ..helpers import indirectStarter


class _Snafu(_ParserScraper):
    # Next and Previous are swapped...
    prevSearch = '//a[@class="next"]'
    imageSearch = '//div[@class="comicpage"]/img'
    latestSearch = '//div[@id="feed"]/a'
    starter = indirectStarter

    def __init__(self, name):
        super(_Snafu, self).__init__('SnafuComics/' + name)

    def namer(self, image_url, page_url):
        year, month, name = image_url.rsplit('/', 3)[1:]
        return "%04s_%02s_%s" % (year, month, name)

    @property
    def url(self):
        return 'http://snafu-comics.com/swmseries/' + self.path


class Braindead(_Snafu):
    path = 'braindead'


class Bunnywith(_Snafu):
    path = 'bunnywith'


class DeliverUsEvil(_Snafu):
    path = 'deliverusevil'


class DigitalPurgatory(_Snafu):
    path = 'digital-purgatory'


class EA(_Snafu):
    path = 'ea'


class FT(_Snafu):
    path = 'ft'


class GrimTalesFromDownBelow(_Snafu):
    path = 'grimtales'


class KOF(_Snafu):
    path = 'kof'


class MyPanda(_Snafu):
    path = 'mypanda'


class NarutoHeroesPath(_Snafu):
    path = 'naruto'


class NewSuperMarioAdventures(_Snafu):
    path = 'nsma'


class PowerPuffGirls(_Snafu):
    path = 'powerpuffgirls'


class PSG2(_Snafu):
    path = 'psg2'


class SatansExcrement(_Snafu):
    path = 'satansexcrement'


class SF(_Snafu):
    path = 'sf'


class SkullBoy(_Snafu):
    path = 'skullboy'


class Snafu(_Snafu):
    path = 'snafu'


class Soul(_Snafu):
    path = 'soul'


class Sugar(_Snafu):
    path = 'sugarbits'


class SureToBeBanD(_Snafu):
    path = 'stbb'


class TheLeague(_Snafu):
    path = 'league'


class Tin(_Snafu):
    path = 'tin'


class Titan(_Snafu):
    path = 'titan'


class TrunksAndSoto(_Snafu):
    path = 'trunks-and-soto'


class TW(_Snafu):
    path = 'tw'


class Zim(_Snafu):
    path = 'zim'

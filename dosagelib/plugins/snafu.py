# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper
from ..helpers import indirectStarter


class Snafu(_ParserScraper):
    # Next and Previous are swapped...
    prevSearch = '//a[@class="next"]'
    imageSearch = '//div[@class="comicpage"]/img'
    latestSearch = '//div[@id="feed"]/a'
    starter = indirectStarter

    def __init__(self, name, path):
        super(Snafu, self).__init__('SnafuComics/' + name)
        self.url = 'http://snafu-comics.com/swmseries/' + path

    def namer(self, image_url, page_url):
        year, month, name = image_url.rsplit('/', 3)[1:]
        return "%04s_%02s_%s" % (year, month, name)

    @classmethod
    def getmodules(cls):
        return [
            cls('Braindead', 'braindead'),
            cls('Bunnywith', 'bunnywith'),
            cls('DeliverUsEvil', 'deliverusevil'),
            cls('EA', 'ea'),
            cls('FT', 'ft'),
            cls('GrimTalesFromDownBelow', 'grimtales'),
            cls('KOF', 'kof'),
            cls('MyPanda', 'mypanda'),
            cls('NarutoHeroesPath', 'naruto'),
            cls('NewSuperMarioAdventures', 'nsma'),
            cls('PowerPuffGirls', 'powerpuffgirls'),
            # cls('PSG2', 'psg2'), -- Strangely broken
            cls('SatansExcrement', 'satansexcrement'),
            cls('SF', 'sf'),
            cls('SkullBoy', 'skullboy'),
            cls('Snafu', 'snafu'),
            cls('Soul', 'soul'),
            cls('Sugar', 'sugarbits'),
            cls('SureToBeBanD', 'stbb'),
            cls('TheLeague', 'league'),
            cls('Tin', 'tin'),
            cls('Titan', 'titan'),
            cls('TrunksAndSoto', 'trunks-and-soto'),
            cls('TW', 'tw'),
            cls('Zim', 'zim'),
        ]

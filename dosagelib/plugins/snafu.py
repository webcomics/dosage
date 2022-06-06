# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
import re

from .common import ComicControlScraper


FILENAMECRAP = re.compile(r'_[0-9a-f]{72}(?=\.)')


class Snafu(ComicControlScraper):
    def __init__(self, name, path):
        super().__init__('SnafuComics/' + name)
        self.url = 'https://snafu-comics.com/' + path

    def namer(self, image_url, page_url):
        return FILENAMECRAP.sub('', image_url.rsplit('/', 1)[-1])

    @classmethod
    def getmodules(cls):
        return (
            cls('Braindead', 'braindead'),
            cls('Bunnywith', 'bunnywith'),
            cls('CrawlingCity', 'crawlingcity'),
            cls('DeliverUsEvil', 'deliverusevil'),
            cls('EA', 'ea'),
            cls('FT', 'ft'),
            cls('GG', 'gg'),
            cls('GrimTalesFromDownBelow', 'grimtales'),
            cls('HalfboundBlade', 'hbp'),
            cls('KayosGaiden', 'titan-kayos'),
            cls('NarutoHeroesPath', 'naruto'),
            cls('NewSuperMarioAdventures', 'nsma'),
            cls('PowerPuffGirls', 'powerpuffgirls'),
            cls('SatansExcrement', 'satansexcrement'),
            cls('SkullBoy', 'skullboy'),
            cls('Soul', 'soul'),
            cls('Sugar', 'sugarbits'),
            cls('SureToBeBanD', 'stbb'),
            cls('TheLeague', 'league'),
            cls('TrunksAndSoto', 'trunks-and-soto'),
            cls('TW', 'tw'),
            cls('Zim', 'zim'),
        )

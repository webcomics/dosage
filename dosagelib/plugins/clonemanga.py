# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
from ..helpers import indirectStarter
from ..scraper import ParserScraper
from ..util import getQueryParams


class CloneManga(ParserScraper):
    baseUrl = 'http://manga.clone-army.org'
    imageSearch = '//div[d:class("subsectionContainer")]//img'
    prevSearch = '//a[span[text()="<<"]]'
    latestSearch = '//a[span[text()=">|"]]'
    starter = indirectStarter
    help = 'Index format: n'

    def __init__(self, name, shortName, endOfLife=False):
        super().__init__('CloneManga/' + name)
        self.stripUrl = '%s/viewer.php?page=%%s&lang=&series=%s&HUDoff=' % (
            self.baseUrl, shortName)
        self.url = self.stripUrl % '1'
        self.endOfLife = endOfLife

    def namer(self, image_url, page_url):
        origname = image_url.rsplit('/', 1)[1]
        params = getQueryParams(page_url)
        if 'page' in params:
            return '{:03}_{}'.format(int(params['page'][0]), origname)
        else:
            return origname

    @classmethod
    def getmodules(cls):
        return (
            cls('ACaptainsWorries', 'captains_worries'),
            cls('AHimehornsDailyLife', 'himehorn'),
            cls('AprilAndMay', 'anm', endOfLife=True),
            cls('DollAndMaker', 'maria_doll', endOfLife=True),
            cls('Kanami', 'kanami', endOfLife=True),
            cls('MomokaCorner', 'momoka', endOfLife=True),
            cls('MyShutInVampirePrincess', 'snax'),
            cls('NanasEverydayLife', 'nana', endOfLife=True),
            cls('NNN', 'nnn', endOfLife=True),
            cls('PaperEleven', 'pxi', endOfLife=True),
            cls('PennyTribute', 'penny', endOfLife=True),
            cls('Tomoyo42sRoom', 't42r'),
        )

# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from ..scraper import ParserScraper
from ..helpers import indirectStarter


class Derideal(ParserScraper):
    baseUrl = 'https://www.derideal.com/'
    imageSearch = '//img[contains(@class, "comic-page")]'
    prevSearch = '//a[i[contains(@class, "fa-angle-left")]]'
    latestSearch = '//a[i[contains(@class, "fa-angle-double-right")]]'

    def __init__(self, name, sub, first, last=None):
        if name == 'Derideal':
            super().__init__(name)
        else:
            super().__init__('Derideal/' + name)

        self.url = self.baseUrl + sub
        self.stripUrl = self.url + '/%s/'
        self.firstStripUrl = self.stripUrl % first
        self.startUrl = self.firstStripUrl

        if last:
            self.endOfLife = True

    def starter(self):
        indexPage = self.getPage(self.url)
        self.chapters = indexPage.xpath('//a[contains(text(), "Read this episode")]/@href')
        self.currentChapter = len(self.chapters)
        return indirectStarter(self)

    def namer(self, imageUrl, pageUrl):
        filename = pageUrl.rstrip('/').rsplit('/', 1)[-1]
        filename = filename.replace('espanol-escape-25', 'escape-26')
        filename = filename.replace('espanol-w-a-l-l-y', 'w-a-l-l-y')
        filename = filename.replace('hogar-prision', 'home-prison')
        filename = filename.replace('strip', 'pe').replace('purpurina-effect', 'pe')
        filename = filename.replace('sector-de-seguridad', 'security-sector')
        filename = 'ch' + str(self.currentChapter) + '-' + filename
        if pageUrl in self.chapters:
            self.currentChapter -= 1
        return filename

    @classmethod
    def getmodules(cls):
        return (
            cls('Derideal', 'derideal', 'cover-prime'),
            cls('Legacy', 'derideal-legacy', 'the-dream-cover', last='derideal-is-on-hiatus'),
            cls('LRE', 'RLE', 'the-leyend-of-the-rose-cover'),
            cls('ProjectPrime', 'project-prime', 'custus-part-i-cover'),
            cls('PurpurinaEffect', 'purpurina-effect', 'purpurina-effect-cover'),
            cls('TheVoid', 'the-void', 'the-void-cover'),
        )

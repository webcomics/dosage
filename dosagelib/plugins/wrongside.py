# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2022 Daniel Ring
from ..scraper import ParserScraper
from ..helpers import indirectStarter


class Wrongside(ParserScraper):
    baseUrl = 'http://ayzewi.com/maingallery3/'
    url = baseUrl + 'index.php?/category/5'
    stripUrl = baseUrl + 'picture.php?%s'
    firstStripUrl = stripUrl % '/175/category/21'
    imageSearch = '//img[@id="theMainImage"]/@src'
    prevSearch = '//a[contains(@title, "Previous :")]'

    def starter(self):
        archivePage = self.getPage(self.url)
        chapterUrls = archivePage.xpath('//ul[@class="albThumbs"]//a/@href')
        self.archive = []
        for chapterUrl in chapterUrls:
            chapterPage = self.getPage(chapterUrl)
            self.archive.append(chapterPage.xpath('(//ul[@id="thumbnails"]//a/@href)[last()]')[0])
        return self.archive[0]

    def getPrevUrl(self, url, data):
        if data.xpath(self.prevSearch) == [] and len(self.archive) > 0:
            return self.archive.pop()
        return super(Wrongside, self).getPrevUrl(url, data)

    def namer(self, imageUrl, pageUrl):
        page = self.getPage(pageUrl)
        title = page.xpath('//div[@class="browsePath"]/h2/text()')[0]
        return title.replace('"', '') + '.' + imageUrl.rsplit('.', 1)[-1]


class WrongsideBeginnings(Wrongside):
    name = 'Wrongside/Beginnings'
    baseUrl = 'http://ayzewi.com/maingallery3/'
    url = baseUrl + 'index.php?/category/4'
    stripUrl = baseUrl + 'picture.php?%s'
    firstStripUrl = stripUrl % '/2/category/18'


class WrongsideSideStories(ParserScraper):
    baseUrl = 'http://ayzewi.com/maingallery3/'
    stripUrl = baseUrl + 'picture.php?%s'
    imageSearch = '//img[@id="theMainImage"]/@src'
    prevSearch = '//a[contains(@title, "Previous :")]'
    latestSearch = '(//ul[@id="thumbnails"]//a/@href)[last()]'
    starter = indirectStarter

    def __init__(self, name, category, first, last=None):
        super().__init__('Wrongside/' + name)
        self.url = self.baseUrl + 'index.php?/category/' + category
        self.firstStripUrl = self.stripUrl % ('/' + first + '/category/' + category)

        if last:
            self.endOfLife = True

    @classmethod
    def getmodules(cls):
        return (
            cls('AnarkisRising', '7', '302'),
            cls('CommonsDreams', '9', '324'),
            cls('Faith', '11', '349'),
            cls('Sarah', '10', '337'),
            cls('ThereAreNoAviansHere', '8', '313'),
            cls('TheScientificProphet', '13', '358'),
            cls('TheStrangers', '12', '361'),
        )

    def namer(self, imageUrl, pageUrl):
        page = self.getPage(pageUrl)
        title = page.xpath('//div[@class="browsePath"]/h2/text()')[0]
        return title.replace('"', '') + '.' + imageUrl.rsplit('.', 1)[-1]

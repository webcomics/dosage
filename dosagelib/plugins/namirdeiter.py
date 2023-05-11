# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from ..scraper import ParserScraper


class NamirDeiter(ParserScraper):
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = ('//a[@rel="prev"]',
                  '//a[./img[contains(@src, "previous")]]',
                  '//a[contains(text(), "Previous")]')

    def __init__(self, name, baseUrl, first=None, last=None):
        if name == 'NamirDeiter':
            super(NamirDeiter, self).__init__(name)
        else:
            super(NamirDeiter, self).__init__('NamirDeiter/' + name)

        self.url = 'https://' + baseUrl + '/'
        self.stripUrl = self.url + 'comics/index.php?date=%s'

        if first:
            self.firstStripUrl = self.stripUrl % first
        else:
            self.firstStripUrl = self.url + 'comics/'

        if last:
            self.url = self.stripUrl % last
            self.endOfLife = True

    def link_modifier(self, fromurl, tourl):
        # Links are often absolute and keep jumping between http and https
        return tourl.replace('http:', 'https:').replace('/www.', '/')

    @classmethod
    def getmodules(cls):
        return (
            cls('ApartmentForTwo', 'apartmentfor2.com'),
            cls('NamirDeiter', 'namirdeiter.com', last='20150410'),
            cls('NicoleAndDerek', 'nicoleandderek.com'),
            cls('OneHundredPercentCat', 'ndunlimited.com/100cat', last='20121001'),
            cls('SpareParts', 'sparepartscomics.com', first='20031022', last='20080331'),
            cls('TheNDU', 'thendu.com'),
            cls('WonderKittens', 'wonderkittens.com'),
            cls('YouSayItFirst', 'yousayitfirst.com', first='20040220', last='20130125'),
        )


class UnlikeMinerva(ParserScraper):
    name = 'NamirDeiter/UnlikeMinerva'
    baseUrl = 'https://unlikeminerva.com/archive/index.php'
    stripUrl = baseUrl + '?week=%s'
    url = stripUrl % '127'
    firstStripUrl = stripUrl % '26'
    imageSearch = '//img[contains(@src, "archive/")]'
    prevSearch = '//a[./img[contains(@src, "previous")]]'
    multipleImagesPerStrip = True
    endOfLife = True

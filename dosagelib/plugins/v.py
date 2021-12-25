# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from ..scraper import _ParserScraper
from ..helpers import bounceStarter, indirectStarter


class VampireHunterBoyfriends(_ParserScraper):
    baseUrl = 'https://boneitisindustries.com/'
    url = baseUrl + 'comics/vampire-hunter-boyfriends/'
    stripUrl = baseUrl + 'comic/%s/'
    firstStripUrl = stripUrl % 'vampire-hunter-boyfriends-chapter-1-cover'
    imageSearch = '//div[@id="content"]//img[d:class("size-full")]'
    prevSearch = '//a[./span[d:class("ticon-chevron-left")]]'
    adult = True

    def starter(self):
        archivePage = self.getPage(self.url)
        self.archive = archivePage.xpath('//div[contains(@class, "vcex-portfolio-grid")]//a/@href')
        return self.archive[-1]

    def getPrevUrl(self, url, data):
        return self.archive[self.archive.index(url) - 1]


class Vexxarr(_ParserScraper):
    baseUrl = 'http://www.vexxarr.com/'
    url = baseUrl + 'Index.php'
    stripUrl = baseUrl + 'archive.php?seldate=%s'
    firstStripUrl = stripUrl % '010105'
    imageSearch = '//p/img'
    prevSearch = '//a[./img[contains(@src, "previous")]]'
    nextSearch = '//a[./img[contains(@src, "next")]]'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        page = pageUrl.rsplit('=', 1)[-1]
        return '20%s-%s-%s' % (page[4:6], page[0:2], page[2:4])


class VGCats(_ParserScraper):
    url = 'https://www.vgcats.com/comics/'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//td/img[contains(@src, "images/")]'
    prevSearch = '//a[img[contains(@src, "back.")]]'
    help = 'Index format: n (unpadded)'


class VickiFox(_ParserScraper):
    url = 'http://www.vickifox.com/comic/strip'
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '001'
    imageSearch = '//img[contains(@src, "comic/")]'
    prevSearch = '//button[@id="btnPrev"]/@value'

    def getPrevUrl(self, url, data):
        return self.stripUrl % self.getPage(url).xpath(self.prevSearch)[0]


class ViiviJaWagner(_ParserScraper):
    url = 'http://www.hs.fi/viivijawagner/'
    imageSearch = '//meta[@property="og:image"]/@content'
    prevSearch = '//a[d:class("prev")]'
    latestSearch = '//div[d:class("cartoon-content")]//a'
    starter = indirectStarter
    lang = 'fi'

    def namer(self, image_url, page_url):
        return page_url.rsplit('-', 1)[1].split('.')[0]


class VirmirWorld(_ParserScraper):
    url = 'http://world.virmir.com/'
    stripUrl = url + 'comic.php?story=%s&page=%s'
    firstStripUrl = stripUrl % ('1', '1')
    imageSearch = '//div[@class="comic"]//img'
    prevSearch = '//a[contains(@class, "prev")]'

    def getIndexStripUrl(self, index):
        index = index.split('-')
        return self.stripUrl % (index[0], index[1])

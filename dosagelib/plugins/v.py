# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring

from ..scraper import ParserScraper, _ParserScraper
from ..helpers import bounceStarter, indirectStarter


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


class Vibe(ParserScraper):
    starter = indirectStarter
    url = 'http://www.vibecomic.com/vibe/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % ''
    imageSearch = '//div[@id="cc-comicbody"]//img'
    prevSearch = '//a[@rel="prev"]'
    nextSearch = '//a[@rel="next"]'
    latestSearch = '//a[@class="last"]'
    help = 'Index format: VIBEnnn (padded)'


class VickiFox(ParserScraper):
    url = 'http://www.vickifox.com/comic/strip'
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '001'
    imageSearch = '//img[contains(@src, "comic/")]'
    prevSearch = '//button[@id="btnPrev"]/@value'

    def link_modifier(self, fromurl, tourl):
        return self.stripUrl % tourl


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


class Vreakerz(ParserScraper):
    url = 'http://vreakerz.angrykitten.nl/'
    stripUrl = url + 'stories/read/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "storypages")]'
    prevSearch = '//a[@class="btn-prior"]'

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, IGNORECASE

from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from ..helpers import indirectStarter
from .common import _ComicControlScraper, _WordPressScraper, xpath_class


class WapsiSquare(_WordPressScraper):
    url = 'http://wapsisquare.com/'
    firstStripUrl = url + 'comic/09092001/'


class WastedTalent(_BasicScraper):
    url = 'http://www.wastedtalent.ca/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'anime-crack'
    imageSearch = compile(tagre("img", "src", r'(http://www\.wastedtalent\.ca/sites/default/files/imagecache/comic_full/comics/\d+/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)',
                               after="comic_prev"))
    help = 'Index format: stripname'


class WebDesignerCOTW(_BasicScraper):
    url = 'http://www.webdesignerdepot.com/'
    rurl = escape(url)
    starter = indirectStarter
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/11/comics-of-the-week-1'
    imageSearch = (
        compile(tagre("img", "src", r'(http://netdna\.webdesignerdepot\.com/uploads/\d+/\d+/\d+s?\.[^"]+)')),
        compile(tagre("img", "src", r'(http://netdna\.webdesignerdepot\.com/uploads/\d+/\d+/Christmas\d+\.[^"]+)')),
        compile(tagre("img", "src", r'(http://netdna\.webdesignerdepot\.com/uploads/comics\d+[a-z0-9]*/\d+a?\.[^"]+)')),
        compile(tagre("img", "src", r'(http://netdna\.webdesignerdepot\.com/uploads/comics/\d+\.[^"]+)')),
    )
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("link", "href", r"(%s\d+/\d+/[^']+)" % rurl,
                               before='prev', quote="'"))
    latestSearch = compile(tagre("a", "href", r'(%s\d+/\d+/[^"]+/)' % rurl))
    help = 'Index format: yyyy/mm/stripname'

    def shouldSkipUrl(self, url, data):
        """Skip non-comic URLs."""
        return 'comics-of-the-week' not in url

    def namer(self, image_url, page_url):
        imagename = image_url.rsplit('/', 1)[1]
        week = compile(r'week-(\d+)').search(page_url).group(1)
        return "%s-%s" % (week, imagename)


class WeCanSleepTomorrow(_BasicScraper):
    url = 'http://wecansleeptomorrow.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Weregeek(_BasicScraper):
    url = 'http://www.weregeek.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/11/27/'
    imageSearch = compile(tagre("img", "src",
                                r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'((%s)?/?\d+/\d+/\d+/)' % rurl) +
                         '\s*' + tagre('img', 'src', '[^"]*previous_day.gif'))
    help = 'Index format: yyyy/mm/dd'


class WhiteNoise(_WordPressScraper):
    url = 'http://whitenoisecomic.com/'
    firstStripUrl = url + 'comic/book-one/'
    prevSearch = '//a[%s]' % xpath_class('previous-webcomic-link')


class Whomp(_ComicControlScraper):
    url = 'http://www.whompcomic.com/'
    firstStripUrl = url + 'comic/06152010'
    textSearch = '//img[@id="cc-comic"]/@title'


class WhyTheLongFace(_BasicScraper):
    baseUrl = 'http://www.absurdnotions.org/'
    rurl = escape(baseUrl)
    url = baseUrl + 'wtlf200709.html'
    stripUrl = baseUrl + 'wtlf%s.html'
    firstStripUrl = stripUrl % '200306'
    imageSearch = compile(r'<img src="(%swtlf.+?|lf\d+.\w{1,4})"' % rurl,
                          IGNORECASE)
    multipleImagesPerStrip = True
    prevSearch = compile(r'HREF="(.+?)"><IMG SRC="nprev.gif" ')
    help = 'Index format: yyyymm'


class Wigu(_ParserScraper):
    stripUrl = 'http://www.wigucomics.com/adventures/index.php?comic=%s'
    url = stripUrl % '-1'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic"]//img[contains(@src, "/comics/")]'
    prevSearch = '//a[@alt="go back"]'
    endOfLife = True
    help = 'Index format: n'


class Wonderella(_BasicScraper):
    url = 'http://nonadventures.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/09/09/the-torment-of-a-thousand-yesterdays'
    imageSearch = compile(tagre("div", "id", r"comic", quote=r'["\']') +
                          r"\s*" +
                          tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl,
                               after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class Wondermark(_BasicScraper):
    url = 'http://wondermark.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(r'<img src="(http://wondermark.com/c/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" rel="prev">')
    help = 'Index format: nnn'


class WorldOfMrToast(_BasicScraper):
    baseUrl = 'http://www.theimaginaryworld.com/'
    url = baseUrl + 'mrTcomicA.html'
    imageSearch = compile(tagre("img", "src", r'(comic[^"]+)'))
    # list the archive links since there is no prev/next navigation
    prevurls = (
        url,
        baseUrl + 'mrTcomicW02.html',
        baseUrl + 'mrTcomicW01.html',
        baseUrl + 'mrGcomic03.html',
        baseUrl + 'mrGcomic02.html',
        baseUrl + 'mrGcomic01.html',
        baseUrl + 'mrTcomicT05.html',
        baseUrl + 'mrTcomicT04.html',
        baseUrl + 'mrTcomicT03.html',
        baseUrl + 'mrTcomicT02.html',
        baseUrl + 'mrTcomicT01.html',
        baseUrl + 'mrTcomicIW3.html',
        baseUrl + 'mrTcomicIW2.html',
        baseUrl + 'mrTcomicIW1.html',
    )
    firstStripUrl = prevurls[-1]
    multipleImagesPerStrip = True
    endOfLife = True

    def getPrevUrl(self, url, data):
        idx = self.prevurls.index(url)
        try:
            return self.prevurls[idx + 1]
        except IndexError:
            return None


class WorldOfWarcraftEh(_WordPressScraper):
    url = 'http://woweh.com/'


class WormWorldSaga(_BasicScraper):
    url = 'http://www.wormworldsaga.com/'
    stripUrl = url + 'chapters/%s/index.php'
    firstStripUrl = stripUrl % 'chapter01/EN'
    imageSearch = (
        compile(tagre("img", "src", r'(images/CH\d+_\d+\.[^"]+)')),
        compile(tagre("img", "src", r'(panels/CH\d+_[^"]+)')),
    )
    latestChapter = 5
    multipleImagesPerStrip = True

    def starter(self):
        return '%schapters/chapter%02d/%s/index.php' % (
            self.url, self.latestChapter, self.lang.upper())

    def getPrevUrl(self, url, data):
        """Find previous URL."""
        if 'chapter04' in url:
            return url.replace('chapter04', 'chapter03')
        if 'chapter03' in url:
            return url.replace('chapter03', 'chapter02')
        if 'chapter02' in url:
            return url.replace('chapter02', 'chapter01')
        return None


class WormWorldSagaFrench(WormWorldSaga):
    lang = 'fr'


class WormWorldSagaGerman(WormWorldSaga):
    lang = 'de'


class WormWorldSagaSpanish(WormWorldSaga):
    lang = 'es'

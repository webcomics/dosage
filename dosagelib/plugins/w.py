# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile, escape, IGNORECASE

from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from ..helpers import bounceStarter
from .common import ComicControlScraper, WordPressScraper, WordPressNaviIn, WordPressWebcomic


class WapsiSquare(WordPressNaviIn):
    url = 'http://wapsisquare.com/'
    firstStripUrl = url + 'comic/09092001/'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return data.xpath('//iframe')  # videos


class WastedTalent(_ParserScraper):
    url = 'http://www.wastedtalent.ca/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'anime-crack'
    imageSearch = '//div[d:class("comic_content")]/img'
    prevSearch = '//li[d:class("previous")]/a'
    multipleImagesPerStrip = True


class WebcomicName(_ParserScraper):
    url = 'https://webcomicname.com/'
    imageSearch = '//figure[d:class("tmblr-full")]//img'
    prevSearch = '//a[d:class("next")]'
    multipleImagesPerStrip = True


class Weregeek(_ParserScraper):
    url = 'http://www.weregeek.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/11/27'
    imageSearch = '//div[@id="comic"]/img'
    prevSearch = '//a[./img[@alt="Previous"]]'
    help = 'Index format: yyyy/mm/dd'


class WereIWolf(_ParserScraper):
    stripUrl = 'https://wolfwares.ca/comics/Were I wolf/strip2.php?name=%s&start=%s'
    url = stripUrl % ('4 Black and White - part 3', 'latest')
    firstStripUrl = stripUrl % ('1 Sirens', '0')
    imageSearch = '//img[contains(@src, "ROW")]'
    prevSearch = '//a[./img[contains(@src, "previous")]]'
    multipleImagesPerStrip = True
    endOfLife = True
    chapters = ('1 Sirens',
                '2 Black and White',
                '3 Black and White - Princess and Knight',
                '4 Black and White - part 3')

    def namer(self, imageUrl, pageUrl):
        # Prepend chapter number to image filename
        for chapter in self.chapters:
            if chapter in pageUrl:
                chapterNum = chapter[0]
        return chapterNum + '_' + imageUrl.rsplit('/', 1)[-1]

    def getPrevUrl(self, url, data):
        # Fix missing navigation links between chapters
        if url == self.stripUrl % (self.chapters[3], '0'):
            return self.stripUrl % (self.chapters[2], 'latest')
        if url == self.stripUrl % (self.chapters[2], '0'):
            return self.stripUrl % (self.chapters[1], 'latest')
        if url == self.stripUrl % (self.chapters[1], '0'):
            return self.stripUrl % (self.chapters[0], 'latest')
        return super(WereIWolf, self).getPrevUrl(url, data)

    def getIndexStripUrl(self, index):
        # Get comic strip URL from index
        index = index.split('-')
        return self.stripUrl % (index[0], index[1])


class WhiteNoise(WordPressWebcomic):
    url = 'http://whitenoisecomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'book-one'
    imageSearch = '//div[@id="comic"]//img'


class WhiteNoiseLee(ComicControlScraper):
    url = 'http://www.white-noise-comic.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '1-0'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 1)[-1] + '.' + imageUrl.rsplit('.', 1)[-1]


class Whomp(ComicControlScraper):
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


class Widdershins(ComicControlScraper):
    url = 'https://widdershinscomic.com/'
    stripUrl = url + 'wdshn/%s'
    firstStripUrl = stripUrl % 'sleight-of-hand-cover'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 1)[-1] + '.' + imageUrl.rsplit('.', 1)[-1]


class Wigu(_ParserScraper):
    stripUrl = 'http://www.wigucomics.com/adventures/index.php?comic=%s'
    url = stripUrl % '-1'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic"]//img[contains(@src, "/comics/")]'
    prevSearch = '//a[@alt="go back"]'
    endOfLife = True
    help = 'Index format: n'


class WildeLife(ComicControlScraper):
    url = 'http://www.wildelifecomic.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '1'


class Wolfpac(WordPressScraper):
    url = 'https://wolfpac.ca/'
    firstStripUrl = url + 'archives/comic/wolfpac-title'


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


class Wondermark(WordPressScraper):
    url = 'http://wondermark.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '001'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: nnn (001-999), 1knn (1000-1099), cnnnn (1100-)'


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

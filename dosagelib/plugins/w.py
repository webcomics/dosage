# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre


class WapsiSquare(_BasicScraper):
    url = 'http://wapsisquare.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(r'<img src="(http://wapsisquare.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>Previous</a>')
    help = 'Index format: strip-name'


class WastedTalent(_BasicScraper):
    url = 'http://www.wastedtalent.ca/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.wastedtalent\.ca/sites/default/files/imagecache/comic_full/comics/\d+/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)', after="comic_prev"))
    help = 'Index format: stripname'


class WayfarersMoon(_BasicScraper):
    url = 'http://www.wayfarersmoon.com/'
    stripUrl = url + 'index.php?page=%s'
    imageSearch = compile(r'<img src="(/admin.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back.gif')
    help = 'Index format: nn'


class WeCanSleepTomorrow(_BasicScraper):
    url = 'http://wecansleeptomorrow.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://wecansleeptomorrow\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://wecansleeptomorrow\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class WhiteNinja(_BasicScraper):
    url = 'http://www.whiteninjacomics.com/comics.shtml'
    stripUrl = 'http://www.whiteninjacomics.com/comics/%s.shtml'
    imageSearch = compile(r'<img src=(/images/comics/(?!t-).+?\.gif) border=0')
    prevSearch = compile(r'(/comics/.+?shtml).+?previous')
    help = 'Index format: s (comic name)'


class WhyTheLongFace(_BasicScraper):
    url = 'http://www.absurdnotions.org/wtlf200709.html'
    stripUrl = 'http://www.absurdnotions.org/wtlf%s.html'
    imageSearch = compile(r'<img src="(http://www.absurdnotions.org/wtlf.+?|lf\d+.\w{1,4})"', IGNORECASE)
    multipleImagesPerStrip = True
    prevSearch = compile(r'HREF="(.+?)"><IMG SRC="nprev.gif" ')
    help = 'Index format: yyyymm'


class Wigu(_BasicScraper):
    url = 'http://wigucomics.com/'
    stripUrl = url + 'adventures/index.php?comic=%s'
    imageSearch = compile(tagre("img", "src", r'(/adventures/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/adventures/index\.php\?comic=\d+)', after="go back"))
    help = 'Index format: n'


class Wonderella(_BasicScraper):
    url = 'http://nonadventures.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://nonadventures\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://nonadventures\.com/\d+/\d+/\d+/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class WorldOfMrToast(_BasicScraper):
    baseurl = 'http://www.theimaginaryworld.com/'
    url = baseurl + 'mrTcomicA.html'
    stripUrl = baseurl + '%s.html'
    imageSearch = compile(tagre("img", "src", r'(comic[^"]+)'))
    # list the archive links since there is no prev/next navigation
    prevurls = (
        url,
        baseurl + 'mrTcomicW02.html',
        baseurl + 'mrTcomicW01.html',
        baseurl + 'mrGcomic03.html',
        baseurl + 'mrGcomic02.html',
        baseurl + 'mrGcomic01.html',
        baseurl + 'mrTcomicT05.html',
        baseurl + 'mrTcomicT04.html',
        baseurl + 'mrTcomicT03.html',
        baseurl + 'mrTcomicT02.html',
        baseurl + 'mrTcomicT01.html',
        baseurl + 'mrTcomicIW3.html',
        baseurl + 'mrTcomicIW2.html',
        baseurl + 'mrTcomicIW1.html',
    )
    firstStripUrl = prevurls[-1]
    multipleImagesPerStrip = True
    help = 'Index format: none'

    def getPrevUrl(self, url, data, baseUrl):
        idx = self.prevurls.index(url)
        try:
            return self.prevurls[idx+1]
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
    latestChapter = 4
    multipleImagesPerStrip = True

    @classmethod
    def starter(cls):
        return '%schapters/chapter%02d/%s/index.php' % (
            cls.url, cls.latestChapter, cls.lang.upper())

    def getPrevUrl(self, url, data, baseUrl):
        """Find previous URL."""
        if 'chapter04' in url:
            return url.replace('chapter04', 'chapter03')
        if 'chapter03' in url:
            return url.replace('chapter03', 'chapter02')
        if 'chapter02' in url:
            return url.replace('chapter02', 'chapter01')
        return None


class WormWorldSagaGerman(WormWorldSaga):
    lang = 'de'

class WormWorldSagaSpanish(WormWorldSaga):
    lang = 'es'

class WormWorldSagaFrench(WormWorldSaga):
    lang = 'fr'


class WotNow(_BasicScraper):
    url = 'http://shadowburn.binmode.com/wotnow/'
    stripUrl = url + 'comic.php?comic_id=%s'
    imageSearch = compile(r'<IMG SRC="(comics/.+?)"')
    prevSearch = compile(r'<A HREF="(.+?)"><IMG SRC="images/b_prev.gif" ')
    help = 'Index format: n (unpadded)'


# XXX disallowed by robots.txt
class _WorldOfWarcraftEh(_BasicScraper):
    url = 'http://woweh.com/'
    stripUrl = None
    imageSearch = compile(r'http://woweh.com/(comics/.+?)"')
    prevSearch = compile(r'woweh.com/(\?p=.+:?)".+:?="prev')


class Wulffmorgenthaler(_BasicScraper):
    url = 'http://wumocomicstrip.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(/img/strip/[^/"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "<span>Previous")
    help = 'Index format: yyyy/mm/dd'


class WhiteNoise(_BasicScraper):
    url = 'http://www.wncomic.com/archive.php'
    stripUrl = 'http://www.wncomic.com/archive_comments.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="images/top_back.jpg" ')
    help = 'Index format: n'


class Wondermark(_BasicScraper):
    url = 'http://wondermark.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(r'<img src="(http://wondermark.com/c/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" rel="prev">')
    help = 'Index format: nnn'

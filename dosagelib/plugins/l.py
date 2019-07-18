# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import bounceStarter, indirectStarter
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNaviIn


class Lackadaisy(_ParserScraper):
    url = 'https://www.lackadaisy.com/comic.php'
    stripUrl = url + '?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="content"]/img'
    prevSearch = '//div[@class="prev"]/a'
    nextSearch = '//div[@class="next"]/a'
    help = 'Index format: n'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        # Use comic id for filename
        num = pageUrl.rsplit('=', 1)[-1]
        ext = imageUrl.rsplit('.', 1)[-1]
        return 'lackadaisy_%s.%s' % (num, ext)


class Laiyu(_WordPressScraper):
    url = 'http://www.flowerlarkstudios.com/comicpage/preliminary-concepts/welcome/'
    firstStripUrl = url
    starter = indirectStarter


class LasLindas(_BasicScraper):
    url = 'http://laslindas.katbox.net/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/[^"]+)' % rurl, after="attachment-full"))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'


class LastResort(_WordPressScraper):
    url = 'http://www.lastres0rt.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'that-sound-you-hear-is-a-shattered-stereotype'


class LeastICouldDo(_ParserScraper):
    url = 'http://www.leasticoulddo.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '20030210'
    imageSearch = '//div[@id="content-comic"]//img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@id="latest-comic"]'
    starter = indirectStarter
    help = 'Index format: yyyymmdd'


class LetsSpeakEnglish(_ComicControlScraper):
    url = 'http://www.marycagle.com'


class LifeAintNoPonyFarm(_WordPressScraper):
    url = 'http://sarahburrini.com/en/'
    firstStripUrl = url + 'comic/my-first-webcomic/'
    multipleImagesPerStrip = True


class LittleGamers(_BasicScraper):
    url = 'http://www.little-gamers.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2000/12/01/99'
    imageSearch = compile(tagre("img", "src", r'(http://little-gamers\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.little-gamers\.com/[^"]+)', before="comic-nav-prev-link"))
    help = 'Index format: yyyy/mm/dd/name'


class LittleTales(_ParserScraper):
    url = 'http://www.little-tales.com/'
    stripUrl = url + 'index.php?Strip=%s'
    firstStripUrl = stripUrl % '1'
    url = stripUrl % '450'
    imageSearch = '//img[contains(@src, "strips/")]'
    prevSearch = '//a[./img[@alt="BACK"]]'
    nextSearch = '//a[./img[@alt="FORWARD"]]'
    starter = bounceStarter
    nav = {
        '517': '515',
        '449': '447'
    }

    def namer(self, imageUrl, pageUrl):
        page = pageUrl.rsplit('=', 1)[-1]
        ext = imageUrl.rsplit('.', 1)[-1]
        return page + '.' + ext

    def getPrevUrl(self, url, data):
        # Skip missing pages with broken navigation links
        page = url.rsplit('=', 1)[1]
        if page in self.nav:
            return self.stripUrl % self.nav[page]
        return super(LittleTales, self).getPrevUrl(url, data)


class LoadingArtist(_ParserScraper):
    url = 'http://www.loadingartist.com/latest'
    imageSearch = '//div[@class="comic"]//img'
    prevSearch = "//a[contains(concat(' ', @class, ' '), ' prev ')]"


class LoFiJinks(_WPNaviIn):
    url = 'http://hijinksensue.com/comic/learning-to-love-again/'
    firstStripUrl = 'http://hijinksensue.com/comic/lo-fijinks-everything-i-know-anout-james-camerons-avatar-movie/'
    endOfLife = True


class LookingForGroup(_ParserScraper):
    url = 'https://www.lfg.co/'
    stripUrl = url + 'page/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic-img"]//img'
    prevSearch = '//a[@class="comic-nav-prev"]'
    latestSearch = '//div[@id="feature-lfg-footer"]/a[contains(@href, "page/")]'
    starter = indirectStarter
    help = 'Index format: nnn'

    def namer(self, imageUrl, pageUrl):
        page = pageUrl.rstrip('/').rsplit('/', 1)[-1]
        return page.replace('2967', '647')

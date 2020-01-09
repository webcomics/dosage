# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..helpers import bounceStarter, indirectStarter
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import _WordPressScraper, _WPNavi


class OctopusPie(_ParserScraper):
    url = 'http://www.octopuspie.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007-05-14/001-pea-wiggle'
    imageSearch = '//img[@title]'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy-mm-dd/nnn-strip-name'


class OffWhite(_ParserScraper):
    stripUrl = 'http://off-white.eu/comic/%s/'
    firstStripUrl = stripUrl % 'prologue-page-1-2'
    url = firstStripUrl
    imageSearch = '//img[@class="comic-page"]'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[text()="A"]'
    starter = indirectStarter
    endOfLife = True

    def fetchUrls(self, url, data, urlSearch):
        # Fix missing page
        if url == self.stripUrl % 'page-37':
            return ['http://off-white.eu/ow_v2/wp-content/uploads/2011/01/new-037.jpg']
        return super(OffWhite, self).fetchUrls(url, data, urlSearch)

    def getPrevUrl(self, url, data):
        # Fix missing page
        if url == self.stripUrl % 'page-37':
            return self.stripUrl % 'page-36'
        return super(OffWhite, self).getPrevUrl(url, data)


class Oglaf(_ParserScraper):
    url = 'http://oglaf.com/'
    stripUrl = url + '%s/'
    imageSearch = '//img[@id="strip"]'
    # search for "previous story" only
    prevSearch = '//link[@rel="prev"]'
    # search for "next page"
    nextSearch = '//link[@rel="next"]'
    multipleImagesPerStrip = True
    adult = True

    def fetchUrls(self, url, data, search):
        urls = []
        urls.extend(super(Oglaf, self).fetchUrls(url, data, search))
        if search == self.imageSearch:
            try:
                nexturls = self.fetchUrls(url, data, self.nextSearch)
            except ValueError:
                pass
            else:
                while nexturls and nexturls[0].startswith(url):
                    data = self.getPage(nexturls[0])
                    urls.extend(super(Oglaf, self).fetchUrls(nexturls, data, search))
                    nexturls = self.fetchUrls(url, data, self.nextSearch)
        return urls


class OhJoySexToy(_WPNavi):
    url = 'http://www.ohjoysextoy.com/'
    firstStripUrl = url + 'introduction/'
    textSearch = '//div[@id="comic"]//img/@alt'
    adult = True


class OkCancel(_BasicScraper):
    url = 'http://okcancel.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%sstrips/okcancel\d{8}\.gif)' % rurl))
    prevSearch = compile(tagre("div", "class", "previous") +
                         tagre("a", "href", r'(%scomic/\d{1,4}\.html)' % rurl))
    help = 'Index format: yyyymmdd'


class OmakeTheater(_ParserScraper):
    url = 'http://omaketheater.com/comic/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    css = True
    imageSearch = ".comicImage img"
    prevSearch = ".previous a"
    help = 'Index format: number (unpadded)'


class OnTheEdge(_WordPressScraper):
    url = 'http://ontheedgecomics.com/'
    firstStripUrl = 'http://ontheedgecomics.com/comic/ote0001/'


class OopsComicAdventure(_WordPressScraper):
    url = ('https://web.archive.org/web/20190102215141/'
        'http://oopscomicadventure.com/')
    endOfLife = True


class Optipess(_WPNavi):
    url = 'http://www.optipess.com/'
    firstStripUrl = url + '2008/12/01/jason-friend-of-the-butterflies/'
    textSearch = '//div[@id="comic"]//img/@alt'
    textOptional = True


class OrderOfTheBlackDog(_WordPressScraper):
    url = 'http://orderoftheblackdog.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        return '%s.%s' % (pageUrl.rsplit('/', 2)[-2], imageUrl.rsplit('.', 1)[-1])


class OriginalLife(_ParserScraper):
    url = 'http://jaynaylor.com/originallife/'
    stripUrl = url + 'archives/%s.html'
    firstStripUrl = stripUrl % '2009/06/001'
    imageSearch = '//img[contains(@src, "/originallife/comic/")]'
    prevSearch = '//a[contains(text(), "Previous")]'
    help = 'Index format: yyyy/mm/<your guess>'


class OurHomePlanet(_ParserScraper):
    url = 'http://www.ourhomeplanet.net/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '01'
    imageSearch = '//a[@rel="next"]/img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: n (unpadded)'


class OutOfPlacers(_WordPressScraper):
    url = 'http://www.valsalia.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'prologue/01'


class OverCompensating(_BasicScraper):
    url = 'http://www.overcompensating.com/'
    stripUrl = url + 'oc/index.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(/oc/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/oc/index\.php\?comic=\d+)',
                               after="go back"))
    help = 'Index format: number'


class OzyAndMillie(_WordPressScraper):
    stripUrl = 'https://ozyandmillie.org/comic/%s/'
    url = stripUrl % 'ozy-and-millie-2131'
    firstStripUrl = stripUrl % 'ozy-and-millie-2'
    endOfLife = True

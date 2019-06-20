# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..helpers import bounceStarter
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import _WordPressScraper, _WPNavi, WP_LATEST_SEARCH


class OctopusPie(_ParserScraper):
    url = 'http://www.octopuspie.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007-05-14/001-pea-wiggle'
    imageSearch = '//img[@title]'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy-mm-dd/nnn-strip-name'


class Oglaf(_ParserScraper):
    url = 'http://oglaf.com/'
    stripUrl = url + '%s/'
    imageSearch = '//img[@id="strip"]'
    # search for "previous story" only
    prevSearch = '//a[div[@id="pvs"]]'
    # search for "next page"
    nextSearch = '//a[div[@id="nx"]]'
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


class OnTheFastrack(_BasicScraper):
    url = 'http://onthefastrack.com/'
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % 'november-13-2000'
    imageSearch = compile(r'(https://safr\.kingfeatures\.com/idn/cnfeed/zone/js/content\.php\?file=.+)"')
    prevSearch = compile(r'id="previouscomic" class="button white"><a href="(%scomics/[a-z0-9-]+/)"' % url)
    help = 'Index format: monthname-dd-yyyy'

    def namer(self, image_url, page_url):
        name = page_url.rsplit('/', 3)[2]
        if name == "onthefastrack.com":
                import datetime
                name = datetime.date.today().strftime("%B-%d-%Y")
        # name.title ensures that the comics are named the same
        # as in the previous scraper
        return "%s.gif" % name.title()


class OopsComicAdventure(_WordPressScraper):
    url = 'http://oopscomicadventure.com/'


class Optipess(_WPNavi):
    url = 'http://www.optipess.com/'
    firstStripUrl = url + '2008/12/01/jason-friend-of-the-butterflies/'
    textSearch = '//div[@id="comic"]//img/@alt'
    textOptional = True


class OrderOfTheBlackDog(_WordPressScraper):
    url = 'http://orderoftheblackdog.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'
    nextSearch = WP_LATEST_SEARCH
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


class OverCompensating(_BasicScraper):
    url = 'http://www.overcompensating.com/'
    stripUrl = url + 'oc/index.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(/oc/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/oc/index\.php\?comic=\d+)',
                               after="go back"))
    help = 'Index format: number'

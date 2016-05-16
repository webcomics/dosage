# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, IGNORECASE

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import _ComicControlScraper, _TumblrScraper, _WordPressScraper


class TheBrads(_BasicScraper):
    url = 'http://bradcolbow.com/archive/C4/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'P125'
    imageSearch = compile(tagre("img", "src", r'(http://s3\.amazonaws\.com/the_brads/the-?brads[-_][^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://bradcolbow\.com/archive/C4/[^"]+)', before="prev"))
    multipleImagesPerStrip = True
    help = 'Index format: a letter and a number'


class TheDevilsPanties(_BasicScraper):
    url = 'http://thedevilspanties.com/'
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '300'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.thedevilspanties\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archives/\d+)',
                               after="Previous"))
    help = 'Index format: number'


class TheDreamlandChronicles(_WordPressScraper):
    url = 'http://www.thedreamlandchronicles.com/'


class TheGamerCat(_ParserScraper):
    url = "http://www.thegamercat.com/"
    stripUrl = url + "comic/%s/"
    firstStripUrl = stripUrl % "06102011"
    css = True
    imageSearch = '#comic img'
    prevSearch = '.comic-nav-previous'
    help = 'Index format: stripname'


class TheGentlemansArmchair(_WordPressScraper):
    url = 'http://thegentlemansarmchair.com/'


class TheLandscaper(_BasicScraper):
    stripUrl = 'http://landscaper.visual-assault.net/comic/%s'
    url = stripUrl % 'latest'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src",
                                r'(/comics/comic/comic_page/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)') +
                         '&lsaquo; Previous')
    help = 'Index format: name'


class TheMelvinChronicles(_WordPressScraper):
    url = 'http://melvin.jeaniebottle.com/'


class TheNoob(_WordPressScraper):
    url = 'http://thenoobcomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '1'
    help = 'Index format: n (unpadded)'


class TheOrderOfTheStick(_BasicScraper):
    url = 'http://www.giantitp.com/'
    stripUrl = url + 'comics/oots%s.html'
    firstStripUrl = stripUrl % '0001'
    imageSearch = compile(r'<IMG src="(/comics/images/[^"]+)">')
    prevSearch = compile(r'<A href="(/comics/oots\d{4}\.html)"><IMG src="/Images/redesign/ComicNav_Back.gif"')
    latestSearch = compile(r'<A href="(/comics/oots\d{4}\.html)"')
    help = 'Index format: n (unpadded)'
    starter = indirectStarter

    def namer(self, image_url, page_url):
        return page_url.rsplit('/', 1)[-1][:-5]


class TheParkingLotIsFull(_BasicScraper):
    baseUrl = 'http://plif.courageunfettered.com/'
    url = baseUrl + 'archive/arch2002.htm'
    stripUrl = baseUrl + 'archive/arch%s.htm'
    firstStripUrl = stripUrl % '1998'
    imageSearch = compile(r'<td align="center"><A TARGET=_parent HREF="(wc\d+\..+?)">')
    multipleImagesPerStrip = True
    prevSearch = compile(r'\d{4} -\s+<A HREF="(arch\d{4}\.htm)">\d{4}')
    help = 'Index format: nnn'


class TheThinHLine(_TumblrScraper):
    url = 'http://thinhline.tumblr.com/'
    firstStripUrl = url + 'post/4177372348/thl-1-a-cats-got-his-tongue-click-on-the'
    imageSearch = '//img[@id="content-image"]/@data-src'
    prevSearch = '//div[@id="pagination"]/a[text()=">"]'
    latestSearch = '//a[@class="timestamp"]'
    adult = True

    indirectImageSearch = '//div[@id="post"]//a[not(@rel) and img]'

    def getComicStrip(self, url, data):
        """The comic strip image is in a separate page."""
        subPage = self.fetchUrl(url, data, self.indirectImageSearch)
        pageData = self.getPage(subPage)
        return super(TheThinHLine, self).getComicStrip(subPage, pageData)


class TheWhiteboard(_BasicScraper):
    url = 'http://www.the-whiteboard.com/'
    stripUrl = url + 'auto%s.html'
    imageSearch = compile(r'<img SRC="(autotwb\d{1,4}.+?|autowb\d{1,4}.+?)">', IGNORECASE)
    prevSearch = compile(r'&nbsp<a href="(.+?)">previous</a>', IGNORECASE)
    help = 'Index format: twb or wb + n wg. twb1000'


class TheWotch(_WordPressScraper):
    url = 'http://www.thewotch.com/'
    firstStripUrl = url + '?comic=enter-the-wotch'


class ThisIsIndexed(_BasicScraper):
    url = 'http://thisisindexed.com/'
    rurl = escape(url)
    stripUrl = url + 'page/%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/card[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("div", "class", "nav-previous") +
                         tagre("a", "href", r'(%spage/\d+/)[^"]*' % rurl))
    help = 'Index format: number'


class ThreePanelSoul(_ComicControlScraper):
    url = 'http://threepanelsoul.com/'
    firstStripUrl = url + 'comic/a-test-comic'


class ToonHole(_WordPressScraper):
    url = 'http://toonhole.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/12/toon-hole-coming-soon-2010'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy/mm/stripname'

    def shouldSkipUrl(self, url, data):
        return url in (self.stripUrl % "2013/03/if-game-of-thrones-was-animated",)


class TracyAndTristan(_BasicScraper):
    url = 'http://tandt.thecomicseries.com/'
    rurl = escape(url)
    stripUrl = url + 'comics/%s'
    imageSearch = compile(tagre("img", "src", r'(%simages/comics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+)', after="prev"))
    help = 'Index format: number'


class TwoGuysAndGuy(_BasicScraper):
    url = 'http://www.twogag.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '4'
    imageSearch = compile(tagre('img', 'src', r'(%scomics/\d{4}-\d{2}-\d{2}[^"]*)' % rurl))
    prevSearch = compile(tagre('a', 'href', r'(%sarchives/\d+)' % rurl,
                               after='title="Previous"'))
    help = 'Index format: number'
    adult = True


class TwoLumps(_BasicScraper):
    url = 'http://www.twolumps.net/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)', after="prev"))
    help = 'Index format: yyyymmdd'

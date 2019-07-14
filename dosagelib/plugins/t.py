# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, MULTILINE

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, xpath_class
from ..util import tagre
from .common import _ComicControlScraper, _TumblrScraper, _WordPressScraper, _WPNavi
import requests


class TheBrads(_ParserScraper):
    url = 'http://bradcolbow.com/archive/'
    imageSearch = '//div[%s]//img' % xpath_class('entry')
    prevSearch = '//a[%s]' % xpath_class('prev')
    multipleImagesPerStrip = True


class TheDevilsPanties(_WPNavi):
    url = 'http://thedevilspanties.com/'
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '300'
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


class TheRockCocks(_BasicScraper):
    url = 'http://rockcocks.slipshine.net/'
    rurl = escape(url)
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % "page-1-nsfw-track-1-start"
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl, after='id="cc-comic"'))
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after='rel="prev"'))
    adult = True


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


class TheWhiteboard(_ParserScraper):
    BROKEN_PAGE_MIDDLE = compile(r'</body></html><')
    url = 'http://www.the-whiteboard.com/'
    imageSearch = '//center/img'
    prevSearch = '//a[text()="previous"]'

    # Another ugly hack :(
    def _parse_page(self, data):
        data = self.BROKEN_PAGE_MIDDLE.sub('<', data)
        return super(TheWhiteboard, self)._parse_page(data)


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
    firstStripUrl = url + 'comic/toon-hole-coming-soon-2010/'

    def shouldSkipUrl(self, url, data):
        return url in (self.url + "comic/if-game-of-thrones-was-animated/",)


class TracyAndTristan(_BasicScraper):
    url = 'http://tandt.thecomicseries.com/'
    rurl = escape(url)
    stripUrl = url + 'comics/%s'
    imageSearch = compile(tagre("img", "src", r'(%simages/comics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+)', after="prev"))
    help = 'Index format: number'


class TrippingOverYou(_BasicScraper):
    url = 'http://www.trippingoveryou.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'wiggle-room'
    imageSearch = compile(tagre("img", "src", r'([^"]+/comics/[^"]+)'))
    prevSearch = compile(r'<a class="cc-prev" rel="prev" href="(.+?)">')
    help = 'Index format: stripname'


class TumbleDryComics(_WordPressScraper):
    url = 'http://tumbledrycomics.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'we-need-to-get-high-jpg'
    textSearch = '//div[@id="comic"]//img/@alt'
    multipleImagesPerStrip = True
    adult = True
    help = 'Index format: name'

    def namer(self, image_url, page_url):
        # Most images have the date they were posted in the filename
        # For those that don't we can get the month and year from the image url
        parts = image_url.rsplit('/', 3)
        year = parts[1]
        month = parts[2]
        filename = parts[3]
        if not filename.startswith(year):
            filename = year + "-" + month + "-" + filename
        return filename


class Turnoff(_ParserScraper):
    name = 'turnoff'
    url = 'https://turnoff.us/'
    imageSearch = '//article[%s]//img' % xpath_class('post-content')
    prevSearch = '//div[%s]//a' % xpath_class('prev')
    stripUrl = url + 'geek/%s'
    firstStripUrl = stripUrl % 'tcp-buddies'
    multipleImagesPerStrip = True

    def __init__(self, *args, **kwargs):
        super(Turnoff, self).__init__(*args, **kwargs)
        # Neither the images nor the pages contain information about dates or indices.
        # However we can extract the order of the images from the JavaScript.
        html = requests.get(self.url).text
        list_regex = compile(r"""^\s*"/geek/(.*)",\s*$""", flags=MULTILINE)
        self.comics_order = list(reversed(list_regex.findall(html)))

    def namer(self, image_url, page_url):
        comic_name = page_url.split('/')[-1]
        try:
            index = self.comics_order.index(comic_name) + 1
        except ValueError:
            index = len(self.comics_order)
        file_name = image_url.split('/')[-1]
        return "%03d-%s" % (index, file_name)


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


class Twokinds(_ParserScraper):
    url = 'http://twokinds.keenspot.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//article[%s]//img' % xpath_class('comic')
    prevSearch = '//a[%s]' % xpath_class('navprev')
    help = 'Index format: n (unpadded)'


class TwoLumps(_BasicScraper):
    url = 'http://www.twolumps.net/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)', after="prev"))
    help = 'Index format: yyyymmdd'

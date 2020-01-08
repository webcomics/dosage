# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNavi


class Underling(_WPNavi):
    url = 'http://underlingcomic.com/'
    firstStripUrl = url + 'page-one/'


class Undertow(_BasicScraper):
    url = 'http://undertow.dreamshards.org/'
    imageSearch = compile(tagre("img", "src", r'([^"]+\.jpg)'))
    prevSearch = compile(r'href="(.+?)".+?teynpoint')
    latestSearch = compile(r'href="(.+?)".+?Most recent page')
    starter = indirectStarter


class unDivine(_ComicControlScraper):
    url = 'http://undivinecomic.com/'


class UnicornJelly(_BasicScraper):
    baseUrl = 'http://unicornjelly.com/'
    url = baseUrl + 'uni666.html'
    stripUrl = baseUrl + 'uni%s.html'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(r'</TABLE>(?:<FONT COLOR="BLACK">)?<IMG SRC="(images/[^"]+)" WIDTH=')
    prevSearch = compile(r'<A HREF="(uni\d{3}[bcs]?\.html)">(<FONT COLOR="BLACK">)?<IMG SRC="images/back00\.gif"')
    help = 'Index format: nnn'


class UnlikeMinerva(_ParserScraper):
    baseUrl = 'https://unlikeminerva.com/archive/index.php'
    stripUrl = baseUrl + '?week=%s'
    url = stripUrl % '127'
    firstStripUrl = stripUrl % '26'
    imageSearch = '//img[contains(@src, "archive/")]'
    prevSearch = '//a[./img[contains(@src, "previous")]]'
    multipleImagesPerStrip = True
    endOfLife = True
    help = 'Index format: number'


class Unsounded(_BasicScraper):
    url = 'http://www.casualvillain.com/Unsounded/'
    stripUrl = url + 'comic/ch%s/ch%s_%s.html'
    firstStripUrl = stripUrl % ('01', '01', '01')
    rurl = escape(url)
    imageSearch = compile(tagre("img", "src", r'(pageart/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*)', after='class="back'))
    latestSearch = compile(tagre("a", "href", r'(%scomic/[^"]*)' % rurl) +
                           tagre("img", "src",
                                 r"%simages/newpages\.png" % rurl))
    starter = indirectStarter
    help = 'Index format: chapter-number'

    def getIndexStripUrl(self, index):
        """Get comic strip URL from index."""
        chapter, num = index.split('-')
        return self.stripUrl % (chapter, chapter, num)


class UrgentTransformationCrisis(_WordPressScraper):
    url = 'http://www.catomix.com/utc/'
    firstStripUrl = url + 'comic/cover1'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1].rsplit('?', 1)[0]
        return filename.replace('FVLYHD', 'LYHDpage').replace('UTC084web', '20091218c')

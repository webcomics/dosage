# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, xpath_class
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNavi


class Underling(_WPNavi):
    url = ('https://web.archive.org/web/20190806120425/'
        'http://underlingcomic.com/')
    firstStripUrl = url + 'page-one/'
    endOfLife = True


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


class Unsounded(_ParserScraper):
    url = 'http://www.casualvillain.com/Unsounded/'
    startUrl = url + 'comic+index/'
    stripUrl = url + 'comic/ch%s/ch%s_%s.html'
    firstStripUrl = stripUrl % ('01', '01', '01')
    imageSearch = '//img[contains(@src, "/pageart/ch")]'
    prevSearch = '//a[{}]'.format(xpath_class('back'))
    latestSearch = '//div[@id="chapter_box"][1]//a[last()]'
    multipleImagesPerStrip = True
    starter = indirectStarter
    help = 'Index format: chapter-page'

    def getPrevUrl(self, url, data):
        # Fix missing navigation links between chapters
        if 'ch13/you_let_me_fall' in url:
            return self.stripUrl % ('13', '13', '85')
        return super(Unsounded, self).getPrevUrl(url, data)

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

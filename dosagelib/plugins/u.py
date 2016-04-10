# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import _WordPressScraper, xpath_class


class Underling(_WordPressScraper):
    url = 'http://underlingcomic.com/'
    firstStripUrl = url + 'page-one/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')


class Undertow(_BasicScraper):
    url = 'http://undertow.dreamshards.org/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'([^"]+\.jpg)'))
    prevSearch = compile(r'href="(.+?)".+?teynpoint')
    help = 'Index format: good luck !'
    starter = indirectStarter(url,
                              compile(r'href="(.+?)".+?Most recent page'))


class UnicornJelly(_BasicScraper):
    baseUrl = 'http://unicornjelly.com/'
    url = baseUrl + 'uni666.html'
    stripUrl = baseUrl + 'uni%s.html'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(r'</TABLE>(?:<FONT COLOR="BLACK">)?<IMG SRC="(images/[^"]+)" WIDTH=')
    prevSearch = compile(r'<A HREF="(uni\d{3}[bcs]?\.html)">(<FONT COLOR="BLACK">)?<IMG SRC="images/back00\.gif"')
    help = 'Index format: nnn'


class Unsounded(_BasicScraper):
    url = 'http://www.casualvillain.com/Unsounded/'
    stripUrl = url + 'comic/ch%s/ch%s_%s.html'
    firstStripUrl = stripUrl % ('01', '01', '01')
    rurl = escape(url)
    imageSearch = compile(tagre("img", "src", r'(pageart/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*)', after='class="back'))
    starter = indirectStarter(
        url, compile(tagre("a", "href", r'(%scomic/[^"]*)' % rurl) +
                     tagre("img", "src", r"%simages/newpages\.png" % rurl)))
    help = 'Index format: chapter-number'

    def getIndexStripUrl(self, index):
        """Get comic strip URL from index."""
        chapter, num = index.split('-')
        return self.stripUrl % (chapter, chapter, num)

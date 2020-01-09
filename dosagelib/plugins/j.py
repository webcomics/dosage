# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper
from ..util import tagre
from ..helpers import indirectStarter, xpath_class
from .common import _ComicControlScraper


class JackCannon(_BasicScraper):
    url = 'http://fancyadventures.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/07/07/2008-07-08'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/page-nnn'


class JimBenton(_BasicScraper):
    url = 'http://www.jimbenton.com/page14/page14.html'
    stripUrl = 'http://www.jimbenton.com/page14/files/JimBentonComic-%s.html'
    starter = indirectStarter
    imageSearch = compile(tagre("img", "src", r'(JimBentonComic-[^"]+)',
                                before="photo-frame"))
    prevSearch = compile(tagre("a", "href", r'(JimBentonComic-[^>]+\.html)',
                               quote="") + "Next")
    latestSearch = compile(tagre("a", "href", r'(files/JimBentonComic-[^>]+\.html)', quote=""))
    help = 'Index format: stripname'


class JoeAndMonkey(_BasicScraper):
    url = 'http://www.joeandmonkey.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'"(/comic/[^"]+)"')
    prevSearch = compile(r"<a href='(/\d+)'>Previous")
    help = 'Index format: nnn'


class JohnnyWander(_ComicControlScraper):
    imageSearch = ('//ul[%s]/li/@data-src' % xpath_class('cc-showbig'),
                   _ComicControlScraper.imageSearch)
    url = 'http://www.johnnywander.com/'


class JustAnotherEscape(_BasicScraper):
    url = 'http://www.justanotherescape.com/'
    rurl = escape(url)
    stripUrl = url + 'index.cgi?date=%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href",
                               r'(%s/index\.cgi\?date=\d+)' % rurl) +
                         tagre("img", "alt", "Previous Comic"))
    help = 'Index format: yyyymmdd'

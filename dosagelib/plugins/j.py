# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
from re import compile, escape

from ..scraper import BasicScraper
from ..util import tagre
from ..helpers import indirectStarter
from .common import ComicControlScraper


class JackCannon(BasicScraper):
    url = 'http://fancyadventures.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/07/07/2008-07-08'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/page-nnn'


class JimBenton(BasicScraper):
    url = 'http://www.jimbenton.com/page14/page14.html'
    stripUrl = 'http://www.jimbenton.com/page14/files/JimBentonComic-%s.html'
    starter = indirectStarter
    imageSearch = compile(tagre("img", "src", r'(JimBentonComic-[^"]+)',
                                before="photo-frame"))
    prevSearch = compile(tagre("a", "href", r'(JimBentonComic-[^>]+\.html)',
                               quote="") + "Next")
    latestSearch = compile(tagre("a", "href", r'(files/JimBentonComic-[^>]+\.html)', quote=""))
    help = 'Index format: stripname'


class JoeAndMonkey(BasicScraper):
    url = 'http://www.joeandmonkey.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'"(/comic/[^"]+)"')
    prevSearch = compile(r"<a href='(/\d+)'>Previous")
    help = 'Index format: nnn'


class JohnnyWander(ComicControlScraper):
    imageSearch = ('//ul[d:class("cc-showbig")]/li/@data-src',
        '//img[@id="cc-comic"]')
    url = 'http://www.johnnywander.com/'

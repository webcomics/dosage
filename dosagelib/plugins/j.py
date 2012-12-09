# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre


class JackCannon(_BasicScraper):
    latestUrl = 'http://fancyadventures.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://fancyadventures\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://fancyadventures\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/page-nnn'


class JerkCity(_BasicScraper):
    latestUrl = 'http://www.jerkcity.com/'
    stripUrl = latestUrl + '_jerkcity%s.html'
    imageSearch = compile(tagre("img", "src", r'(/jerkcity[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/_jerkcity[^"]+)') + r'&lt;&lt;Previous')
    help = 'Index format: n'


class JoeAndMonkey(_BasicScraper):
    latestUrl = 'http://www.joeandmonkey.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'"(/comic/[^"]+)"')
    prevSearch = compile(r"<a href='(/\d+)'>Previous")
    help = 'Index format: nnn'


class JohnnyWander(_BasicScraper):
    latestUrl = 'http://www.johnnywander.com/'
    stripUrl = latestUrl + 'comics/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.johnnywander\.com/files/comics/\d+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+)') + r'prev')
    help = 'Index format: nnn'


class JustAnotherEscape(_BasicScraper):
    latestUrl = 'http://www.justanotherescape.com/'
    stripUrl = latestUrl + 'index.cgi?date=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.justanotherescape\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.justanotherescape\.com//index\.cgi\?date=\d+)')
     + tagre("img", "alt", "Previous Comic"))
    help = 'Index format: yyyymmdd'

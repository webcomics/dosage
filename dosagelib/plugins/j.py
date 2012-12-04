# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre


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

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..util import tagre


class JackCannon(_BasicScraper):
    url = 'http://fancyadventures.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/page-nnn'


class JerkCity(_BasicScraper):
    url = 'http://www.jerkcity.com/'
    stripUrl = url + '_jerkcity%s.html'
    imageSearch = compile(tagre("img", "src", r'(/jerkcity[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/_jerkcity[^"]+)') + r'&lt;&lt;Previous')
    help = 'Index format: n'


class JoeAndMonkey(_BasicScraper):
    url = 'http://www.joeandmonkey.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'"(/comic/[^"]+)"')
    prevSearch = compile(r"<a href='(/\d+)'>Previous")
    help = 'Index format: nnn'


class JohnnyWander(_BasicScraper):
    url = 'http://www.johnnywander.com/'
    stripUrl = url + 'comics/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.johnnywander\.com/files/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+)') + r'prev')
    help = 'Index format: nnn'


class JustAnotherEscape(_BasicScraper):
    url = 'http://www.justanotherescape.com/'
    rurl = escape(url)
    stripUrl = url + 'index.cgi?date=%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.cgi\?date=\d+)' % rurl)
     + tagre("img", "alt", "Previous Comic"))
    help = 'Index format: yyyymmdd'

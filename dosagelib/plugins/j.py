# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..util import tagre
from ..helpers import indirectStarter


class JackCannon(_BasicScraper):
    url = 'http://fancyadventures.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/07/07/2008-07-08'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/page-nnn'


class JerkCity(_BasicScraper):
    url = 'http://www.jerkcity.com/'
    stripUrl = url + '_jerkcity%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/jerkcity[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/_jerkcity[^"]+)') + r'&lt;&lt;Previous')
    help = 'Index format: n'


class JimBenton(_BasicScraper):
    url = 'http://www.jimbenton.com/page14/page14.html'
    stripUrl = 'http://www.jimbenton.com/page14/files/JimBentonComic-%s.html'
    starter = indirectStarter(url, compile(tagre("a", "href", r'(files/JimBentonComic-[^>]+\.html)', quote="")))
    imageSearch = compile(tagre("img", "src", r'(JimBentonComic-[^"]+)', before="photo-frame"))
    prevSearch = compile(tagre("a", "href", r'(JimBentonComic-[^>]+\.html)', quote="") + "Next")
    help = 'Index format: stripname'


class JoeAndMonkey(_BasicScraper):
    url = 'http://www.joeandmonkey.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'"(/comic/[^"]+)"')
    prevSearch = compile(r"<a href='(/\d+)'>Previous")
    help = 'Index format: nnn'


class JohnnyWander(_BasicScraper):
    url = 'http://www.johnnywander.com/'
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % '423'
    imageSearch = compile(tagre("img", "src", r'(http://www\.johnnywander\.com/files/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+)') + r'prev')
    help = 'Index format: nnn'


class JustAnotherEscape(_BasicScraper):
    url = 'http://www.justanotherescape.com/'
    rurl = escape(url)
    stripUrl = url + 'index.cgi?date=%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s/index\.cgi\?date=\d+)' % rurl)
     + tagre("img", "alt", "Previous Comic"))
    help = 'Index format: yyyymmdd'

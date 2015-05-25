# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..util import tagre


class IAmArg(_BasicScraper):
    url = 'http://iamarg.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2011/05/08/05082011'
    imageSearch = compile(tagre("img", "src", r'(//iamarg.com/comics/\d+-\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ICanBarelyDraw(_BasicScraper):
    url = 'http://www.icanbarelydraw.com/comic/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '39'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+-[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+)' % rurl))
    help = 'Index format: number'


class InternetWebcomic(_BasicScraper):
    url = 'http://www.internet-webcomic.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '30'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"/]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="navi navi-prev"))
    help = 'Index format: n'


class IrregularWebcomic(_BasicScraper):
    url = 'http://www.irregularwebcomic.net/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<img .*src="(.*comics/.*(png|jpg|gif))".*>')
    prevSearch = compile(r'<a href="(/\d+\.html|/cgi-bin/comic\.pl\?comic=\d+)">Previous ')
    help = 'Index format: nnn'

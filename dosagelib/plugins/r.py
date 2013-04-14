# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..helpers import bounceStarter
from ..util import tagre


class RadioactivePanda(_BasicScraper):
    url = 'http://www.radioactivepanda.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(r'<img src="(/Assets/.*?)".+?"comicimg"')
    prevSearch = compile(r'<a href="(/comic/.*?)".+?previous_btn')
    help = 'Index format: n (no padding)'


class RealLife(_BasicScraper):
    url = 'http://www.reallifecomics.com/'
    stripUrl = url + 'archive/%s.html'
    firstStripUrl = stripUrl % '991115'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/\d+.html)') + tagre("img", "src", r'/images/nav_prev\.png'))
    help = 'Index format: yymmdd)'


class RealmOfAtland(_BasicScraper):
    url = 'http://www.realmofatland.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '1'
    prevSearch = compile(tagre("a", "href", r'(\?p=\d+)', after="cg_back"))
    imageSearch = compile(tagre("img", "src", r'(images/strips/atland\d+.[^"]+)'))
    help = 'Index format: nnn'


class RedMeat(_BasicScraper):
    baseUrl = 'http://www.redmeat.com/redmeat/'
    url = baseUrl + 'current/index.html'
    starter = bounceStarter(url, compile(r'<a href="(\.\./\d{4}-\d{2}-\d{2}/index\.html)">next</a>'))
    stripUrl = baseUrl + '%s/index.html'
    firstStripUrl = stripUrl % '1996-06-10'
    imageSearch = compile(r'<img src="(index-1\.gif)" width="\d+" height="\d+" [^>]*>')
    prevSearch = compile(r'<a href="(\.\./\d{4}-\d{2}-\d{2}/index\.html)">previous</a>')
    help = 'Index format: yyyy-mm-dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.split('/')[-2]


class RedString(_BasicScraper):
    description = u'A web comics about love and growing up. Art by Gina Biggs.'
    url = 'http://www.redstring.strawberrycomics.com/'
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '434'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/index\.php\?id=\d+)', after="prev"))
    help = 'Index format: nnn'


class Roza(_BasicScraper):
    url = 'http://www.junglestudio.com/roza/index.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2007-05-01'
    imageSearch = compile(r'<img src="(pages/.+?)"')
    prevSearch = compile(r'<a href="(index.php\?date=.+?)">[^>].+?navtable_01.gif')
    help = 'Index format: yyyy-mm-dd'


class Ruthe(_BasicScraper):
    url = 'http://ruthe.de/'
    stripUrl = url + 'index.php?pic=%s&sort=datum&order=ASC'
    firstStripUrl = stripUrl % '1'
    lang = 'de'
    imageSearch = compile(tagre("img", "src", r'(cartoons/strip_\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?pic=[^"]+)', before="b_back"))
    help = 'Index format: number'

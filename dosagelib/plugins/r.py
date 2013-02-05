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
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/\d+.html)') + tagre("img", "src", r'/images/nav_prev\.png'))
    help = 'Index format: yymmdd)'


class RedString(_BasicScraper):
    url = 'http://www.redstring.strawberrycomics.com/'
    stripUrl = url + 'index.php?id=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/index\.php\?id=\d+)', after="prev"))
    help = 'Index format: nnn'


class Roza(_BasicScraper):
    url = 'http://www.junglestudio.com/roza/index.php'
    stripUrl = url + '?date=%s'
    imageSearch = compile(r'<img src="(pages/.+?)"')
    prevSearch = compile(r'<a href="(index.php\?date=.+?)">[^>].+?navtable_01.gif')
    help = 'Index format: yyyy-mm-dd'


class RedMeat(_BasicScraper):
    url = 'http://www.redmeat.com/redmeat/current/index.html'
    starter = bounceStarter(url, compile(r'<a href="(\.\./\d{4}-\d{2}-\d{2}/index\.html)">next</a>'))
    stripUrl = 'http://www.redmeat.com/redmeat/%s/index.html'
    imageSearch = compile(r'<img src="(index-1\.gif)" width="\d+" height="\d+" [^>]*>')
    prevSearch = compile(r'<a href="(\.\./\d{4}-\d{2}-\d{2}/index\.html)">previous</a>')
    help = 'Index format: yyyy-mm-dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.split('/')[-2]

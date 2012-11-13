# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, MULTILINE

from ..scraper import _BasicScraper


class YAFGC(_BasicScraper):
    latestUrl = 'http://yafgc.shipsinker.com/'
    stripUrl = 'http://yafgc.shipsinker.com/index.php?strip_id=%s'
    imageSearch = compile(r'(istrip_.+?)"')
    prevSearch = compile(r'(/.+?)">\r\n.+?prev.gif', MULTILINE)
    help = 'Index format: n'


class YouSayItFirst(_BasicScraper):
    latestUrl = 'http://www.yousayitfirst.com/'
    stripUrl = 'http://www.soapylemon.com/comics/index.php?date=%s'
    imageSearch = compile(r'(http://.+?comics/.+?.jpg)[^<]')
    prevSearch = compile(r'(/comics/index.php\?date=.+?)".+?P')
    help = 'Index format: yyyymmdd'


class Yirmumah(_BasicScraper):
    latestUrl = 'http://yirmumah.net/archives.php'
    stripUrl = 'http://yirmumah.net/archives.php?date=%s'
    imageSearch = compile(r'<img src="(strips/\d{8}\..*?)"')
    prevSearch = compile(r'<a href="(\?date=\d{8})">.*Previous')
    help = 'Index format: yyyymmdd'

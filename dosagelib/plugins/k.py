# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, xpath_class


class KevinAndKell(_BasicScraper):
    url = 'http://www.kevinandkell.com/'
    stripUrl = url + '%s/kk%s%s.html'
    firstStripUrl = stripUrl % ('1995', '09', '03')
    imageSearch = compile(r'<img.+?src="(/?(\d+/)?strips/kk\d+.(gif|jpg))"',
                          IGNORECASE)
    prevSearch = compile(
        r'<a.+?href="(/?(\.\./)?\d+/kk\d+\.html)"[^>]*><span>Previous Strip',
        IGNORECASE)
    help = 'Index format: yyyy-mm-dd'

    def getIndexStripUrl(self, index):
        return self.stripUrl % tuple(map(int, index.split('-')))


class Key(_BasicScraper):
    baseUrl = 'http://key.shadilyn.com/'
    url = baseUrl + 'latestpage.html'
    stripUrl = baseUrl + 'pages/%s.html'
    imageSearch = compile(r'"((?:images/.+?)|(?:pages/images/.+?))"')
    prevSearch = compile(r'</a><a href="(.+?html)".+?prev')
    help = 'Index format: nnn'


class KickInTheHead(_WordPressScraper):
    url = 'http://www.kickinthehead.org/'
    firstStripUrl = url + '2003/03/20/ipod-envy/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')


class KillSixBillionDemons(_WordPressScraper):
    url = 'http://killsixbilliondemons.com/'
    firstStripUrl = url + 'comic/kill-six-billion-demons-chapter-1/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')
    multipleImagesPerStrip = True
    adult = True


class KiwiBlitz(_ComicControlScraper):
    url = 'http://www.kiwiblitz.com'


class Krakow(_BasicScraper):
    url = 'http://www.krakow.krakowstudios.com/'
    stripUrl = url + 'archive.php?date=%s'
    firstStripUrl = stripUrl % '20081111'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(
        r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class Kukuburi(_BasicScraper):
    baseUrl = 'http://www.kukuburi.com/'
    url = baseUrl + 'current/'
    stripUrl = baseUrl + 'v2/%s/'
    firstStripUrl = stripUrl % '2007/08/09/one'
    imageSearch = compile(
        tagre("img", "src", r'(http://www\.kukuburi\.com/v2/comics/[^"]+)',
              after='alt="[^"]'))
    prevSearch = compile(r'nav-previous.+?"(http.+?)"')
    help = 'Index format: yyyy/mm/dd/stripname'


class KuroShouri(_BasicScraper):
    url = 'http://kuroshouri.com/'
    rurl = escape(url)
    stripUrl = url + '?webcomic_post=%s'
    imageSearch = compile(
        tagre("img", "src",
              r"(%swp-content/webcomic/kuroshouri/[^'\"]+)" % rurl,
              quote="['\"]"))
    prevSearch = compile(
        tagre("a", "href", r'(%s\?webcomic_post\=[^"]+)' % rurl,
              after="previous"))
    help = 'Index format: chapter-n-page-m'

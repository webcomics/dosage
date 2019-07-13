# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, IGNORECASE

from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNavi


class Kaspall(_ParserScraper):
    stripUrl = 'http://www.kaspall.com/comic/%s'
    url = stripUrl % '2015/10/11'
    firstStripUrl = '2004/08/05'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[./img[contains(@src, "prev_comic")]]'
    endOfLife = True


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


class KickInTheHead(_WPNavi):
    url = 'http://www.kickinthehead.org/'
    firstStripUrl = url + '2003/03/20/ipod-envy/'


class KillSixBillionDemons(_WPNavi):
    url = 'http://killsixbilliondemons.com/'
    firstStripUrl = url + 'comic/kill-six-billion-demons-chapter-1/'
    multipleImagesPerStrip = True
    adult = True


class Kitfox(_WordPressScraper):
    url = 'http://www.kitfox.com/wordpress/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'the-adventure-begins-almost'


class KiwiBlitz(_ComicControlScraper):
    url = 'http://www.kiwiblitz.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'welcome-to-kb'


class Krakow(_BasicScraper):
    url = 'http://www.krakow.krakowstudios.com/'
    stripUrl = url + 'archive.php?date=%s'
    firstStripUrl = stripUrl % '20081111'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(
        r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


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

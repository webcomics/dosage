# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile, IGNORECASE

from ..scraper import BasicScraper, ParserScraper
from .common import ComicControlScraper, WordPressScraper, WordPressNavi, WordPressWebcomic


class Kaspall(ParserScraper):
    stripUrl = 'http://www.kaspall.com/comic/%s'
    url = stripUrl % '2015/10/11'
    firstStripUrl = '2004/08/05'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[./img[contains(@src, "prev_comic")]]'
    endOfLife = True


class KevinAndKell(BasicScraper):
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


class KickInTheHead(WordPressNavi):
    url = 'http://www.kickinthehead.org/'
    firstStripUrl = url + '2003/03/20/ipod-envy/'


class KillSixBillionDemons(WordPressNavi):
    url = 'http://killsixbilliondemons.com/'
    firstStripUrl = url + 'comic/kill-six-billion-demons-chapter-1/'
    multipleImagesPerStrip = True
    adult = True


class Kitfox(WordPressScraper):
    url = 'http://www.kitfox.com/wordpress/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'the-adventure-begins-almost'


class KiwiBlitz(ComicControlScraper):
    url = 'http://www.kiwiblitz.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'welcome-to-kb'


class Krakow(BasicScraper):
    url = 'http://www.krakow.krakowstudios.com/'
    stripUrl = url + 'archive.php?date=%s'
    firstStripUrl = stripUrl % '20081111'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(
        r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class KuroShouri(WordPressWebcomic):
    url = 'http://kuroshouri.com/'
    stripUrl = url + 'kuroshouri/%s/'
    firstStripUrl = stripUrl % 'kuro-shouri'

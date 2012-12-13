# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, IGNORECASE
from ..scraper import _BasicScraper
from ..util import tagre

class Key(_BasicScraper):
    latestUrl = 'http://key.shadilyn.com/latestpage.html'
    stripUrl = 'http://key.shadilyn.com/pages/%s.html'
    imageSearch = compile(r'"((?:images/.+?)|(?:pages/images/.+?))"')
    prevSearch = compile(r'</a><a href="(.+?html)".+?prev')
    help = 'Index format: nnn'


class Krakow(_BasicScraper):
    latestUrl = 'http://www.krakow.krakowstudios.com/'
    stripUrl = latestUrl + 'archive.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class Kukuburi(_BasicScraper):
    latestUrl = 'http://www.kukuburi.com/current/'
    stripUrl = 'http://www.kukuburi.com/v2/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.kukuburi\.com/v2/comics/[^"]+)', after='alt="[^"]'))
    prevSearch = compile(r'nav-previous.+?"(http.+?)"')
    help = 'Index format: yyyy/mm/dd/stripname'


class KevinAndKell(_BasicScraper):
    latestUrl = 'http://www.kevinandkell.com/'
    stripUrl = latestUrl + '%s/kk%s%s.html'
    imageSearch = compile(r'<img.+?src="(/?(\d+/)?strips/kk\d+.gif)"', IGNORECASE)
    prevSearch = compile(r'<a.+?href="(/?(\.\./)?\d+/kk\d+\.html)"[^>]*><span>Previous Strip', IGNORECASE)
    help = 'Index format: yyyy-mm-dd'

    def setStrip(self, index):
        self.currentUrl = self.stripUrl % tuple(map(int, index.split('-')))


class KhaosKomix(_BasicScraper):
    adult = True
    latestUrl = 'http://www.khaoskomix.com/'
    stripUrl = latestUrl + 'komix/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.khaoskomix\.com/komiximg/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.khaoskomix\.com/komix/[^"]+)', after="Prev"))
    help = 'Index format: stripname'


class KillerKomics(_BasicScraper):
    latestUrl = 'http://www.killerkomics.com/web-comics/index_ang.cfm'
    stripUrl = 'http://www.killerkomics.com/web-comics/%s.cfm'
    imageSearch = compile(r'<img src="(http://www.killerkomics.com/FichiersUpload/Comics/.+?)"')
    prevSearch = compile(r'<div id="precedent"><a href="(.+?)"')
    help = 'Index format: strip-name'


# XXX disallowed by robots.txt
class _Kofightclub(_BasicScraper):
    latestUrl = 'http://www.kofightclub.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(\.\./images/\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'((?:http://www\.kofightclub\.com)?/d/\d+\.html)')
     + tagre("img", "alt", "Previous comic"))
    help = 'Index format: yyyymmdd'


class KuroShouri(_BasicScraper):
   latestUrl = 'http://kuroshouri.com/'
   stripUrl = latestUrl + '?webcomic_post=%s'
   imageSearch = compile(tagre("img", "src", r"(http://kuroshouri\.com/wp-content/webcomic/kuroshouri/[^'\"]+)", quote="['\"]"))
   prevSearch = compile(tagre("a", "href", r'(http://kuroshouri\.com/\?webcomic_post=[^"]+)', after="previous"))
   help = 'Index format: chapter-n-page-m'

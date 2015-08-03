# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape, IGNORECASE
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from ..helpers import indirectStarter


class KevinAndKell(_BasicScraper):
    url = 'http://www.kevinandkell.com/'
    stripUrl = url + '%s/kk%s%s.html'
    firstStripUrl = stripUrl % ('1995', '09', '03')
    imageSearch = compile(r'<img.+?src="(/?(\d+/)?strips/kk\d+.(gif|jpg))"', IGNORECASE)
    prevSearch = compile(r'<a.+?href="(/?(\.\./)?\d+/kk\d+\.html)"[^>]*><span>Previous Strip', IGNORECASE)
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


class KickInTheHead(_BasicScraper):
    url = 'http://www.kickinthehead.org/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/03/20/ipod-envy'
    imageSearch = compile(tagre("img", "src", r'(%skickinthehead3/comics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class KillerKomics(_BasicScraper):
    baseUrl = 'http://www.killerkomics.com/web-comics/'
    url = baseUrl + 'index_ang.cfm'
    stripUrl = baseUrl + '%s.cfm'
    imageSearch = compile(r'<img src="(http://www.killerkomics.com/FichiersUpload/Comics/.+?)"')
    prevSearch = compile(r'<div id="precedent"><a href="(.+?)"')
    help = 'Index format: strip-name'


# XXX disallowed by robots.txt
class _Kofightclub(_BasicScraper):
    url = 'http://www.kofightclub.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(\.\./images/\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'((?:http://www\.kofightclub\.com)?/d/\d+\.html)')
     + tagre("img", "alt", "Previous comic"))
    help = 'Index format: yyyymmdd'


class Krakow(_BasicScraper):
    url = 'http://www.krakow.krakowstudios.com/'
    stripUrl = url + 'archive.php?date=%s'
    firstStripUrl = stripUrl % '20081111'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class Kukuburi(_BasicScraper):
    baseUrl = 'http://www.kukuburi.com/'
    url = baseUrl + 'current/'
    stripUrl = baseUrl + 'v2/%s/'
    firstStripUrl = stripUrl % '2007/08/09/one'
    imageSearch = compile(tagre("img", "src", r'(http://www\.kukuburi\.com/v2/comics/[^"]+)', after='alt="[^"]'))
    prevSearch = compile(r'nav-previous.+?"(http.+?)"')
    help = 'Index format: yyyy/mm/dd/stripname'


class KuroShouri(_BasicScraper):
    url = 'http://kuroshouri.com/'
    rurl = escape(url)
    stripUrl = url + '?webcomic_post=%s'
    imageSearch = compile(tagre("img", "src", r"(%swp-content/webcomic/kuroshouri/[^'\"]+)" % rurl, quote="['\"]"))
    prevSearch = compile(tagre("a", "href", r'(%s\?webcomic_post\=[^"]+)' % rurl, after="previous"))
    help = 'Index format: chapter-n-page-m'
    starter = indirectStarter(url, prevSearch)

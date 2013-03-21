# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, IGNORECASE
from ..scraper import _BasicScraper
from ..util import tagre

class KatzenfutterGeleespritzer(_BasicScraper):
    url = 'http://www.katzenfuttergeleespritzer.de/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'dont-drink-and-drive'
    imageSearch = compile(tagre("img", "src", r'(http://www.katzenfuttergeleespritzer.de/wp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www.katzenfuttergeleespritzer.de/comic/[^"]+)', after="navi-prev"))
    help = 'Index format: stripname'
    lang = 'de'


class KevinAndKell(_BasicScraper):
    url = 'http://www.kevinandkell.com/'
    stripUrl = url + '%s/kk%s%s.html'
    imageSearch = compile(r'<img.+?src="(/?(\d+/)?strips/kk\d+.gif)"', IGNORECASE)
    prevSearch = compile(r'<a.+?href="(/?(\.\./)?\d+/kk\d+\.html)"[^>]*><span>Previous Strip', IGNORECASE)
    help = 'Index format: yyyy-mm-dd'

    def getIndexStripUrl(self, index):
        return self.stripUrl % tuple(map(int, index.split('-')))


class Key(_BasicScraper):
    url = 'http://key.shadilyn.com/latestpage.html'
    stripUrl = 'http://key.shadilyn.com/pages/%s.html'
    imageSearch = compile(r'"((?:images/.+?)|(?:pages/images/.+?))"')
    prevSearch = compile(r'</a><a href="(.+?html)".+?prev')
    help = 'Index format: nnn'


class KickInTheHead(_BasicScraper):
    url = 'http://www.kickinthehead.org/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/03/20/ipod-envy'
    imageSearch = compile(tagre("img", "src", r'(http://www\.kickinthehead\.org/kickinthehead3/comics/\d+-\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.kickinthehead\.org/\d+/\d+/\d+/[^"]+)', after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class KillerKomics(_BasicScraper):
    url = 'http://www.killerkomics.com/web-comics/index_ang.cfm'
    stripUrl = 'http://www.killerkomics.com/web-comics/%s.cfm'
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
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class Kukuburi(_BasicScraper):
    url = 'http://www.kukuburi.com/current/'
    stripUrl = 'http://www.kukuburi.com/v2/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.kukuburi\.com/v2/comics/[^"]+)', after='alt="[^"]'))
    prevSearch = compile(r'nav-previous.+?"(http.+?)"')
    help = 'Index format: yyyy/mm/dd/stripname'


class KuroShouri(_BasicScraper):
   url = 'http://kuroshouri.com/'
   stripUrl = url + '?webcomic_post=%s'
   imageSearch = compile(tagre("img", "src", r"(http://kuroshouri\.com/wp-content/webcomic/kuroshouri/[^'\"]+)", quote="['\"]"))
   prevSearch = compile(tagre("a", "href", r'(http://kuroshouri\.com/\?webcomic_post=[^"]+)', after="previous"))
   help = 'Index format: chapter-n-page-m'

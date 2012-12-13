# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre


class WayfarersMoon(_BasicScraper):
    latestUrl = 'http://www.wayfarersmoon.com/'
    stripUrl = latestUrl + 'index.php?page=%s'
    imageSearch = compile(r'<img src="(/admin.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back.gif')
    help = 'Index format: nn'


class WhiteNinja(_BasicScraper):
    latestUrl = 'http://www.whiteninjacomics.com/comics.shtml'
    stripUrl = 'http://www.whiteninjacomics.com/comics/%s.shtml'
    imageSearch = compile(r'<img src=(/images/comics/(?!t-).+?\.gif) border=0')
    prevSearch = compile(r'(/comics/.+?shtml).+?previous')
    help = 'Index format: s (comic name)'


class WhiteNoise(_BasicScraper):
    latestUrl = 'http://www.wncomic.com/archive.php'
    stripUrl = 'http://www.wncomic.com/archive_comments.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First .+?"(archive.+?)".+?top_back')
    help = 'Index format: n'


class WhyTheLongFace(_BasicScraper):
    latestUrl = 'http://www.absurdnotions.org/wtlf200709.html'
    stripUrl = 'http://www.absurdnotions.org/wtlf%s.html'
    imageSearch = compile(r'<img src="(http://www.absurdnotions.org/wtlf.+?|lf\d+.\w{1,4})"', IGNORECASE)
    multipleImagesPerStrip = True
    prevSearch = compile(r'HREF="(.+?)"><IMG SRC="nprev.gif" ')
    help = 'Index format: yyyymm'


class Wigu(_BasicScraper):
    latestUrl = 'http://wigucomics.com/'
    stripUrl = latestUrl + 'adventures/index.php?comic=%s'
    imageSearch = compile(tagre("img", "src", r'(/adventures/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/adventures/index\.php\?comic=\d+)', after="go back"))
    help = 'Index format: n'


class WotNow(_BasicScraper):
    latestUrl = 'http://shadowburn.binmode.com/wotnow/'
    stripUrl = latestUrl + 'comic.php?comic_id=%s'
    imageSearch = compile(r'<IMG SRC="(comics/.+?)"')
    prevSearch = compile(r'<A HREF="(.+?)"><IMG SRC="images/b_prev.gif" ')
    help = 'Index format: n (unpadded)'


# XXX disallowed by robots.txt
class _WorldOfWarcraftEh(_BasicScraper):
    latestUrl = 'http://woweh.com/'
    stripUrl = None
    imageSearch = compile(r'http://woweh.com/(comics/.+?)"')
    prevSearch = compile(r'woweh.com/(\?p=.+:?)".+:?="prev')


class Wulffmorgenthaler(_BasicScraper):
    latestUrl = 'http://wumocomicstrip.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(/img/strip/[^/"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "<span>Previous")
    help = 'Index format: yyyy/mm/dd'


class WhiteNoise(_BasicScraper):
    latestUrl = 'http://www.wncomic.com/archive.php'
    stripUrl = 'http://www.wncomic.com/archive_comments.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="images/top_back.jpg" ')
    help = 'Index format: n'


class WapsiSquare(_BasicScraper):
    latestUrl = 'http://wapsisquare.com/'
    stripUrl = latestUrl + 'comic/%s'
    imageSearch = compile(r'<img src="(http://wapsisquare.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>Previous</a>')
    help = 'Index format: strip-name'


class WeCanSleepTomorrow(_BasicScraper):
    latestUrl = 'http://wecansleeptomorrow.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://wecansleeptomorrow\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://wecansleeptomorrow\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Wondermark(_BasicScraper):
    latestUrl = 'http://wondermark.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(r'<img src="(http://wondermark.com/c/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" rel="prev">')
    help = 'Index format: nnn'

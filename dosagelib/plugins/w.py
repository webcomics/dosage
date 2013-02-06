# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre


class WayfarersMoon(_BasicScraper):
    url = 'http://www.wayfarersmoon.com/'
    stripUrl = url + 'index.php?page=%s'
    imageSearch = compile(r'<img src="(/admin.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back.gif')
    help = 'Index format: nn'


class WastedTalent(_BasicScraper):
    url = 'http://www.wastedtalent.ca/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.wastedtalent\.ca/sites/default/files/imagecache/comic_full/comics/\d+/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)', after="comic_prev"))
    help = 'Index format: stripname'


class WhiteNinja(_BasicScraper):
    url = 'http://www.whiteninjacomics.com/comics.shtml'
    stripUrl = 'http://www.whiteninjacomics.com/comics/%s.shtml'
    imageSearch = compile(r'<img src=(/images/comics/(?!t-).+?\.gif) border=0')
    prevSearch = compile(r'(/comics/.+?shtml).+?previous')
    help = 'Index format: s (comic name)'


class WhiteNoise(_BasicScraper):
    url = 'http://www.wncomic.com/archive.php'
    stripUrl = 'http://www.wncomic.com/archive_comments.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First .+?"(archive.+?)".+?top_back')
    help = 'Index format: n'


class WhyTheLongFace(_BasicScraper):
    url = 'http://www.absurdnotions.org/wtlf200709.html'
    stripUrl = 'http://www.absurdnotions.org/wtlf%s.html'
    imageSearch = compile(r'<img src="(http://www.absurdnotions.org/wtlf.+?|lf\d+.\w{1,4})"', IGNORECASE)
    multipleImagesPerStrip = True
    prevSearch = compile(r'HREF="(.+?)"><IMG SRC="nprev.gif" ')
    help = 'Index format: yyyymm'


class Wigu(_BasicScraper):
    url = 'http://wigucomics.com/'
    stripUrl = url + 'adventures/index.php?comic=%s'
    imageSearch = compile(tagre("img", "src", r'(/adventures/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/adventures/index\.php\?comic=\d+)', after="go back"))
    help = 'Index format: n'


class Wonderella(_BasicScraper):
    url = 'http://nonadventures.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://nonadventures\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://nonadventures\.com/\d+/\d+/\d+/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class WotNow(_BasicScraper):
    url = 'http://shadowburn.binmode.com/wotnow/'
    stripUrl = url + 'comic.php?comic_id=%s'
    imageSearch = compile(r'<IMG SRC="(comics/.+?)"')
    prevSearch = compile(r'<A HREF="(.+?)"><IMG SRC="images/b_prev.gif" ')
    help = 'Index format: n (unpadded)'


# XXX disallowed by robots.txt
class _WorldOfWarcraftEh(_BasicScraper):
    url = 'http://woweh.com/'
    stripUrl = None
    imageSearch = compile(r'http://woweh.com/(comics/.+?)"')
    prevSearch = compile(r'woweh.com/(\?p=.+:?)".+:?="prev')


class Wulffmorgenthaler(_BasicScraper):
    url = 'http://wumocomicstrip.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(/img/strip/[^/"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "<span>Previous")
    help = 'Index format: yyyy/mm/dd'


class WhiteNoise(_BasicScraper):
    url = 'http://www.wncomic.com/archive.php'
    stripUrl = 'http://www.wncomic.com/archive_comments.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="images/top_back.jpg" ')
    help = 'Index format: n'


class WapsiSquare(_BasicScraper):
    url = 'http://wapsisquare.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(r'<img src="(http://wapsisquare.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>Previous</a>')
    help = 'Index format: strip-name'


class WeCanSleepTomorrow(_BasicScraper):
    url = 'http://wecansleeptomorrow.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://wecansleeptomorrow\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://wecansleeptomorrow\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Wondermark(_BasicScraper):
    url = 'http://wondermark.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(r'<img src="(http://wondermark.com/c/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" rel="prev">')
    help = 'Index format: nnn'

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..helpers import queryNamer
from ..util import tagre


class MadamAndEve(_BasicScraper):
    latestUrl = 'http://www.madamandeve.co.za/week_of_cartns.php'
    stripUrl = None
    imageSearch = compile(r'<IMG BORDER="0" SRC="(cartoons/me\d{6}\.(gif|jpg))">')
    prevSearch = compile(r'<a href="(weekend_cartoon.php)"')


class MagicHigh(_BasicScraper):
    latestUrl = 'http://www.doomnstuff.com/magichigh/index.php'
    stripUrl = latestUrl + '?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First .+?"(/magichigh.+?)".+?top_back')
    help = 'Index format: n'



class Marilith(_BasicScraper):
    latestUrl = 'http://www.marilith.com/'
    stripUrl = latestUrl + 'archive.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)" border')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'



class MarryMe(_BasicScraper):
    latestUrl = 'http://marrymemovie.com/main/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'(/comicfolder/.+?)"')
    prevSearch = compile(r'Previous Comic:</small><br />&#171; <a href="(.+?)">')
    help = 'Index format: good luck !'


class Meek(_BasicScraper):
    latestUrl = 'http://www.meekcomic.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'meekcomic.com(/comics/.+?)"')
    prevSearch = compile(r'\s.+?(http://www.meekcomic.com/.+?)".+?Previous<')
    help = 'Index format: yyyy/mm/dd/ch-p/'


class MegaTokyo(_BasicScraper):
    latestUrl = 'http://www.megatokyo.com/'
    stripUrl = latestUrl + 'strip/%s'
    imageSearch = compile(r'"(strips/.+?)"', IGNORECASE)
    prevSearch = compile(r'"(./strip/\d+?)">Prev')
    help = 'Index format: nnnn'


class MyPrivateLittleHell(_BasicScraper):
    latestUrl = 'http://mutt.purrsia.com/mplh/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(r'<img.+?src="(comics/.+?)"')
    prevSearch = compile(r'<a.+?href="(\?date=\d+/\d+/\d+)">Prev</a>')
    help = 'Index format: mm/dd/yyyy'



class MacHall(_BasicScraper):
    latestUrl = 'http://www.machall.com/'
    stripUrl = latestUrl + 'view.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img[^>]+?src=\'drop_shadow/previous.gif\'>')
    help = 'Index format: yyyy-mm-dd'


class Melonpool(_BasicScraper):
    latestUrl = 'http://www.melonpool.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch = compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help = 'Index format: yyyymmdd'


class Misfile(_BasicScraper):
    latestUrl = 'http://www.misfile.com/'
    stripUrl = latestUrl + '?page=%s'
    imageSearch = compile(r'<img src="(overlay\.php\?pageCalled=\d+)">')
    prevSearch = compile(r'<a href="(\?page=\d+)"><img src="/images/back\.gif"')
    help = 'Index format: n (unpadded)'
    namer = queryNamer('pageCalled')



class MysteriesOfTheArcana(_BasicScraper):
    latestUrl = 'http://mysteriesofthearcana.com/'
    stripUrl = latestUrl + 'index.php?action=comics&cid='
    imageSearch = compile(r'(image.php\?type=com&i=.+?)"')
    prevSearch = compile(r'(index.php\?action=comics&cid=.+?)".+?show_prev1')
    help = 'Index format: n (unpadded)'



class MysticRevolution(_BasicScraper):
    latestUrl = 'http://www.mysticrev.com/index.php'
    stripUrl = latestUrl + '?cid=%s'
    imageSearch = compile(r'(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?prev.gif')
    help = 'Index format: n (unpadded)'



class MontyAndWooly(_BasicScraper):
    latestUrl = 'http://www.montyandwoolley.co.uk/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'<img src="(http://montyandwoolley.co.uk/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)">')
    help = 'Index format: yyyy/mm/dd/strip-name'

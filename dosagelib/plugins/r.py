# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..scraper import _BasicScraper
from ..helpers import bounceStarter


class RadioactivePanda(_BasicScraper):
    latestUrl = 'http://www.radioactivepanda.com/'
    stripUrl = latestUrl + 'comic/%s'
    imageSearch = compile(r'<img src="(/Assets/.*?)".+?"comicimg"')
    prevSearch = compile(r'<a href="(/comic/.*?)".+?previous_btn')
    help = 'Index format: n (no padding)'


class Rascals(_BasicScraper):
    latestUrl = 'http://petitesymphony.com/rascals'
    stripUrl = 'http://petitesymphony.com/comic/rascals/%s'
    imageSearch = compile(r'(http://petitesymphony.com/comics/.+?)"')
    prevSearch = compile(r"KR-nav-previous.><a href=.(http.+?).>")
    help = 'Index format: non'


class RealLife(_BasicScraper):
    latestUrl = 'http://www.reallifecomics.com/'
    stripUrl = latestUrl + 'achive/%s.html'
    imageSearch = compile(r'"(/comics/.+?)"')
    prevSearch = compile(r'"(/archive/.+?)".+?nav_previous')
    help = 'Index format: yymmdd)'



class RedString(_BasicScraper):
    latestUrl = 'http://www.redstring.strawberrycomics.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'<img src="(http://www.redstring.strawberrycomics.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous Comic</a>')
    help = 'Index format: nnn'



class Roza(_BasicScraper):
    latestUrl = 'http://www.junglestudio.com/roza/index.php'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(r'<img src="(pages/.+?)"')
    prevSearch = compile(r'<a href="(index.php\?date=.+?)">[^>].+?navtable_01.gif')
    help = 'Index format: yyyy-mm-dd'


class RedMeat(_BasicScraper):
    starter = bounceStarter('http://www.redmeat.com/redmeat/current/index.html', compile(r'<a href="(\.\./\d{4}-\d{2}-\d{2}/index\.html)">next</a>'))
    stripUrl = 'http://www.redmeat.com/redmeat/%s/index.html'
    imageSearch = compile(r'<img src="(index-1\.gif)" width="\d+" height="\d+" [^>]*>')
    prevSearch = compile(r'<a href="(\.\./\d{4}-\d{2}-\d{2}/index\.html)">previous</a>')
    help = 'Index format: yyyy-mm-dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.split('/')[-2]

class RunningWild(_BasicScraper):
    latestUrl = 'http://runningwild.katbox.net/'
    stripUrl = latestUrl + 'index.php?strip_id=%s'
    imageSearch = compile(r'="(.+?strips/.+?)"')
    prevSearch = compile(r'(index.php\?strip_id=.+?)".+?navigation_back')
    help = 'Index format: n (unpadded)'

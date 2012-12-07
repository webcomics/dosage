# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, IGNORECASE
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class TheNoob(_BasicScraper):
    latestUrl = 'http://www.thenoobcomic.com/index.php'
    stripUrl = latestUrl + '?pos=%s'
    imageSearch = compile(tagre("img", "src", r'(/headquarters/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?pos=\d+)', before="comic_nav_previous_button"))
    help = 'Index format: nnnn'


class TheOrderOfTheStick(_BasicScraper):
    latestUrl = 'http://www.giantitp.com/comics/oots0863.html'
    stripUrl = 'http://www.giantitp.com/comics/oots%s.html'
    imageSearch = compile(r'<IMG src="(/comics/images/[^"]+)">')
    prevSearch = compile(r'<A href="(/comics/oots\d{4}\.html)"><IMG src="/Images/redesign/ComicNav_Back.gif"')
    help = 'Index format: n (unpadded)'
    starter = indirectStarter('http://www.giantitp.com/', compile(r'<A href="(/comics/oots\d{4}\.html)"'))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 1)[-1][:-5]


class TheParkingLotIsFull(_BasicScraper):
    latestUrl = 'http://plif.courageunfettered.com/archive/arch2002.htm'
    stripUrl = 'http://plif.courageunfettered.com/archive/arch%s.htm'
    imageSearch = compile(r'<td align="center"><A TARGET=_parent HREF="(wc\d+\..+?)">')
    multipleImagesPerStrip = True
    prevSearch = compile(r'\d{4} -\s+<A HREF="(arch\d{4}\.htm)">\d{4}')
    help = 'Index format: nnn'


class TheWotch(_BasicScraper):
    latestUrl = 'http://www.thewotch.com/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(r"<img.+?src='(comics/.+?)'")
    prevSearch = compile(r"<link rel='Previous' href='(/\?date=\d+-\d+-\d+)'")
    help = 'Index format: yyyy-mm-dd'


class TinyKittenTeeth(_BasicScraper):
    latestUrl = 'http://www.tinykittenteeth.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.tinykittenteeth\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripname (unpadded)'


class TwoTwoOneFour(_BasicScraper):
    latestUrl = 'http://www.nitrocosm.com/go/2214_classic/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://content\.nitrocosm\.com/[^"]+)', before="gallery_display"))
    prevSearch = compile(tagre("a", "href", r'(http://www\.nitrocosm\.com/go/2214_classic/\d+/)', after="Previous"))
    help = 'Index format: n (unpadded)'


class TheWhiteboard(_BasicScraper):
    latestUrl = 'http://www.the-whiteboard.com/'
    stripUrl = latestUrl + 'auto%s.html'
    imageSearch = compile(r'<img SRC="(autotwb\d{1,4}.+?|autowb\d{1,4}.+?)">', IGNORECASE)
    prevSearch = compile(r'&nbsp<a href="(.+?)">previous</a>', IGNORECASE)
    help = 'Index format: twb or wb + n wg. twb1000'



class HMHigh(_BasicScraper):
    name = 'TheFallenAngel/HMHigh'
    latestUrl = 'http://www.thefallenangel.co.uk/hmhigh/'
    stripUrl = latestUrl + '?id=%s'
    imageSearch = compile(r'<img src="(http://www.thefallenangel.co.uk/hmhigh/img/comic/.+?)"')
    prevSearch = compile(r' <a href="(http://www.thefallenangel.co.uk/.+?)" title=".+?">Prev</a>')
    help = 'Index format: nnn'



class TheOuterQuarter(_BasicScraper):
    latestUrl = 'http://theouterquarter.com/'
    stripUrl = latestUrl + 'comic/%s'
    imageSearch = compile(r'<img src="(http://theouterquarter.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: nnn'

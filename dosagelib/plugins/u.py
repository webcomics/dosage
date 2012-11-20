# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..helpers import bounceStarter, indirectStarter
from ..util import getQueryParams, tagre


class UglyHill(_BasicScraper):
    latestUrl = 'http://www.uglyhill.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch = compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help = 'Index format: yyyymmdd'


class UnderPower(_BasicScraper):
    latestUrl = 'http://underpower.non-essential.com/'
    stripUrl = latestUrl + 'index.php?comic=%s'
    imageSearch = compile(r'<img src="(comics/\d{8}\..+?)"')
    prevSearch = compile(r'<a href="(/index.php\?comic=\d{8})"><img src="images/previous-comic\.gif"')
    help = 'Index format: yyyymmdd'


class Undertow(_BasicScraper):
    stripUrl = 'http://undertow.dreamshards.org/%s'
    imageSearch = compile(r'<img src="(.+?)"')
    prevSearch = compile(r'href="(.+?)".+?teynpoint')
    help = 'Index format: good luck !'
    starter = indirectStarter('http://undertow.dreamshards.org/',
                              compile(r'href="(.+?)".+?Most recent page'))


class UnicornJelly(_BasicScraper):
    latestUrl = 'http://unicornjelly.com/uni666.html'
    stripUrl = 'http://unicornjelly.com/uni%s.html'
    imageSearch = compile(r'</TABLE>(?:<FONT COLOR="BLACK">)?<IMG SRC="(images/[^"]+)" WIDTH=')
    prevSearch = compile(r'<A HREF="(uni\d{3}[bcs]?\.html)">(<FONT COLOR="BLACK">)?<IMG SRC="images/back00\.gif"')
    help = 'Index format: nnn'


class UserFriendly(_BasicScraper):
    starter = bounceStarter('http://ars.userfriendly.org/cartoons/?mode=classic', compile(r'<area shape="rect" href="(/cartoons/\?id=\d{8}&mode=classic)" coords="[\d, ]+?" alt="">'))
    stripUrl = 'http://ars.userfriendly.org/cartoons/?id=%s&mode=classic'
    imageSearch = compile(r'<img border="0" src="(http://www.userfriendly.org/cartoons/archives/\d{2}\w{3}/.+?\.gif)"')
    prevSearch = compile(r'<area shape="rect" href="(/cartoons/\?id=\d{8}&mode=classic)" coords="[\d, ]+?" alt="Previous Cartoon">')
    help = 'Index format: yyyymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return 'uf%s' % (getQueryParams(pageUrl)['id'][0][2:],)


class UndeadFriend(_BasicScraper):
    latestUrl = 'http://www.undeadfriend.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(r'src="(http://www\.undeadfriend\.com/comics/.+?)"', IGNORECASE)
    prevSearch = compile(r'<a.+?href="(http://www\.undeadfriend\.com/d/\d+?\.html)"><img border="0" name="previous_day" alt="Previous comic" src="http://www\.undeadfriend\.com/images/previous_day\.jpg', IGNORECASE)
    help = 'Index format: yyyymmdd'


class UnspeakableVault(_BasicScraper):
    stripUrl = 'http://www.macguff.fr/goomi/unspeakable/WEBIMAGES/CARTOON/vault%s.html'
    imageSearch = compile(r'(WEBIMAGES/CARTOON/.+?)"')
    prevSearch = compile(r'PREVIOUS.+?" href="(.+?)"')
    help = 'Index format: nn or nnn'
    starter = indirectStarter('http://www.macguff.fr/goomi/unspeakable/home.html',
                              compile(r'http://www.macguff.fr/goomi/unspeakable/(.+?)"'))

    @classmethod
    def namer(cls, imageUrl, imageSearch):
        return '%s-%s' % (imageSearch.split('/')[-1].split('.')[0],imageUrl.split('/')[-1].split('.')[0])

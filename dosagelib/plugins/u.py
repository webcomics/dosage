# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..helpers import bounceStarter, indirectStarter
from ..util import getQueryParams, tagre


class Undertow(_BasicScraper):
    stripUrl = 'http://undertow.dreamshards.org/%s'
    imageSearch = compile(tagre("img", "src", r'([^"]+\.jpg)'))
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


# XXX disallowed by robots.txt
class _UserFriendly(_BasicScraper):
    starter = bounceStarter('http://ars.userfriendly.org/cartoons/?mode=classic', compile(r'<area shape="rect" href="(/cartoons/\?id=\d{8}&mode=classic)" coords="[\d, ]+?" alt="">'))
    stripUrl = 'http://ars.userfriendly.org/cartoons/?id=%s&mode=classic'
    imageSearch = compile(r'<img border="0" src="\s*(http://www.userfriendly.org/cartoons/archives/\d{2}\w{3}/.+?\.gif)"')
    prevSearch = compile(r'<area shape="rect" href="(/cartoons/\?id=\d{8}&mode=classic)" coords="[\d, ]+?" alt="Previous Cartoon">')
    help = 'Index format: yyyymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return 'uf%s' % (getQueryParams(pageUrl)['id'][0][2:],)

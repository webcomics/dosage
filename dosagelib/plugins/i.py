# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre


class IanJay(_BasicScraper):
    url = 'http://ianjay.net/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://ianjay\.net/comics/\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://ianjay\.net/\?p=\d+)', after="Previous"))
    help = 'Index foramt: nnn'


class IDreamOfAJeanieBottle(_BasicScraper):
    url = 'http://jeaniebottle.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(http://jeaniebottle\.com/\?p=\d+)', after="prev"))
    help = 'Index format: n (unpadded)'


class IrregularWebcomic(_BasicScraper):
    url = 'http://www.irregularwebcomic.net/'
    stripUrl = url + '%s.html'
    imageSearch = compile(r'<img .*src="(.*comics/.*(png|jpg|gif))".*>')
    prevSearch = compile(r'<a href="(/\d+\.html|/cgi-bin/comic\.pl\?comic=\d+)">Previous ')
    help = 'Index format: nnn'


class InsideOut(_BasicScraper):
    url = 'http://www.insideoutcomic.com/'
    stripUrl = url + 'html/%s.html'
    imageSearch = compile(r'Picture12LYR.+?C="(.+?/assets/images/.+?)"')
    prevSearch = compile(r'Picture7LYR.+?F="(.+?/html/.+?)"')
    help = 'Index format: n_comic_name'


class ItsWalky(_BasicScraper):
    url = 'http://www.itswalky.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch = compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help = 'Index format: yyyymmdd'

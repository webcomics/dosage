# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..util import tagre


class VGCats(_BasicScraper):
    latestUrl = 'http://www.vgcats.com/comics/'
    stripUrl = latestUrl + '?strip_id=%s'
    imageSearch = compile(tagre("img", "src", r'(images/\d{6}\.[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') +
      tagre("img", "src", r"back\.gif"))
    help = 'Index format: n (unpadded)'


class VGCatsSuper(VGCats):
    name = 'VGCats/Super'
    latestUrl = 'http://www.vgcats.com/super/'
    stripUrl = latestUrl + '?strip_id=%s'


class VGCatsAdventure(VGCats):
    name = 'VGCats/Adventure'
    latestUrl = 'http://www.vgcats.com/ffxi/'
    stripUrl = latestUrl + '?strip_id=%s'


class ViiviJaWagner(_BasicScraper):
    latestUrl = 'http://www.hs.fi/viivijawagner/'
    stripUrl = None
    imageSearch = compile(tagre("link", "href", r'(http://hs\d+\.snstatic\.fi/webkuva/oletus/[^"]+)', before="image_src"))
    prevSearch = compile(tagre("a", "href", r'(/viivijawagner/[^"]+)', before="prev-cm"))
    help = 'Index format: none'

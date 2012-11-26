# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..util import tagre


# XXX make dynamic
class _VGCats(_BasicScraper):
    latestUrl = 'http://www.vgcats.com/comics/'
    imageSearch = compile(r'<img src="(images/\d{6}\..+?)"')
    prevSearch = compile(r'<a href="(\?strip_id=\d+)"><img src="back.gif" border="0"')
    help = 'Index format: n (unpadded)'

    @property
    def stripUrl(self):
        return self.latestUrl + '?strip_id=%s'


class Super(_VGCats):
    name = 'VGCats/Super'
    latestUrl = 'http://www.vgcats.com/super/'


class Adventure(_VGCats):
    name = 'VGCats/Adventure'
    latestUrl = 'http://www.vgcats.com/ffxi/'



class ViiviJaWagner(_BasicScraper):
    latestUrl = 'http://www.hs.fi/viivijawagner/'
    imageSearch = compile(tagre("link", "href", r'(http://hs12\.snstatic\.fi/webkuva/oletus/[^"]+)', before="image_src"))
    prevSearch = compile(tagre("a", "href", r'(/viivijawagner/\d+)', before="prev-cm"))
    help = 'Index format: none'

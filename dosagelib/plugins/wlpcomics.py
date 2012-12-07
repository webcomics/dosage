# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..util import tagre
from ..scraper import make_scraper
from ..helpers import bounceStarter


_imageSearch = compile(tagre("img", "src", r'(http://www\.wlpcomics\.com/(?:adult|general)/[^"]+/comics/[^"]+)'))
_prevSearch = compile(tagre("a", "href", r'(\w+.html)') + 'Previous')
_nextSearch = compile(tagre("a", "href", r'(\w+.html)') + 'Next')


def add(name, path):
    baseUrl = 'http://www.wlpcomics.com/' + path
    classname = 'WLP_' + name

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]

    globals()[classname] = make_scraper(classname,
       name = 'WLP/' + name,
       starter = bounceStarter(baseUrl, _nextSearch),
       stripUrl = baseUrl + '%s.html',
       imageSearch = _imageSearch,
       prevSearch = _prevSearch,
       namer = namer,
       help = 'Index format: nnn',
    )


add('ChichiChan', 'adult/chichi/')
add('ChocolateMilkMaid', 'adult/cm/')
add('MaidAttack', 'general/maidattack/')
add('ShadowChasers', 'general/shadowchasers/')

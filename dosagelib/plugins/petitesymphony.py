# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre

_imageSearch = compile(tagre("img", "src", r'(http://[a-z0-9]+\.petitesymphony\.com/files/comics/[^"]+)'))
_prevSearch = compile(tagre("a", "href", r'(http://[a-z0-9]+\.petitesymphony\.com/comic/[^"]+)', after="navi-prev"))

def add(name):
    classname = 'PetiteSymphony_%s' % name.capitalize()
    latestUrl = 'http://%s.petitesymphony.com/' % name
    globals()[classname] = make_scraper(classname,
        name='PetiteSymphony/' + name.capitalize(),
        latestUrl = latestUrl,
        stripUrl = latestUrl + 'comic/%s',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help='Index format: named number'
    )


add("djandora")
add("generation17")
add("knuckleup")
add("kickinrad")
add("orangegrind")
add("rascals")
add("sangria")
add("seed")

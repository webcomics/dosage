# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre

_imageSearch = compile(tagre("img", "src", r'(http://v\.cdn\.nuklearpower\.com/comics/[^"]+)'))
_prevSearch = compile(tagre("a", "href", r'([^"]+)') + "Previous")

def add(name, shortname):
    baseUrl = 'http://www.nuklearpower.com/'
    latestUrl = baseUrl + shortname + '/'
    classname = 'NuklearPower_%s' % name

    globals()[classname] = make_scraper(classname,
        name='NuklearPower/' + name,
        latestUrl = latestUrl,
        stripUrl = baseUrl + '%s',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help = 'Index format: yyyy/mm/dd/name',
    )


add('8BitTheater', '8-bit-theater')
add('Warbot', 'warbot')
add('HowIKilledYourMaster', 'hikym')
add('AtomicRobo', 'atomic-robo')

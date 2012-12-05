# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper

_imageSearch = compile(r'<img src=http://\w+\.snafu-comics\.com/(comics/\d{6}_\w*\.\w{3,4})')
_prevSearch = compile(r'<a href="(\?comic_id=\d+)">Previous</a>')


def add(name, host):
    baseUrl = 'http://%s.snafu-comics.com/' % host
    classname = 'SnafuComics_%s' % name

    globals()[classname] = make_scraper(classname,
        name='SnafuComics/%s' % name,
        latestUrl = baseUrl,
        stripUrl = baseUrl + '?comic_id=%s',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help = 'Index format: n (unpadded)',
    )


add('KOF', 'kof')
add('PowerPuffGirls', 'ppg')
add('Tin', 'tin')
add('TW', 'tw')
add('Sugar', 'sugar')
add('SF', 'sf')
add('Titan', 'titan')
add('EA', 'ea')
add('Zim', 'zim')
add('Soul', 'soul')
add('FT', 'ft')
add('Bunnywith', 'bunnywith')
add('Braindead', 'braindead')

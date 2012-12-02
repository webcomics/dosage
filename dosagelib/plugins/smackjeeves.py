# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from re import compile
from ..scraper import make_scraper
from ..helpers import bounceStarter
from ..util import tagre

_imageSearch = compile(tagre("img", "src", r'(http://(?:www|img2)\.smackjeeves\.com/images/uploaded/comics/[^"]+)'))
_linkSearch = tagre("a", "href", r'([^"]*/comics/\d+/[^"]*)')
_prevSearch = compile(_linkSearch + '(?:<img[^>]*alt="< Previous"|&lt; Back)')
_nextSearch = compile(_linkSearch + '(?:<img[^>]*alt="Next >"|Next &gt;)')

def add(name):
    classname = 'SmackJeeves/' + name
    # XXX mature content can be viewed directly with:
    # http://www.smackjeeves.com/mature.php?ref=<percent-encoded-url>
    baseUrl = 'http://%s.smackjeeves.com/comics/' % name

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-2]

    globals()[classname] = make_scraper(classname,
        starter=bounceStarter(baseUrl, _nextSearch),
        stripUrl = baseUrl + '%s/',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help = 'Index format: nnnn (some increasing number)',
        namer = namer,
    )


add('20galaxies')
add('axe13')
add('beartholomew')
add('bliss')
add('durian')
add('heard')
add('mpmcomic')
add('nlmo-project')
add('paranoidloyd')
add('thatdreamagain')
add('wowcomics')

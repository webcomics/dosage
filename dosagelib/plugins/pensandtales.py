# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
from re import compile
from ..scraper import make_scraper
from ..util import tagre

_imageSearch = compile(tagre("img", "src", r'([^"]*wp-content/uploads/[^"]+)'))

def add(name, baseUrl, param="date"):
    classname = 'PensAndTales_%s' % name
    _prevSearch = compile(tagre("span", "class", "mininav-prev") +
    tagre("a", "href", r'([^"]*\?%s=[-\d]+)' % param))
    globals()[classname] = make_scraper(classname,
        name='PensAndTales/' + name,
        url = baseUrl,
        stripUrl = baseUrl + '?' + param + '=%s',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help='Index format: yyyymmdd'
    )


# Most of the comics linked at pensandtales are broken and
# the rest does not have a common layout. It seems they allow
# almost arbitrary HTML layout.

add('FireflyCross', 'http://www.fireflycross.pensandtales.com/', param="comic")
add('Evilish', 'http://evilish.pensandtales.com/')

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..helpers import bounceStarter
from ..util import tagre


class xkcd(_BasicScraper):
    baseUrl = 'http://xkcd.com/'
    starter = bounceStarter(baseUrl, compile(tagre("a", "href", r'(/\d+/)', before="next")))
    stripUrl = baseUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://imgs\.xkcd\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\d+/)', before="prev"))
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').rsplit('/', 1)[-1])
        name = imageUrl.rsplit('/', 1)[-1].split('.')[0]
        return '%03d-%s' % (index, name)

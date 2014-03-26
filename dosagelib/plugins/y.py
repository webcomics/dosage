# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre


class YAFGC(_BasicScraper):
    description = u'Yet Another Fantasy Gamer Comic'
    url = 'http://yafgc.net/'
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://(?:www\.)?yafgc\.net/img/comic/\d+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(http://(?:www\.)?yafgc\.net/\?id=\d+)') +
      tagre("img", "src", r'/img/navbar/go_to_previous\.gif'))
    help = 'Index format: number'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("www.yafgc.net", "yafgc.net")

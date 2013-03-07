# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre


class YAFGC(_BasicScraper):
    url = 'http://yafgc.net/'
    stripUrl = url + '?id=%s'
    imageSearch = compile(tagre("img", "src", r'(http://yafgc\.net/img/comic/\d+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(http://yafgc\.net/\?id=\d+)') +
      tagre("img", "src", r'/img/navbar/go_to_previous\.gif'))
    help = 'Index format: n'

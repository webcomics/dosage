# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper
from .common import _WordPressScraper


class YAFGC(_WordPressScraper):
    url = 'http://yafgc.net/'


class YouSayItFirst(_ParserScraper):
    stripUrl = 'https://www.yousayitfirst.com/comics/index.php?date=%s'
    url = stripUrl % '20130125'
    firstStripUrl = stripUrl % '20040220'
    imageSearch = '//a/img'
    prevSearch = '//a[text()="Previous"]'
    endOfLife = True
    help = 'Index format: yyyymmdd'

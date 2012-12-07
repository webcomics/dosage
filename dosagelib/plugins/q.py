# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre


class QuestionableContent(_BasicScraper):
    latestUrl = 'http://www.questionablecontent.net/'
    stripUrl = latestUrl + 'view.php?comic=%s'
    imageSearch = compile(tagre("img", "src", r'([^"]+/comics/[^"]+)', before="strip"))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?comic=\d+)') + 'Previous')
    help = 'Index format: n (unpadded)'


class Qwantz(_BasicScraper):
    latestUrl = 'http://www.qwantz.com/index.php'
    stripUrl = latestUrl + '?comic=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.qwantz\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.qwantz\.com/index\.php\?comic=\d+)', before="prev"))
    help = 'Index format: n'

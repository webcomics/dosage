# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..util import tagre


class QuestionableContent(_BasicScraper):
    url = 'http://www.questionablecontent.net/'
    stripUrl = url + 'view.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'([^"]+/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?comic=\d+)') + 'Previous')
    help = 'Index format: n (unpadded)'


class Qwantz(_BasicScraper):
    baseUrl = 'http://www.qwantz.com/'
    url = baseUrl + 'index.php'
    rurl = escape(baseUrl)
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php\?comic=\d+)' % rurl, before="prev"))
    help = 'Index format: n'

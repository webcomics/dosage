# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper
from ..helpers import xpath_class


class QuantumVibe(_ParserScraper):
    url = 'https://www.quantumvibe.com/'
    stripUrl = url + 'strip?page=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "disppageV3?story=qv")]'
    prevSearch = '//a[./img[contains(@src, "nav/prevstrip")]]'


class QuentynQuinnSpaceRanger(_ParserScraper):
    stripUrl = 'http://www.rhjunior.com/%s/'
    firstStripUrl = stripUrl % 'quentyn-quinn-space-ranger-0001'
    url = stripUrl % 'comics/quentyn-quinn-space-ranger'
    imageSearch = '//div[contains(@class, "entry-content")]//img'
    prevSearch = ('//a[@rel="prev"]', '//a[@title="Quentyn Quinn, Space Ranger"]')


class QuestionableContent(_ParserScraper):
    url = 'http://www.questionablecontent.net/'
    stripUrl = url + 'view.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[text()="Previous"]'
    help = 'Index format: n (unpadded)'


class Qwantz(_ParserScraper):
    url = 'http://www.qwantz.com/index.php'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[{}]'.format(xpath_class('comic'))
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: n'

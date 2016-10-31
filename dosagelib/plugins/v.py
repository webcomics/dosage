# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function
from re import compile

from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import xpath_class


class VampireCheerleaders(_BasicScraper):
    url = 'http://www.vampirecheerleaders.net/'
    stripUrl = url + 'strips-vc/%s'
    firstStripUrl = stripUrl % 'fang_service'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.vampirecheerleaders\.net/strips-vc/[^"]+)', before="cndprev"))
    help = 'Index format: name'


class VGCats(_BasicScraper):
    url = 'http://www.vgcats.com/comics/'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(images/\d{6}\.[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') +
                         tagre("img", "src", r"back\.gif"))
    help = 'Index format: n (unpadded)'


class VGCatsAdventure(VGCats):
    name = 'VGCats/Adventure'
    url = 'http://www.vgcats.com/ffxi/'
    stripUrl = url + '?strip_id=%s'


class VGCatsSuper(VGCats):
    name = 'VGCats/Super'
    url = 'http://www.vgcats.com/super/'
    stripUrl = url + '?strip_id=%s'


class VictimsOfTheSystem(_BasicScraper):
    url = 'http://www.votscomic.com/'
    stripUrl = url + '?id=%s.jpg'
    firstStripUrl = stripUrl % '070103-002452'
    imageSearch = compile(tagre("img", "src", r'(comicpro/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?id=\d+-\d+\.jpg)') +
                         "Previous")
    help = 'Index format: nnn-nnn'


class ViiviJaWagner(_ParserScraper):
    url = 'http://www.hs.fi/viivijawagner/'
    imageSearch = '//div[@id="full-comic"]//img'
    prevSearch = '//a[%s]' % xpath_class('prev-cm')
    lang = 'fi'

    def namer(self, image_url, page_url):
        return image_url.split('=')[1]

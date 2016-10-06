# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class _WebcomicEu(_ParserScraper):
    imageSearch = '//img[@id="comicimg"]'
    prevSearch = '//a[img[contains(@src, "navi-zurueck")]]'
    help = 'Index format: number'

    def __init__(self, name):
        super(_WebcomicEu, self).__init__('WebcomicEu/' + name)

    @property
    def url(self):
        return 'http://%s.webcomic.eu/' % self.sub

    @property
    def stripUrl(self):
        return self.url + '?id=%s'

    @property
    def firstStripUrl(self):
        return self.stripUrl % '1'


class TheBessEffect(_WebcomicEu):
    lang = 'de'
    sub = 'thebesseffect'


class TheBessEffectEnglish(_WebcomicEu):
    sub = 'tbe-english'


class Talandor(_WebcomicEu):
    lang = 'de'
    sub = 'talandor'

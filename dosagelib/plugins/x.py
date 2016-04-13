# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile

from ..scraper import _BasicScraper
from ..helpers import bounceStarter
from ..util import tagre


class Xkcd(_BasicScraper):
    name = 'xkcd'
    url = 'http://xkcd.com/'
    starter = bounceStarter
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src",
                                r'(//imgs\.xkcd\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\d+/)', before="prev"))
    nextSearch = compile(tagre("a", "href", r'(/\d+/)', before="next"))
    help = 'Index format: n (unpadded)'
    textSearch = compile(tagre("img", "title", r'([^"]+)',
                               before=r'//imgs\.xkcd\.com/comics/'))

    @classmethod
    def namer(cls, image_url, page_url):
        index = int(page_url.rstrip('/').rsplit('/', 1)[-1])
        name = image_url.rsplit('/', 1)[-1].split('.')[0]
        return '%03d-%s' % (index, name)

    @classmethod
    def imageUrlModifier(cls, url, data):
        if url and '/large/' in data:
            return url.replace(".png", "_large.png")
        return url

    def shouldSkipUrl(self, url, data):
        return url in (
            self.stripUrl % '1663',  # Garden
        )

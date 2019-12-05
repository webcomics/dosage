# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper
from ..helpers import bounceStarter


class Xkcd(_ParserScraper):
    name = 'xkcd'
    url = 'https://xkcd.com/'
    starter = bounceStarter
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@rel="prev"]'
    nextSearch = '//a[@rel="next"]'
    help = 'Index format: n (unpadded)'
    textSearch = '//div[@id="comic"]//img/@title'

    def namer(self, image_url, page_url):
        index = int(page_url.rstrip('/').rsplit('/', 1)[-1])
        name = image_url.rsplit('/', 1)[-1].split('.')[0]
        return '%03d-%s' % (index, name)

    def imageUrlModifier(self, url, data):
        if url and '/large/' in data:
            return url.replace(".png", "_large.png")
        return url

    def shouldSkipUrl(self, url, data):
        return url in (
            self.stripUrl % '1663',  # Garden
        )

# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from ..scraper import ParserScraper
from ..helpers import bounceStarter


class xkcd(ParserScraper):
    url = 'https://xkcd.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic"]//img'
    textSearch = imageSearch + '/@title'
    prevSearch = '//a[@rel="prev"]'
    nextSearch = '//a[@rel="next"]'
    starter = bounceStarter
    help = 'Index format: n (unpadded)'

    def namer(self, image_url, page_url):
        index = int(page_url.rstrip('/').rsplit('/', 1)[-1])
        name = image_url.rsplit('/', 1)[-1].split('.')[0]
        return '%04d-%s' % (index, name)

    def imageUrlModifier(self, url, data):
        if url and '/large/' in data:
            return url.replace(".png", "_large.png")
        return url

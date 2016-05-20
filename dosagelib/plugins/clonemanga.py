# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile

from ..scraper import _BasicScraper
from ..util import tagre, getQueryParams


class CloneManga(_BasicScraper):
    _linkTag = tagre("a", "href", r'([^"]+)')
    prevSearch = compile(_linkTag + tagre("img", "src", r"previous\.gif"))
    nextSearch = compile(_linkTag + tagre("img", "src", r"next\.gif"))
    latestSearch = compile(_linkTag + tagre("img", "src", r"last\.gif"))
    help = 'Index format: n'

    def __init__(self, name, shortName, imageFolder=None, lastStrip=None):
        super(CloneManga, self).__init__('CloneManga/' + name)

        _url = 'http://manga.clone-army.org'
        self.url = '%s/%s.php' % (_url, shortName)
        if imageFolder is None:
            imageFolder = shortName
        self.stripUrl = self.url + '?page=%s'
        self.imageSearch = compile(tagre("img", "src", r'((?:%s/)?%s/[^"]+)' % (_url, imageFolder), after="center"))

        if lastStrip is None:
            self.starter = self._starter
        else:
            self.url = self.stripUrl % lastStrip

    def namer(self, image_url, page_url):
        return '%03d' % int(getQueryParams(page_url)['page'][0])

    def _starter(self):
        # first, try hopping to previous and next comic
        data = self.getPage(self.url)
        try:
            url = self.fetchUrl(self.url, data, self.prevSearch)
        except ValueError:
            # no previous link found, try hopping to last comic
            return self.fetchUrl(self.url, data, self.latestSearch)
        else:
            data = self.getPage(url)
            return self.fetchUrl(url, data, self.nextSearch)

    @classmethod
    def getmodules(cls):
        return [
            cls('AprilAndMay', 'anm', imageFolder='AAM'),
            cls('Kanami', 'kanami'),
            cls('MomokaCorner', 'momoka'),
            cls('NanasEverydayLife', 'nana', lastStrip='78'),
            cls('PaperEleven', 'pxi', imageFolder='papereleven', lastStrip='311'),
            cls('Tomoyo42sRoom', 't42r'),
            cls('PennyTribute', 'penny'),
        ]

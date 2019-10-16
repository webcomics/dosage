# -*- coding: utf-8 -*-
# Copyright (C) 2019-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class StudioKhimera(_ParserScraper):
    imageSearch = '//figure[@class="gallery-item"]//img/@data-src'
    prevSearch = '//a[@rel="prev"]'

    def __init__(self, name, sub, last=None, adult=False, fixNames=False):
        super(StudioKhimera, self).__init__('StudioKhimera/' + name)

        self.baseUrl = 'https://%s.studiokhimera.com/' % sub
        self.stripUrl = self.baseUrl + '%s/'
        self.url = self.baseUrl + 'category/comicChapter/?latest'

        self.multipleImagesPerStrip = True

        if last:
            self.last = True
            self.url = self.stripUrl % last
            self.endOfLife = True

        if adult:
            self.adult = True

    def starter(self):
        # Retrieve list of chapter links
        chapterPage = self.getPage(self.baseUrl + 'archive/')
        self.chapters = chapterPage.xpath('//main//a/@href')
        self.firstStripUrl = self.chapters[0]
        return self.chapters[-1]

    def getPrevUrl(self, url, data):
        # Select previous chapter from list
        index = [i for i, ch in enumerate(self.chapters) if ch == url][0]
        if index == 0:
            return None
        return self.chapters[index - 1]

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        if 'uberquest' in pageUrl:
            filename = filename.replace('Page', 'UberQuest')
            filename = filename.replace('UberQuest01.', 'UberQuest001.')
            filename = filename.replace('UberQuest98.', 'UberQuest098.')
            filename = filename.replace('UberQuest99.', 'UberQuest099.')
        return filename

    @classmethod
    def getmodules(cls):
        return (
            cls('Draconia', 'thedraconiachronicles', adult=True),
            cls('Eorah', 'eorah'),
            cls('Mousechievous', 'mousechievous'),
            cls('UberQuest', 'uberquest'),
        )

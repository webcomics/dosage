# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from .common import _WordPressScraper, _WPNavi


class PetiteSymphony(_WPNavi):
    multipleImagesPerStrip = True
    help = 'Index format: named number'

    def __init__(self, name):
        super(PetiteSymphony, self).__init__('PetiteSymphony/' +
                                             name.capitalize())
        self.url = 'http://%s.petitesymphony.com/' % name
        self.stripUrl = self.url + 'comic/%s'

    @classmethod
    def getmodules(cls):
        return (
            cls("knuckleup"),
            cls("sangria"),
        )


class ComicsBreak(_WordPressScraper):
    def __init__(self, name, archive=None):
        super(ComicsBreak, self).__init__('ComicsBreak/' + name)
        self.url = 'http://%s.comicsbreak.com/' % name.lower()
        if archive:
            self.url = 'https://web.archive.org/web/{}/{}'.format(
                archive, self.url)
            self.endOfLife = True

    def namer(self, imageUrl, pageUrl):
        if self.name == 'ComicsBreak/Djandora':
            # Fix inconsistent filenames
            filename = imageUrl.rsplit('/', 1)[-1]
            filename = filename.replace('2014-10-31-Page70', 'Page70')
            filename = filename.replace('a3p69eng', 'Page69')
            if '2015/08/a4p57eng' in imageUrl:
                filename = filename.replace('p57', 'p56')
            return filename
        else:
            return super(ComicsBreak, self).namer(imageUrl, pageUrl)

    @classmethod
    def getmodules(cls):
        return (
            cls('Djandora', archive='20170923062433'),
            cls("Generation17"),
        )

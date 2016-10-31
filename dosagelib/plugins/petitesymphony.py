# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile

from ..scraper import _BasicScraper
from ..util import tagre
from .common import _WordPressScraper


class PetiteSymphony(_BasicScraper):
    imageSearch = compile(tagre("img", "src", r'(http://[a-z0-9]+\.petitesymphony\.com/files/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://[a-z0-9]+\.petitesymphony\.com/comic/[^"]+)', after="navi-prev"))
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

    def __init__(self, name):
        super(ComicsBreak, self).__init__('ComicsBreak/' + name)
        self.url = 'http://%s.comicsbreak.com/' % name.lower()

    @classmethod
    def getmodules(cls):
        return (
            cls("Djandora"),
            cls("Generation17"),
        )

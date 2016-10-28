# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class Nitrocosm(_ParserScraper):
    imageSearch = '//img[@class="gallery_display"]'
    prevSearch = '//a[@class="nav_btn_previous"]'

    def __init__(self, name, path):
        super(Nitrocosm, self).__init__(name)
        self.url = 'http://www.nitrocosm.com/go/' + path

    @classmethod
    def getmodules(cls):
        return [
            cls('2214', '2214_classic/'),
            cls('OTE', 'ote/'),
            cls('ProperBarn', 'gag/'),
        ]

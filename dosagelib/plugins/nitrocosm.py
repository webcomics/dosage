# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
from ..scraper import ParserScraper


class Nitrocosm(ParserScraper):
    imageSearch = '//img[@class="gallery_display"]'
    prevSearch = '//a[@class="nav_btn_previous"]'

    def __init__(self, name, path):
        super().__init__(name)
        self.url = 'http://www.nitrocosm.com/go/' + path

    @classmethod
    def getmodules(cls):
        return [
            cls('2214', '2214_classic/'),
            cls('OTE', 'ote/'),
            cls('ProperBarn', 'gag/'),
        ]

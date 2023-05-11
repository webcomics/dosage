# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
from .common import WordPressScraper


class SandraAndWoo(WordPressScraper):
    prevSearch = '//a[@rel="prev"]'

    def __init__(self, name, urlName, firstUrl, lang='en'):
        super().__init__(name)
        self.url = 'http://www.sandraandwoo.com/' + urlName
        self.firstStripUrl = self.url + firstUrl
        self.lang = lang

    @classmethod
    def getmodules(cls):
        return (
            cls('Gaia', 'gaia/', '2000/01/01/welcome-to-gaia/'),
            cls('GaiaGerman', 'gaiade/', '2000/01/01/welcome-to-gaia/', lang='de'),
            cls('SandraAndWoo', '', '2000/01/01/welcome-to-sandra-and-woo/'),
            cls('SandraAndWooGerman', 'woode/',
                '2008/10/19/ein-ausgefuchster-waschbar/', lang='de'),
        )

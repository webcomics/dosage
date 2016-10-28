# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from .common import _WordPressScraper


class SandraAndWoo(_WordPressScraper):
    prevSearch = '//a[@rel="prev"]'

    def __init__(self, name, urlName, firstUrl, lang='en'):
        super(SandraAndWoo, self).__init__(name)
        self.url = 'http://www.sandraandwoo.com/' + urlName
        self.firstStripUrl = self.url + firstUrl
        self.lang = lang

    @classmethod
    def getmodules(cls):
        return [
            cls('Gaia', 'gaia/', '2000/01/01/welcome-to-gaia/'),
            cls('GaiaGerman', 'gaiade/', '2000/01/01/welcome-to-gaia/', lang='de'),
            cls('SandraAndWoo', '', '2000/01/01/welcome-to-sandra-and-woo/'),
            cls('SandraAndWooGerman', 'woode/', '2008/10/19/ein-ausgefuchster-waschbar/', lang='de'),
        ]

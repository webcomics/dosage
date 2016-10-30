# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class KindOfNormal(_ParserScraper):
    imageSearch = '//article[1]//div[@class="box-content"]//img'
    prevSearch = '//a[@class="prev"]'

    def __init__(self, name, url):
        super(KindOfNormal, self).__init__(name)
        self.url = 'http://wumo.com/' + url

    @classmethod
    def getmodules(cls):
        return (
            cls('MeAndDanielle', 'meanddanielle'),
            cls('TruthFacts', 'truthfacts'),
            cls('Wumo', 'wumo'),
        )

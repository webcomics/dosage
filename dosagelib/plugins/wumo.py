# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
from ..scraper import ParserScraper


class KindOfNormal(ParserScraper):
    imageSearch = '//article[1]//div[@class="box-content"]//img'
    prevSearch = '//a[@class="prev"]'

    def __init__(self, name, url):
        super().__init__(name)
        self.url = 'http://wumo.com/' + url

    @classmethod
    def getmodules(cls):
        return (
            cls('MeAndDanielle', 'meanddanielle'),
            cls('TruthFacts', 'truthfacts'),
            cls('Wumo', 'wumo'),
        )

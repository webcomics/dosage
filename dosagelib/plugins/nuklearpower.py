# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
from ..scraper import ParserScraper
from .common import ComicControlScraper


class NuklearPower(ParserScraper):
    prevSearch = '//a[@rel="prev"]'
    imageSearch = '//div[@id="comic"]/img'

    def __init__(self, name, path):
        super().__init__('NuklearPower/' + name)
        self.url = 'http://www.nuklearpower.com/' + path + '/'

    @classmethod
    def getmodules(cls):
        return (
            cls('8BitTheater', '8-bit-theater'),
            cls('HowIKilledYourMaster', 'hikym'),
            cls('TheDreadful', 'dreadful'),
            cls('Warbot', 'warbot'),
        )

class NPAtomicRobo(ComicControlScraper):
    name = 'NuklearPower/AtomicRobo'
    url = 'http://www.atomic-robo.com/'

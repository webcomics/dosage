# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2016 Tobias Gruetzmacher

from ..scraper import _ParserScraper


class _NuklearPower(_ParserScraper):
    url = 'http://www.nuklearpower.com/'
    prevSearch = '//a[@rel="prev"]'
    imageSearch = '//div[@id="comic"]/img'

    def starter(self):
        return self.url + self.path + '/'

    @classmethod
    def getName(cls):
        return 'NuklearPower/' + cls.__name__[2:]


class NP8BitTheater(_NuklearPower):
    path = '8-bit-theater'


class NPAtomicRobo(_NuklearPower):
    url = 'http://www.atomic-robo.com/'
    imageSearch = '//img[@id="cc-comic"]'
    path = 'atomicrobo'


class NPHowIKilledYourMaster(_NuklearPower):
    path = 'hikym'


class NPTheDreadful(_NuklearPower):
    path = 'dreadful'


class NPWarbot(_NuklearPower):
    path = 'warbot'

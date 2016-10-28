# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class _NuklearPower(_ParserScraper):
    prevSearch = '//a[@rel="prev"]'
    imageSearch = '//div[@id="comic"]/img'

    def __init__(self, name):
        super(_NuklearPower, self).__init__('NuklearPower/' + name[2:])

    @property
    def url(self):
        return 'http://www.nuklearpower.com/' + self.path + '/'


class NP8BitTheater(_NuklearPower):
    path = '8-bit-theater'


class NPAtomicRobo(_NuklearPower):
    url = 'http://www.atomic-robo.com/'
    imageSearch = '//img[@id="cc-comic"]'


class NPHowIKilledYourMaster(_NuklearPower):
    path = 'hikym'


class NPTheDreadful(_NuklearPower):
    path = 'dreadful'


class NPWarbot(_NuklearPower):
    path = 'warbot'

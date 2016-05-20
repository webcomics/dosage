# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile

from ..scraper import _BasicScraper
from ..util import tagre


class KeenSpot(_BasicScraper):
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    _stripPattern = r'([^"]*/d/\d{8}\.html)'
    prevSearch = (
        compile(tagre("link", "href", _stripPattern, before="prev")),
        compile(tagre("a", "href", _stripPattern, after="prev")),
        compile(tagre("a", "href", _stripPattern) + tagre("img", "id", r"previous_day1")),
        compile(tagre("a", "href", _stripPattern) + tagre("img", "id", r"katc7")),
    )
    help = 'Index format: yyyymmdd'

    def __init__(self, name, sub):
        super(KeenSpot, self).__init__('KeenSpot/' + name)
        self.url = 'http://%s.keenspot.com/' % sub
        self.stripUrl = self.url + 'd/%s.html'

    @classmethod
    def getmodules(cls):
        return [
            # do not edit anything below since these entries are generated from
            # scripts/update_plugins.sh
            # DO NOT REMOVE
            cls('27TwentySeven', 'twenty-seven'),
            cls('Adventurers', 'adventurers'),
            cls('AntiheroForHire', 'antihero'),
            cls('BanzaiGirl', 'banzaigirl'),
            cls('Barker', 'barkercomic'),
            cls('Buzzboy', 'buzzboy'),
            cls('ChoppingBlock', 'choppingblock'),
            cls('ClichFlamb', 'clicheflambe'),
            cls('CountYourSheep', 'countyoursheep'),
            cls('EverythingJake', 'everythingjake'),
            cls('FallOutToyWorks', 'fallouttoyworks'),
            cls('FriarAndBrimstone', 'friarandbrimstone'),
            cls('GeneCatlow', 'genecatlow'),
            cls('GodMode', 'godmode'),
            cls('GreenWake', 'greenwake'),
            cls('HeadTrip', 'headtrip'),
            cls('HoaxHunters', 'hoaxhunters'),
            cls('InHere', 'inhere'),
            cls('Katrina', 'katrina'),
            cls('Landis', 'landis'),
            cls('MakeshiftMiracle', 'makeshiftmiracle'),
            cls('Marksmen', 'marksmen'),
            cls('MarryMe', 'marryme'),
            cls('MedusasDaughter', 'medusasdaughter'),
            cls('MonsterMassacre', 'monstermassacre'),
            cls('Newshounds', 'newshounds'),
            cls('NoPinkPonies', 'nopinkponies'),
            cls('OutThere', 'outthere'),
            cls('Porcelain', 'porcelain'),
            cls('QUILTBAG', 'quiltbag'),
            cls('RedSpike', 'redspike'),
            cls('RumbleFall', 'rumblefall'),
            cls('SamuraisBlood', 'samuraisblood'),
            cls('Sharky', 'sharky'),
            cls('SomethingHappens', 'somethinghappens'),
            cls('SoreThumbs', 'sorethumbs'),
            cls('Striptease', 'striptease'),
            cls('Superosity', 'superosity'),
            cls('TheFirstDaughter', 'thefirstdaughter'),
            cls('TheGodChild', 'godchild'),
            cls('TheHuntersofSalamanstra', 'salamanstra'),
            cls('TheLounge', 'thelounge'),
            cls('WICKEDPOWERED', 'wickedpowered'),
        ]

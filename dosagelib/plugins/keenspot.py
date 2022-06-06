# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from ..scraper import ParserScraper


class KeenSpot(ParserScraper):
    multipleImagesPerStrip = True
    imageSearch = (
        '//img[contains(@src, "/comics/")]',
        # Gene Catlow Alternate
        '//img[contains(@src, "/altcomics/")]',
        # Shockwave Darkside
        '//img[contains(@src, "/comics2D/")]',
        '//img[contains(@src, "com/shockwave")]',
        # Sore Thumbs
        '//img[contains(@src, "com/st2")]',
        # Wayward Sons
        '//img[contains(@src, "com/2")]',
    )
    prevSearch = (
        '//link[@rel="prev"]',
        '//a[@rel="prev"]',
        # Exposure
        '//a[img[@id="exp29"]]',
        # Hero By Night
        '//area[contains(@coords, ",-7,")]',
        # Katrina
        '//a[img[@id="katc7"]]',
        # No Room For Magic, Everyone Loves Adis, Wisdom Of Moo
        '//a[text()="Previous comic"]',
        # Supernovas
        '//a[img[@id="p_top_nav"]]',
    )
    help = 'Index format: yyyymmdd'

    def __init__(self, name, sub, last=None, adult=False, path='d/%s.html'):
        super(KeenSpot, self).__init__('KeenSpot/' + name)
        self.url = 'http://%s.keenspot.com/' % sub
        self.stripUrl = self.url + path

        if last:
            self.url = self.stripUrl % last
            self.endOfLife = True

        if adult:
            self.adult = adult

    @classmethod
    def getmodules(cls):
        return (
            # Not on frontpage...
            cls('Buzzboy', 'buzzboy'),
            cls('EveryoneLovesAdis', 'adis'),
            cls('GeneCatlowAlternate', 'genecatlow', last='20170302',
                adult=True, path='altd/%s.html'),

            # do not edit anything below since these entries are generated from
            # scripts/update_plugins.sh
            # START AUTOUPDATE
            cls('27TwentySeven', 'twenty-seven'),
            cls('Avengelyne', 'avengelyne'),
            cls('BanzaiGirl', 'banzaigirl'),
            cls('Barker', 'barkercomic'),
            cls('ChoppingBlock', 'choppingblock'),
            cls('ClichFlamb', 'clicheflambe'),
            cls('CountYourSheep', 'countyoursheep'),
            cls('CrowScare', 'crowscare', last='20111031'),
            cls('Dreamless', 'dreamless', last='20100726'),
            cls('EverythingJake', 'everythingjake'),
            cls('Exposure', 'exposure'),
            cls('FallOutToyWorks', 'fallouttoyworks'),
            cls('FriarAndBrimstone', 'friarandbrimstone'),
            cls('GeneCatlow', 'genecatlow', last='20170412'),
            cls('GodMode', 'godmode'),
            cls('GreenWake', 'greenwake'),
            cls('HeadTrip', 'headtrip'),
            cls('HeroByNight', 'herobynight'),
            cls('HoaxHunters', 'hoaxhunters'),
            cls('InHere', 'inhere'),
            cls('JadeWarriors', 'jadewarriors'),
            cls('Katrina', 'katrina'),
            cls('LutherStrode', 'lutherstrode'),
            cls('MakeshiftMiracle', 'makeshiftmiracle'),
            cls('Marksmen', 'marksmen'),
            cls('MarryMe', 'marryme'),
            cls('MedusasDaughter', 'medusasdaughter'),
            cls('MonsterMassacre', 'monstermassacre'),
            cls('MysticRevolution', 'mysticrevolution', path='?cid=%s'),
            cls('NoPinkPonies', 'nopinkponies'),
            cls('NoRoomForMagic', 'noroomformagic'),
            cls('OutThere', 'outthere'),
            cls('Porcelain', 'porcelain'),
            cls('ProjectionEdge', 'newshounds'),
            cls('PunchAnPie', 'punchanpie', path='daily/%s.html'),
            cls('QUILTBAG', 'quiltbag'),
            cls('RedSpike', 'redspike'),
            cls('RumbleFall', 'rumblefall'),
            cls('SamuraisBlood', 'samuraisblood'),
            cls('Sharky', 'sharky'),
            cls('ShockwaveDarkside', 'shockwave', path='2d/%s.html'),
            cls('SomethingHappens', 'somethinghappens'),
            cls('SoreThumbs', 'sorethumbs'),
            cls('Striptease', 'striptease'),
            cls('Supernovas', 'supernovas'),
            cls('Superosity', 'superosity'),
            cls('TheFirstDaughter', 'thefirstdaughter'),
            cls('TheHopeVirus', 'hopevirus'),
            cls('TheHuntersOfSalamanstra', 'salamanstra'),
            cls('TheLounge', 'thelounge'),
            cls('TheVault', 'thevault'),
            cls('WaywardSons', 'waywardsons'),
            cls('WeirdingWillows', 'weirdingwillows'),
            cls('WICKEDPOWERED', 'wickedpowered'),
            cls('WisdomOfMoo', 'wisdomofmoo'),
            # END AUTOUPDATE
        )

    def shouldSkipUrl(self, url, data):
        return url in (
            'http://sorethumbs.keenspot.com/d/20160117.html'
        )

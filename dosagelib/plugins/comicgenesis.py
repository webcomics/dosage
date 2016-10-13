# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile

from ..scraper import _BasicScraper
from ..util import tagre

# Comicgenesis has a lot of comics, but most of them are disallowed by
# robots.txt


class ComicGenesis(_BasicScraper):
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/d/\d{8}\.html)') +
                         '(?:Previous comic' + '|' +
                         tagre("img", "alt", "Previous comic") + '|' +
                         tagre("img", "src", "images/back\.gif") +
                         ')')
    multipleImagesPerStrip = True
    help = 'Index format: yyyymmdd'

    def prevUrlModifier(self, prev_url):
        if prev_url:
            return prev_url.replace(
                "keenspace.com", "comicgenesis.com").replace(
                "keenspot.com", "comicgenesis.com").replace(
                "toonspace.com", "comicgenesis.com").replace(
                "comicgen.com", "comicgenesis.com")

    def __init__(self, name, sub=None, last=None, baseUrl=None):
        super(ComicGenesis, self).__init__('ComicGenesis/' + name)

        if sub:
            baseUrl = 'http://%s.comicgenesis.com/' % sub

        self.stripUrl = baseUrl + 'd/%s.html'
        if last:
            self.url = self.stripUrl % last
            self.endOfLife = True
        else:
            self.url = baseUrl

    @classmethod
    def getmodules(cls):
        return [
            # do not edit anything below since these entries are generated from
            # scripts/update_plugins.sh
            # START AUTOUPDATE
            cls('AAAAA', 'aaaaa'),
            cls('AdventuresofKiltman', 'kiltman'),
            cls('AmorModerno', 'amormoderno'),
            cls('AnythingButRealLife', 'anythingbutreallife'),
            cls('Ardra', 'ardra'),
            cls('Artwork', 'artwork'),
            cls('BabeintheWoods', 'babeinthewoods'),
            cls('BackwaterPlanet', 'bobthespirit'),
            cls('BendyStrawVampires', 'bsvampires'),
            cls('BlindSight', 'blindsight'),
            cls('BreakingtheDoldrum', 'breakingthedoldrum'),
            cls('Candi', baseUrl='http://candicomics.com/'),
            cls('CorporateLife', 'corporatelife'),
            cls('DarkWelkin', 'darkwelkin'),
            cls('DemonEater', 'demoneater'),
            cls('DoodleDiaries', 'doodlediaries'),
            cls('DormSweetDorm', 'dormsweetdorm'),
            cls('DoubleyouTeeEff', 'doubleyouteeeff'),
            cls('DragonsBane', 'jasonwhitewaterz'),
            cls('Dreamaniac', 'dreamaniaccomic'),
            cls('ElnifiChronicles', 'elnifichronicles'),
            cls('EvesApple', 'evesapple'),
            cls('FancyThat', 'fancythat'),
            cls('FantasyQwest', 'creatorauthorman'),
            cls('Fantazine', 'fantazin'),
            cls('Flounderville', 'flounderville'),
            cls('GEM', 'keltzy'),
            cls('Gonefor300days', 'g4300d'),
            cls('IBlameDanny', 'vileterror'),
            cls('ImpendingDoom', 'impending'),
            cls('InANutshell', 'nutshellcomics'),
            cls('KernyMantisComics', 'kernymantis'),
            cls('KitsuneJewel', 'kitsunejewel'),
            cls('KittyCattyGames', 'kittycattygames'),
            cls('KiwiDayN', 'kiwidayn'),
            cls('KungFounded', 'kungfounded'),
            cls('LabBratz', 'labbratz'),
            cls('Laserwing', 'laserwing'),
            cls('LumiasKingdom', 'lumia'),
            cls('Majestic7', 'majestic7'),
            cls('MaximumWhimsy', 'maximumwhimsy'),
            cls('MenschunsererZeitGerman', 'muz'),
            cls('MoonCrest24', 'mooncrest', last='20121117'),
            cls('Mushian', 'tentoumushi'),
            cls('NightwolfCentral', 'nightwolfcentral'),
            cls('NoTimeForLife', 'randyraven'),
            cls('NoneMoreComic', 'nonemore'),
            cls('ODCKS', 'odcks'),
            cls('OfDoom', 'ofdoom'),
            cls('OpportunityofaLifetime', 'carpathia'),
            cls('Orbz', 'orbz'),
            cls('OwMySanity', 'owmysanity'),
            cls('PhantomThesis', 'phantomthesis'),
            cls('ProfessorSaltinesAstrodynamicDirigible', 'drsaltine'),
            cls('PsychicDyslexiaInstitute', 'pdi'),
            cls('PublicidadeEnganosa', 'publicidadeenganosa'),
            cls('RandomAxeOfKindness', 'randomaxe'),
            cls('SalemUncommons', 'salemuncommons'),
            cls('SamandElisAdventures', 'sameliadv'),
            cls('SarahZero', 'plughead'),
            cls('SixByNineCollege', 'sixbyninecollege'),
            cls('SpoononHighandFireontheMountian', 'spoon'),
            cls('SynapticMisfires', 'synapticmisfires'),
            cls('TakingStock', 'mapaghimagsik'),
            cls('TemplarArizona', 'templaraz'),
            cls('TheAdventuresofKaniraBaxter', 'kanirabaxter'),
            cls('TheAdventuresofVindibuddSuperheroInTraining', 'vindibudd', last='20070720'),
            cls('TheEasyBreather', 'easybreather'),
            cls('TheMisadventuresofOkk', 'okk'),
            cls('ThePath', 'thepath'),
            cls('TheTalesofKalduras', 'kalduras'),
            cls('Unconventional', 'unconventional'),
            cls('WarMageNC17', 'warmage'),
            cls('WebcomicTheWebcomicWebcomicWebcomicWebcomic', 'dannormnsanidey'),
            cls('WhatYouDontSee', 'phantomlady4'),
            cls('Wierdman', 'asa'),
            # END AUTOUPDATE
        ]

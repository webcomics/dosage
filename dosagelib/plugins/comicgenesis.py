# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre


_imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
_prevSearch = compile(tagre("a", "href", r'([^"]*/d/\d{8}\.html)') +
   '(?:Previous comic' + '|' +
    tagre("img", "alt", "Previous comic") + '|' +
    tagre("img", "src", "images/back\.gif") +
    ')')

def add(name, url):
    classname = 'ComicGenesis_%s' % name
    if '/d/' in url:
        stripUrl = url.split('/d/')[0] + '/d/%s.html'
    else:
        stripUrl = url + 'd/%s.html'

    @classmethod
    def _prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("keenspace.com", "comicgenesis.com"
              ).replace("keenspot.com", "comicgenesis.com"
              ).replace("toonspace.com", "comicgenesis.com"
              ).replace("comicgen.com", "comicgenesis.com")

    globals()[classname] = make_scraper(classname,
        name='ComicGenesis/' + name,
        url=url,
        stripUrl=stripUrl,
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        prevUrlModifier = _prevUrlModifier,
        multipleImagesPerStrip = True,
        help = 'Index format: yyyymmdd',
    )

# Comicgenesis has a lot of comics, but most of them are disallowed by robots.txt
# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
add('AAAAA', 'http://aaaaa.comicgenesis.com/')
add('AdventuresofKiltman', 'http://kiltman.comicgenesis.com/')
add('AmorModerno', 'http://amormoderno.comicgenesis.com/')
add('AnythingButRealLife', 'http://anythingbutreallife.comicgenesis.com/')
add('Ardra', 'http://ardra.comicgenesis.com/')
add('Artwork', 'http://artwork.comicgenesis.com/')
add('BabeintheWoods', 'http://babeinthewoods.comicgenesis.com/')
add('BackwaterPlanet', 'http://bobthespirit.comicgenesis.com/')
add('BendyStrawVampires', 'http://bsvampires.comicgenesis.com/')
add('BlindSight', 'http://blindsight.comicgenesis.com/')
add('BreakingtheDoldrum', 'http://breakingthedoldrum.comicgenesis.com/')
add('Candi', 'http://candicomics.com/')
add('CorporateLife', 'http://corporatelife.comicgenesis.com/')
add('CryHavoc', 'http://cryhavoc.comicgenesis.com/')
add('DarkWelkin', 'http://darkwelkin.comicgenesis.com/')
add('DemonEater', 'http://demoneater.comicgenesis.com/')
add('DoodleDiaries', 'http://doodlediaries.comicgenesis.com/')
add('DormSweetDorm', 'http://dormsweetdorm.comicgenesis.com/')
add('DoubleyouTeeEff', 'http://doubleyouteeeff.comicgenesis.com/')
add('DragonsBane', 'http://jasonwhitewaterz.comicgenesis.com/')
add('Dreamaniac', 'http://dreamaniaccomic.comicgenesis.com/')
add('ElnifiChronicles', 'http://elnifichronicles.comicgenesis.com/')
add('EvesApple', 'http://evesapple.comicgenesis.com/')
add('FancyThat', 'http://fancythat.comicgenesis.com/')
add('FantasyQwest', 'http://creatorauthorman.comicgenesis.com/')
add('Fantazine', 'http://fantazin.comicgenesis.com/')
add('Flounderville', 'http://flounderville.comicgenesis.com/')
add('GEM', 'http://keltzy.comicgenesis.com/')
add('Gonefor300days', 'http://g4300d.comicgenesis.com/')
add('IBlameDanny', 'http://vileterror.comicgenesis.com/')
add('ImpendingDoom', 'http://impending.comicgenesis.com/')
add('InANutshell', 'http://nutshellcomics.comicgenesis.com/')
add('KernyMantisComics', 'http://kernymantis.comicgenesis.com/')
add('KitsuneJewel', 'http://kitsunejewel.comicgenesis.com/')
add('KittyCattyGames', 'http://kittycattygames.comicgenesis.com/')
add('KiwiDayN', 'http://kiwidayn.comicgenesis.com/')
add('KungFounded', 'http://kungfounded.comicgenesis.com/')
add('LabBratz', 'http://labbratz.comicgenesis.com/')
add('Laserwing', 'http://laserwing.comicgenesis.com/')
add('LumiasKingdom', 'http://lumia.comicgenesis.com/')
add('Majestic7', 'http://majestic7.comicgenesis.com/')
add('MaximumWhimsy', 'http://maximumwhimsy.comicgenesis.com/')
add('MenschunsererZeitGerman', 'http://muz.comicgenesis.com/')
add('MoonCrest24', 'http://mooncrest.comicgenesis.com/d/20121117.html')
add('Mushian', 'http://tentoumushi.comicgenesis.com/')
add('NightwolfCentral', 'http://nightwolfcentral.comicgenesis.com/')
add('NoTimeForLife', 'http://randyraven.comicgenesis.com/')
add('NoneMoreComic', 'http://nonemore.comicgenesis.com/')
add('ODCKS', 'http://odcks.comicgenesis.com/')
add('OfDoom', 'http://ofdoom.comicgenesis.com/')
add('OpportunityofaLifetime', 'http://carpathia.comicgenesis.com/')
add('Orbz', 'http://orbz.comicgenesis.com/')
add('OwMySanity', 'http://owmysanity.comicgenesis.com/')
add('PhantomThesis', 'http://phantomthesis.comicgenesis.com/')
add('ProfessorSaltinesAstrodynamicDirigible', 'http://drsaltine.comicgenesis.com/')
add('PsychicDyslexiaInstitute', 'http://pdi.comicgenesis.com/')
add('PublicidadeEnganosa', 'http://publicidadeenganosa.comicgenesis.com/')
add('RandomAxeOfKindness', 'http://randomaxe.comicgenesis.com/')
add('SalemUncommons', 'http://salemuncommons.comicgenesis.com/')
add('SamandElisAdventures', 'http://sameliadv.comicgenesis.com/')
add('SarahZero', 'http://plughead.comicgenesis.com/')
add('SixByNineCollege', 'http://sixbyninecollege.comicgenesis.com/')
add('SpoononHighandFireontheMountian', 'http://spoon.comicgenesis.com/')
add('SueosdelSur', 'http://sds.comicgenesis.com/')
add('SynapticMisfires', 'http://synapticmisfires.comicgenesis.com/')
add('TakingStock', 'http://mapaghimagsik.comicgenesis.com/')
add('TemplarArizona', 'http://templaraz.comicgenesis.com/')
add('TheAdventuresofKaniraBaxter', 'http://kanirabaxter.comicgenesis.com/')
add('TheAdventuresofVindibuddSuperheroInTraining', 'http://vindibudd.comicgenesis.com/d/20070720.html')
add('TheEasyBreather', 'http://easybreather.comicgenesis.com/')
add('TheLounge', 'http://thelounge.comicgenesis.com/')
add('TheMisadventuresofOkk', 'http://okk.comicgenesis.com/')
add('ThePath', 'http://thepath.comicgenesis.com/')
add('TheTalesofKalduras', 'http://kalduras.comicgenesis.com/')
add('Unconventional', 'http://unconventional.comicgenesis.com/')
add('WarMageNC17', 'http://warmage.comicgenesis.com/')
add('WebcomicTheWebcomicWebcomicWebcomicWebcomic', 'http://dannormnsanidey.comicgenesis.com/')
add('WhatYouDontSee', 'http://phantomlady4.comicgenesis.com/')
add('Wierdman', 'http://asa.comicgenesis.com/')

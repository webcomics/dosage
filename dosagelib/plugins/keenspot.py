# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre


_imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
_stripPattern = r'([^"]*/d/\d{8}\.html)'
_prevSearch = (
    compile(tagre("link", "href", _stripPattern, before="prev")),
    compile(tagre("a", "href", _stripPattern, after="prev")),
    compile(tagre("a", "href", _stripPattern) + tagre("img", "id", r"previous_day1")),
    compile(tagre("a", "href", _stripPattern) + tagre("img", "id", r"katc7")),
)

def add(name, url):
    classname = 'KeenSpot_%s' % name
    if '/d/' in url:
        stripUrl = url.split('/d/')[0] + '/d/%s.html'
    else:
        stripUrl = url + 'd/%s.html'

    globals()[classname] = make_scraper(classname,
        name='KeenSpot/' + name,
        url=url,
        stripUrl=stripUrl,
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help = 'Index format: yyyymmdd',
    )

# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
add('27TwentySeven', 'http://twenty-seven.keenspot.com/')
add('Adventurers', 'http://adventurers.keenspot.com/')
add('AntiheroForHire', 'http://antihero.keenspot.com/')
add('BanzaiGirl', 'http://banzaigirl.keenspot.com/')
add('Barker', 'http://barkercomic.keenspot.com/')
add('Buzzboy', 'http://buzzboy.keenspot.com/')
add('ChoppingBlock', 'http://choppingblock.keenspot.com/')
add('ClichFlamb', 'http://clicheflambe.keenspot.com/')
add('CountYourSheep', 'http://countyoursheep.keenspot.com/')
add('EverythingJake', 'http://everythingjake.keenspot.com/')
add('FallOutToyWorks', 'http://fallouttoyworks.keenspot.com/')
add('FriarAndBrimstone', 'http://friarandbrimstone.keenspot.com/')
add('GeneCatlow', 'http://genecatlow.keenspot.com/')
add('GodMode', 'http://godmode.keenspot.com/')
add('GreenWake', 'http://greenwake.keenspot.com/')
add('HeadTrip', 'http://headtrip.keenspot.com/')
add('HoaxHunters', 'http://hoaxhunters.keenspot.com/')
add('InHere', 'http://inhere.keenspot.com/')
add('Katrina', 'http://katrina.keenspot.com/')
add('Landis', 'http://landis.keenspot.com/')
add('MakeshiftMiracle', 'http://makeshiftmiracle.keenspot.com/')
add('Marksmen', 'http://marksmen.keenspot.com/')
add('MarryMe', 'http://marryme.keenspot.com/')
add('MedusasDaughter', 'http://medusasdaughter.keenspot.com/')
add('MonsterMassacre', 'http://monstermassacre.keenspot.com/')
add('Newshounds', 'http://newshounds.keenspot.com/')
add('NoPinkPonies', 'http://nopinkponies.keenspot.com/')
add('OutThere', 'http://outthere.keenspot.com/')
add('Porcelain', 'http://porcelain.keenspot.com/')
add('QUILTBAG', 'http://quiltbag.keenspot.com/')
add('RedSpike', 'http://redspike.keenspot.com/')
add('RumbleFall', 'http://rumblefall.keenspot.com/')
add('SamuraisBlood', 'http://samuraisblood.keenspot.com/')
add('Sharky', 'http://sharky.keenspot.com/')
add('SomethingHappens', 'http://somethinghappens.keenspot.com/')
add('SoreThumbs', 'http://sorethumbs.keenspot.com/')
add('Striptease', 'http://striptease.keenspot.com/')
add('Superosity', 'http://superosity.keenspot.com/')
add('TheFirstDaughter', 'http://thefirstdaughter.keenspot.com/')
add('TheGodChild', 'http://godchild.keenspot.com/')
add('TheHuntersofSalamanstra', 'http://salamanstra.keenspot.com/')
add('TheLounge', 'http://thelounge.keenspot.com/')
add('WICKEDPOWERED', 'http://wickedpowered.keenspot.com/')

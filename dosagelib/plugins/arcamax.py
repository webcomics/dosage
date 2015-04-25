# -*- coding: iso-8859-1 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
"""
Arcamax comic strips
"""
from re import compile
from ..scraper import make_scraper
from ..util import tagre


_imageSearch = compile(tagre("img", "data-zoom-image", r'(/newspics/[^"]+)'))
_prevSearch = compile(tagre("a", "href", r'(/[^"]+)', before='prev'))

def add(name, shortname):
    url = 'http://www.arcamax.com%s' % shortname
    classname = 'Arcamax_%s' % name

    globals()[classname] = make_scraper(classname,
        name='Arcamax/' + name,
        url = url,
        stripUrl = url + '%s',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help = 'Index format: none',
    )

# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
#add('9ChickweedLane', '/thefunnies/ninechickweedlane/')
#add('Agnes', '/thefunnies/agnes/')
#add('AndyCapp', '/thefunnies/andycapp/')
#add('Archie', '/thefunnies/archie/')
add('ArcticCircle', '/thefunnies/arcticcircle/')
#add('AskShagg', '/thefunnies/askshagg/')
#add('BC', '/thefunnies/bc/')
add('BabyBlues', '/thefunnies/babyblues/')
#add('BallardStreet', '/thefunnies/ballardstreet/')
#add('BarneyAndClyde', '/thefunnies/barneyandclyde/')
add('BarneyGoogleAndSnuffySmith', '/thefunnies/barneygoogle/')
add('BeetleBailey', '/thefunnies/beetlebailey/')
add('Bizarro', '/thefunnies/bizarro/')
add('BleekerTheRechargeableDog', '/thefunnies/bleekertherechargeabledog/')
add('Blondie', '/thefunnies/blondie/')
add('Boondocks', '/thefunnies/boondocks/')
add('BrilliantMindofEdisonLee', '/thefunnies/brilliantmindofedisonlee/')
#add('Candorville', '/thefunnies/candorville/')
#add('Cathy', '/thefunnies/cathy/')
#add('ChuckleBros', '/thefunnies/chucklebros/')
add('Crankshaft', '/thefunnies/crankshaft/')
#add('CuldeSac', '/thefunnies/culdesac/')
add('Curtis', '/thefunnies/curtis/')
#add('DaddysHome', '/thefunnies/daddyshome/')
add('DeFlocked', '/thefunnies/deflocked/')
add('DennistheMenace', '/thefunnies/dennisthemenace/')
#add('DiamondLil', '/thefunnies/diamondlil/')
#add('Dilbert', '/thefunnies/dilbert/')
add('DinetteSet', '/thefunnies/thedinetteset/')
#add('DogEatDoug', '/thefunnies/dogeatdoug/')
#add('DogsofCKennel', '/thefunnies/dogsofckennel/')
#add('Doonesbury', '/thefunnies/doonesbury/')
add('Dustin', '/thefunnies/dustin/')
add('FamilyCircus', '/thefunnies/familycircus/')
#add('FloAndFriends', '/thefunnies/floandfriends/')
#add('ForHeavensSake', '/thefunnies/forheavenssake/')
#add('FortKnox', '/thefunnies/fortknox/')
#add('FreeRange', '/thefunnies/freerange/')
#add('Garfield', '/thefunnies/garfield/')
#add('GetFuzzy', '/thefunnies/getfuzzy/')
#add('Heathcliff', '/thefunnies/heathcliff/')
#add('HerbandJamaal', '/thefunnies/herbandjamaal/')
add('HiandLois', '/thefunnies/hiandlois/')
#add('HomeAndAway', '/thefunnies/homeandaway/')
add('IntelligentLife', '/thefunnies/intelligentlife/')
add('JerryKingCartoons', '/thefunnies/humorcartoon/')
#add('LittleDogLost', '/thefunnies/littledoglost/')
#add('LongStoryShort', '/thefunnies/longstoryshort/')
#add('LooseParts', '/thefunnies/looseparts/')
#add('Luann', '/thefunnies/luann/')
add('MallardFillmore', '/thefunnies/mallardfillmore/')
add('Marvin', '/thefunnies/marvin/')
add('MeaningofLila', '/thefunnies/meaningoflila/')
#add('MikeDuJour', '/thefunnies/mikedujour/')
#add('Momma', '/thefunnies/momma/')
add('MotherGooseAndGrimm', '/thefunnies/mothergooseandgrimm/')
add('Mutts', '/thefunnies/mutts/')
#add('NestHeads', '/thefunnies/nestheads/')
#add('NonSequitur', '/thefunnies/nonsequitur/')
#add('OneBigHappy', '/thefunnies/onebighappy/')
#add('Peanuts', '/thefunnies/peanuts/')
#add('PearlsBeforeSwine', '/thefunnies/pearlsbeforeswine/')
#add('Pickles', '/thefunnies/pickles/')
#add('RedandRover', '/thefunnies/redandrover/')
#add('ReplyAll', '/thefunnies/replyall/')
add('RhymeswithOrange', '/thefunnies/rhymeswithorange/')
#add('Rubes', '/thefunnies/rubes/')
#add('RudyPark', '/thefunnies/rudypark/')
#add('Rugrats', '/thefunnies/rugrats/')
#add('ScaryGary', '/thefunnies/scarygary/')
#add('SpeedBump', '/thefunnies/speedbump/')
#add('StrangeBrew', '/thefunnies/strangebrew/')
add('TakeItFromTheTinkersons', '/thefunnies/takeitfromthetinkersons/')
#add('TheBarn', '/thefunnies/thebarn/')
add('TheLockhorns', '/thefunnies/thelockhorns/')
#add('TheOtherCoast', '/thefunnies/theothercoast/')
add('TinasGroove', '/thefunnies/tinasgroove/')
#add('WeePals', '/thefunnies/weepals/')
#add('WizardofId', '/thefunnies/wizardofid/')
#add('WorkingitOut', '/thefunnies/workingitout/')
#add('Wumo', '/thefunnies/wumo/')
#add('ZackHill', '/thefunnies/zackhill/')
add('Zits', '/thefunnies/zits/')

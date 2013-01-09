# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre

_imageSearch = compile(tagre("a", "href", r'(/comics/\d+/[^"]+)'))

def add(name, path):
    baseurl = 'http://www.creators.com'
    classname = 'Creators_%s' % name
    globals()[classname] = make_scraper(classname,
        name = 'Creators/' + name,
        latestUrl = baseurl + path + '.html',
        stripUrl = baseurl + path + '/%s.html',
        imageSearch = _imageSearch,
        prevSearch = compile(tagre("a", "href", r'(%s/\d+\.html)' % path) +
          tagre("img", "src", r'/img_comics/arrow_l\.gif')),
        help = 'Index format: n',
    )

# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
add('Agnes', '/comics/agnes')
add('AndyCapp', '/comics/andy-capp')
add('Archie', '/comics/archie')
add('ArchieinSpanish', '/comics/archie-spanish')
add('AskShagg', '/comics/ask-shagg')
add('BC', '/comics/bc')
add('BCinSpanish', '/comics/bc-spanish')
add('BallardStreet', '/comics/ballard-street')
add('CafeconLeche', '/comics/cafe-con-leche')
add('ChuckleBros', '/comics/chuckle-bros')
add('DaddysHome', '/comics/daddys-home')
add('DiamondLil', '/comics/diamond-lil')
add('DogEatDoug', '/comics/dog-eat-doug')
add('DogsofCKennel', '/comics/dogs-of-c-kennel')
add('DonaldDuck', '/comics/donald-duck')
add('Flare', '/comics/flare')
add('FlightDeck', '/comics/flight-deck')
add('FloandFriends', '/comics/flo-and-friends')
add('ForHeavensSake', '/comics/for-heavens-sake')
add('FreeRange', '/comics/free-range')
add('GirlsAndSports', '/comics/girls-and-sports')
add('GirlsandSportsinSpanish', '/comics/girls-and-sports-spanish')
add('Heathcliff', '/comics/heathcliff')
add('HeathcliffinSpanish', '/comics/heathcliff-spanish')
add('HerbandJamaal', '/comics/herb-and-jamaal')
add('HomeOffice', '/comics/stay-at-home-dad')
add('HopeAndDeath', '/comics/hope-and-death')
add('LibertyMeadows', '/comics/liberty-meadows')
add('LongStoryShort', '/comics/long-story-short')
add('MickeyMouse', '/comics/mickey-mouse')
add('Momma', '/comics/momma')
add('NestHeads', '/comics/nest-heads')
add('OffCenter', '/comics/off-center')
add('OnaClaireDay', '/comics/on-a-claire-day')
add('OneBigHappy', '/comics/one-big-happy')
add('Recess', '/comics/recess')
add('Rubes', '/comics/rubes')
add('Rugrats', '/comics/rugrats')
add('RugratsinSpanish', '/comics/rugrats-spanish')
add('ScaryGary', '/comics/scary-gary')
add('SpeedBump', '/comics/speed-bump')
add('StrangeBrew', '/comics/strange-brew')
add('TheBarn', '/comics/the-barn')
add('TheDinetteSet', '/comics/dinette-set')
add('TheMeaningofLila', '/comics/meaning-of-lila')
add('TheOtherCoast', '/comics/the-other-coast')
add('TheQuigmans', '/comics/the-quigmans')
add('TheWizardofIdinSpanish', '/comics/wizard-of-id-spanish')
add('ThinLines', '/comics/thin-lines')
add('WeePals', '/comics/wee-pals')
add('WizardofId', '/comics/wizard-of-id')
add('WorkingitOut', '/comics/working-it-out')
add('ZackHill', '/comics/zack-hill')

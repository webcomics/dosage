# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre

_imageSearch = compile(tagre("a", "href", r'(/comics/\d+/[^"]+)'))

def add(name, path):
    baseUrl = 'http://www.creators.com'
    classname = 'Creators_%s' % name
    globals()[classname] = make_scraper(classname,
        name = 'Creators/' + name,
        url = baseUrl + path + '.html',
        stripUrl = baseUrl + path + '/%s.html',
        lang = 'es' if name.lower().endswith('spanish') else 'en',
        imageSearch = _imageSearch,
        prevSearch = compile(tagre("a", "href", r'(%s/\d+\.html)' % path) +
          tagre("img", "src", r'/img_comics/arrow_l\.gif')),
        help = 'Index format: n',
    )

# do not edit anything below since these entries are generated from scripts/update.sh
# DO NOT REMOVE
# duplicate of gocomics add('Agnes', '/comics/agnes')
# duplicate of gocomics add('AndyCapp', '/comics/andy-capp')
add('Archie', '/comics/archie')
add('ArchieinSpanish', '/comics/archie-spanish')
# duplicate of gocomics add('AskShagg', '/comics/ask-shagg')
# duplicate of gocomics add('BC', '/comics/bc')
add('BCinSpanish', '/comics/bc-spanish')
# duplicate of gocomics add('BallardStreet', '/comics/ballard-street')
add('CafeconLeche', '/comics/cafe-con-leche')
# duplicate of gocomics add('ChuckleBros', '/comics/chuckle-bros')
# duplicate of gocomics add('DaddysHome', '/comics/daddys-home')
# duplicate of gocomics add('DiamondLil', '/comics/diamond-lil')
# duplicate of gocomics add('DogEatDoug', '/comics/dog-eat-doug')
# duplicate of gocomics add('DogsofCKennel', '/comics/dogs-of-c-kennel')
add('DonaldDuck', '/comics/donald-duck')
add('Flare', '/comics/flare')
add('FlightDeck', '/comics/flight-deck')
# duplicate of gocomics add('FloandFriends', '/comics/flo-and-friends')
# duplicate of gocomics add('ForHeavensSake', '/comics/for-heavens-sake')
# duplicate of gocomics add('FreeRange', '/comics/free-range')
add('GirlsAndSports', '/comics/girls-and-sports')
add('GirlsandSportsinSpanish', '/comics/girls-and-sports-spanish')
# duplicate of gocomics add('Heathcliff', '/comics/heathcliff')
add('HeathcliffinSpanish', '/comics/heathcliff-spanish')
# duplicate of gocomics add('HerbandJamaal', '/comics/herb-and-jamaal')
add('HomeOffice', '/comics/stay-at-home-dad')
add('HopeAndDeath', '/comics/hope-and-death')
# duplicate of gocomics add('LibertyMeadows', '/comics/liberty-meadows')
add('LongStoryShort', '/comics/long-story-short')
add('MickeyMouse', '/comics/mickey-mouse')
# duplicate of gocomics add('Momma', '/comics/momma')
# duplicate of gocomics add('NestHeads', '/comics/nest-heads')
add('OffCenter', '/comics/off-center')
# duplicate of gocomics add('OnaClaireDay', '/comics/on-a-claire-day')
# duplicate of gocomics add('OneBigHappy', '/comics/one-big-happy')
add('Recess', '/comics/recess')
# duplicate of gocomics add('Rubes', '/comics/rubes')
add('Rugrats', '/comics/rugrats')
add('RugratsinSpanish', '/comics/rugrats-spanish')
# duplicate of gocomics add('ScaryGary', '/comics/scary-gary')
# duplicate of gocomics add('SpeedBump', '/comics/speed-bump')
# duplicate of gocomics add('StrangeBrew', '/comics/strange-brew')
# duplicate of gocomics add('TheBarn', '/comics/the-barn')
# duplicate of gocomics add('TheDinetteSet', '/comics/dinette-set')
# duplicate of gocomics add('TheMeaningofLila', '/comics/meaning-of-lila')
# duplicate of gocomics add('TheOtherCoast', '/comics/the-other-coast')
add('TheQuigmans', '/comics/the-quigmans')
add('TheWizardofIdinSpanish', '/comics/wizard-of-id-spanish')
# duplicate of gocomics add('ThinLines', '/comics/thin-lines')
# duplicate of gocomics add('WeePals', '/comics/wee-pals')
# duplicate of gocomics add('WizardofId', '/comics/wizard-of-id')
# duplicate of gocomics add('WorkingitOut', '/comics/working-it-out')
# duplicate of gocomics add('ZackHill', '/comics/zack-hill')

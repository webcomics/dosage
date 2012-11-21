# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from ..scraper import _BasicScraper
from ..util import tagre

def creators(name, shortname):
    baseUrl = 'http://www.creators.com/comics/'
    return type('Creators_%s' % name,
        (_BasicScraper,),
        dict(
        name='Creators/' + name,
        latestUrl='%s%s.html' % (baseUrl, shortname),
        stripUrl='%s%s/%%s.html' % (baseUrl, shortname),
        imageSearch=compile(tagre("img", "src", r'(/comics/\d+/[^"]+)')),
        prevSearch=compile(tagre("a", "href", r'(/comics/%s/\d+\.html)' % shortname) +
          tagre("img", "src", r'/img_comics/arrow_l\.gif')),
        help='Index format: n')
    )


# for a complete list see http://www.creators.com/comics/cat-seeall.html
comics = {
    'Agnes': 'agnes',
    'AndyCapp': 'andy-capp',
    'Archie': 'archie',
    'AskShagg': 'ask-shagg',
    'BallardStreet': 'ballard-street',
    'BC': 'bc',
    'TheBarn': 'the-barn',
    'CafeConLeche': 'cafe-con-leche',
    'ChuckleBros': 'chuckle-bros',
    'DaddysHome': 'daddys-home',
    'DiamondLil': 'diamond-lil',
    'TheDinetteSet': 'dinette-set',
    'DogEatDoug': 'dog-eat-doug',
    'DogsOfCKennel': 'dogs-of-c-kennel',
    'DonaldDuck': 'donald-duck',
    'FloAndFriends': 'flo-and-friends',
    'Flare': 'flare',
    'FlightDeck': 'flight-deck',
    'ForHeavensSake': 'for-heavens-sake',
    'FreeRange': 'free-range',
    'GirlsAndSports': 'girls-and-sports',
    'Heathcliff': 'heathcliff',
    'HerbAndJamaal': 'herb-and-jamaal',
    'HopeAndDeath': 'hope-and-death',
    'LibertyMeadows': 'liberty-meadows',
    'TheMeaningOfLila': 'meaning-of-lila',
    'MickeyMouse': 'mickey-mouse',
    'Momma': 'momma',
    'NestHeads': 'nest-heads',
    'OneBigHappy': 'one-big-happy',
    'OnAClaireDay': 'on-a-clair-day',
    'TheOtherCoast': 'other-coast',
    'TheQuigmans': 'quigmans',
    'Rubes': 'rubes',
    'Rugrats': 'rugrats',
    'ScaryGary': 'scary-gary',
    'SpeedBump': 'speed-bump',
    'StrangeBrew': 'strange-brew',
    'ThinLines': 'thin-lines',
    'WeePals': 'wee-pals',
    'WizardOfId': 'wizard-of-id',
    'WorkingItOut': 'working-it-out',
    'ZackHill': 'zack-hill',
    'BCSpanish': 'bc-spanish',
    'WizardOfIdSpanish': 'wizard-of-id-spanish',
    'ArchieSpanish': 'archie-spanish',
    'HeathcliffSpanish': 'heathcliff-spanish',
    'RugratsSpanish': 'rugrats-spanish',
    'LongStoryShort': 'long-story-short',
    'Recess': 'recess',
    'HomeOffice': 'stay-at-home-dad',
    'OffCenter': 'off-center',
    'GirlsAndSportsSpanish': 'girls-and-sports-spanish',
}

for name, shortname in comics.items():
    globals()[name] = creators(name, shortname)

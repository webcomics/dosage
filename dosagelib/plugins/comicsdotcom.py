# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from re import compile, sub

from ..scraper import _BasicScraper
from ..util import tagre

def comicsDotCom(name, section):
    baseUrl = 'http://www.gocomics.com/'
    classname = sub("[^0-9a-zA-Z_]", "", name)

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        prefix, year, month, day = pageUrl.split('/', 3)
        return "%s_%s%s%s.gif" % (name, year, month, day)

    return type('GoComicsDotCom_%s' % classname,
        (_BasicScraper,),
        dict(
        latestUrl=baseUrl + name,
        name='GoComicsDotCom/' + classname,
        stripUrl=baseUrl + name + '/%s',
        imageSearch=compile(tagre("img", "src", r'(http://assets\.amuniversal\.com/[0-9a-f]+)')),
        prevSearch=compile(tagre("a", "href", r'(/[^"]+/\d+/\d+/\d+)', after="prev")),
        help='Index format: yyyy/mm/dd',
        namer=namer)
    )

# http://www.gocomics.com/features
# XXX

# http://www.gocomics.com/explore/editorial_list
# XXX

# http://www.gocomics.com/explore/sherpa_list
# XXX

agnes = comicsDotCom('agnes', 'creators')
andycapp = comicsDotCom('andycapp', 'creators')
barkeaterlake = comicsDotCom('barkeaterlake', 'comics')
bc = comicsDotCom('bc', 'creators')
ben = comicsDotCom('ben', 'comics')
betty = comicsDotCom('betty', 'comics')
bignate = comicsDotCom('bignate', 'comics')
bonanas = comicsDotCom('bonanas', 'wash')
thebornloser = comicsDotCom('the-born-loser', 'comics')
thebuckets = comicsDotCom('thebuckets', 'comics')
candorville = comicsDotCom('candorville', 'wash')
calvinandhobbes = comicsDotCom('calvinandhobbes', 'comics')
chickweed = comicsDotCom('9chickweedlane', 'comics')
committed = comicsDotCom('committed', 'comics')
dilbert = comicsDotCom('dilbert', 'comics')
drabble = comicsDotCom('drabble', 'comics')
floandfriends = comicsDotCom('floandfriends', 'creators')
frazz = comicsDotCom('frazz', 'comics')
geech = comicsDotCom('geech', 'comics')
getfuzzy = comicsDotCom('getfuzzy', 'comics')
graffiti = comicsDotCom('graffiti', 'comics')
grandave = comicsDotCom('grand-avenue', 'comics')
heathcliff = comicsDotCom('heathcliff', 'creators')
herman = comicsDotCom('herman', 'comics')
janesworld = comicsDotCom('janesworld', 'comics')
jumpstart = comicsDotCom('jumpstart', 'comics')
kitandcarlyle = comicsDotCom('kitandcarlyle', 'comics')
luann = comicsDotCom('luann', 'comics')
marmaduke = comicsDotCom('marmaduke', 'comics')
moderatelyconfused = comicsDotCom('moderately-confused', 'comics')
momma = comicsDotCom('momma', 'creators')
monty = comicsDotCom('monty', 'comics')
nancy = comicsDotCom('nancy', 'comics')
offthemark = comicsDotCom('offthemark', 'comics')
onebighappy = comicsDotCom('onebighappy', 'creators')
peanuts = comicsDotCom('peanuts', 'comics')
pearlsbeforeswine = comicsDotCom('pearlsbeforeswine', 'comics')
pibgorn = comicsDotCom('pibgorn', 'comics')
pickles = comicsDotCom('pickles', 'wash')
redandrover = comicsDotCom('redandrover', 'wash')
roseisrose = comicsDotCom('roseisrose', 'comics')
rubes = comicsDotCom('rubes', 'creators')
rudypark = comicsDotCom('rudypark', 'comics')
speedbump = comicsDotCom('speedbump', 'creators')
strangebrew = comicsDotCom('strangebrew', 'creators')
tarzan = comicsDotCom('tarzan', 'comics')
wizardofid = comicsDotCom('wizardofid', 'creators')
workingdaze = comicsDotCom('working-daze', 'comics')
workingitout = comicsDotCom('workingitout', 'creators')

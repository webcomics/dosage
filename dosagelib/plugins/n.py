# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, sub
from ..scraper import _BasicScraper
from ..helpers import indirectStarter, _PHPScraper
from ..util import tagre


class NamirDeiter(_BasicScraper):
    latestUrl = 'http://www.namirdeiter.com/'
    stripUrl = latestUrl + 'comics/index.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.namirdeiter\.com/comics/\d\.jpg)', quote=""))
    prevSearch = compile(tagre("a", "href", r'(http://www\.namirdeiter\.com/comics/index\.php\?date=\d+)', quote="'")+"Previous")
    help = 'Index format: yyyymmdd'


class NeoEarth(_BasicScraper):
    latestUrl = 'http://www.neo-earth.com/NE/'
    stripUrl = latestUrl + 'index.php?date=%s'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'


class NewAdventuresOfBobbin(_BasicScraper):
    latestUrl = 'http://www.bobbin-comic.com/bobbin_strips/'
    imageSearch = compile(tagre("a", "href", r'(\d+\.gif)'))
    prevSearch = None
    help = 'Index format: none'


class NewWorld(_BasicScraper):
    latestUrl = 'http://www.tfsnewworld.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'<img src="(http://www.tfsnewworld.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/stripn'


class Nicky510(_BasicScraper):
    latestUrl = 'http://www.nickyitis.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.nickyitis\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.nickyitis\.com/comic/[^"]+)', after="Previous"))
    help = 'Index format: stripname'


class NoNeedForBushido(_BasicScraper):
    latestUrl = 'http://noneedforbushido.com/latest/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://noneedforbushido\.com/comics/comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://noneedforbushido\.com/[^"]+)', after="previous-comic-link"))
    help = 'Index format: yyyy/comic/nnn'


class Nukees(_BasicScraper):
    latestUrl = 'http://www.nukees.com/'
    stripUrl = latestUrl + 'd/%s'
    imageSearch = compile(r'"comic".+?"(/comics/.+?)"')
    prevSearch = compile(r'"(/d/.+?)".+?previous')
    help = 'Index format: yyyymmdd.html'



def nuklearpower(name, shortname):
    baseUrl = 'http://www.nuklearpower.com/'
    latestUrl = "%s%s/" % (baseUrl, shortname)
    classname = sub("[^0-9a-zA-Z_]", "", name)

    globals()[classname] = type('NuklearPower_%s' % classname,
        (_BasicScraper,),
        dict(
        name='NuklearPower/' + classname,
        latestUrl = latestUrl,
        stripUrl = latestUrl + '%s',
        imageSearch = compile(tagre("img", "src", r'(http://www\.nuklearpower\.com/comics/[^"]+)')),
        prevSearch = compile(tagre("a", "href", r'([^"]+)') + "Previous"),
        help = 'Index format: yyyy/mm/dd/name',
        )
    )


npstrips = {
    '8BitTheater': '8-bit-theater',
    'Warbot': 'warbot',
    'HowIKilledYourMaster': 'hikym',
    'AtomicRobo': 'atomic-robo',
}

for name, shortname in npstrips.items():
    nuklearpower(name, shortname)


class NekoTheKitty(_PHPScraper):
    basePath = 'http://www.nekothekitty.net/cusp/'
    latestUrl = basePath
    prevSearch = compile(tagre("a", "href", r'(http://www.nekothekitty.net/comics/[^"]+)') +
      tagre("img", "src", r'http://www\.nekothekitty\.net/files/smallprev.png'))



class NichtLustig(_BasicScraper):
    stripUrl = 'http://www.nichtlustig.de/toondb/%s.html'
    imageSearch = compile('background-image:url\((http://static\.nichtlustig\.de/comics/full/\d+\.jpg)')
    prevSearch = compile(tagre("a", "href", r'(http://static\.nichtlustig\.de/toondb/\d+\.html)'))
    help = 'Index format: yymmdd'
    starter = indirectStarter('http://www.nichtlustig.de/main.html',
                              compile(tagre("a", "href", r'([^"]*toondb/\d+\.html)')))


class Nodwick(_BasicScraper):
    latestUrl = 'http://comic.nodwick.com/'
    stripUrl = latestUrl + "?p=%s"
    imageSearch = compile(tagre("img", "src", r'(http://comic\.nodwick\.com/nodwickstrips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://comic\.nodwick\.com/\?p=\d+)', after="prev"))
    help = 'Index format: stripnumber'


class NekkoAndJoruba(_BasicScraper):
    latestUrl = 'http://www.nekkoandjoruba.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'<img src="(http://www.nekkoandjoruba.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">&lsaquo;</a>')
    help = 'Index format: nnn'



class NobodyScores(_BasicScraper):
    latestUrl = 'http://nobodyscores.loosenutstudio.com/'
    stripUrl = latestUrl + 'index.php?id=%s'
    imageSearch = compile(r'><img src="(http://nobodyscores\.loosenutstudio\.com/comix/.+?)"')
    prevSearch = compile(r'<a href="(http://nobodyscores\.loosenutstudio\.com/index.php.+?)">the one before </a>')
    help = 'Index format: nnn'

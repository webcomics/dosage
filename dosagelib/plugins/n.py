# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..helpers import indirectStarter, _PHPScraper



class NamirDeiter(_BasicScraper):
    latestUrl = 'http://www.namirdeiter.com/'
    stripUrl = 'http://www.namirdeiter.com/comics/index.php?date=%s'
    imageSearch = compile(r'<img.+?(/comics/\d{8}.+?)[\'|\"]')
    prevSearch = compile(r'(/comics/index.php\?date=.+?|http://www.namirdeiter.com/comics/index.php\?date=.+?)[\'|\"].+?previous')
    help = 'Index format: yyyymmdd'



class NeoEarth(_BasicScraper):
    latestUrl = 'http://www.neo-earth.com/NE/'
    stripUrl = 'http://www.neo-earth.com/NE/index.php?date=%s'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'



class Nervillsaga(_BasicScraper):
    latestUrl = 'http://www.nervillsaga.com/'
    stripUrl = 'http://www.nervillsaga.com/index.php?s=%s'
    imageSearch = compile(r'"(pic/.+?)"')
    prevSearch = compile(r'"(.+?)">Previous')
    help = 'Index format: nnn'



class NewAdventuresOfBobbin(_BasicScraper):
    latestUrl = 'http://bobbin-comic.com/'
    stripUrl = 'http://www.bobbin-comic.com/wordpress/?p=%s'
    imageSearch = compile(r'<img src="(http://www.bobbin-comic.com/wordpress/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><span class="prev">')
    help = 'Index format: n'



class NewWorld(_BasicScraper):
    latestUrl = 'http://www.tfsnewworld.com/'
    stripUrl = 'http://www.tfsnewworld.com/%s'
    imageSearch = compile(r'<img src="(http://www.tfsnewworld.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/stripn'



class Nicky510(_BasicScraper):
    latestUrl = 'http://www.nicky510.com/'
    stripUrl = 'http://www.nicky510.com/%s'
    imageSearch = compile(r'(http://www.nicky510.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.nicky510.com/.+?)" class="navi navi-prev"')
    help = 'Index format: yyyy/mm/dd/stripname/'



class NoNeedForBushido(_BasicScraper):
    latestUrl = 'http://www.noneedforbushido.com/latest/'
    stripUrl = 'http://www.noneedforbushido.com/%s'
    imageSearch = compile(r'<div class="comics"><img src="([^"]+)"')
    prevSearch = compile(r'<a href="([^"]+)" title="[^"]*" class="previous-comic-link')
    help = 'Index format: yyyy/comic/nnn'



class Nukees(_BasicScraper):
    latestUrl = 'http://www.nukees.com/'
    stripUrl = 'http://www.nukees.com/d/%s'
    imageSearch = compile(r'"comic".+?"(/comics/.+?)"')
    prevSearch = compile(r'"(/d/.+?)".+?previous')
    help = 'Index format: yyyymmdd.html'



class _NuklearPower(_BasicScraper):
    imageSearch = compile(r'<img src="(http://www.nuklearpower.com/comics/.+?)"')
    prevSearch = compile(r'><a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy/mm/dd/name'

    @property
    def baseUrl(self):
        return 'http://www.nuklearpower.com/%s/' % (self.shortName,)

    def starter(self):
        return self.baseUrl

    @property
    def stripUrl(self):
        return self.baseUrl + '%s'



class NP8BitTheater(_NuklearPower):
    name = 'NuklearPower/8BitTheater'
    shortName = '8-bit-theater'



class NPWarbot(_NuklearPower):
    name = 'NuklearPower/Warbot'
    shortName = 'warbot'



class NPHIKYM(_NuklearPower):
    name = 'NuklearPower/HowIKilledYourMaster'
    shortName = 'hikym'



class NPAtomicRobo(_NuklearPower):
    name = 'NuklearPower/AtomicRobo'
    shortName = 'atomic-robo'



class NekoTheKitty(_PHPScraper):
    basePath = 'http://www.nekothekitty.net/cusp/'
    latestUrl = 'latest.php'
    prevSearch = compile(r"<a href=\"(http://www\.nekothekitty\.net/cusp/daily\.php\?date=\d+)\"><img[^>]+alt='Previous Comic'")



class NichtLustig(_BasicScraper):
    stripUrl = 'http://www.nichtlustig.de/toondb/%s.html'
    imageSearch = compile(r'<img src="([^"]+)" id="cartoon"', IGNORECASE)
    prevSearch = compile(r'<a href="(\d+\.html)"[^<>]*><img[^<>]*id="pfeil_links', IGNORECASE)
    help = 'Index format: yymmdd'
    starter = indirectStarter('http://www.nichtlustig.de/main.html',
                              compile(r'<a href="([^"]*toondb/\d+\.html)"', IGNORECASE))


class NinthElsewhere(_BasicScraper):
    latestUrl = 'http://www.9thelsewhere.com/icenter.html'
    stripUrl = 'http://www.9thelsewhere.com/%s/9e%s_%s.html'
    imageSearch = compile(r'<img src="([^"]*9e\d+_\d+\.jpg)"')
    prevSearch = compile(r'<a href="([^"]+\.html)">\s*PREV')
    help = 'Index format: year-chapter-page'

    def setStrip(self, index):
        self.currentUrl = self.stripUrl % tuple(map(int, index.split('-')))


class Nodwick(_BasicScraper):
    stripUrl = None
    imageSearch = compile(r'<img src="(http://nodwick.humor.gamespy.com/gamespyarchive/strips/[^"]*)"', IGNORECASE)
    prevSearch = compile(r'<a href="(index.php\?date=[0-9-]*)"><img src="back.jpg"', IGNORECASE)
    starter = indirectStarter('http://nodwick.humor.gamespy.com/gamespyarchive/index.php', prevSearch)
    help = 'Index format: None'



class NekkoAndJoruba(_BasicScraper):
    latestUrl = 'http://www.nekkoandjoruba.com/'
    stripUrl = 'http://www.nekkoandjoruba.com/?p=%s'
    imageSearch = compile(r'<img src="(http://www.nekkoandjoruba.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">&lsaquo;</a>')
    help = 'Index format: nnn'



class NobodyScores(_BasicScraper):
    latestUrl = 'http://nobodyscores.loosenutstudio.com/'
    stripUrl = 'http://nobodyscores.loosenutstudio.com/index.php?id=%s'
    imageSearch = compile(r'><img src="(http://nobodyscores.loosenutstudio.com/comix/.+?)"')
    prevSearch = compile(r'<a href="(http://nobodyscores.loosenutstudio.com/index.php.+?)">the one before </a>')
    help = 'Index format: nnn'

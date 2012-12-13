# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, MULTILINE
from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import regexNamer, bounceStarter, indirectStarter


class ALessonIsLearned(_BasicScraper):
    baseUrl = 'http://www.alessonislearned.com/'
    prevSearch = compile(tagre("a", "href", r"(index\.php\?comic=\d+)", quote="'")+r"[^>]+previous")
    starter = indirectStarter(baseUrl, prevSearch)
    stripUrl = baseUrl + 'index.php?comic=%s'
    imageSearch = compile(tagre("img", "src", r"(cmx/lesson\d+\.[a-z]+)"))
    help = 'Index format: nnn'


class ASofterWorld(_BasicScraper):
    latestUrl = 'http://www.asofterworld.com/'
    stripUrl = latestUrl + 'index.php?id=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.asofterworld\.com/clean/[^"]+)'))
    prevSearch = compile(tagre("a", "href", "(index\.php\?id=\d+)")+'< back')
    help = 'Index format: n (unpadded)'


class AbleAndBaker(_BasicScraper):
    latestUrl = 'http://www.jimburgessdesign.com/comics/index.php'
    stripUrl = latestUrl + '?comic=%s'
    imageSearch = compile(tagre('img', 'src', r'(comics/.+)'))
    prevSearch = compile(tagre('a', 'href', r'(.+\d+)') + '.+?previous.gif')
    help = 'Index format: nnn'


class AbominableCharlesChristopher(_BasicScraper):
    latestUrl = 'http://www.abominable.cc/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.abominable\.cc/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"[^<]+Previous")
    help = 'Index format: yyyy/mm/dd/comicname'


class AbsurdNotions(_BasicScraper):
    latestUrl = 'http://www.absurdnotions.org/page129.html'
    stripUrl = 'http://www.absurdnotions.org/page%s.html'
    imageSearch = compile(tagre('img', 'src', r'(an[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre('a', 'href', r'([^"]+)') + tagre('img', 'src', 'nprev\.gif'))
    help = 'Index format: n (unpadded)'


class AbstruseGoose(_BasicScraper):
    starter = bounceStarter('http://abstrusegoose.com/',
       compile(tagre('a', 'href', r'(http://abstrusegoose\.com/\d+)')+"Next &raquo;</a>"))
    stripUrl = 'http://abstrusegoose.com/%s'
    imageSearch = compile(tagre('img', 'src', r'(http://abstrusegoose\.com/strips/[^<>"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(http://abstrusegoose\.com/\d+)') + r'&laquo; Previous</a>')
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').split('/')[-1])
        name = imageUrl.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)


class AcademyVale(_BasicScraper):
    latestUrl = 'http://www.imagerie.com/vale/'
    stripUrl = latestUrl + 'avarch.cgi?%s'
    imageSearch = compile(tagre('img', 'src', r'(avale\d{4}-\d{2}\.gif)'))
    prevSearch = compile(tagre('a', 'href', r'(avarch[^">]+)', quote="") + tagre('img', 'src', 'AVNavBack\.gif'))
    help = 'Index format: nnn'


class Alice(_BasicScraper):
    latestUrl = 'http://alice.alicecomics.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://alice\.alicecomics\.com/wp-content/webcomic/alicecomics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://alice\.alicecomics\.com/archive/[^"]+)', after="previous"))
    help = 'Index format: name'


class AlienLovesPredator(_BasicScraper):
    latestUrl = 'http://alienlovespredator.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'([^"]+)', after='border="1" alt="" width="750"'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name/'


class Altermeta(_BasicScraper):
    latestUrl = 'http://altermeta.net/'
    stripUrl = latestUrl + 'archive.php?comic=%s'
    imageSearch = compile(r'<img src="(comics/[^"]+)" />')
    prevSearch = compile(r'<a href="([^"]+)"><img src="http://altermeta\.net/template/default/images/sasha/back\.png')
    help = 'Index format: n (unpadded)'


class AltermetaOld(Altermeta):
    name = 'Altermeta/Old'
    latestUrl = 'http://altermeta.net/oldarchive/index.php'
    stripUrl = 'http://altermeta.net/oldarchive/archive.php?comic=%s'
    prevSearch = compile(r'<a href="([^"]+)">Back')


class Angels2200(_BasicScraper):
    latestUrl = 'http://www.janahoffmann.com/angels/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.janahoffmann\.com/angels/comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"&laquo; Previous")
    help = 'Index format: yyyy/mm/dd/part-<n>-comic-<n>'


class AppleGeeks(_BasicScraper):
    latestUrl = 'http://www.applegeeks.com/'
    stripUrl = latestUrl + 'comics/viewcomic.php?issue=%s'
    imageSearch = compile(tagre("img", "src", r'((?:/comics/)?issue\d+\.jpg)'))
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    help = 'Index format: n (unpadded)'


class Achewood(_BasicScraper):
    latestUrl = 'http://www.achewood.com/'
    stripUrl = latestUrl + 'index.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(/comic\.php\?date=\d+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)', after="Previous"))
    help = 'Index format: mmddyyyy'
    namer = regexNamer(compile(r'date=(\d+)'))


class AstronomyPOTD(_BasicScraper):
    starter = bounceStarter(
        'http://antwrp.gsfc.nasa.gov/apod/astropix.html',
        compile(r'<a href="(ap\d{6}\.html)">&gt;</a>'))
    stripUrl = 'http://antwrp.gsfc.nasa.gov/apod/ap%s.html'
    imageSearch = compile(r'<a href="(image/\d{4}/[^"]+)"')
    multipleImagesPerStrip = True
    prevSearch = compile(r'<a href="(ap\d{6}\.html)">&lt;</a>')
    help = 'Index format: yymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%s-%s' % (pageUrl.split('/')[-1].split('.')[0][2:],
                          imageUrl.split('/')[-1].split('.')[0])


class AfterStrife(_BasicScraper):
    latestUrl = 'http://afterstrife.com/?p=262'
    stripUrl = 'http://afterstrife.com/?p=%s'
    imageSearch = compile(r'<img src="(http://afterstrife.com/strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" class="navi navi-prev"')
    help = 'Index format: nnn'


class ALLCAPS(_BasicScraper):
    latestUrl = 'http://www.allcapscomix.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.allcapscomix\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+r"[^<]+Previous</a>")
    help = 'Index format: yyyy/mm/strip-name'


class ASkeweredParadise(_BasicScraper):
    latestUrl = 'http://aspcomics.net/'
    stripUrl = latestUrl + 'comic/%s'
    imageSearch = compile(tagre("img", "src", r'(http://aspcomics\.net/sites/default/files[^"]*/asp\d+\.jpg)[^"]+'))
    prevSearch = compile(tagre("a", "href", "(/comic/\d+)")+r"[^>]+Previous")
    help = 'Index format: nnn'


class AGirlAndHerFed(_BasicScraper):
    starter = bounceStarter('http://www.agirlandherfed.com/',
      compile(r'<a href="([^"]+)">[^>]+Back'))
    stripUrl = 'http://www.agirlandherfed.com/1.%s.html'
    imageSearch = compile(tagre("img", "src", r'(img/strip/[^"]+\.jpg)'))
    prevSearch = compile(r'<a href="([^"]+)">[^>]+Back')
    help = 'Index format: nnn'


class AetheriaEpics(_BasicScraper):
    latestUrl = 'http://aetheria-epics.schala.net/'
    stripUrl = latestUrl + '%s.html'
    imageSearch = compile(tagre("img", "src", r'(\d{5}\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(\d{5}\.html)') + "Previous")
    help = 'Index format: nnn'


class AirForceBlues(_BasicScraper):
    latestUrl = 'http://www.afblues.com/'
    stripUrl = latestUrl + 'wordpress/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.afblues\.com/wordpress/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='Previous'))
    help = 'Index format: yyyy/mm/dd/name/'


class AlienShores(_BasicScraper):
    latestUrl = 'http://alienshores.com/alienshores_band/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://alienshores\.com/alienshores_band/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://alienshores\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/p<nn>/'


class AllTheGrowingThings(_BasicScraper):
    latestUrl = 'http://growingthings.typodmary.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://growingthings\.typodmary\.com/files/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://growingthings\.typodmary\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name'


class Amya(_BasicScraper):
    latestUrl = 'http://www.amyachronicles.com/'
    stripUrl = latestUrl + 'archives/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.amyachronicles\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.amyachronicles\.com/archives/\d+)', after="Previous"))
    help = 'Index format: n'


class Angband(_BasicScraper):
    latestUrl = 'http://angband.calamarain.net/'
    stripUrl = latestUrl + 'view.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/Scroll[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date\=[^"]+)')+"Previous")
    help = 'Index format: yyyy-mm-dd'


class AlsoBagels(_BasicScraper):
    latestUrl = 'http://alsobagels.com/'
    stripUrl = latestUrl + 'index.php/comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://alsobagels\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://alsobagels\.com/index\.php/comic/[^"]+)', after="Previous"))
    help = 'Index format: strip-name'


class Annyseed(_BasicScraper):
    latestUrl = 'http://www.colourofivy.com/annyseed_webcomic_latest.htm'
    stripUrl = 'http://www.colourofivy.com/annyseed_webcomic%s.htm'
    imageSearch = compile(tagre("img", "src", r'(Annyseed[^"]+)'))
    prevSearch = compile(r'<a href="(http://www\.colourofivy\.com/[^"]+)"><img src="Last.gif"')
    help = 'Index format: nnn'

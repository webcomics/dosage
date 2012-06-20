# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, MULTILINE

from ..helpers import _BasicScraper, regexNamer, bounceStarter, indirectStarter


class ALessonIsLearned(_BasicScraper):
    latestUrl = 'http://www.alessonislearned.com/'
    imageUrl = 'http://www.alessonislearned.com/lesson%s.html'
    imageSearch = compile(r'<img src="(cmx/.+?)"')
    prevSearch = compile(r"<a href='(index.php\?comic=.+?)'.+?previous")
    help = 'Index format: nnn'


class ASofterWorld(_BasicScraper):
    latestUrl = 'http://www.asofterworld.com/'
    imageUrl = 'http://www.asofterworld.com/index.php?id=%s'
    imageSearch = compile(r'<img src="(http://www.asofterworld.com/clean/[^"]+)"')
    prevSearch = compile(r'"([^"]+)">back')
    help = 'Index format: n (unpadded)'


class AbleAndBaker(_BasicScraper):
    latestUrl = 'http://www.jimburgessdesign.com/comics/index.php'
    imageUrl = 'http://www.jimburgessdesign.com/comics/index.php?comic=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+\d+?)".+previous.gif')
    help = 'Index format: nnn'


class AbominableCharlesChristopher(_BasicScraper):
    latestUrl = 'http://abominable.cc/'
    imageUrl = 'http://abominable.cc/%s'
    imageSearch = compile(r'cc(/comics/.+?)"')
    prevSearch = compile(r'cc(/.+?)".+?prev')
    help = 'Index format: yyyy/mm/dd/comicname'


class AbstractGender(_BasicScraper):
    latestUrl = 'http://www.abstractgender.com/'
    imageUrl = 'http://www.abstractgender.com/?comic=%s'
    imageSearch = compile(r'<img[^>]+src="(comics/\d+\.\w+)"')
    prevSearch = compile(r'<a\W+href="(\?comic=\d+)"><img[^>]+id="comic_menu_prev"')
    help = 'Index format: n (unpadded)'


class AbsurdNotions(_BasicScraper):
    latestUrl = 'http://www.absurdnotions.org/page129.html'
    imageUrl = 'http://www.absurdnotions.org/page%s.html'
    imageSearch = compile(r'<IMG SRC="(an[^"]+)"')
    prevSearch = compile(r'HREF="([^"]+)"><IMG SRC="nprev\.gif"')
    help = 'Index format: n (unpadded)'



class AbstruseGoose(_BasicScraper):
    starter = bounceStarter('http://abstrusegoose.com/',
                            compile(r'<a href = "(http://abstrusegoose.com/\d+)">Next &raquo;</a>'))
    imageUrl = 'http://abstrusegoose.com/c%s.html'
    imageSearch = compile(r'<img[^<]+src="(http://abstrusegoose.com/strips/[^<>"]+)"')
    prevSearch = compile(r'<a href = "(http://abstrusegoose.com/\d+)">&laquo; Previous</a>')
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').split('/')[-1])
        name = imageUrl.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)



class AcademyVale(_BasicScraper):
    latestUrl = 'http://imagerie.com/vale/'
    imageUrl = 'http://imagerie.com/vale/avarch.cgi?%s'
    imageSearch = compile(r'<IMG.+?SRC="(avale\d{4}-\d{2}\..*?)"')
    prevSearch = compile(r'HREF=(avarch.*?)><IMG SRC="AVNavBack.gif"')
    help = 'Index format: nnn'



class Alice(_BasicScraper):
    latestUrl = 'http://alice.alicecomics.com/'
    imageUrl = 'http://alice.alicecomics.com/%s'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'	.+"?com(/.+?)" rel="prev')
    help = 'Index format: non'



class AlienLovesPredator(_BasicScraper):
    imageUrl = 'http://alienlovespredator.com/%s'
    imageSearch = compile(r'<img src="(.+?)"[^>]+>(<center>\n|\n|</center>\n)<div style="height: 2px;">&nbsp;</div>', MULTILINE)
    prevSearch = compile(r'<a href="(.+?)"><img src="/images/nav_previous.jpg"')
    help = 'Index format: nnn'
    starter = bounceStarter('http://alienlovespredator.com/index.php', compile(r'<a href="(.+?)"><img src="/images/nav_next.jpg"'))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        vol = pageUrl.split('/')[-5]
        num = pageUrl.split('/')[-4]
        ccc = pageUrl.split('/')[-3]
        ddd = pageUrl.split('/')[-2]
        return '%s-%s-%s-%s' % (vol, num, ccc, ddd)



class AnarchySD(_BasicScraper):
    imageUrl = 'http://www.anarchycomic.com/page%s.php'
    imageSearch = compile(r'<img.+src="../(images/page\d+\..+?)"')
    prevSearch = compile(r'<a href="(page\d+\.php)">PREVIOUS PAGE')
    help = 'Index format: n (unpadded)'
    starter = indirectStarter(
        'http://www.anarchycomic.com/page1.php',
        compile(r'<a href="(page\d+\.php)" class="style15">LATEST'))



class Altermeta(_BasicScraper):
    latestUrl = 'http://altermeta.net/'
    imageUrl = 'http://altermeta.net/archive.php?comic=%s&view=showfiller'
    imageSearch = compile(r'<img src="(comics/[^"]+)" />')
    prevSearch = compile(r'<a href="([^"]+)"><img src="http://altermeta\.net/template/default/images/sasha/back\.png')
    help = 'Index format: n (unpadded)'



class AltermetaOld(Altermeta):
    name = 'Altermeta/Old'
    latestUrl = 'http://altermeta.net/oldarchive/index.php'
    imageUrl = 'http://altermeta.net/oldarchive/archive.php?comic=%s'
    prevSearch = compile(r'<a href="([^"]+)">Back')



class Angels2200(_BasicScraper):
    latestUrl = 'http://www.janahoffmann.com/angels/'
    imageSearch = compile(r"<img src='(http://www.janahoffmann.com/angels/comics/[^']+)'>")
    prevSearch = compile(r'<a href="([^"]+)">&laquo; Previous</a>')



class AppleGeeks(_BasicScraper):
    latestUrl = 'http://www.applegeeks.com/'
    imageUrl = 'http://www.applegeeks.com/comics/viewcomic.php?issue=%s'
    imageSearch = compile(r'<img src="((?:/comics/)?issue\d+?\..+?)"')
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    help = 'Index format: n (unpadded)'


class AppleGeeksLite(_BasicScraper):
    latestUrl = 'http://www.applegeeks.com/lite/'
    imageUrl = 'http://applegeeks.com/lite/index.php?aglitecomic=%s'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(index.php\?aglitecomic=.+?)".+?back')
    help = 'Index format: yyyy-mm-dd'



class Achewood(_BasicScraper):
    latestUrl = 'http://www.achewood.com/'
    imageUrl = 'http://www.achewood.com/index.php?date=%s'
    imageSearch = compile(r'<img src="(http://m.assetbar.com/achewood/autaux.+?)"')
    prevSearch = compile(r'<a href="(index\.php\?date=\d{8})" class="dateNav" title="Previous comic"')
    help = 'Index format: mmddyyyy'
    namer = regexNamer(compile(r'date%3D(\d{8})'))



class AstronomyPOTD(_BasicScraper):
    starter = bounceStarter(
        'http://antwrp.gsfc.nasa.gov/apod/astropix.html',
        compile(r'<a href="(ap\d{6}\.html)">&gt;</a>'))
    imageUrl = 'http://antwrp.gsfc.nasa.gov/apod/ap%s.html'
    imageSearch = compile(r'<a href="(image/\d{4}/.+\..+?)">')
    prevSearch = compile(r'<a href="(ap\d{6}\.html)">&lt;</a>')
    help = 'Index format: yymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%s-%s' % (pageUrl.split('/')[-1].split('.')[0][2:],
                          imageUrl.split('/')[-1].split('.')[0])



class AfterStrife(_BasicScraper):
    latestUrl = 'http://afterstrife.com/?p=262'
    imageUrl = 'http://afterstrife.com/?p=%s'
    imageSearch = compile(r'<img src="(http://afterstrife.com/strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" class="navi navi-prev"')
    help = 'Index format: nnn'



class AnUnrehearsedRiot(_BasicScraper):
    latestUrl = 'http://unrehearsedriot.com/'
    imageUrl = 'http://unrehearsedriot.com/%s'
    imageSearch = compile(r'<img src="(http://unrehearsedriot.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://unrehearsedriot.com/.+?)" class="navi navi-prev"')
    help = 'Index format: yyyy/mm/dd/strip-name'



class ALLCAPS(_BasicScraper):
    latestUrl = 'http://www.allcapscomix.com/'
    imageUrl = 'http://www.allcapscomix.com/%s'
    imageSearch = compile(r'<img src="(http://www.allcapscomix.com/comics/.+?)"')
    prevSearch = compile(r'href="(.+?)">(&#9668; Previous|<span class="prev">)')
    help = 'Index format: yyyy/mm/strip-name'



class ASkeweredParadise(_BasicScraper):
    latestUrl = 'http://aspcomics.net/'
    imageUrl = 'http://aspcomics.net/archindex.php?strip_id=%s'
    imageSearch = compile(r'<img src="(istrip_files/strips/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="images/previous_day.jpg"')
    help = 'Index format: nnn'



class AGirlAndHerFed(_BasicScraper):
    starter = bounceStarter('http://www.agirlandherfed.com/',
                            compile(r' href="(/comic/\?\d+)" class="navigationActive">Next</a>\]'))
    imageUrl = 'http://www.agirlandherfed.com/comic/?%s'
    imageSearch = compile(r'<img src="(/images/comics/.+?)"')
    prevSearch = compile(r' href="(/comic/\?\d+)" class="navigationActive">Previous</a>\]')
    help = 'Index format: nnn'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('?')[-1]



class AetheriaEpics(_BasicScraper):
    latestUrl = 'http://aetheria-epics.schala.net/'
    imageUrl = 'http://aetheria-epics.schala.net/%s.html'
    imageSearch = compile(r'<td><img src="(\d{5}.\w{3,4})"')
    prevSearch = compile(r'<a href="(\d{5}.html)"><img src="prev.jpg"\/>')
    help = 'Index format: nnn'



class Adrift(_BasicScraper):
    latestUrl = 'http://www.adriftcomic.com/'
    imageUrl = 'http://www.adriftcomic.com/page%s.html'
    imageSearch = compile(r'<IMG SRC="(Adrift_Web_Page\d+.jpg)"')
    prevSearch = compile(r'<A HREF="(.+?)"><IMG SRC="AdriftBackLink.gif"')
    help = 'Index format: nnn'



class AirForceBlues(_BasicScraper):
    latestUrl = 'http://www.afblues.com/'
    imageUrl = 'http://www.afblues.com/?p=%s'
    imageSearch = compile(r'<img src=\'(http://www.afblues.com/comics/.+?)\'>')
    prevSearch = compile(r'<a href="(http://www.afblues.com/.+?)">&laquo; Previous')
    help = 'Index format: nnn'



class AlienShores(_BasicScraper):
    latestUrl = 'http://alienshores.com/alienshores_band/'
    imageUrl = 'http://alienshores.com/alienshores_band/?p=%s'
    imageSearch = compile(r'><img src="(http://alienshores.com/alienshores_band/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://alienshores.com/.+?)" rel="prev">')
    help = 'Index format: nnn'



class AllKindsOfBees(_BasicScraper):
    latestUrl = 'http://www.allkindsofbees.com/'
    imageUrl = 'http://www.allkindsofbees.com/?p=%s'
    imageSearch = compile(r'<img src="(http://www.allkindsofbees.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.allkindsofbees.com/.+?)">')
    help = 'Index format: nnn'



class AllTheGrowingThings(_BasicScraper):
    latestUrl = 'http://typodmary.com/growingthings/'
    imageUrl = 'http://typodmary.com/growingthings/%s/'
    imageSearch = compile(r'<img src="(http://typodmary.com/growingthings/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://typodmary.com/growingthings/.+?)"')
    help = 'Index format: yyyy/mm/dd/strip-name'



class Amya(_BasicScraper):
    latestUrl = 'http://www.amyachronicles.com/'
    imageUrl = 'http://www.amyachronicles.com/archives/%s'
    imageSearch = compile(r'<img src="(http://www.amyachronicles.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.amyachronicles.com/archives/.+?)"')
    help = 'Index format: nnn'



class Angband(_BasicScraper):
    latestUrl = 'http://angband.calamarain.net/index.php'
    imageUrl = 'http://angband.calamarain.net/view.php?date=%s'
    imageSearch = compile(r'<img src="(comics/Strip.+?)"')
    prevSearch = compile(r'<a href="(view.php\?date\=.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'



class ArcticBlast(_BasicScraper):
    latestUrl = 'http://www.arcticblastcomic.com/'
    imageUrl = 'http://www.arcticblastcomic.com/?p=%s'
    imageSearch = compile(r'<img src="(http://www.arcticblastcomic.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.arcticblastcomic.com/.+?)"')
    help = 'Index format: nnn'



class ActionAthena(_BasicScraper):
    latestUrl = 'http://actionathena.com/'
    imageUrl = 'http://actionathena.com/2%s'
    imageSearch = compile(r'<img src=\'(http://actionathena.com/comics/.+?)\'>')
    prevSearch = compile(r'<a href="(http://actionathena.com/.+?)">&laquo; Previous</a>')
    help = 'Index format: yyyy/mm/dd/strip-name'



class AlsoBagels(_BasicScraper):
    latestUrl = 'http://www.alsobagels.com/'
    imageUrl = 'http://alsobagels.com/index.php/comic/%s/'
    imageSearch = compile(r'<img src="(http://alsobagels.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://alsobagels.com/index.php/comic/.+?)">')
    help = 'Index format: strip-name'



class Annyseed(_BasicScraper):
    latestUrl = 'http://www.colourofivy.com/annyseed_webcomic_latest.htm'
    imageUrl = 'http://www.colourofivy.com/annyseed_webcomic%s.htm'
    imageSearch = compile(r'<td width="570" height="887" valign="top"><img src="(.+?)"')
    prevSearch = compile(r'<a href="(http://www.colourofivy.com/.+?)"><img src="Last.gif"')
    help = 'Index format: nnn'

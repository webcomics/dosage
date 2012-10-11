# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..util import tagre
from ..scraper import _BasicScraper


class BadlyDrawnKitties(_BasicScraper):
    latestUrl = 'http://www.badlydrawnkitties.com/'
    imageUrl = 'http://www.badlydrawnkitties.com/new/%s.html'
    imageSearch = compile(r'<img src="(/new/.+?)">')
    prevSearch = compile(r'"(/new/.+?)".+?previous.gif')
    help = 'Index format: n (unpadded)'


class Bardsworth(_BasicScraper):
    latestUrl = 'http://www.bardsworth.com/'
    imageUrl = 'http://www.bardsworth.com/archive.php?p=s%'
    imageSearch = compile(r'(strips/.+?)"')
    prevSearch = compile(r'"(http.+?)".+?/prev')
    help = 'Index format: nnn'


class BetterDays(_BasicScraper):
    latestUrl = 'http://www.jaynaylor.com/betterdays/'
    imageUrl = 'http://www.jaynaylor.com/betterdays/archives/%s'
    imageSearch = compile(r'<img src=(/betterdays/comic/.+?)>')
    prevSearch = compile(r'<a href="(.+)">&laquo; Previous')
    help = 'Index format: yyyy/mm/<your guess>.html'


class BetterYouThanMe(_BasicScraper):
    latestUrl = 'http://betteryouthanme.net/'
    imageUrl = 'http://betteryouthanme.net/archive.php?date=%s.gif'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'"(archive.php\?date=.+?)">.+?previous')
    help = 'Index format: yyyymmdd'


class BiggerThanCheeses(_BasicScraper):
    latestUrl = 'http://www.biggercheese.com'
    imageUrl = 'http://www.biggercheese.com/index.php?comic=%s'
    imageSearch = compile(r'src="(comics/.+?)" alt')
    prevSearch = compile(r'"(index.php\?comic=.+?)".+?_back')
    help = 'Index format: n (unpadded)'



class BizarreUprising(_BasicScraper):
    latestUrl = 'http://www.bizarreuprising.com/'
    imageUrl = 'http://www.bizarreuprising.com/view/%s'
    imageSearch = compile(r'<img src="(comic/[^"]+)"')
    prevSearch = compile(r'<a href="(view/\d+/[^"]+)"><img src="images/b_prev\.gif"')
    help = 'Index format: n/name'



class Blip(_BasicScraper):
    latestUrl = 'http://blipcomic.com/'
    imageUrl = 'http://blipcomic.com/index.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First.+?"(index.php\?strip_id=.+?)".+?prev')
    help = 'Index format: n'


class BlueCrashKit(_BasicScraper):
    latestUrl = 'http://www.bluecrashkit.com/cheese/'
    imageUrl = 'http://www.bluecrashkit.com/cheese/node/%s'
    imageSearch = compile(r'(/cheese/files/comics/.+?)"')
    prevSearch = compile(r'(/cheese/node/.+?)".+?previous')
    help = 'Index format: non'


class BMovieComic(_BasicScraper):
    latestUrl = 'http://www.bmoviecomic.com/'
    imageUrl = 'http://www.bmoviecomic.com/?cid=%s'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?Prev')
    help = 'Index format: n'


### With BratHalla there is no 'previous' link at comic 360
### You will need to use
### mainline -c BratHalla:360-backup-dad-unstable-plans/
### to get earlier comics
class BratHalla(_BasicScraper):
    latestUrl = 'http://brat-halla.com/'
    imageUrl = 'http://brat-halla.com/comic/%s'
    imageSearch = compile(r"(/comics/.+?)' target='_blank")
    prevSearch = compile(r'headernav2".+?"(http.+?)"')
    help = 'Index format: non'


class Brink(_BasicScraper):
    latestUrl = 'http://paperfangs.com/brink/'
    imageUrl = 'http://paperfangs.com/brink/?p=%s'
    imageSearch = compile(r'/(comics/.+?)"')
    prevSearch = compile(r'previous.+?/brink/(.+?)".+?Previous')
    help = 'Index format: non'



class BonoboConspiracy(_BasicScraper):
    latestUrl = 'http://ansuz.sooke.bc.ca/bonobo-conspiracy/'
    imageUrl = 'http://ansuz.sooke.bc.ca/bonobo-conspiracy/%s'
    imageSearch = compile(r'<P.+?<IMG SRC="(.+?)" ALT')
    prevSearch = compile(r'ansuz.+?/(\?i=.+?)".+?Previous')
    help = 'Index format: nnn'


class BoredAndEvil(_BasicScraper):
    latestUrl = 'http://www.boredandevil.com/'
    imageUrl = 'http://www.boredandevil.com/archive.php?date=%s'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'First Comic.+<a href="(.+?)".+previous-on.gif')
    help = 'Index format: yyyy-mm-dd'



class BoyOnAStickAndSlither(_BasicScraper):
    latestUrl = 'http://www.boasas.com/'
    imageUrl = 'http://www.boasas.com/?c=%s'
    imageSearch = compile(r'"(boasas/\d+\..+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img src="images/left_20.png"')
    help = 'Index format: n (unpadded)'



class ButternutSquash(_BasicScraper):
    latestUrl = 'http://www.butternutsquash.net/'
    imageUrl = 'http://www.butternutsquash.net/v3/%s'
    imageSearch = compile(r'<img src="(http://www.butternutsquash.net/v3/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.butternutsquash.net/v3/.+?)">(<span class="prev">&#9668;|&#8656; Previous</a>)')
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'



class Bhag(_BasicScraper):
    latestUrl = 'http://bhag.sackofjustice.com/'
    imageUrl = 'http://bhag.sackofjustice.com/daily.php?date='
    imageSearch = compile(r'/(comics/.+?)">')
    prevSearch = compile(r'first.+?/(daily.php\?date=.+?)".+?previous')
    help = 'Index format: yymmdd'


def blankLabel(name, baseUrl):
    return type('BlankLabel_%s' % name,
        (_BasicScraper,),
        dict(
        name='BlankLabel/' + name,
        latestUrl=baseUrl,
        imageUrl='/d/%s.shtml',
        imageSearch=compile(tagre("img", "src", r'(/comic[s|/][^"]+)')),
        prevSearch=compile(tagre("a", "href", r'(/d/\d+\.shtml)')+r"[^>]+/images/nav_02\.gif"),
        #prevSearch=compile(r'(?:"([^"]*(?:/d/[^"\r\n]*)|(?:/strip/.+?))")(?:(?:.{43}starshift_back.gif)|(?:.+?cxn_previous)|(?:.{43}previous)|(?:[^<>]*>[^<>]*<[^<>]*previous)|(?:.*?back_button)|(?:.*?comicnav-previous))'),
        help='Index format: yyyymmdd')
    )


checkerboard = blankLabel('CheckerboardNightmare', 'http://www.checkerboardnightmare.com')
courtingDisaster = blankLabel('CourtingDisaster', 'http://www.courting-disaster.com/')
evilInc = blankLabel('EvilInc', 'http://www.evil-comic.com/')
greystoneInn = blankLabel('GreystoneInn', 'http://www.greystoneinn.net/')
itsWalky = blankLabel('ItsWalky', 'http://www.itswalky.com/')
# one strip name starts with %20
#krazyLarry = blankLabel('KrazyLarry', 'http://www.krazylarry.com/')
melonpool = blankLabel('Melonpool', 'http://www.melonpool.com/')
# strip names = index.php
#realLife = blankLabel('RealLife', 'http://www.reallifecomics.com/')
schlockMercenary = blankLabel('SchlockMercenary', 'http://www.schlockmercenary.com/')
# hosted on ComicsDotCom
#sheldon = blankLabel('Sheldon', 'http://www.sheldoncomics.com/')
shortpacked = blankLabel('Shortpacked', 'http://www.shortpacked.com/')
starslipCrisis = blankLabel('StarslipCrisis', 'http://www.starslipcrisis.com/')
uglyHill = blankLabel('UglyHill', 'http://www.uglyhill.com/')



class BeePower(_BasicScraper):
    latestUrl = 'http://comicswithoutviolence.com/d/20080713.html'
    imageUrl = 'http://comicswithoutviolence.com/d/%s.html'
    imageSearch = compile(r'src="(/comics/.+?)"')
    prevSearch = compile(r'(\d+\.html)"><img[^>]+?src="/images/previous_day.png"')
    help = 'Index format: yyyy/mm/dd'



class Bellen(_BasicScraper):
    latestUrl = 'http://boxbrown.com/'
    imageUrl = 'http://boxbrown.com/?p=%s'
    imageSearch = compile(r'<img src="(http://boxbrown.com/comics/[^"]+)"')
    prevSearch = compile(r'<a href="(.+?)"><span class="prev">')
    help = 'Index format: nnn'



class BlankIt(_BasicScraper):
    latestUrl = 'http://blankitcomics.com/'
    imageUrl = 'http://blankitcomics.com/%s'
    imageSearch = compile(r'<img src="(http://blankitcomics.com/bicomics/.+?)"')
    prevSearch = compile(r'<a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/name'



class BobWhite(_BasicScraper):
    latestUrl = 'http://www.bobwhitecomics.com/'
    imageUrl = 'http://www.bobwhitecomics.com/?webcomic_post=%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.bobwhitecomics\.com/wp/wp-content/webcomic/untitled/\d+.jpg)"))
    prevSearch = compile(tagre("a", "href", "(http://www\.bobwhitecomics\.com/\?webcomic_post=\d+)")+r'[^"]+Previous')
    help = 'Index format: yyyymmdd'



class BigFatWhale(_BasicScraper):
    latestUrl = 'http://www.bigfatwhale.com/'
    imageUrl = 'http://www.bigfatwhale.com/archives/bfw_%s.htm'
    imageSearch = compile(r'<img src="(archives/bfw_.+?|bfw_.+?)"')
    prevSearch = compile(r' HREF="(.+?)" TARGET="_top" TITLE="Previous Cartoon"')
    help = 'Index format: nnn'



class BadassMuthas(_BasicScraper):
    latestUrl = 'http://badassmuthas.com/pages/comic.php'
    imageUrl = 'http://badassmuthas.com/pages/comic.php?%s'
    imageSearch = compile(r'<img src="(/images/comicsissue.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img src="/images/comicsbuttonBack.gif" ')
    help = 'Index format: nnn'



class Boozeathon4Billion(_BasicScraper):
    latestUrl = 'http://boozeathon4billion.com/'
    imageUrl = 'http://boozeathon4billion.com/comics/%s'
    imageSearch = compile(r'<img src="(http://boozeathon4billion.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>Previous</a>')
    help = 'Index format: (sometimes chapternumber/)-yyyy-mm-dd/stripname'



class BrightlyWound(_BasicScraper):
    latestUrl = 'http://www.brightlywound.com/'
    imageUrl = 'http://www.brightlywound.com/?comic=%s'
    imageSearch = compile(r'<img src=\'(comic/.+?)\'')
    prevSearch = compile(r'<div id=\'navback\'><a href=\'(\?comic\=\d+)\'><img src=\'images/previous.png\'')
    help = 'Index format: nnn'



class BlueCrashKit(_BasicScraper):
    latestUrl = 'http://robhamm.com/bluecrashkit'
    imageUrl = 'http://robhamm.com/comics/blue-crash-kit/%s'
    imageSearch = compile(r'src="(http://robhamm.com/sites/default/files/comics/.+?)"')
    prevSearch = compile(r'<li class="previous"><a href="(.+?)">')
    help = 'Index format: yyyy-mm-dd'



class BloodBound(_BasicScraper):
    latestUrl = 'http://www.bloodboundcomic.com/'
    imageUrl = 'http://www.bloodboundcomic.com/d/%s.html'
    imageSearch = compile(r' src="(/comics/.+?)"')
    prevSearch = compile(r' <a href="(/d/.+?)"><img[^>]+?src="/images/previous_day.jpg"')
    help = 'Index format: yyyymmdd'



class BookOfBiff(_BasicScraper):
    latestUrl = 'http://www.thebookofbiff.com/'
    imageUrl = 'http://www.thebookofbiff.com/%s'
    imageSearch = compile(r'<img src="(http://www.thebookofbiff.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.thebookofbiff.com/.+?)">&#9668; Previous</a>')
    help = 'Index format: yyyy/mm/dd/stripnum-strip-name'



class BillyTheDunce(_BasicScraper):
    latestUrl = 'http://www.duncepress.com/'
    imageUrl = 'http://www.duncepress.com/%s/'
    imageSearch = compile(r'<img src="(http://www.duncepress.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.duncepress.com/[^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/strip-name'



class BackwaterPlanet(_BasicScraper):
    latestUrl = 'http://www.backwaterplanet.com/current.htm'
    imageUrl = 'http://www.backwaterplanet.com/archive/bwp%s.htm'
    imageSearch = compile(r'<img src="(/images/comic/bwp.+?)">')
    prevSearch = compile(r'<a href="(/archive/bwp.+?)"><img src="(images/Previous.jpg|/images/Previous.jpg)"')
    help = 'Index format: yymmdd'



class Baroquen(_BasicScraper):
    latestUrl = 'http://www.baroquencomics.com/'
    imageUrl = 'http://www.baroquencomics.com/2010/01/04/the-man-from-omi/'
    imageSearch = compile(r'<img src="(http://www.baroquencomics.com/Comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.baroquencomics.com/.+?)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/strip-name'



class BetweenFailures(_BasicScraper):
    latestUrl = 'http://betweenfailures.com/'
    imageUrl = 'http://betweenfailures.com/%s'
    imageSearch = compile(r'<img src=\'(http://betweenfailures.com/comics/.+?)\'>')
    prevSearch = compile(r'<a href="(http://betweenfailures.com/.+?)">&laquo; Previous</a>')
    help = 'Index format: yyyy/mm/dd/stripnum-strip-name'



class BillyTheBeaker(_BasicScraper):
    latestUrl = 'http://billy.defectivejunk.com/'
    imageUrl = 'http://billy.defectivejunk.com/index.php?strip=%s'
    imageSearch = compile(r'<img src="(bub\d+_\d+.+?)"')
    prevSearch = compile(r' <a href="(index.php\?strip\=.+?)" title="Previous strip">')
    help = 'Index format: nnn'

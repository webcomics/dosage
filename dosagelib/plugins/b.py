# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile

from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import indirectStarter


class BadMachinery(_BasicScraper):
    url = 'http://scarygoround.com/'
    stripUrl = url + '?date=%s'
    imageSearch = compile(tagre("img", "src", r'(strips/\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?date=\d+)') + 'Previous')
    help = 'Index format: yyyymmdd'


class Bardsworth(_BasicScraper):
    url = 'http://www.bardsworth.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.bardsworth\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.bardsworth\.com/[^"]+)', after="prev"))
    help = 'Index format: nnn'


class Bearmageddon(_BasicScraper):
    url = 'http://bearmageddon.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2011/08/01/page-1'
    imageSearch = compile(tagre("img", "src", r'(http://bearmageddon\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://bearmageddon\.com/\d+/\d+/\d+/[^"]+)', after='navi-prev'))
    help = 'Index format: yyyy/mm/dd/stripname'


class BetterDays(_BasicScraper):
    url = 'http://jaynaylor.com/betterdays/'
    stripUrl = url + 'archives/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/betterdays/comic/[^>]+)', quote=""))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + '&laquo; Previous')
    help = 'Index format: yyyy/mm/<your guess>'


class BiggerThanCheeses(_BasicScraper):
    url = 'http://www.biggercheese.com/'
    stripUrl = url + 'index.php?comic=%s'
    imageSearch = compile(r'src="(comics/.+?)" alt')
    prevSearch = compile(r'"(index.php\?comic=.+?)".+?_back')
    help = 'Index format: n (unpadded)'


class BizarreUprising(_BasicScraper):
    url = 'http://www.bizarreuprising.com/'
    stripUrl = url + 'view/%s'
    imageSearch = compile(tagre("img", "src", r'(comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view/\d+/[^"]+)') + tagre("img", "src", r'images/b_prev\.gif'))
    help = 'Index format: n/name'


class Blip(_BasicScraper):
    url = 'http://blipcomic.com/'
    stripUrl = url + 'index.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First.+?"(index.php\?strip_id=.+?)".+?prev')
    help = 'Index format: n'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("www.blipcomic.com", "blipcomic.com")


class BlueCrashKit(_BasicScraper):
    url = 'http://robhamm.com/bluecrashkit/'
    stripUrl = url + 'comics/blue-crash-kit/%s'
    imageSearch = compile(tagre("img", "src", r'(http://robhamm\.com/bluecrashkit/sites/default/files/comics/[^"]+)'))
    prevSearch = compile(r'<li class="previous"><a href="([^"]+)">')
    help = 'Index format: yyyy-mm-dd'


class BMovieComic(_BasicScraper):
    url = 'http://www.bmoviecomic.com/'
    stripUrl = url + '?cid=%s'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?Prev')
    help = 'Index format: n'


### With BratHalla there is no 'previous' link at comic 360
### You will need to use
### mainline -c BratHalla:360-backup-dad-unstable-plans/
### to get earlier comics
class BratHalla(_BasicScraper):
    url = 'http://brat-halla.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(r"(/comics/.+?)' target='_blank")
    prevSearch = compile(r'headernav2".+?"(http.+?)"')
    help = 'Index format: non'


class BrentalFloss(_BasicScraper):
    url = 'http://brentalflossthecomic.com/'
    stripUrl = url + '?id=%s'
    imageSearch = compile(tagre("img", "src", r'([^"]*/img/comic/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*)') + "Prev")
    help = 'Index format: n'


class BrentalFlossFit(BrentalFloss):
    name = 'BrentalFloss/FlossedInTime'
    url = 'http://brentalflossthecomic.com/fit/'
    stripUrl = url + '?id=%s'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("\n", "")

    @classmethod
    def imageUrlModifier(cls, url):
        if url:
            return url.replace("\n", "")

class BrentalFlossGuest(BrentalFloss):
    name = 'BrentalFloss/GuestComics'
    url = 'http://brentalflossthecomic.com/guestcomics/'
    stripUrl = url + '?id=%s'


# XXX disallowed by robots.txt
class _BringBackRoomies(_BasicScraper):
    url = "http://www.bringbackroomies.com/"
    stripUrl = url + "comic/%s"
    imageSearch = compile(tagre("img", "src", r'(http://www\.bringbackroomies\.com/wp-content/uploads/\d+/\d+/[^"]+)'))
    prevSearch = compile(tagre("span", "class", "mininav-prev") +
        tagre("a", "href", r'(http://www\.bringbackroomies\.com/comic/[^"]+)'))
    help = 'Index format: stripname'


class Brink(_BasicScraper):
    url = 'http://paperfangs.com/brink/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://paperfangs\.com/brink/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://paperfangs\.com/brink/[^"]+)', after="prev"))
    help = 'Index format: n'


class BoredAndEvil(_BasicScraper):
    url = 'http://www.boredandevil.com/'
    stripUrl = url + '?date=%s'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(r'First Comic.+<a href="(.+?)".+previous-on.gif')
    starter = indirectStarter(url, prevSearch)
    help = 'Index format: yyyy-mm-dd'


class BoyOnAStickAndSlither(_BasicScraper):
    url = 'http://www.boasas.com/'
    stripUrl = url + 'page/%s'
    imageSearch = compile(tagre("img", "src", r'(http://\d+\.media\.tumblr\.com/[^"]+_1280\.png)'))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') + "<span>Next page")
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.rsplit('/')[-1]


class BoxerHockey(_BasicScraper):
    url = 'http://boxerhockey.fireball20xl.com/'
    stripUrl = url + '?id=%s'
    imageSearch = compile(tagre("img", "src", r'(img/comic/[^"]+)', after="comicimg"))
    prevSearch = compile(tagre("a", "href", r'(http://www\.boxerhockey\.com/\?id=\d+)') +
        r'[^>]+Previous')
    help = 'Index format: n (unpadded)'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("www.boxerhockey.com", "boxerhockey.fireball20xl.com")


class BroodHollow(_BasicScraper):
    url = 'http://broodhollow.chainsawsuit.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://broodhollow\.chainsawsuit\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://broodhollow\.chainsawsuit\.com/\d+/\d+/\d+/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ButterSafe(_BasicScraper):
    url = 'http://buttersafe.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://buttersafe\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://buttersafe\.com/\d+\d+/\d+/\d+/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


# XXX disallowed by robots.txt
class _ButtercupFestival(_BasicScraper):
    url = 'http://www.buttercupfestival.com/'
    stripUrl = url + '%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://www\.buttercupfestival\.com/\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\d+-\d+\.html)', quote="") + "previous")
    help = 'Index format: number-number'


class ButternutSquash(_BasicScraper):
    url = 'http://www.butternutsquash.net/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.butternutsquash\.net/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.butternutsquash\.net/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'


class BlankIt(_BasicScraper):
    url = 'http://blankitcomics.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://blankitcomics\.com/bicomics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='rel="prev"'))
    help = 'Index format: yyyy/mm/dd/name'


class BobWhite(_BasicScraper):
    url = 'http://www.bobwhitecomics.com/'
    stripUrl = url + '?webcomic_post=%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.bobwhitecomics\.com/wp/wp-content/webcomic/untitled/\d+.jpg)"))
    prevSearch = compile(tagre("a", "href", "(http://www\.bobwhitecomics\.com/\?webcomic_post=\d+)")+r'[^"]+Previous')
    help = 'Index format: yyyymmdd'


class BigFatWhale(_BasicScraper):
    url = 'http://www.bigfatwhale.com/'
    stripUrl = url + 'archives/bfw_%s.htm'
    imageSearch = compile(tagre("img", "src", r'(archives/bfw_[^"]+|bfw_[^"]+)'))
    prevSearch = compile(r' HREF="(.+?)" TARGET="_top" TITLE="Previous Cartoon"')
    help = 'Index format: nnn'


class BadassMuthas(_BasicScraper):
    url = 'http://badassmuthas.com/pages/comic.php'
    stripUrl = url + '?%s'
    imageSearch = compile(tagre("img", "src", r'(/images/comicsissue[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'/images/comicsbuttonBack\.gif'))
    help = 'Index format: nnn'


class BrightlyWound(_BasicScraper):
    baseUrl = 'http://www.brightlywound.com/'
    url = baseUrl + '?comic=137'
    stripUrl = baseUrl + '?comic=%s'
    imageSearch = compile(tagre("img", "src", r"(comic/[^']+)", quote="'"))
    prevSearch = compile(r'<div id=\'navback\'><a href=\'(\?comic\=\d+)\'><img src=\'images/previous.png\'')
    help = 'Index format: nnn'


class BloodBound(_BasicScraper):
    url = 'http://bloodboundcomic.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://bloodboundcomic\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://bloodboundcomic\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/name'


class BookOfBiff(_BasicScraper):
    url = 'http://www.thebookofbiff.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'([^"]+/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripnum-strip-name'


class BillyTheDunce(_BasicScraper):
    url = 'http://www.duncepress.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.duncepress\.com/comics/[^"]+)'))
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.duncepress.com/[^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/strip-name'


class BackwaterPlanet(_BasicScraper):
    url = 'http://www.backwaterplanet.com/current.htm'
    stripUrl = 'http://www.backwaterplanet.com/archive/bwp%s.htm'
    imageSearch = compile(r'<img src="(/images/comic/bwp.+?)">')
    prevSearch = compile(r'<a href="(/archive/bwp.+?)"><img src="(images/Previous.jpg|/images/Previous.jpg)"')
    help = 'Index format: yymmdd'


class Baroquen(_BasicScraper):
    url = 'http://www.baroquencomics.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.baroquencomics\.com/Comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.baroquencomics\.com/[^"]+)', after='prev'))
    help = 'Index format: yyyy/mm/dd/strip-name'


class BetweenFailures(_BasicScraper):
    url = 'http://betweenfailures.com/'
    stripUrl = url + 'archives/archive/%s'
    imageSearch = compile(tagre("img", "src", r'(http://betweenfailures\.com/wp-content/webcomic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://betweenfailures\.com/archives/archive/[^"]+)', after="previous"))
    help = 'Index format: stripnum-strip-name'

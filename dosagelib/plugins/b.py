# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape

from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import indirectStarter


class BackwaterPlanet(_BasicScraper):
    url = 'http://www.backwaterplanet.com/current.htm'
    stripUrl = 'http://www.backwaterplanet.com/archive/bwp%s.htm'
    imageSearch = compile(r'<img src="(/images/comic/bwp.+?)">')
    prevSearch = compile(r'<a href="(/archive/bwp.+?)"><img src="(images/Previous.jpg|/images/Previous.jpg)"')
    help = 'Index format: yymmdd'


class BadassMuthas(_BasicScraper):
    description = u'Nobody wants to work for a living. Get yourself some super-powers and come ill with us. Full color update every Friday.'
    url = 'http://badassmuthas.com/pages/comic.php'
    stripUrl = url + '?%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/images/comicsissue[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'/images/comicsbuttonBack\.gif'))
    help = 'Index format: nnn'


class BadMachinery(_BasicScraper):
    url = 'http://scarygoround.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20090918'
    imageSearch = compile(tagre("img", "src", r'(strips/\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?date=\d+)') + 'Previous')
    help = 'Index format: yyyymmdd'


class Bardsworth(_BasicScraper):
    description = u'Bardsworth - Magic, Mischief, and Cookies'
    url = 'http://www.bardsworth.com/'
    rurl = escape(url)
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % '750'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: stripname'


class Baroquen(_BasicScraper):
    url = 'http://www.baroquencomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/11/05/raise-the-curtains'
    imageSearch = compile(tagre("img", "src", r'(%sComics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after='prev'))
    help = 'Index format: yyyy/mm/dd/strip-name'


class Bearmageddon(_BasicScraper):
    url = 'http://bearmageddon.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2011/08/01/page-1'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after='navi-prev'))
    help = 'Index format: yyyy/mm/dd/stripname'


class Beetlebum(_BasicScraper):
    description = u'JoJos Illustrierter Blog'
    url = 'http://blog.beetlebum.de/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2006/03/10/quiz-fur-ruskiphile'
    starter = indirectStarter(url, compile(tagre('a', 'href', r'(%s\d{4}/\d{2}/\d{2}/[^"]+)' % rurl, after='bookmark')))
    multipleImagesPerStrip = True
    imageSearch = compile(tagre('img', 'src', r'(http://blog\.beetlebum\.de/wp-content/uploads/[^"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(%s\d{4}/\d{2}/\d{2}/[^"]*)' % rurl, after='prev'))
    help = 'Index format: yyyy/mm/dd/striptitle'
    lang = 'de'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        indexes = tuple(pageUrl.rstrip('/').split('/')[-4:])
        name = '%s-%s-%s-%s' % indexes
        name = name + '_' + imageUrl.split( '/' )[-1]
        return name


class BetterDays(_BasicScraper):
    description = u'Better Days'
    url = 'http://jaynaylor.com/betterdays/'
    stripUrl = url + 'archives/%s.html'
    firstStripUrl = stripUrl % '2003/04/post-2'
    imageSearch = compile(tagre("img", "src", r'(/betterdays/comic/[^>]+)', quote=""))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + '&laquo; Previous')
    help = 'Index format: yyyy/mm/<your guess>'


class BetweenFailures(_BasicScraper):
    description = u'Between Failures'
    url = 'http://betweenfailures.com/'
    rurl = escape(url)
    stripUrl = url + 'comics1/%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomics1/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'


class BigFatWhale(_BasicScraper):
    description = u'A weekly comic strip for those who are not dumb.'
    url = 'http://www.bigfatwhale.com/'
    stripUrl = url + 'archives/bfw_%s.htm'
    imageSearch = compile(tagre("img", "src", r'(archives/bfw_[^"]+|bfw_[^"]+)'))
    prevSearch = compile(r' HREF="(.+?)" TARGET="_top" TITLE="Previous Cartoon"')
    help = 'Index format: nnn'


class BiggerThanCheeses(_BasicScraper):
    description = u'Bigger Than Cheeses - My webcomic will knife fight your webcomic'
    url = 'http://www.biggercheese.com/'
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'src="(comics/.+?)" alt')
    prevSearch = compile(r'"(index.php\?comic=.+?)".+?_back')
    help = 'Index format: n (unpadded)'


class BillyTheDunce(_BasicScraper):
    description = u"Billy the Dunce: A webcomic about some genius kids, some supernatural creatures, and one dumb kid who's stuck with them. Like Goonies, but with more Lovecraft."
    url = 'http://www.duncepress.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/06/an-introduction-of-sorts'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(r'<div class="nav-previous"><a href="(%s[^"]+)" rel="prev">' % rurl)
    help = 'Index format: yyyy/mm/stripname'


class BizarreUprising(_BasicScraper):
    description = u"Bizarre Uprising - Manga that's not just good, it's good for you!"
    url = 'http://www.bizarreuprising.com/'
    stripUrl = url + 'view/%s'
    firstStripUrl = stripUrl % '1/awakening-splash'
    imageSearch = compile(tagre("img", "src", r'(comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view/\d+/[^"]+)') + tagre("img", "src", r'images/b_prev\.gif'))
    help = 'Index format: n/name'


class BlankIt(_BasicScraper):
    description = u'An absurd, insane, and delightful webcomic from Aric McKeown and Lem Pew.'
    url = 'http://blankitcomics.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '0001'
    imageSearch = compile(tagre("img", "src", r'(http://blankitcomics\.com/bicomics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='rel="prev"'))
    help = 'Index format: stripname'


class Blip(_BasicScraper):
    url = 'http://blipcomic.com/'
    stripUrl = url + 'index.php?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First.+?"(index.php\?strip_id=.+?)".+?prev')
    help = 'Index format: n'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("www.blipcomic.com", "blipcomic.com")


class BloodBound(_BasicScraper):
    description = u'Demonic Vampire Hotness'
    adult = True
    url = 'http://bloodboundcomic.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/06/06112006'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/name'


class BMovieComic(_BasicScraper):
    description = u"A group of unlikely heroes tackles monsters, mutants and aliens from Hollywood's past and present. See what happens. Or they'll say you haven't seen it."
    url = 'http://www.bmoviecomic.com/'
    stripUrl = url + '?cid=%s'
    firstStripUrl = stripUrl % '8'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?Prev')
    help = 'Index format: n'


class BobWhite(_BasicScraper):
    description = u'Bobwhite by Magnolia Porter'
    url = 'http://www.bobwhitecomics.com/'
    rurl = escape(url)
    stripUrl = url + '?webcomic_post=%s'
    firstStripUrl = stripUrl % '20110504'
    imageSearch = compile(tagre("img", "src", r"(%swp/wp-content/webcomic/untitled/\d+.jpg)" % rurl))
    prevSearch = compile(tagre("a", "href", "(%s\?webcomic_post=\d+)" % rurl)+r'[^"]+Previous')
    help = 'Index format: yyyymmdd'


class BookOfBiff(_BasicScraper):
    description = u'The Book of Biff - new adventures every monday through friday'
    url = 'http://thebookofbiff.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/01/02/4'
    imageSearch = compile(tagre("img", "src", r'([^"]+/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripnum-stripname'


class BoredAndEvil(_BasicScraper):
    url = 'http://www.boredandevil.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2004-06-07'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(r'First Comic.+<a href="(.+?)".+previous-on.gif')
    starter = indirectStarter(url, prevSearch)
    help = 'Index format: yyyy-mm-dd'


class BoxerHockey(_BasicScraper):
    description = u'Boxer Hockey'
    url = 'http://boxerhockey.fireball20xl.com/'
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '56'
    imageSearch = compile(tagre("img", "src", r'(img/comic/[^"]+)', after="comicimg"))
    prevSearch = compile(tagre("a", "href", r'(http://www\.boxerhockey\.com/\?id=\d+)') +
        r'[^>]+Previous')
    help = 'Index format: n (unpadded)'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("www.boxerhockey.com", "boxerhockey.fireball20xl.com")


class BoyOnAStickAndSlither(_BasicScraper):
    description = u'A comic about killer bees, time travel, ethics and despair.'
    url = 'http://www.boasas.com/'
    stripUrl = url + 'page/%s'
    firstStripUrl = stripUrl % '2'
    imageSearch = compile(tagre("img", "src", r'(http://\d+\.media\.tumblr\.com/[^"]+_1280\.png)'))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') + "<span>Next page")
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.rsplit('/')[-1]


class BratHalla(_BasicScraper):
    description = u'Norse mythology webcomic where young Thor, Loki, Balder, Hod and more face off against grade school and make an old man out of their immortal dad Odin'
    url = 'http://brat-halla.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '1-balder-dash'
    imageSearch = compile(r"(/comics/.+?)' target='_blank")
    prevSearch = compile(r'headernav2".+?"(http.+?)"')
    help = 'Index format: number-stripname'


class BrentalFloss(_BasicScraper):
    description = u'brentalfloss the comic :: Off To The Races'
    url = 'http://brentalflossthecomic.com/'
    stripUrl = url + '?id=%s'
    fristStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'([^"]*/img/comic/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*)') + "Prev")
    help = 'Index format: n'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("www.", "")


class BrentalFlossFit(BrentalFloss):
    name = 'BrentalFloss/FlossedInTime'
    url = 'http://brentalflossthecomic.com/fit/'
    stripUrl = url + '?id=%s'
    fristStripUrl = stripUrl % '1'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            return prevUrl.replace("\n", "")

    @classmethod
    def imageUrlModifier(cls, url, data):
        if url:
            return url.replace("\n", "")


class BrentalFlossGuest(BrentalFloss):
    name = 'BrentalFloss/GuestComics'
    url = 'http://brentalflossthecomic.com/guestcomics/'
    stripUrl = url + '?id=%s'
    fristStripUrl = stripUrl % '1'


# XXX disallowed by robots.txt
class _BringBackRoomies(_BasicScraper):
    url = "http://www.bringbackroomies.com/"
    rurl = escape(url)
    stripUrl = url + "comic/%s"
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("span", "class", "mininav-prev") +
        tagre("a", "href", r'(%scomic/[^"]+)' % rurl))
    help = 'Index format: stripname'


class Brink(_BasicScraper):
    description = u"BRINK - You're not as crazy as you think you are"
    url = 'http://paperfangs.com/brink/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '5'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: number'


class BrightlyWound(_BasicScraper):
    description = u'A webcomic of physics, astronomy, math, and grammar.'
    baseUrl = 'http://www.brightlywound.com/'
    url = baseUrl + '?comic=137'
    stripUrl = baseUrl + '?comic=%s'
    fristStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r"(comic/[^']+)", quote="'"))
    prevSearch = compile(r'<div id=\'navback\'><a href=\'(\?comic\=\d+)\'><img src=\'images/previous.png\'')
    help = 'Index format: nnn'


class BroodHollow(_BasicScraper):
    description = u'Broodhollow - A MWF cosmic horror adventure comic by Kris Straub'
    url = 'http://broodhollow.chainsawsuit.com/'
    rurl = escape(url)
    stripUrl = url + 'page/%s/'
    firstStripUrl = stripUrl % '2012/10/08/broodhollow'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%spage/\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


# XXX disallowed by robots.txt
class _ButtercupFestival(_BasicScraper):
    url = 'http://www.buttercupfestival.com/'
    stripUrl = url + '%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://www\.buttercupfestival\.com/\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\d+-\d+\.html)', quote="") + "previous")
    help = 'Index format: number-number'


class ButterSafe(_BasicScraper):
    url = 'http://buttersafe.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/04/03/breakfast-sad-turtle'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ButternutSquash(_BasicScraper):
    description = u'ButterNutSquash - by P\xe9rez & Coughler'
    url = 'http://www.butternutsquash.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/04/16/meet-da-punks'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'

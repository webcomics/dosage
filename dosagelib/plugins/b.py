# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape

from ..util import tagre, getPageContent
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter


class BackwaterPlanet(_BasicScraper):
    url = 'http://www.backwaterplanet.com/current.htm'
    stripUrl = 'http://www.backwaterplanet.com/archive/bwp%s.htm'
    imageSearch = compile(r'<img src="(/images/comic/bwp.+?)">')
    prevSearch = compile(r'<a href="(/archive/bwp.+?)"><img src="(images/Previous.jpg|/images/Previous.jpg)"')
    help = 'Index format: yymmdd'


class BadassMuthas(_BasicScraper):
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
    url = 'http://jaynaylor.com/betterdays/'
    stripUrl = url + 'archives/%s.html'
    firstStripUrl = stripUrl % '2003/04/post-2'
    imageSearch = compile(tagre("img", "src", r'(/betterdays/comic/[^>]+)', quote=""))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + '&laquo; Previous')
    help = 'Index format: yyyy/mm/<your guess>'


class BetweenFailures(_BasicScraper):
    url = 'http://betweenfailures.com/'
    rurl = escape(url)
    stripUrl = url + 'comics1/%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomics1/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'


class BigFatWhale(_BasicScraper):
    url = 'http://www.bigfatwhale.com/'
    stripUrl = url + 'archives/bfw_%s.htm'
    imageSearch = compile(tagre("img", "src", r'(archives/bfw_[^"]+|bfw_[^"]+)'))
    prevSearch = compile(r' HREF="(.+?)" TARGET="_top" TITLE="Previous Cartoon"')
    help = 'Index format: nnn'


class BiggerThanCheeses(_BasicScraper):
    url = 'http://www.biggercheese.com/'
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'src="(comics/.+?)" alt')
    prevSearch = compile(r'"(index.php\?comic=.+?)".+?_back')
    help = 'Index format: n (unpadded)'


class BillyTheDunce(_BasicScraper):
    url = 'http://www.duncepress.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/06/an-introduction-of-sorts'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(r'<div class="nav-previous"><a href="(%s[^"]+)" rel="prev">' % rurl)
    help = 'Index format: yyyy/mm/stripname'


class BizarreUprising(_BasicScraper):
    url = 'http://www.bizarreuprising.com/'
    stripUrl = url + 'view/%s'
    firstStripUrl = stripUrl % '1/awakening-splash'
    imageSearch = compile(tagre("img", "src", r'(comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view/\d+/[^"]+)') + tagre("img", "src", r'images/b_prev\.gif'))
    help = 'Index format: n/name'


class BlankIt(_BasicScraper):
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

class BloomingFaeries(_BasicScraper):
    adult = True
    url = 'http://www.bloomingfaeries.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/public/%s/'
    firstStripUrl = stripUrl % "pit-stop"
    imageSearch = compile(tagre("img", "src", r'(http://www.bloomingfaeries.com/wp-content/uploads[^"]+)', after='title'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='comic-nav-base comic-nav-previous'))
    help = 'Index format: stripname'
 
    @classmethod
    def namer(cls, imageUrl, pageUrl):
        bf = imageUrl.split('/')
        name = bf[-1]
        re = compile(tagre("div","class",r'comic-id-([^"]+)'))
        content = getPageContent(pageUrl, cls.session)
        match = re.search(content)
        if not match:
            return None
        return "BF%s_%s" % (match.group(1),name)

class BMovieComic(_BasicScraper):
    url = 'http://www.bmoviecomic.com/'
    stripUrl = url + '?cid=%s'
    firstStripUrl = stripUrl % '8'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?Prev')
    help = 'Index format: n'


class BobWhite(_BasicScraper):
    url = 'http://www.bobwhitecomics.com/'
    rurl = escape(url)
    stripUrl = url + '?webcomic_post=%s'
    firstStripUrl = stripUrl % '20110504'
    imageSearch = compile(tagre("img", "src", r"(%swp/wp-content/webcomic/untitled/\d+.jpg)" % rurl))
    prevSearch = compile(tagre("a", "href", "(%s\?webcomic_post=\d+)" % rurl)+r'[^"]+Previous')
    help = 'Index format: yyyymmdd'


class BookOfBiff(_BasicScraper):
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
    url = 'http://www.boasas.com/'
    stripUrl = url + 'page/%s'
    firstStripUrl = stripUrl % '2'
    imageSearch = compile(tagre("img", "src", r'(http://\d+\.media\.tumblr\.com/[^"]+_1280\.png)'))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') + "<span>Next page")
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.rsplit('/')[-1]


class BrentalFloss(_BasicScraper):
    url = 'http://brentalflossthecomic.com/'
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '1'
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
    firstStripUrl = stripUrl % '1'

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
    firstStripUrl = stripUrl % '1'


class Brink(_BasicScraper):
    url = 'http://paperfangs.com/brink/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '5'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: number'


class BrightlyWound(_BasicScraper):
    baseUrl = 'http://www.brightlywound.com/'
    url = baseUrl + '?comic=137'
    stripUrl = baseUrl + '?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r"(comic/[^']+)", quote="'"))
    prevSearch = compile(r'<div id=\'navback\'><a href=\'(\?comic\=\d+)\'><img src=\'images/previous.png\'')
    help = 'Index format: nnn'


class ButtercupFestival(_ParserScraper):
    url = 'http://www.buttercupfestival.com/'
    stripUrl = url + '%s.htm'
    firstStripUrl = stripUrl % '2-1'
    imageSearch = '//center/img'
    prevSearch = '//a[text()="previous"]'
    help = 'Index format: 2-number'


class ButterSafe(_BasicScraper):
    url = 'http://buttersafe.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/04/03/breakfast-sad-turtle'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ButternutSquash(_BasicScraper):
    url = 'http://www.butternutsquash.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/04/16/meet-da-punks'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'

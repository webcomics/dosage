# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..util import tagre
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, xpath_class
from .common import _ComicControlScraper, _WordPressScraper, _WPNaviIn, _WPWebcomic


class BadassMuthas(_BasicScraper):
    url = 'http://badassmuthas.com/pages/comic.php'
    stripUrl = url + '?%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/images/comicsissue[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') +
                         tagre("img", "src", r'/images/comicsbuttonBack\.gif'))
    help = 'Index format: nnn'


class BadMachinery(_ParserScraper):
    url = 'http://scarygoround.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20090918'
    imageSearch = '//img[@class="comicimg"]'
    prevSearch = '//a[contains(text(), "Previous")]'
    broken_html_bugfix = True
    help = 'Index format: yyyymmdd'


class BalderDash(_ComicControlScraper):
    url = 'http://www.balderdashcomic.com/'


class BallerinaMafia(_ParserScraper):
    url = 'http://www.ballerinamafia.net/'
    stripUrl = url + 'index.php?pid=%s'
    firstStripUrl = stripUrl % '20100906'
    imageSearch = ('//img[contains(@alt, "Comic")]',
                   '//a[contains(@href, "comics/")]')
    prevSearch = '//a[@class="prev"]'
    adult = True
    endOfLife = True


class Bardsworth(_WordPressScraper):
    url = 'http://www.bardsworth.com/'
    latestSearch = '//a[@rel="bookmark"]'
    starter = indirectStarter


class Baroquen(_BasicScraper):
    url = 'http://www.baroquencomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/11/05/raise-the-curtains'
    imageSearch = compile(tagre("img", "src", r'(%sComics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after='prev'))
    help = 'Index format: yyyy/mm/dd/strip-name'


class Bearmageddon(_WordPressScraper):
    url = 'http://bearmageddon.com/bearmo/page-1/'
    firstStripUrl = url
    latestSearch = '//a[%s]' % xpath_class('comic-nav-last')
    starter = indirectStarter


class Beetlebum(_BasicScraper):
    url = 'http://blog.beetlebum.de/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2006/03/10/quiz-fur-ruskiphile'
    starter = indirectStarter
    multipleImagesPerStrip = True
    imageSearch = compile(tagre('img', 'src', r'(http://blog\.beetlebum\.de/wp-content/uploads/[^"]+)'))
    prevSearch = compile(tagre('a', 'href',
                               r'(%s\d{4}/\d{2}/\d{2}/[^"]*)' % rurl,
                               after='prev'))
    latestSearch = compile(tagre('a', 'href',
                                 r'(%s\d{4}/\d{2}/\d{2}/[^"]+)' % rurl,
                                 after='bookmark'))
    help = 'Index format: yyyy/mm/dd/striptitle'
    lang = 'de'

    def namer(self, image_url, page_url):
        indexes = tuple(page_url.rstrip('/').split('/')[-4:])
        name = '%s-%s-%s-%s' % indexes
        name = name + '_' + image_url.split('/')[-1]
        return name


class Bethellium(_WPWebcomic):
    stripUrl = 'http://dbcomics.darkblueworkshop.com/bethellium/%s/'
    firstStripUrl = stripUrl % 'chapter-1/webcomic-bethellium-chapter-1-cover'
    url = firstStripUrl
    starter = indirectStarter

    def namer(self, imageUrl, pageUrl):
        # Prepend chapter title to page filenames
        chapter = pageUrl.rstrip('/').rsplit('/', 3)[-2]
        chapter = chapter.replace('chapter-1', 'chapter-1-the-magic-city')
        page = imageUrl.rsplit('/', 1)[-1]
        return chapter + '_' + page


class BetterDays(_ParserScraper):
    url = 'http://jaynaylor.com/betterdays/'
    stripUrl = url + 'archives/%s.html'
    firstStripUrl = stripUrl % '2003/04/post-2'
    imageSearch = '//img[contains(@src, "/betterdays/comic/")]'
    prevSearch = '//a[contains(text(), "Previous")]'
    endOfLife = True
    help = 'Index format: yyyy/mm/<your guess>'


class BetweenFailures(_BasicScraper):
    url = 'http://betweenfailures.com/'
    rurl = escape(url)
    stripUrl = url + 'comics1/%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomics1/[^"]+)' % rurl,
                               after="previous"))
    help = 'Index format: stripname'


class BeyondTheVeil(_WordPressScraper):
    url = 'http://beyondtheveilcomic.com/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % '01252010'
    endOfLife = True

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        filename = filename.replace('BtV_pg43_bw', '2014-04-25-BtV_pg43_bw')
        filename = filename.replace('BtVpg28Ch7b', '2014-07-04-BtVpg28Ch7b')
        return filename


class BiggerThanCheeses(_BasicScraper):
    url = 'http://www.biggercheese.com/'
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'src="(comics/.+?)" alt')
    prevSearch = compile(r'"(index.php\?comic=.+?)".+?_back')
    help = 'Index format: n (unpadded)'


class BillyTheDunce(_ParserScraper):
    stripUrl = ('https://web.archive.org/web/20180404142544/'
        'http://www.duncepress.com/%s/')
    url = stripUrl % '2012/02/losing-more'
    firstStripUrl = stripUrl % '2009/06/an-introduction-of-sorts'
    imageSearch = '//div[@class="entry"]/p[1]/a'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True


class BittersweetCandyBowl(_ParserScraper):
    url = 'https://www.bittersweetcandybowl.com/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % 'c1/p1'
    imageSearch = '//img[@id="page_img"]'
    prevSearch = '//a[@rel="prev"]'

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 2)
        return filename[1] + '_' + filename[2]


class BlankIt(_ParserScraper):
    url = 'http://blankitcomics.com/'
    firstStripUrl = url + 'comic/well-what-would-you-do'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[%s]' % xpath_class('comic-nav-previous')
    latestSearch = '//a[%s]' % xpath_class('comic-nav-last')
    starter = indirectStarter


class BlondeSunrise(_ParserScraper):
    url = 'https://blondesunrise.com/comic.php?page=latest'
    firstStripUrl = 'https://blondesunrise.com/comic/comic.php?page=1'
    imageSearch = '//img[contains(@src, "comic_imgs/")]'
    prevSearch = '//a[img[contains(@src, "previous")]]'


class BloodBound(_WordPressScraper):
    url = 'http://bloodboundcomic.com/'
    firstStripUrl = 'http://bloodboundcomic.com/comic/06112006/'


class Bloodline(_WordPressScraper):
    url = 'http://w0lfmare.xepher.net/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'pg-1-2'
    imageSearch = '//div[@id="comic"]//img[not(contains(@src, "TWC-vote-image"))]'

    def namer(self, imageUrl, pageUrl):
        # Fix filenames of early comics
        return imageUrl.rsplit('/', 1)[-1].replace('gen-6', 'Bloodline')


class BloomingFaeries(_WordPressScraper):
    adult = True
    url = 'http://www.bloomingfaeries.com/'
    firstStripUrl = url + 'comic/public/pit-stop/'

    def namer(self, image_url, page_url):
        return "_".join(image_url.rsplit('/', 3)[1:])


class BMovieComic(_BasicScraper):
    url = 'http://www.bmoviecomic.com/'
    stripUrl = url + '?cid=%s'
    firstStripUrl = stripUrl % '8'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?Prev')
    help = 'Index format: n'


class BobWhite(_ParserScraper):
    url = 'http://www.bobwhitecomics.com/'
    imageSearch = '//span[%s]/img' % xpath_class('webcomic-object')
    prevSearch = '//a[@rel="previous"]'


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
    latestSearch = prevSearch
    starter = indirectStarter
    help = 'Index format: yyyy-mm-dd'


class BratHalla(_WordPressScraper):
    url = 'http://brat-halla.com/'


class Brink(_BasicScraper):
    url = 'http://paperfangs.com/brink/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '5'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: number'


class BroodHollow(_WordPressScraper):
    url = 'http://broodhollow.chainsawsuit.com/'
    firstStripUrl = 'http://broodhollow.chainsawsuit.com/page/2012/10/06/book-1-curious-little-thing'

    def shouldSkipUrl(self, url, data):
        return data.xpath('//div[@id="comic"]//iframe')


class Buni(_WordPressScraper):
    url = 'http://www.bunicomic.com/'


class BusinessCat(_WPNaviIn):
    url = 'http://www.businesscat.happyjar.com/'


class ButImACatPerson(_WordPressScraper):
    url = 'https://www.bicatperson.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = 'sketches-1'


class ButtercupFestival(_ParserScraper):
    url = 'http://www.buttercupfestival.com/'
    stripUrl = url + '%s.htm'
    firstStripUrl = stripUrl % '2-1'
    imageSearch = '//center/img'
    prevSearch = '//a[text()="previous"]'
    help = 'Index format: 2-number'


class ButternutSquash(_BasicScraper):
    url = 'http://www.butternutsquash.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/04/16/meet-da-punks'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'


class ButterSafe(_BasicScraper):
    url = 'http://buttersafe.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/04/03/breakfast-sad-turtle'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+\d+/\d+/\d+/[^"]+)' % rurl,
                               after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'

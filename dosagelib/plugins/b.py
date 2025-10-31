# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import compile, escape

from ..helpers import indirectStarter, joinPathPartsNamer
from ..scraper import ParserScraper, _BasicScraper, _ParserScraper
from ..util import tagre
from .common import (
    ComicControlScraper,
    WordPressNavi,
    WordPressScraper,
    WordPressWebcomic,
)


class BackOffice(WordPressNavi):
    url = 'https://rawrtacular.com/bo/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'back-office'


class BadassMuthas(ParserScraper):
    url = ('https://web.archive.org/web/20200117233227/'
        'http://badassmuthas.com/pages/comic.php')
    stripUrl = url + '?%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src,"/comicsissue")]'
    prevSearch = '//a[./img[contains(@src,"/comicsbuttonBack")]]'
    help = 'Index format: nnn'


class BadMachinery(_ParserScraper):
    url = 'https://scarygoround.com/badmachinery/index.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20090921'
    imageSearch = '//img[@class="comicimg"]'
    prevSearch = '//a[contains(text(), "Previous")]'
    endOfLife = True
    help = 'Index format: yyyymmdd'


class BalderDash(ComicControlScraper):
    url = 'http://www.balderdashcomic.com/'


class BallerinaMafia(_ParserScraper):
    url = 'https://web.archive.org/web/20200115230012/http://ballerinamafia.net/'
    stripUrl = url + 'index.php?pid=%s'
    firstStripUrl = stripUrl % '20100906'
    imageSearch = ('//img[contains(@alt, "Comic")]',
                   '//a[contains(@href, "comics/")]')
    prevSearch = '//a[@class="prev"]'
    adult = True
    endOfLife = True


class Bardsworth(WordPressScraper):
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


class BeachWzrd(WordPressScraper):
    url = 'https://mcnostril.com/comic/chapter-1-cover/'
    firstStripUrl = url
    imageSearch = '//div[@id="comic"]//noscript/img'
    latestSearch = '//a[d:class("comic-nav-last")]'
    starter = indirectStarter


class Bearmageddon(WordPressScraper):
    url = 'http://bearmageddon.com/bearmo/page-1/'
    firstStripUrl = url
    latestSearch = '//a[d:class("comic-nav-last")]'
    starter = indirectStarter


class Beetlebum(ParserScraper):
    url = 'https://blog.beetlebum.de/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2005/08/12/my-first-blog'
    starter = indirectStarter
    namer = joinPathPartsNamer(pageparts=range(-4, 0), imageparts=(-1,))
    multipleImagesPerStrip = True
    imageSearch = '//div[d:class("entry-content")]//img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@rel="bookmark"]'
    help = 'Index format: yyyy/mm/dd/striptitle'
    lang = 'de'


class Bethellium(WordPressWebcomic):
    url = 'https://bethellium.darkbluecomics.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'cover'


class BetterDays(_ParserScraper):
    url = 'https://web.archive.org/web/20200201203404/http://jaynaylor.com/betterdays/'
    stripUrl = url + 'archives/%s.html'
    firstStripUrl = stripUrl % '2003/04/post-2'
    imageSearch = '//img[contains(@src, "/betterdays/comic/")]'
    prevSearch = '//a[contains(text(), "Previous")]'
    adult = True
    endOfLife = True


class BetweenFailures(WordPressWebcomic):
    url = 'https://betweenfailures.com/'
    stripUrl = url + 'comics1/%s'
    firstStripUrl = stripUrl % 'every-story-has-to-start-somewhere'
    help = 'Index format: stripname'


class BeyondTheVeil(WordPressScraper):
    url = 'https://web.archive.org/web/20201009235642/http://beyondtheveilcomic.com/'
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


class BirdBoy(WordPressScraper):
    url = 'https://bird-boy.com/'
    stripUrl = url + 'comic/{0}-{1}/'
    firstStripUrl = stripUrl.format('volume-i', 'the-sword-of-mali-mani')
    help = 'volume-page # Examples: i-the-sword-of-mali-mani, iii-7, synopsis-2'

    def getIndexStripUrl(self, index):
        (volume, strip) = index.split('-', maxsplit=1)
        try:
            pageNr = int(strip)
        except ValueError:
            pageNr = None  # Use the string to fetch a cover page
        if volume == 'synopsis':
            strip = '{0}{1}'.format(pageNr, '-02' if strip in [1, 3] else '')
        else:
            volume = 'volume-' + volume
            if pageNr is not None:
                strip = 'page-{0}'.format(pageNr)
        return self.stripUrl.format(volume, strip)

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        if filename == 'image.jpg':
            [year, month] = imageUrl.rsplit('/', 3)[-3:-1]
            pageNr = int(pageUrl.rsplit('/', 1)[-2].rsplit('-', 1)[-1])
            filename = '{0}-{1}-Vol2-pg{2}.jpg'.format(year, month, pageNr)
        elif filename == '27637.jpg':
            filename = 'BB_Vol2_Cover.jpg'
        return filename


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
    prevSearch = '//a[d:class("comic-nav-previous")]'
    latestSearch = '//a[d:class("comic-nav-last")]'
    starter = indirectStarter


class BlondeSunrise(_ParserScraper):
    url = 'https://blondesunrise.com/comic.php?page=latest'
    firstStripUrl = 'https://blondesunrise.com/comic/comic.php?page=1'
    imageSearch = '//img[contains(@src, "comic_imgs/")]'
    prevSearch = '//a[img[contains(@src, "previous")]]'


class Bloodline(WordPressScraper):
    url = 'http://w0lfmare.xepher.net/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'pg-1-2'
    imageSearch = '//div[@id="comic"]//img[not(contains(@src, "TWC-vote-image"))]'

    def namer(self, imageUrl, pageUrl):
        # Fix filenames of early comics
        return imageUrl.rsplit('/', 1)[-1].replace('gen-6', 'Bloodline')


class BloomingFaeries(ParserScraper):
    url = 'https://www.bloomingfaeries.com/'
    firstStripUrl = url + 'comic/public/pit-stop/'
    imageSearch = '//div[@id="spliced-comic"]//img'
    prevSearch = '//a[d:class("previous-comic")]'
    adult = True
    namer = joinPathPartsNamer(imageparts=range(-3, 0))


class BMovieComic(_ParserScraper):
    url = 'https://bmoviecomic.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'chapter-1-strip-1'
    multipleImagesPerStrip = True
    imageSearch = '//div[d:class("entry-content")]//img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: pagename'


class BobWhite(_ParserScraper):
    url = 'http://www.bobwhitecomics.com/'
    imageSearch = '//span[d:class("webcomic-object")]/img'
    prevSearch = '//a[@rel="previous"]'


class BookOfBiff(WordPressScraper):
    url = 'https://thebookofbiff.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '4'


class BoredAndEvil(_ParserScraper):
    url = 'http://orphanedcomics.com/boredandevil/'
    stripUrl = url + 'webcomic-%s.html'
    firstStripUrl = stripUrl % '2004-06-07'
    imageSearch = '//img[d:class("webcomic")]'
    prevSearch = '//a[img[@title="Previous"]]'
    endOfLife = True
    help = 'Index format: yyyy-mm-dd'


class BratHalla(WordPressScraper):
    url = 'http://brat-halla.com/'


class Brink(WordPressScraper):
    stripUrl = 'https://paperfangs.com/brink/?comic=%s'
    firstStripUrl = stripUrl % 'chapter1coversmall'
    url = stripUrl % 'brink639small'
    endOfLife = True


class Buni(WordPressScraper):
    url = 'http://www.bunicomic.com/'


class BusinessCat(_ParserScraper):
    url = 'https://www.businesscatcomic.com/'
    imageSearch = '//div[d:class("comic-image")]//img'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True


class ButImACatPerson(WordPressScraper):
    url = 'https://www.bicatperson.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = 'sketches-1'
    endOfLife = True


class ButtercupFestival(_ParserScraper):
    url = 'http://www.buttercupfestival.com/'
    stripUrl = url + '%s.htm'
    firstStripUrl = stripUrl % '2-1'
    imageSearch = '//center/img'
    prevSearch = (
        '//a[img[contains(@src, "previous")]]',  # 3-x
        '//a[text()="previous"]',  # 2-x
    )


class ButternutSquash(ParserScraper):
    url = ('https://web.archive.org/web/20170319023859/'
        'http://www.butternutsquash.net/')
    stripUrl = url + '2003/04/16/meet-da-punks/%s/'  # The website is very broken
    firstStripUrl = stripUrl % '2003/04/16/meet-da-punks'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'


class ButterSafe(_ParserScraper):
    url = 'https://www.buttersafe.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/04/03/breakfast-sad-turtle'
    imageSearch = '//div[@id="comic"]/img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy/mm/dd/stripname'


class ByTheBook(WordPressScraper):
    url = 'http://www.btbcomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'chapter-1-page-0'
    adult = True

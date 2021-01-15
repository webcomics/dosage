# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile, escape

from ..util import tagre
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from .common import _ComicControlScraper, _WordPressScraper, _WPNavi, _WPWebcomic


class BackOffice(_WPNavi):
    url = 'https://rawrtacular.com/bo/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'back-office'


class BadassMuthas(_BasicScraper):
    url = 'http://badassmuthas.com/pages/comic.php'
    stripUrl = url + '?%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/images/comicsissue[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') +
                         tagre("img", "src", r'/images/comicsbuttonBack\.gif'))
    help = 'Index format: nnn'


class BadMachinery(_ParserScraper):
    url = 'https://scarygoround.com/badmachinery/index.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20090921'
    imageSearch = '//img[@class="comicimg"]'
    prevSearch = '//a[contains(text(), "Previous")]'
    endOfLife = True
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
    latestSearch = '//a[d:class("comic-nav-last")]'
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
        return name + '_' + image_url.split('/')[-1]


class Bethellium(_WPWebcomic):
    stripUrl = 'http://dbcomics.darkblueworkshop.com/bethellium/%s/'
    firstStripUrl = stripUrl % 'chapter-1/cover'
    url = firstStripUrl
    latestSearch = '//main' + _WPWebcomic.latestSearch
    starter = indirectStarter

    def getPrevUrl(self, url, data):
        prevUrl = super(Bethellium, self).getPrevUrl(url, data)
        return prevUrl.replace('%webcomic2_storyline%', 'chapter-2-the-hemlocks-scar')

    def namer(self, imageUrl, pageUrl):
        # Prepend chapter title to page filenames
        chapter = pageUrl.rstrip('/').rsplit('/', 3)[-2]
        chapter = chapter.replace('chapter-1', 'chapter-1-the-magic-city')
        page = imageUrl.rsplit('/', 1)[-1]
        return chapter + '_' + page


class BetterDays(_ParserScraper):
    url = 'https://web.archive.org/web/20200201203404/http://jaynaylor.com/betterdays/'
    stripUrl = url + 'archives/%s.html'
    firstStripUrl = stripUrl % '2003/04/post-2'
    imageSearch = '//img[contains(@src, "/betterdays/comic/")]'
    prevSearch = '//a[contains(text(), "Previous")]'
    adult = True
    endOfLife = True


class BetweenFailures(_WPWebcomic):
    url = 'https://betweenfailures.com/'
    stripUrl = url + 'comics1/%s'
    firstStripUrl = stripUrl % 'every-story-has-to-start-somewhere'
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


class BirdBoy(_ParserScraper):
    url = 'http://bird-boy.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/volume-{0}-{1}/'
    firstStripUrl = stripUrl.format('i', 'the-sword-of-mali-mani')
    imageSearch = '//div[@id="comic"]/a/img'
    prevSearch = '//link[@rel="prev"]'
    help = '(volume,page) # Examples: (i,the-sword-of-mali-mani), (iii,7)'

    def getIndexStripUrl(self, index):
        volume = index[0]
        strip = index[1]
        try:
            pageNr = int(strip)
            strip = 'page-{0}'.format(pageNr)
        return self.stripUrl.format(volume, strip)


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


class BookOfBiff(_WordPressScraper):
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


class BratHalla(_WordPressScraper):
    url = 'http://brat-halla.com/'


class Brink(_WordPressScraper):
    stripUrl = 'https://paperfangs.com/brink/?comic=%s'
    firstStripUrl = stripUrl % 'chapter1coversmall'
    url = stripUrl % 'brink639small'
    endOfLife = True


class BroodHollow(_WordPressScraper):
    url = 'https://broodhollow.chainsawsuit.com/'
    firstStripUrl = url + 'page/2012/10/06/book-1-curious-little-thing'

    def shouldSkipUrl(self, url, data):
        return data.xpath('//div[@id="comic"]//iframe')


class Buni(_WordPressScraper):
    url = 'http://www.bunicomic.com/'


class BusinessCat(_ParserScraper):
    url = 'https://www.businesscatcomic.com/'
    imageSearch = '//div[d:class("comic-image")]//img'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True


class ButImACatPerson(_WordPressScraper):
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


class ButternutSquash(_BasicScraper):
    url = 'http://www.butternutsquash.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/04/16/meet-da-punks'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'


class ButterSafe(_ParserScraper):
    url = 'https://www.buttersafe.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/04/03/breakfast-sad-turtle'
    imageSearch = '//div[@id="comic"]/img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy/mm/dd/stripname'

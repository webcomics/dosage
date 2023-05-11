# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2021 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile, escape

from ..util import tagre
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, joinPathPartsNamer
from .common import ComicControlScraper, WordPressNaviIn, WordPressScraper


class FalconTwin(_BasicScraper):
    url = 'http://www.falcontwin.com/'
    stripUrl = url + 'index.html?strip=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'"(strips/.+?)"')
    prevSearch = compile(r'"prev"><a href="(index.+?)"')
    help = 'Index format: nnn'


class FalseStart(_ParserScraper):
    baseUrl = 'https://boneitisindustries.com/'
    url = baseUrl + 'comics/false-start/'
    stripUrl = baseUrl + 'comic/%s/'
    firstStripUrl = stripUrl % 'false-start-chapter-zero-page-1'
    imageSearch = '//div[@id="content"]//img[d:class("size-full")]'
    prevSearch = '//a[./span[d:class("ticon-chevron-left")]]'
    adult = True

    def starter(self):
        archivePage = self.getPage(self.url)
        self.archive = archivePage.xpath('//div[contains(@class, "vcex-portfolio-grid")]//a/@href')
        return self.archive[-1]

    def getPrevUrl(self, url, data):
        return self.archive[self.archive.index(url) - 1]


class Faneurysm(WordPressNaviIn):
    url = 'http://hijinksensue.com/comic/think-only-tree/'
    firstStripUrl = 'http://hijinksensue.com/comic/captains-prerogative/'
    endOfLife = True


class FantasyRealms(_ParserScraper):
    stripUrl = ('https://web.archive.org/web/20161204192651/'
        'http://fantasyrealmsonline.com/manga/%s.php')
    url = stripUrl % '091'
    firstStripUrl = stripUrl % '001'
    imageSearch = '//img[contains(@src, "/manga/0")]'
    prevSearch = '//a[img[contains(@src, "nav-back")]]'
    endOfLife = True
    help = 'Index format: nnn'


class FarToTheNorth(ComicControlScraper):
    url = 'http://www.farnorthcomic.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'don39t-tell'


class FauxPas(_ParserScraper):
    url = 'http://www.ozfoxes.net/cgi/pl-fp1.cgi'
    stripUrl = url + '?%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@name]'
    prevSearch = '//a[img[@alt="Previous"]]'
    help = 'Index format: nnn'


class FireflyCross(WordPressScraper):
    url = 'http://www.fireflycross.pensandtales.com/'
    firstStripUrl = url + '?comic=05062002'


class FirstWorldProblems(_ParserScraper):
    url = ('https://web.archive.org/web/20150710053456/'
        'http://bradcolbow.com/archive/C5/')
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'P10'
    imageSearch = '//div[d:class("entry")]//img'
    prevSearch = '//a[d:class("prev")]'
    multipleImagesPerStrip = True
    endOfLife = True


class FlakyPastry(_BasicScraper):
    baseUrl = 'http://flakypastry.runningwithpencils.com/'
    url = baseUrl + 'index.php'
    stripUrl = baseUrl + 'comic.php?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back')
    help = 'Index format: nnnn'


class Flemcomics(_ParserScraper):
    url = ('https://web.archive.org/web/20180414110349/'
        'http://www.flemcomics.com/')
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '19980101'
    imageSearch = '//img[d:class("ksc")]'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True
    help = 'Index format: yyyymmdd'


class Flipside(_ParserScraper):
    url = 'http://flipside.keenspot.com/comic.php'
    stripUrl = url + '?i=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "comic/")]'
    prevSearch = '//a[@rel="prev"]'
    adult = True
    help = 'Index format: nnnn'


class FonFlatter(_ParserScraper):
    url = 'https://www.fonflatter.de/'
    stripUrl = url + '%s/'
    firstStripUrl = url + '2005/09/20/01-begegnung-mit-batman/'
    lang = 'de'
    imageSearch = r'//img[re:test(@src, "/fred_\d+")]'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy/mm/dd/number-stripname'

    def shouldSkipUrl(self, url, data):
        return url in (
            self.stripUrl % "2006/11/30/adventskalender",
            self.stripUrl % "2006/09/21/danke",
            self.stripUrl % "2006/08/23/zgf-zuweilen-gestellte-fragen",
            self.stripUrl % "2005/10/19/naq-never-asked-questions",
        )


class ForestHill(WordPressScraper):
    url = 'https://www.foresthillcomic.org/'


class ForLackOfABetterComic(_ParserScraper):
    url = 'https://web.archive.org/web/20200224010115/http://forlackofabettercomic.com/'
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@id="comicimg"]'
    prevSearch = '//a[text()="Prev"]'
    help = 'Index format: number'
    endOfLife = True


class FoxDad(_ParserScraper):
    url = 'https://foxdad.com/'
    stripUrl = url + 'post/%s'
    firstStripUrl = stripUrl % '149683014997/some-people-are-just-different-support-the-comic'
    imageSearch = ('//figure[@class="photo-hires-item"]//img', '//figure[@class="tmblr-full"]//img')
    prevSearch = '//a[@class="previous-button"]'

    def namer(self, imageUrl, pageUrl):
        page = self.getPage(pageUrl)
        post = page.xpath('//link[@type="application/json+oembed"]')[0].get('href')
        post = post.replace('https://www.tumblr.com/oembed/1.0?url=https://foxdad.com/post', '')
        post = post.replace('-support-me-on-patreon', '')
        return post.replace('/', '-')


class FoxTails(_ParserScraper):
    stripUrl = 'https://web.archive.org/web/20200920134555/http:/foxtails.magickitsune.com/strips/%s.html'
    url = stripUrl % 'current'
    firstStripUrl = stripUrl % '20041024'
    imageSearch = '//img[contains(@src, "img/2")]'
    prevSearch = '//a[./img[contains(@src, "prev")]]'
    endOfLife = True

    def getPrevUrl(self, url, data):
        # Include pre-reboot archive
        if url == self.stripUrl % '20090906':
            return self.stripUrl % '20090704'
        return super().getPrevUrl(url, data)


class Fragile(_ParserScraper):
    url = ('https://web.archive.org/web/20190308203109/'
        'http://www.fragilestory.com/')
    imageSearch = '//div[@id="comic_strip"]/a[@class="nobg"]/img'
    prevSearch = '//div[@id="nav_comic_a"]/a[2]'
    firstStripUrl = url + 'strips/chapter_01'
    endOfLife = True


class FredoAndPidjin(_ParserScraper):
    url = 'https://www.pidjin.net/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/02/19/goofy-monday'
    imageSearch = '//div[d:class("episode")]//img'
    multipleImagesPerStrip = True
    prevSearch = '//span[d:class("prev")]/a'
    latestSearch = '//section[d:class("latest")]//a'
    starter = indirectStarter
    namer = joinPathPartsNamer((0, 1, 2))


class Freefall(_ParserScraper):
    url = 'http://freefall.purrsia.com/'
    stripUrl = url + 'ff%d/%s%05d.htm'
    firstStripUrl = stripUrl % (100, 'fv', 1)
    imageSearch = '//img[contains(@src, "/ff")]'
    prevSearch = '//a[text()="Previous"]'
    multipleImagesPerStrip = True

    def getIndexStripUrl(self, index):
        # Get comic strip URL from index
        index = int(index)
        chapter = index + 100 - (index % 100)
        color = 'fc' if index > 1252 else 'fv'
        return self.stripUrl % (chapter, color, index)


class FreighterTails(_ParserScraper):
    url = 'http://www.mzzkiti.com/'
    stripUrl = url + 'log%s.htm'
    firstStripUrl = stripUrl % '001'
    imageSearch = ('//img[contains(@src, "Strip")]',
                   '//img[contains(@src, "Caption")]')
    prevSearch = '//a[./img[contains(@src, "prev")]]'
    endOfLife = True


class FriendsYouAreStuckWith(WordPressScraper):
    url = 'http://friendsyasw.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'wanted'

    def namer(self, imageUrl, pageUrl):
        page = self.getPage(pageUrl)
        strip = page.xpath('//div[@id="comic-wrap"]/@class')[0].replace('comic-id-', '')
        return strip + '_' + imageUrl.rstrip('/').rsplit('/', 1)[-1]


class FullFrontalNerdity(_BasicScraper):
    url = 'http://ffn.nodwick.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '6'
    imageSearch = compile(tagre("img", "src", r'(%sffnstrips/\d+-\d+-\d+\.[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: number'


class FunInJammies(WordPressScraper):
    url = ('https://web.archive.org/web/20170205105241/'
        'http://funinjammies.com/')
    stripUrl = url + 'comic.php?issue=%s'
    firstStripUrl = stripUrl % '1'
    prevSearch = '//a[text()="< Prev"]'
    endOfLife = True
    help = 'Index format: n (unpadded)'


class FurPiled(_ParserScraper):
    stripUrl = ('https://web.archive.org/web/20160404074145/'
        'http://www.liondogworks.com/images/fp-%03d.jpg')
    url = stripUrl % 427
    firstStripUrl = stripUrl % 1
    endOfLife = True

    def getPrevUrl(self, url, data):
        # Skip missing pages
        nextStrip = int(url.rsplit('/', 1)[-1].split('.', 1)[0].replace('fp-', '')) - 1
        if nextStrip in [407, 258, 131, 110, 97, 31]:
            nextStrip = nextStrip - 1
        return self.stripUrl % nextStrip

    def fetchUrls(self, url, data, urlSearch):
        # URLs are direct links to images
        return [url]


class FurthiaHigh(_ParserScraper):
    url = 'http://furthiahigh.concessioncomic.com/'
    stripUrl = url + 'index.php?pid=%s'
    firstStripUrl = stripUrl % '20080128'
    imageSearch = '//img[contains(@alt, "Comic")]'
    prevSearch = '//a[./img[@alt="Previous"]]'
    multipleImagesPerStrip = True

# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
import json
from re import compile, escape, IGNORECASE

from ..helpers import indirectStarter
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from ..xml import NS
from .common import ComicControlScraper, WordPressScraper, WordPressWebcomic


class MacHall(_BasicScraper):
    url = 'http://www.machall.com/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2000-11-07'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img[^>]+?src=\'drop_shadow/previous.gif\'>')
    help = 'Index format: yyyy-mm-dd'


class MadamAndEve(_BasicScraper):
    url = 'http://www.madamandeve.co.za/'
    stripUrl = None
    imageSearch = compile(tagre('img', 'src', r'(/cartoons/me\d{6}\.(gif|jpg))'))
    multipleImagesPerStrip = True


class Magellan(WordPressScraper):
    url = 'https://magellanverse.com/'
    firstStripUrl = url + 'comic/20040307wannabe/'


class MagickChicks(ComicControlScraper):
    url = 'https://pixietrixcomix.com/magick-chicks/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'tis-but-a-trifle-2'
    help = 'Index format: name'
    endOfLife = True


class ManlyGuysDoingManlyThings(_ParserScraper):
    url = 'http://thepunchlineismachismo.com/'
    stripUrl = url + 'archives/comic/%s'
    firstStripUrl = stripUrl % '02222010'
    css = True
    imageSearch = "#comic img"
    prevSearch = ".comic-nav-previous"
    help = 'Index format: ddmmyyyy'


class MareInternum(WordPressScraper):
    url = 'https://www.marecomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'intro-page-1'


class Marilith(_BasicScraper):
    url = 'http://www.marilith.com/'
    stripUrl = url + 'archive.php?date=%s'
    firstStripUrl = stripUrl % '20041215'
    imageSearch = compile(r'<img src="(comics/.+?)" border')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class MarriedToTheSea(_ParserScraper):
    url = 'http://marriedtothesea.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '022806'
    imageSearch = '//div[d:class("jumbotron")]//p/img'
    prevSearch = '//a[contains(text(), "Yesterday")]'
    help = 'Index format: mmddyy'

    def namer(self, image_url, page_url):
        unused, date, filename = image_url.rsplit('/', 2)
        return '%s-%s' % (date, filename)


class MarryMe(_ParserScraper):
    url = 'http://marryme.keenspot.com/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20120730'
    imageSearch = '//img[@class="ksc"]'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True


class MaxOveracts(_ParserScraper):
    url = 'http://occasionalcomics.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = '#comic img'
    prevSearch = '.nav-previous > a'
    help = 'Index format: nnn'


class Meek(WordPressScraper):
    url = 'https://www.meekcomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'chapter-1-cover'


class MegaTokyo(_BasicScraper):
    url = 'https://megatokyo.com/'
    stripUrl = url + 'strip/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'"(strips/.+?)"', IGNORECASE)
    prevSearch = compile(r'"(./strip/\d+?)">Prev')
    help = 'Index format: nnnn'


class Meiosis(WordPressScraper):
    url = 'http://meiosiswebcomic.com/'


class Melonpool(WordPressScraper):
    url = 'http://www.melonpool.com/'
    allow_errors = (500,)


class MenageA3(ComicControlScraper):
    adult = True
    url = 'https://pixietrixcomix.com/menage-a-3/'
    firstStripUrl = url + 'for-new-readers'
    endOfLife = True


class Metacarpolis(ComicControlScraper):
    url = 'http://www.metacarpolis.com'


class Misfile(ComicControlScraper):
    url = 'http://www.misfile.com/misfile/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2004-02-22'
    endOfLife = True
    help = 'Index format: yyyy-mm-dd'


class MisfileHellHigh(Misfile):
    name = 'Misfile/HellHigh'
    url = 'http://www.misfile.com/hell-high/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2019-08-29'
    help = 'Index format: yyyy-mm-dd'


class MistyTheMouse(WordPressScraper):
    url = 'http://www.mistythemouse.com/'
    prevSearch = '//a[@rel="prev"]'
    firstStripUrl = 'http://www.mistythemouse.com/?p=12'


class MonkeyUser(_ParserScraper):
    url = 'https://www.monkeyuser.com/'
    prevSearch = '//div[@title="previous"]/a'
    imageSearch = '//div[d:class("content")]/p/img'

    def shouldSkipUrl(self, url, data):
        # videos
        return data.xpath('//div[d:class("video-container")]', namespaces=NS)


class MonsieurLeChien(_BasicScraper):
    url = 'http://www.monsieur-le-chien.fr/'
    stripUrl = url + 'index.php?planche=%s'
    firstStripUrl = stripUrl % '2'
    lang = 'fr'
    imageSearch = compile(tagre("img", "src", r'(i/planches/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') +
                         tagre("img", "src", "i/precedent.gif"))
    help = 'Index format: n'


class MonsterSoup(WordPressScraper):
    url = 'https://monstersoupcomic.com/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'chapter-1-cover'


class Moonlace(WordPressWebcomic):
    url = 'https://moonlace.darkbluecomics.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'page-0-1'
    adult = True

    def starter(self):
        # Set age-gate cookie
        self.session.cookies.set('age_gate', '1', domain='moonlace.darkblueworkshop.com')
        return indirectStarter(self)


class Moonsticks(_ParserScraper):
    url = "http://moonsticks.org/"
    imageSearch = "//div[@class='entry']//img"
    prevSearch = u"//a[text()='\u00AB Prev']"


class MrLovenstein(_BasicScraper):
    url = 'http://www.mrlovenstein.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = (
        # captures rollover comic
        compile(tagre("div", "class", r'comic_image') + r'\s*.*\s*' +
                tagre("div", "style", r'display: none;') + r'\s*.*\s' +
                tagre("img", "src", r'(/images/comics/[^"]+)')),
        # captures standard comic
        compile(tagre("img", "src", r'(/images/comics/[^"]+)',
                      before="comic_main_image")),
    )
    prevSearch = compile(tagre("a", "href", r'([^"]+)') +
                         tagre("img", "src", "/images/nav_left.png"))
    textSearch = compile(r'<meta name="description" content="(.+?)" />')
    help = 'Index Format: n'


class MyCartoons(_BasicScraper):
    url = 'http://mycartoons.de/'
    rurl = escape(url)
    stripUrl = url + 'page/%s'
    imageSearch = (
        compile(tagre("img", "src", r'(%swp-content/cartoons/(?:[^"]+/)?\d+-\d+-\d+[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(%scartoons/[^"]+/\d+-\d+-\d+[^"]+)' % rurl)),
    )
    prevSearch = compile(tagre("a", "href", r'(%spage/[^"]+)' % rurl) +
                         "&laquo;")
    help = 'Index format: number'
    lang = 'de'


class MyLifeWithFel(_ParserScraper):
    baseUrl = 'https://www.mylifewithfel.com/'
    stripUrl = baseUrl + 'api/posts/%s'
    firstStripUrl = stripUrl % '1'
    url = firstStripUrl
    adult = True

    def starter(self):
        # Retrieve comic metadata from API
        data = self.session.get(self.url)
        data.raise_for_status()
        return self.stripUrl % data.json()['last']['id']

    def getPrevUrl(self, url, data):
        return self.stripUrl % json.loads(data.text_content())['previous']['id']

    def fetchUrls(self, url, data, urlSearch):
        return [self.baseUrl + json.loads(data.text_content())['post']['image']]

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 1)[-1]


class MynarskiForest(_ParserScraper):
    stripUrl = 'http://mynarskiforest.purrsia.com/xsl%s.htm'
    url = stripUrl % '09_36'
    firstStripUrl = stripUrl % '97_01'
    imageSearch = '//img[not(contains(@src, "arrow"))]'
    prevSearch = '//a[./img[contains(@src, "arrowbk")]]'
    multipleImagesPerStrip = True
    endOfLife = True


class MysteriesOfTheArcana(_ParserScraper):
    url = 'http://mysteriesofthearcana.com/'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@class="navprevious"]'


class MonsterUnderTheBed(WordPressScraper):
    url = 'http://themonsterunderthebed.net/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'test-post'
    adult = True

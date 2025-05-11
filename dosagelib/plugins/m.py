# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
import json
from re import IGNORECASE, compile

from ..helpers import indirectStarter
from ..scraper import ParserScraper, _BasicScraper, _ParserScraper
from ..util import tagre
from .common import ComicControlScraper, WordPressScraper, WordPressWebcomic


class MacHall(ComicControlScraper):
    url = 'https://www.machall.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'moving-in'


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


class Marilith(ParserScraper):
    url = 'https://web.archive.org/web/20170619193143/http://www.marilith.com/'
    stripUrl = url + 'archive.php?date=%s'
    firstStripUrl = stripUrl % '20041215'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[img[@name="previous_day"]]'
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


class MarryMe(ParserScraper):
    stripUrl = 'http://marryme.keenspot.com/d/%s.html'
    url = stripUrl % '20191001'
    firstStripUrl = stripUrl % '20120730'
    imageSearch = '//img[@class="ksc"]'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True
    help = 'Index format: yyyymmdd'


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


class MistyTheMouse(ParserScraper):
    url = 'http://www.mistythemouse.com/'
    imageSearch = '//center/p/img'
    prevSearch = '//a[img[contains(@src, "Previous")]]'
    firstStripUrl = url + 'The_Live_In.html'


class MonkeyUser(ParserScraper):
    url = 'https://www.monkeyuser.com/'
    imageSearch = '//div[d:class("content")]/p/img'
    prevSearch = '//a[d:class("link-reverse")]'
    latestSearch = '//div[d:class("comic")]/a'
    starter = indirectStarter

    def shouldSkipUrl(self, url, data):
        # videos
        return self.match(data, '//div[d:class("video-container")]')


class MonsieurLeChien(ParserScraper):
    url = ('https://web.archive.org/web/20210311002403/'
        'http:/www.monsieur-le-chien.fr/')
    stripUrl = url + 'index.php?planche=%s'
    firstStripUrl = stripUrl % '2'
    lang = 'fr'
    imageSearch = '//img[contains(@src,"i/planches/")]'
    prevSearch = '//a[img[contains(@src,"i/precedent.gif")]]'
    endOfLife = True
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


class Moonsticks(ParserScraper):
    url = "https://moonsticks.org/"
    imageSearch = "//div[d:class('entry-content')]//img"
    prevSearch = ('//a[@rel="prev"]', "//a[text()='\u00AB Prev']")


class MyLifeWithFel(ParserScraper):
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

    def extract_image_urls(self, url, data):
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

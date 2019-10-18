# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import json
from re import compile, escape, IGNORECASE

from ..helpers import indirectStarter, xpath_class
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPWebcomic


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


class Magellan(_ParserScraper):
    url = 'http://magellanverse.com/'
    css = True
    imageSearch = '#comic-1 > a:first-child img'
    prevSearch = '.nav-previous > a'


class MagickChicks(_BasicScraper):
    url = 'http://www.magickchicks.com/'
    stripUrl = url + 'strips-mc/%s'
    firstStripUrl = stripUrl % 'tis_but_a_trifle'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-mc/[^"]+)',
                               before="cn[id]prevt"))
    help = 'Index format: name'


class ManlyGuysDoingManlyThings(_ParserScraper):
    url = 'http://thepunchlineismachismo.com/'
    stripUrl = url + 'archives/comic/%s'
    firstStripUrl = stripUrl % '02222010'
    css = True
    imageSearch = "#comic img"
    prevSearch = ".comic-nav-previous"
    help = 'Index format: ddmmyyyy'


class MareInternum(_WordPressScraper):
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
    imageSearch = '//div[%s]//p/img' % xpath_class('jumbotron')
    prevSearch = '//a[contains(text(), "Yesterday")]'
    help = 'Index format: mmddyy'

    def namer(self, image_url, page_url):
        unused, date, filename = image_url.rsplit('/', 2)
        return '%s-%s' % (date, filename)


class MaxOveracts(_ParserScraper):
    url = 'http://occasionalcomics.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = '#comic img'
    prevSearch = '.nav-previous > a'
    help = 'Index format: nnn'


class Meek(_WordPressScraper):
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


class Meiosis(_WordPressScraper):
    url = 'http://meiosiswebcomic.com/'


class Melonpool(_WordPressScraper):
    url = 'http://www.melonpool.com/'
    allow_errors = (500,)


class MenageA3(_ComicControlScraper):
    adult = True
    url = 'http://www.ma3comic.com/'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Remove random junk from image names."""
        imgname = imageUrl.split('/')[-1]
        imgbase = imgname.rsplit('-', 1)[1]
        return '%s' % (imgbase)

    help = 'Index format: name'


class Metacarpolis(_ComicControlScraper):
    url = 'http://www.metacarpolis.com'


class Misfile(_ComicControlScraper):
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


class MistyTheMouse(_WordPressScraper):
    url = 'http://www.mistythemouse.com/'
    prevSearch = '//a[@rel="prev"]'
    firstStripUrl = 'http://www.mistythemouse.com/?p=12'


class MonkeyUser(_ParserScraper):
    url = 'https://www.monkeyuser.com/'
    prevSearch = '//div[@title="previous"]/a'
    imageSearch = '//div[@class="content"]/p/img'


class MonsieurLeChien(_BasicScraper):
    url = 'http://www.monsieur-le-chien.fr/'
    stripUrl = url + 'index.php?planche=%s'
    firstStripUrl = stripUrl % '2'
    lang = 'fr'
    imageSearch = compile(tagre("img", "src", r'(i/planches/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') +
                         tagre("img", "src", "i/precedent.gif"))
    help = 'Index format: n'


class Moonlace(_WPWebcomic):
    stripUrl = 'http://dbcomics.darkblueworkshop.com/moonlace/%s/'
    firstStripUrl = stripUrl % 'prologue/page-1'
    url = firstStripUrl
    adult = True

    def starter(self):
        # Set age-gate cookie
        self.session.get(self.firstStripUrl + '?webcomic_birthday=1')
        return indirectStarter(self)

    def namer(self, imageUrl, pageUrl):
        # Prepend chapter title to page filenames
        chapter = pageUrl.rstrip('/').rsplit('/', 3)[-2]
        chapter = chapter.replace('prologue', 'chapter-0-prologue')
        chapter = chapter.replace('chapter-1', 'chapter-1-heritage')
        chapter = chapter.replace('chapter2', 'chapter-2')
        page = imageUrl.rsplit('/', 1)[-1]
        return chapter + '_' + page


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


class MonsterUnderTheBed(_WordPressScraper):
    url = 'http://themonsterunderthebed.net/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'test-post'
    adult = True

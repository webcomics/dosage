# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2018 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, MULTILINE

from ..util import tagre
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import regexNamer, bounceStarter, indirectStarter
from .common import _WordPressScraper, _WPNavi, WP_LATEST_SEARCH


class AbstruseGoose(_BasicScraper):
    url = 'https://abstrusegoose.com/'
    rurl = escape(url)
    starter = bounceStarter
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src',
                                r'(https://abstrusegoose\.com/strips/[^<>"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(%s\d+)' % rurl) +
                         r'(?:&laquo;|«) Previous')
    nextSearch = compile(tagre('a', 'href', r'(%s\d+)' % rurl) +
                         r'(?:Next &raquo;|»)')
    help = 'Index format: n (unpadded)'
    textSearch = compile(tagre("img", "title", r'([^"]+)'))

    def namer(self, image_url, page_url):
        index = int(page_url.rstrip('/').split('/')[-1])
        name = image_url.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)


class AbsurdNotions(_BasicScraper):
    baseUrl = 'http://www.absurdnotions.org/'
    url = baseUrl + 'page129.html'
    stripUrl = baseUrl + 'page%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src', r'(an[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre('a', 'href', r'([^"]+)') +
                         tagre('img', 'src', r'nprev\.gif'))
    help = 'Index format: n (unpadded)'


class AcademyVale(_BasicScraper):
    url = 'http://www.imagerie.com/vale/'
    stripUrl = url + 'avarch.cgi?%s'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(tagre('img', 'src', r'(avale\d{4}-\d{2}\.gif)'))
    prevSearch = compile(tagre('a', 'href', r'(avarch[^">]+)', quote="") +
                         tagre('img', 'src', r'AVNavBack\.gif'))
    help = 'Index format: nnn'


class Achewood(_BasicScraper):
    url = 'http://www.achewood.com/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '00000000'
    imageSearch = compile(tagre("img", "src", r'(/comic\.php\?date=\d+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)',
                               after="Previous"))
    help = 'Index format: mmddyyyy'
    namer = regexNamer(compile(r'date=(\d+)'))


class AfterStrife(_WPNavi):
    baseUrl = 'http://afterstrife.com/'
    stripUrl = baseUrl + '?p=%s'
    url = stripUrl % '262'
    firstStripUrl = stripUrl % '1'
    help = 'Index format: nnn'
    endOfLife = True


class AGirlAndHerFed(_BasicScraper):
    url = 'http://www.agirlandherfed.com/'
    stripUrl = url + '1.%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(img/strip/[^"]+\.jpg)'))
    prevSearch = compile(r'<a href="([^"]+)">[^>]+Back')
    help = 'Index format: nnn'


class AhoiPolloi(_ParserScraper):
    url = 'https://ahoipolloi.blogger.de/'
    stripUrl = url + '?day=%s'
    firstStripUrl = stripUrl % '20060306'
    multipleImagesPerStrip = True
    lang = 'de'
    imageSearch = '//img[contains(@src, "/static/antville/ahoipolloi/")]'
    prevSearch = '//a[contains(@href, "/?day=")]'
    help = 'Index format: yyyymmdd'


class AhoyEarth(_WPNavi):
    url = 'http://www.ahoyearth.com/'


class AirForceBlues(_WordPressScraper):
    url = 'http://farvatoons.com/'
    firstStripUrl = url + 'comic/in-texas-there-are-texans/'


class ALessonIsLearned(_BasicScraper):
    url = 'http://www.alessonislearned.com/'
    prevSearch = compile(tagre("a", "href", r"(index\.php\?comic=\d+)",
                               quote="'") + r"[^>]+previous")
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(cmx/lesson\d+\.[a-z]+)"))
    help = 'Index format: nnn'


class Alice(_WordPressScraper):
    url = 'http://www.alicecomics.com/'
    latestSearch = '//a[text()="Latest Alice!"]'
    starter = indirectStarter


class AlienLovesPredator(_BasicScraper):
    url = 'http://alienlovespredator.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2004/10/12/unavoidable-delay'
    imageSearch = compile(tagre("img", "src", r'([^"]+)',
                                after='border="1" alt="" width="750"'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class AlienShores(_WordPressScraper):
    url = 'http://alienshores.com/alienshores_band/'
    firstStripUrl = url + 'AScomic/updated-cover/'


class AllTheGrowingThings(_BasicScraper):
    url = 'http://growingthings.typodmary.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/04/21/all-the-growing-things'
    imageSearch = compile(tagre("img", "src", r'(%sfiles/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name'


class AlphaLuna(_BasicScraper):
    url = 'http://www.alphaluna.net/'
    stripUrl = url + 'issue-%s/'
    firstStripUrl = stripUrl % '1/cover'
    imageSearch = compile(tagre("a", "href",
                                r'[^"]*/(?:issue-|support/upcoming)[^"]+') +
                          tagre("img", "src", r'([^"]*/PAGINAS/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') +
                         tagre("img", "alt", "Prev"))
    help = 'Index format: issue/page (e.g. 4/05)'


class AlphaLunaSpanish(AlphaLuna):
    name = 'AlphaLuna/Spanish'
    lang = 'es'
    url = 'http://alphaluna.net/spanish/'
    stripUrl = url + 'issue-%s/'
    firstStripUrl = stripUrl % '1/portada'


class Altermeta(_BasicScraper):
    url = 'http://altermeta.net/'
    rurl = escape(url)
    stripUrl = url + 'archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'<img src="(comics/[^"]+)" />')
    prevSearch = compile(r'<a href="([^"]+)"><img src="%stemplate/default/images/sasha/back\.png' % rurl)
    help = 'Index format: n (unpadded)'


class AltermetaOld(Altermeta):
    url = Altermeta.url + 'oldarchive/index.php'
    stripUrl = Altermeta.url + 'oldarchive/archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    prevSearch = compile(r'<a href="([^"]+)">Back')


class AmazingSuperPowers(_BasicScraper):
    url = 'http://www.amazingsuperpowers.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/09/heredity'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/name'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            # video
            self.stripUrl % '2013/05/orbital-deathray-kickstarter',
        )


class Amya(_WordPressScraper):
    url = 'http://www.amyachronicles.com/'


class Angband(_BasicScraper):
    url = 'http://angband.calamarain.net/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2005-12-30'
    imageSearch = compile(tagre("img", "src", r'(comics/Scroll[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date\=[^"]+)') +
                         "Previous")
    help = 'Index format: yyyy-mm-dd'


class Angels2200(_BasicScraper):
    url = 'http://www.janahoffmann.com/angels/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.janahoffmann\.com/angels/comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "&laquo; Previous")
    help = 'Index format: yyyy/mm/dd/part-<n>-comic-<n>'


class Annyseed(_ParserScraper):
    baseUrl = 'http://www.mirrorwoodcomics.com/'
    url = baseUrl + 'AnnyseedLatest.htm'
    stripUrl = baseUrl + 'Annyseed%s.htm'
    imageSearch = '//div/img[contains(@src, "Annyseed")]'
    prevSearch = '//a[img[@name="Previousbtn"]]'
    help = 'Index format: nnn'
    FIX_RE = compile(r'Annyseed/Finished%20For%20Print/')

    def imageUrlModifier(self, image_url, data):
        return self.FIX_RE.sub('', image_url)

    def link_modifier(self, fromurl, tourl):
        """Fix circular link."""
        if 'Annyseed150' in fromurl and 'Annyseed150' in tourl:
            return self.stripUrl % '149'
        return tourl


class AppleGeeks(_BasicScraper):
    url = 'http://www.applegeeks.com/'
    stripUrl = url + 'comics/viewcomic.php?issue=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'((?:/comics/)?issue\d+\.jpg)'))
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    allow_errors = (404,)
    help = 'Index format: n (unpadded)'


class ARedTailsDream(_BasicScraper):
    baseUrl = 'http://www.minnasundberg.fi/'
    stripUrl = baseUrl + 'comic/page%s.php'
    firstStripUrl = stripUrl % '00'
    url = baseUrl + 'comic/recent.php'
    imageSearch = compile(tagre('img', 'src', r'(chapter.+?/eng[^"]*)'))
    prevSearch = compile(tagre('a', 'href', r'(page\d+\.php)') +
                         tagre("img", "src", r'.*?aprev.*?'))
    help = 'Index format: nn'


class Ashes(_WordPressScraper):
    url = 'http://www.flowerlarkstudios.com/comicpage/prologue/10232009/'
    firstStripUrl = url
    latestSearch = WP_LATEST_SEARCH
    starter = indirectStarter


class AstronomyPOTD(_ParserScraper):
    baseUrl = 'http://apod.nasa.gov/apod/'
    url = baseUrl + 'astropix.html'
    starter = bounceStarter
    stripUrl = baseUrl + 'ap%s.html'
    firstStripUrl = stripUrl % '061012'
    imageSearch = '//a/img'
    multipleImagesPerStrip = True
    prevSearch = '//a[text()="<"]'
    nextSearch = '//a[text()=">"]'
    help = 'Index format: yymmdd'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return data.xpath('//iframe')  # videos

    def namer(self, image_url, page_url):
        return '%s-%s' % (page_url.split('/')[-1].split('.')[0][2:],
                          image_url.split('/')[-1].split('.')[0])


class AxeCop(_WordPressScraper):
    url = 'http://axecop.com/comic/season-two/'

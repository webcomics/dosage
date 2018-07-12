# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2018 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, IGNORECASE, sub
from os.path import splitext
import datetime

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, bounceStarter, xpath_class
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNavi, WP_LATEST_SEARCH


class SabrinaOnline(_BasicScraper):
    url = 'http://sabrina-online.com/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '1996-01'
    imageSearch = compile(tagre("img", "src", r'(pages/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r"(\d\d\d\d-\d\d.html)") +
                         tagre("img", "src", "b_back.gif"))
    help = 'Index format: yyyy-qq'
    adult = True
    multipleImagesPerStrip = True

    def starter(self):
        """Pick last one in a list of archive pages."""
        archive = self.url + 'archive.html'
        data = self.getPage(archive)
        search = compile(tagre("a", "href", r"(\d\d\d\d-\d\d.html)"))
        archivepages = self.fetchUrls(archive, data, search)
        return archivepages[-1]

class SafelyEndangered(_WPNavi):
    url = 'http://www.safelyendangered.com/'
    firstStripUrl = url + 'comic/ignored/'


class SailorsunOrg(_WordPressScraper):
    url = 'http://sailorsun.org/'


class SamAndFuzzy(_ParserScraper):
    url = 'http://www.samandfuzzy.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@class="comic-image"]'
    prevSearch = '//li[@class="prev-page"]/a'
    help = 'Index format: n (unpadded)'


class SandraOnTheRocks(_BasicScraper):
    url = 'http://www.sandraontherocks.com/'
    stripUrl = url + 'strips-sotr/%s'
    firstStripUrl = stripUrl % 'start_by_running'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-sotr/[^"]+)', before="cn[id]prev"))
    help = 'Index format: name'


class ScandinaviaAndTheWorld(_ParserScraper):
    url = 'https://satwcomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'sweden-denmark-and-norway'
    starter = indirectStarter
    imageSearch = '//img[@itemprop="image"]'
    prevSearch = '//a[@accesskey="p"]'
    latestSearch = '//a[text()="View latest comic"]'
    textSearch = '//span[@itemprop="articleBody"]'
    help = 'Index format: stripname'


class ScaryGoRound(_ParserScraper):
    url = 'http://www.scarygoround.com/sgr/ar.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20020604'
    imageSearch = '//img[contains(@src, "/strips/")]'
    prevSearch = '//a[contains(text(), "Previous")]'
    endOfLife = True
    help = 'Index format: yyyymmdd'


class ScenesFromAMultiverse(_BasicScraper):
    url = 'http://amultiverse.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2010/06/14/parenthood'
    imageSearch = (
        compile(tagre("div", "id", "comic") + r"\s*" +
            tagre("img", "src",
                r'(.*amultiverse.com/wp-content/uploads/\d+/\d+/[^"]+)')),
        compile(tagre("div", "id", "comic") + r"\s*" +
            tagre("a", "href", r'[^"]*') +
            tagre("img", "src",
                r'(.*amultiverse.com/wp-content/uploads/\d+/\d+/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(%scomic/\d+\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class SchlockMercenary(_ParserScraper):
    url = 'http://www.schlockmercenary.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2000-06-12'
    imageSearch = '//div[@class="strip-image-wrapper"]/img'
    multipleImagesPerStrip = True
    prevSearch = '//a[@class="previous-strip"]'
    help = 'Index format: yyyy-mm-dd'


class SchoolBites(_BasicScraper):
    url = 'http://schoolbites.net/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.schoolbites\.net/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://schoolbites\.net/d/\d+\.html)', after="prev"))
    help = 'Index format: yyyymmdd'


class Schuelert(_BasicScraper):
    url = 'http://www.schuelert.de/'
    rurl = escape(url)
    stripUrl = url + 'index.php?paged=%s'
    firstStripUrl = stripUrl % '5'
    imageSearch = compile(tagre("img", "src", r"(%swp-content/[^']+)" % rurl, quote="'"))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php\?paged=\d+)' % rurl) + "&laquo;")
    multipleImagesPerStrip = True
    help = 'Index format: none'
    lang = 'de'


class Science(_BasicScraper):
    url = 'http://sci-ence.org/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'periodic-table-element-ass'
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+/)' % rurl, after="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    help = 'Index format: stripname'


class SequentialArt(_BasicScraper):
    url = 'http://www.collectedcurios.com/sequentialart.php'
    stripUrl = url + '?s=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'([^"]+)', before="strip"))
    prevSearch = compile(tagre("a", "href", r'(/sequentialart\.php\?s=\d+)') +
                         tagre("img", "src", "Nav_BackOne\.gif"))
    help = 'Index format: name'


class SexyLosers(_ParserScraper):
    adult = True
    url = 'https://www.sexylosers.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '003'
    imageSearch = '//div[@class="entry-content"]//img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@rel="bookmark"]'
    help = 'Index format: nnn'
    starter = indirectStarter

    def namer(self, image_url, page_url):
        index = page_url.rsplit('/', 2)[1]
        title = image_url.rsplit('/', 1)[1]
        return index + '-' + title


class Sharksplode(_WordPressScraper):
    url = 'http://sharksplode.com/'
    textSearch = '//div[@id="comic"]//img/@alt'
    allow_errors = (403,)


class Sheldon(_BasicScraper):
    url = 'http://www.sheldoncomics.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s.html'
    firstStripUrl = stripUrl % '011130'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.sheldoncomics\.com/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/\d+\.html)' % rurl,
                               after="sidenav-prev"))
    help = 'Index format: yymmdd'


class ShermansLagoon(_BasicScraper):
    url = 'http://shermanslagoon.com/'
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % '/december-29-2003/'
    imageSearch = compile(tagre("img", "src", r'(https://safr\.kingfeatures\.com/idn/cnfeed/zone/js/content\.php\?file=.+?)'))
    prevSearch = compile(r'id="previouscomic" class="button white"><a href="(%scomics/[a-z0-9-]+/)"' % url)
    help = 'Index format: monthname-day-year'

    def namer(self, image_url, page_url):
        name = page_url.rsplit('/', 3)[2]
        if name == "shermanslagoon.com":
            name = datetime.date.today().strftime("%B-%d-%Y").lower()
        # name is monthname-day-year
        month, day, year = name.split('-')
        return "%s-%s-%s" % (year, month, day)


class ShipInABottle(_WPNavi):
    url = 'http://shipinbottle.pepsaga.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '281'
    adult = True
    help = 'Index format: number'


class Shivae(_WordPressScraper):
    url = 'http://shivae.com/'
    firstStripUrl = url + 'gnip/ck-chapter-01/caidenkoel-title-01/'


class Shortpacked(_ParserScraper):
    url = 'http://www.shortpacked.com/index.php'
    stripUrl = url + '?id=%s'
    css = True
    imageSearch = 'img#comic'
    prevSearch = 'a.prev'
    help = 'Index format: nnn'


class ShotgunShuffle(_WordPressScraper):
    url = 'http://shotgunshuffle.com/'
    firstStripUrl = url + 'comic/pilot/'


class SinFest(_BasicScraper):
    url = 'http://www.sinfest.net/'
    stripUrl = url + 'view.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(btphp/comics/.+)',
                                after="alt"))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date=.+)') + '\\s*' +
                         tagre("img", "src", r'\.\./images/prev\.gif'))
    help = 'Index format: yyyy-mm-dd'


class Sithrah(_ParserScraper):
    url = 'http://sithrah.com/'
    imageSearch = '//div[@class="webcomic-image"]/img'
    prevSearch = '//a[%s]' % xpath_class('previous-webcomic-link')


class SkinDeep(_ParserScraper):
    url = 'http://www.skindeepcomic.com/'
    imageSearch = '//a[%s]/img' % xpath_class('webcomic-link')
    prevSearch = '//a[%s]' % xpath_class('previous-webcomic-link')


class SleeplessDomain(_ComicControlScraper):
    url = 'http://www.sleeplessdomain.com/'


class SlightlyDamned(_ComicControlScraper):
    url = 'http://www.sdamned.com/'
    firstStripUrl = url + 'comic/part-one-to-hell-and-back'


class SluggyFreelance(_ParserScraper):
    url = 'http://sluggy.com/'
    stripUrl = 'http://archives.sluggy.com/book.php?chapter=%s'
    imageSearch = '//div[%s]/img/@data-src' % xpath_class('comic_content')
    prevSearch = '//div[%s]/a' % xpath_class('previous')
    latestSearch = '//a[%s]' % xpath_class('archives_link')
    starter = indirectStarter
    multipleImagesPerStrip = True
    help = 'Index format: chapter'

    def namer(self, imageurl, pageurl):
        """Remove random noise from name."""
        fn = imageurl.rsplit('/', 1)[-1]
        return sub(r'\.(png|gif|jpg).*\.\1', '', fn)


class SMBC(_ComicControlScraper):
    url = 'http://www.smbc-comics.com/'
    firstStripUrl = url + 'comic/2002-09-05'
    multipleImagesPerStrip = True
    imageSearch = ['//img[@id="cc-comic"]', '//div[@id="aftercomic"]/img']
    prevSearch = '//a[@class="prev"]'
    help = 'Index format: nnnn'
    textSearch = '//img[@id="cc-comic"]/@title'

    def namer(self, image_url, page_url):
        """Remove random noise from name."""
        return image_url.rsplit('-', 1)[-1]


class SnowFlame(_WordPressScraper):
    url = 'http://www.snowflamecomic.com/'
    stripUrl = url + '?comic=snowflame-%s-%s'
    firstStripUrl = stripUrl % ('01', '01')
    starter = bounceStarter
    nextSearch = WP_LATEST_SEARCH
    help = 'Index format: chapter-page'

    def getIndexStripUrl(self, index):
        return self.stripUrl % tuple(index.split('-'))

    def namer(self, image_url, page_url):
        prefix, filename = image_url.rsplit('/', 1)
        ro = compile(r'snowflame-([^-]+)-([^-]+)')
        mo = ro.search(page_url)
        chapter = mo.group(1)
        page = mo.group(2)
        return "%s-%s-%s" % (chapter, page, filename)


class SodiumEyes(_WordPressScraper):
    url = 'http://sodiumeyes.com/'


class SomethingPositive(_BasicScraper):
    url = 'http://www.somethingpositive.net/'
    stripUrl = url + 'sp%s.shtml'
    imageSearch = (
        compile(tagre("img", "src", r'(sp\d+\.png)')),
        compile(tagre("img", "src", r'(twither\.gif)')),
    )
    prevSearch = compile(tagre("a", "href", r'(sp\d+\.shtml)') + "(?:" +
                         tagre("img", "src", r'images/previous\.gif') +
                         "|Previous)")
    help = 'Index format: mmddyyyy'


class Sorcery101(_ParserScraper):
    baseUrl = 'http://www.sorcery101.net/sorcery-101/'
    stripUrl = baseUrl + '%s/'
    url = stripUrl % 'sorcery101-ch-01'
    firstStripUrl = url
    imageSearch = '//div[@class="webcomic-image"]/img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[%s]' % xpath_class('last-webcomic-link')
    starter = indirectStarter
    allow_errors = (500,)
    help = 'Index format: stripname'


class SpaceJunkArlia(_ParserScraper):
    url = 'http://spacejunkarlia.com/'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//div[%s]/img' % xpath_class('content')
    prevSearch = '//a[text()="<"]'
    help = 'Index format: number'


class SpaceTrawler(_ParserScraper):
    url = 'https://www.baldwinpage.com/spacetrawler/'
    firstStripUrl = url + '2010/01/01/spacetrawler-4/'
    imageSearch = '//img[%s]' % xpath_class('size-full')
    prevSearch = '//a[@rel="prev"]'


class Spamusement(_BasicScraper):
    url = 'http://spamusement.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php/comics/view/%s'
    imageSearch = compile(r'<img src="(%sgfx/\d+\..+?)"' % rurl, IGNORECASE)
    prevSearch = compile(r'<a href="(%sindex.php/comics/view/.+?)">' % rurl,
                         IGNORECASE)
    latestSearch = prevSearch
    help = 'Index format: n (unpadded)'
    starter = indirectStarter


class SpareParts(_BasicScraper):
    baseUrl = 'http://www.sparepartscomics.com/'
    url = baseUrl + 'comics/?date=20080328'
    stripUrl = baseUrl + 'comics/index.php?date=%s'
    firstStripUrl = stripUrl % '20031022'
    imageSearch = compile(tagre("img", "src", r'(http://www\.sparepartscomics\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)',
                               quote="'") + "Previous Comic")
    help = 'Index format: yyyymmdd'


class Spinnerette(_ComicControlScraper):
    url = 'http://www.spinnyverse.com'


class SPQRBlues(_WordPressScraper):
    url = 'http://spqrblues.com/IV/'


class StandStillStaySilent(_ParserScraper):
    url = 'http://www.sssscomic.com/comic.php'
    stripUrl = url + '?page=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@class="comicnormal"]'
    prevSearch = '//a[div[@id="navprev"]]'
    help = 'Index Format: number'


class StarCrossdDestiny(_ParserScraper):
    baseUrl = 'http://starcrossd.net/'
    url = baseUrl + 'comic.html'
    stripUrl = baseUrl + 'archives/%s.html'
    firstStripUrl = stripUrl % '00000001'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[text()="prev"]'
    help = 'Index format: nnnnnnnn'

    def namer(self, image_url, page_url):
        if image_url.find('ch1') == -1:
            # At first all images were stored in a strips/ directory but
            # that was changed with the introduction of book2
            image_url = sub('(?:strips)|(?:images)', 'book1', image_url)
        elif not image_url.find('strips') == -1:
            image_url = image_url.replace('strips/', '')
        directory, filename = image_url.split('/')[-2:]
        filename, extension = splitext(filename)
        return directory + '-' + filename


class StationV3(_ParserScraper):
    url = 'http://www.stationv3.com/'
    stripUrl = url + 'd3/%s.html'
    firstStripUrl = stripUrl % '20170101'
    imageSearch = '//img[contains(@src,"/comics3/")]'
    prevSearch = '//a[img[contains(@src,"/previous2")]]'
    help = 'Index format: yyyymmdd'


class StickyDillyBuns(_BasicScraper):
    url = 'http://www.stickydillybuns.com/'
    stripUrl = url + 'strips-sdb/%s'
    firstStripUrl = stripUrl % 'awesome_leading_man'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-sdb/[^"]+)',
                               before="cn[id]prev"))
    help = 'Index format: name'


class StreetFighter(_ComicControlScraper):
    url = 'http://www.streetfightercomics.com'


class StringTheory(_WPNavi):
    url = 'http://www.stringtheorycomic.com/'
    firstStripUrl = url + 'comics/chapterone/chapterone/'


class StrongFemaleProtagonist(_ParserScraper):
    url = 'http://strongfemaleprotagonist.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = 'article p img'
    prevSearch = 'a.page-nav__item--left'
    help = 'Index format: issue-?/page-??'

    def shouldSkipUrl(self, url, data):
        """Skip hiatus & non-comic pages."""
        return url in (
            self.stripUrl % 'guest-art/tuesday',
            self.stripUrl % 'guest-art/friday',
            self.stripUrl % 'guest-art/wednesday',
            self.stripUrl % 'issue-5/newspaper',
            self.stripUrl % 'issue-5/hiatus-1',
            self.stripUrl % 'issue-5/hiatus-2',
            self.stripUrl % 'issue-1/no-page',
        )


class StuffNoOneToldMe(_BasicScraper):
    url = 'http://www.snotm.com/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '2010/05/01'
    olderHref = r"(http://www\.snotm\.com/\d+/\d+/[^']+\.html)"
    starter = indirectStarter
    imageSearch = (
        compile(tagre("img", "src", r'(http://i\.imgur\.com/[^"]+)') +
                r"(?:</a>|<br />)"),
        compile(tagre("img", "src", r'(http://\d+\.bp\.blogspot\.com/[^"]+)') +
                r"(?:(?:&nbsp;)?</a>|<span |<br />)"),
        compile(tagre("img", "src", r'(https://lh\d+\.googleusercontent\.com/[^"]+)') + r"</a>"),
    )
    prevSearch = compile(tagre("a", "href", olderHref, quote="'",
                               before="older-link"))
    latestSearch = compile(tagre("a", "href", olderHref, quote="'"))
    multipleImagesPerStrip = True
    help = 'Index format: yyyy/mm/stripname'

    def namer(self, image_url, page_url):
        """Use page URL to construct meaningful image name."""
        parts, year, month, stripname = page_url.rsplit('/', 3)
        stripname = stripname.rsplit('.', 1)[0]
        parts, imagename = image_url.rsplit('/', 1)
        return '%s-%s-%s-%s' % (year, month, stripname, imagename)

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            self.stripUrl % '2016/05/so-you-would-like-to-share-my-comics',  # no comic
            self.stripUrl % '2012/08/self-rant',  # no comic
            self.stripUrl % '2012/06/if-you-wonder-where-ive-been',  # video
            self.stripUrl % '2011/10/i-didnt-make-this-nor-have-anything-to',  # video
            self.stripUrl % '2010/12/first-snotm-fans-in-sao-paulo',  # no comic
            self.stripUrl % '2010/11/ear-infection',  # no comic
        )


class SupernormalStep(_ComicControlScraper):
    url = 'http://supernormalstep.com/'


class SurvivingTheWorld(_ParserScraper):
    url = 'http://survivingtheworld.net/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % 'Lesson1'
    imageSearch = (
        '//div[@class="img"]/img',      # When there's one image per strip
        '//div[@class="img"]/p/img',    # When there's multiple images per strip
        '//td/img'                      # Special case for Lesson1296.html
    )
    prevSearch = (
        '//li[@class="previous"]/a',
        '//td/a'                        # Special case for Lesson1296.html
    )
    multipleImagesPerStrip = True
    help = 'Index format: name'

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, xpath_class
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNavi, _WPWebcomic


class Namesake(_ComicControlScraper):
    url = 'http://namesakecomic.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'the-journey-begins'


class NatalieDee(_BasicScraper):
    url = 'http://www.nataliedee.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '022806'
    imageSearch = compile(tagre("img", "src", r'(%s\d+/[^"]+)' % rurl,
                                before="overflow"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "&lt;&lt; Yesterday")
    help = 'Index format: mmddyy'

    def namer(self, image_url, page_url):
        unused, date, filename = image_url.rsplit('/', 2)
        return '%s-%s' % (date, filename)


class Nedroid(_WordPressScraper):
    url = 'http://nedroid.com/'
    prevSearch = '//a[@rel="prev"]'


class NeoCTC(_ParserScraper):
    url = 'http://www.hirezfox.com/neoctc/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20071205'
    imageSearch = '//img[contains(@src, "neoctc/comics")]'
    prevSearch = '//a[./img[@alt="Previous Day"]]'
    multipleImagesPerStrip = True


class NeoEarth(_BasicScraper):
    url = 'http://www.neo-earth.com/NE/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '2007-03-23'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'


class NerfNow(_WordPressScraper):
    url = 'https://www.nerfnow.com/'
    prevSearch = '//li[@id="nav_previous"]/a'


class Newshounds(_ParserScraper):
    stripUrl = 'http://www.newshounds.com/%s.html'
    url = stripUrl % 'nh2/20140929'
    firstStripUrl = stripUrl % 'nh1/19971101'
    imageSearch = '//img[@class="ksc"]'
    prevSearch = '//a[./img[@alt="Previous comic"]]'
    endOfLife = True

    def getPrevUrl(self, url, data):
        # Add navigation link between comic and graphic novel
        if url == self.stripUrl % 'nh2/20070201':
            return self.stripUrl % 'nh1/20061208'
        return super(Newshounds, self).getPrevUrl(url, data)


class NewWorld(_WordPressScraper):
    url = ('https://web.archive.org/web/20190718012133/'
        'http://www.tfsnewworld.com/')
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/08/30/63'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True
    help = 'Index format: yyyy/mm/dd/stripn'


class NichtLustig(_BasicScraper):
    url = 'http://www.nichtlustig.de/main.html'
    stripUrl = 'http://static.nichtlustig.de/toondb/%s.html'
    lang = 'de'
    imageSearch = compile(r'background-image:url\((http://static\.nichtlustig\.de/comics/full/\d+\.jpg)')
    prevSearch = compile(tagre("a", "href", r'(http://static\.nichtlustig\.de/toondb/\d+\.html)'))
    latestSearch = compile(tagre("a", "href", r'([^"]*toondb/\d+\.html)'))
    help = 'Index format: yymmdd'
    starter = indirectStarter


class Nicky510(_WPNavi):
    url = ('https://web.archive.org/web/20160510215718/'
        'http://www.nickyitis.com/')
    endOfLife = True


class Nightshift(_ParserScraper):
    url = 'http://www.poecatcomix.com/comics/nightshift/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'nightshift-volume1/ns-chapter-1'
    imageSearch = '//div[@id="gallery-1"]//img'
    prevSearch = ('//a[./span[text()="PAST CHAPTER"]]',
                  '//a[./span[text()="LAST CHAPTER"]]')
    latestSearch = '//a[./img[contains(@src, "Latest-Page")]]'
    starter = indirectStarter
    multipleImagesPerStrip = True
    adult = True

    def namer(self, imageUrl, pageUrl):
        # Prepend chapter title to page filenames
        chapter = pageUrl.rstrip('/').rsplit('/', 1)[-1].replace('ns-', 'ns1-')
        page = imageUrl.rsplit('/', 1)[-1]
        return chapter + '_' + page


class Nimona(_ParserScraper):
    url = ('https://web.archive.org/web/20141008095502/'
        'http://gingerhaze.com/nimona/')
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % "page-1"
    imageSearch = '//div[{}]//img'.format(xpath_class('field-name-field-comic-page'))
    prevSearch = '//a[img[contains(@src, "/comicdrop_prev_label")]]'
    endOfLife = True


class NineToNine(_ParserScraper):
    url = 'https://www.tigerknight.com/99'
    stripUrl = url + '/%s'
    firstStripUrl = stripUrl % '2014-01-01'
    imageSearch = '//img[@class="comic-image"]'
    prevSearch = '//a[@class="prev"]'
    multipleImagesPerStrip = True


class NobodyScores(_BasicScraper):
    url = 'http://nobodyscores.loosenutstudio.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '4'
    imageSearch = compile(tagre("img", "src", r'(%scomix/[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(r'<a href="(%sindex.php.+?)">the one before </a>' % rurl)
    help = 'Index format: nnn'


class NoMoreSavePoints(_WordPressScraper):
    url = 'http://www.flowerlarkstudios.com/comicpage/no-more-save-points/mushroom-hopping/'
    firstStripUrl = url
    starter = indirectStarter


class NoNeedForBushido(_ParserScraper):
    url = 'http://nn4b.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = '//div[@id="comic-image"]//img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: nnn'


class NonPlayerCharacter(_ParserScraper):
    url = 'https://www.lfg.co/'
    stripUrl = url + 'npc/tale/%s/'
    firstStripUrl = stripUrl % '1-1'
    imageSearch = '//div[@id="comic-img"]//img'
    prevSearch = '//a[@class="comic-nav-prev"]'
    latestSearch = '//div[@id="feature-npc-footer"]/a[contains(@href, "npc/tale/")]'
    starter = indirectStarter

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rstrip('/').rsplit('/', 1)[-1]


class NotAVillain(_WPWebcomic):
    url = 'http://navcomic.com/'
    stripUrl = url + 'not-a-villain/%s/'
    firstStripUrl = stripUrl % 'v1-001'

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[-1]
        # Fix filenames missing "Page"
        if filename[2].isdigit():
            filename = filename[0] + '-Page' + filename[2:]
        # Fix filenames of early comics
        filename = filename.replace('Page-', '1-Page')
        if filename.startswith('0-Page'):
            filename = '1' + filename[1:]
        return filename


class NotInventedHere(_ParserScraper):
    url = 'http://notinventedhe.re/'
    stripUrl = url + 'on/%s'
    firstStripUrl = stripUrl % '2009-9-21'
    imageSearch = '//div[@id="comic-content"]//img'
    prevSearch = '//a[@id="nav-previous"]'
    help = 'Index format: yyyy-m-d'


class Nukees(_BasicScraper):
    url = 'http://www.nukees.com/'
    stripUrl = url + 'd/%s'
    firstStripUrl = stripUrl % '19970121'
    imageSearch = compile(r'"comic".+?"(/comics/.+?)"')
    prevSearch = compile(r'"(/d/.+?)".+?previous')
    help = 'Index format: yyyymmdd.html'

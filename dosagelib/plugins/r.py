# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile
from six.moves.urllib.parse import urljoin

from ..helpers import bounceStarter, xpath_class
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import _WordPressScraper, _WPWebcomic


class RalfTheDestroyer(_WordPressScraper):
    url = 'http://ralfthedestroyer.com/'


class RaynaOnTheRiver(_WordPressScraper):
    url = 'http://www.catomix.com/rayna/'
    firstStripUrl = url + 'archives/comic/teaser-poster'


class RealLife(_WordPressScraper):
    url = 'https://reallifecomics.com/'
    stripUrl = url + 'comic.php?comic=%s'
    firstStripUrl = stripUrl % 'title-1'
    help = 'Index format: monthname-dd-yyyy'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsisntent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        if pageUrl.rsplit('=', 1)[-1] == 'may-27-2014':
            filename = filename.replace('20140219_3121', '20140527')
        filename = filename.replace('5-Finished', '20140623_3161')
        filename = filename.replace('520140722', '20140722')
        filename = filename.replace('520140724', '20140724')
        return filename

    def getPrevUrl(self, url, data):
        # "Parse" JavaScript
        prevtag = data.find_class('comic-nav-previous')
        if not prevtag:
            return None
        target = prevtag[0].get('onclick').split("'")[1]
        return urljoin(url, target)


class RealmOfAtland(_BasicScraper):
    url = 'http://www.realmofatland.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '1'
    prevSearch = compile(tagre("a", "href", r'(\?p=\d+)', after="cg_back"))
    imageSearch = compile(tagre("img", "src", r'(images/strips/atland\d+.[^"]+)'))
    help = 'Index format: nnn'


class RedMeat(_ParserScraper):
    url = 'http://www.redmeat.com/max-cannon/FreshMeat'
    imageSearch = '//div[@class="comicStrip"]//img'
    prevSearch = '//a[@class="prev"]'

    def namer(self, image_url, page_url):
        parts = image_url.rsplit('/', 2)
        return '_'.join(parts[1:3])


class Replay(_ParserScraper):
    url = 'http://replaycomic.com/'
    stripUrl = url + 'comic/%s/'
    url = stripUrl % 'trying-it-out'
    firstStripUrl = stripUrl % 'red-desert'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[contains(@class, "comic-nav-previous")]'
    nextSearch = '//a[contains(@class, "comic-nav-next")]'

    def starter(self):
        # Retrieve archive page to identify chapters
        archivePage = self.getPage(self.url + 'archive')
        archive = archivePage.xpath('//div[@class="comic-archive-chapter-wrap"]')
        self.chapter = len(archive) - 1
        self.startOfChapter = []
        for archiveChapter in archive:
            self.startOfChapter.append(archiveChapter.xpath('.//a')[0].get('href'))
        return bounceStarter(self)

    def namer(self, imageUrl, pageUrl):
        # Name pages based on chapter, index, and post title
        name = pageUrl.rstrip('/').rsplit('/', 1)[-1]
        page = imageUrl.rsplit('/', 1)[-1].rsplit('.', 1)

        # Fix inconsistent page number formatting
        if page[0].isdigit() and len(page[0]) > 2 and self.chapter == 1 and name != 'through-the-woods':
            page[0] = page[0][:2] + '-' + page[0][2:]

        name = '%d-%s-%s.%s' % (self.chapter, page[0], name, page[1])
        if pageUrl in self.startOfChapter:
            self.chapter -= 1
        return name


class RiversideExtras(_WPWebcomic):
    url = 'https://riversidecomics.com/'


class RomanticallyApocalyptic(_ParserScraper):
    url = 'http://romanticallyapocalyptic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//div[%s]/center//img' % xpath_class('comicpanel')
    prevSearch = '//a[@accesskey="p"]'
    help = 'Index format: n'
    adult = True


class Roza(_ParserScraper):
    url = 'http://www.junglestudio.com/roza/index.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2007-05-01'
    imageSearch = '//img[contains(@src, "pages/")]'
    prevSearch = '//a[img[contains(@src, "navtable_01.gif")]]'
    help = 'Index format: yyyy-mm-dd'


class Ruthe(_BasicScraper):
    url = 'http://ruthe.de/'
    stripUrl = url + 'cartoon/%s/datum/asc/'
    firstStripUrl = stripUrl % '1'
    lang = 'de'
    imageSearch = compile(tagre("img", "src", r'(/?cartoons/strip_\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/cartoon/\d+/datum/asc/)') +
                         'vorheriger')
    help = 'Index format: number'


class Ryugou(_WPWebcomic):
    url = 'http://ryugou.swashbuckledcomics.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = 'ryugou-chapter-1-cover'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        title = pageUrl.rstrip('/').rsplit('/', 1)[-1]
        ext = imageUrl.rsplit('.', 1)[-1]
        return title + '.' + ext

    def fetchUrls(self, url, data, urlSearch):
        imageUrls = super(Ryugou, self).fetchUrls(url, data, urlSearch)
        if url == self.stripUrl % '1-3':
            imageUrls = [imageUrls[1]]
        return imageUrls

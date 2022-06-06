# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2021 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile
from urllib.parse import urljoin

from ..helpers import bounceStarter
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import WordPressScraper, WordPressNavi, WordPressWebcomic


class RalfTheDestroyer(WordPressScraper):
    url = 'http://ralfthedestroyer.com/'


class RayFox(WordPressNavi):
    url = 'https://www.rayfoxthecomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'not-a-super-hero/it-begins'

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[-1].split('.', 1)[0]
        ext = imageUrl.rsplit('.', 1)[-1]
        if filename == 'j':
            filename = 'RF_E3_P52'
        elif filename == '46' or filename == '55' or filename == '61':
            filename = 'RF_E3_P' + filename
        elif 'chapter-3-cover' in filename:
            filename = 'RF_E3_Cover'
        elif 'Cover2' in filename:
            filename = 'RF_E1_' + filename
        elif 'Volume-1-Cover' in filename:
            filename = filename.replace('Ray-Fox-Volume-1-', 'RF_E1_')
        elif filename[0] == '0':
            filename = 'RF_E1_P' + filename
        return filename + '.' + ext


class RaynaOnTheRiver(WordPressScraper):
    url = 'http://www.catomix.com/rayna/'
    firstStripUrl = url + 'archives/comic/teaser-poster'


class RealLife(WordPressScraper):
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


class RealmOfAtland(_ParserScraper):
    url = 'https://web.archive.org/web/20201225151926/http://www.realmofatland.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '1'
    prevSearch = '//a[@id="cg_back"]'
    imageSearch = '//p[@id="cg_img"]//img'
    endOfLife = True
    help = 'Index format: nnn'


class Recursion(_ParserScraper):
    url = 'https://recursioncomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '0001'
    imageSearch = '//div[@class="content"]//img'
    prevSearch = '//link[@rel="prev"]'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        filename = filename.replace('0bf62e92-2c98-4fb2-8ed7-4584980beb17', 'page0005')
        filename = filename.replace('76112837-c5cd-4df7-8c53-3ed5c25194cf', 'page0003')
        filename = filename.replace('ed271080-6b1b-4d7a-8509-b2d8a15da805', 'page0002')
        filename = filename.replace('7b194ef7-ac77-4b5c-aed0-826901d13d04', 'page0001')
        return filename


class RedMeat(_ParserScraper):
    url = 'http://www.redmeat.com/max-cannon/FreshMeat'
    imageSearch = '//div[@class="comicStrip"]//img'
    prevSearch = '//a[@class="prev"]'

    def namer(self, image_url, page_url):
        parts = image_url.rsplit('/', 2)
        return '_'.join(parts[1:3])


class Requiem(WordPressScraper):
    baseUrl = 'http://requiem.spiderforest.com/'
    url = baseUrl + '?latest'
    stripUrl = baseUrl + 'comic/%s'
    firstStripUrl = stripUrl % '2004-06-07-3'


class Replay(_ParserScraper):
    url = 'http://replaycomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'red-desert'
    imageSearch = '//div[@id="comic"]//img[@alt]'
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


class RiversideExtras(WordPressWebcomic):
    url = 'https://riversidecomics.com/'


class RomanticallyApocalyptic(_ParserScraper):
    url = 'http://romanticallyapocalyptic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//div[d:class("comicpanel")]/center//img'
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
    prevSearch = compile(tagre("a", "href", r'(/cartoon/\d+/datum/asc/)'))
    help = 'Index format: number'

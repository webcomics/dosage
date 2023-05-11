# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile
from urllib.parse import urljoin
from lxml import etree

from ..scraper import BasicScraper, ParserScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import ComicControlScraper, WordPressScraper, WordPressNavi


class Underling(WordPressNavi):
    url = ('https://web.archive.org/web/20190806120425/'
        'http://underlingcomic.com/')
    firstStripUrl = url + 'page-one/'
    endOfLife = True


class Undertow(BasicScraper):
    url = 'http://undertow.dreamshards.org/'
    imageSearch = compile(tagre("img", "src", r'([^"]+\.jpg)'))
    prevSearch = compile(r'href="(.+?)".+?teynpoint')
    latestSearch = compile(r'href="(.+?)".+?Most recent page')
    starter = indirectStarter


class unDivine(ComicControlScraper):
    url = 'https://www.undivinecomic.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'page-1'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1].replace(' ', '-')
        filename = filename.replace('10B311D9-0992-4D74-AEB8-DAB714DA67C6', 'UD-322')
        filename = filename.replace('99266624-7EF7-4E99-9EC9-DDB5F59CBDFD', 'UD-311')
        filename = filename.replace('33C6A5A1-F703-4A0A-BCD5-DE1A09359D8E', 'UD-310')
        filename = filename.replace('6CE01E81-C299-43C7-A221-8DE0670EFA30', 'ch4endbonusq4')
        filename = filename.replace('DB66D93B-1FE5-49C7-90E0-FFF981DCD6B3', 'bipolar')
        if len(filename) > 15 and filename[0].isdigit() and filename[10] == '-':
            filename = filename[11:]
        return filename


class UnicornJelly(BasicScraper):
    baseUrl = 'http://unicornjelly.com/'
    url = baseUrl + 'uni666.html'
    stripUrl = baseUrl + 'uni%s.html'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(r'</TABLE>(?:<FONT COLOR="BLACK">)?<IMG SRC="(images/[^"]+)" WIDTH=')
    prevSearch = compile(r'<A HREF="(uni\d{3}[bcs]?\.html)">(<FONT COLOR="BLACK">)?<IMG SRC="images/back00\.gif"')
    help = 'Index format: nnn'


class Unsounded(ParserScraper):
    url = 'http://www.casualvillain.com/Unsounded/'
    startUrl = url + 'comic+index/'
    stripUrl = url + 'comic/ch%s/ch%s_%s.html'
    firstStripUrl = stripUrl % ('01', '01', '01')
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[d:class("back")]'
    latestSearch = '//div[@id="chapter_box"][1]//a[last()]'
    multipleImagesPerStrip = True
    starter = indirectStarter
    help = 'Index format: chapter-page'

    def fetchUrls(self, url, data, urlSearch):
        imageUrls = super(Unsounded, self).fetchUrls(url, data, urlSearch)
        # Include background for multi-image pages
        imageRegex = compile(r'background-image: url\((pageart/.*)\)')
        for match in imageRegex.finditer(str(etree.tostring(data))):
            print(match)
            searchUrls.append(normaliseURL(urljoin(data[1], match.group(1))))
        return imageUrls

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[-1]
        pagename = pageUrl.rsplit('/', 1)[-1]
        if pagename.split('.', 1)[0] != filename.split('.', 1)[0]:
            filename = pagename.split('_', 1)[0] + '_' + filename
        return filename

    def getPrevUrl(self, url, data):
        # Fix missing navigation links between chapters
        if 'ch13/you_let_me_fall' in url:
            return self.stripUrl % ('13', '13', '85')
        return super(Unsounded, self).getPrevUrl(url, data)

    def getIndexStripUrl(self, index):
        chapter, num = index.split('-')
        return self.stripUrl % (chapter, chapter, num)


class UrgentTransformationCrisis(WordPressScraper):
    url = 'http://www.catomix.com/utc/'
    firstStripUrl = url + 'comic/cover1'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1].rsplit('?', 1)[0]
        return filename.replace('FVLYHD', 'LYHDpage').replace('UTC084web', '20091218c')

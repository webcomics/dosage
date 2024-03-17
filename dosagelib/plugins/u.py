# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from __future__ import annotations

import json
import re
from contextlib import suppress
from re import compile

from ..scraper import BasicScraper, ParserScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import ComicControlScraper, WordPressScraper, WordPressNavi


class UberQuest(ParserScraper):
    baseUrl = 'https://uberquest.studiokhimera.com/'
    url = baseUrl + 'wp-json/keeros_comics/v1/chapters'
    stripUrl = baseUrl + 'wp-json/wp/v2/cfx_comic_page?page_number=%s'
    firstStripUrl = stripUrl % 'cover'

    def starter(self):
        # Retrieve comic metadata from API
        data = self.session.get(self.url)
        data.raise_for_status()
        return self.stripUrl % data.json()[-1]['pages'][-1]['page_number']

    def getPrevUrl(self, url, data):
        return self.stripUrl % json.loads(data.text_content())[0]['prev_id']

    def extract_image_urls(self, url, data):
        return [json.loads(data.text_content())[0]['attachment']]

    def namer(self, imageUrl, pageUrl):
        return 'UberQuest-' + pageUrl.rsplit('=', 1)[-1]


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
    url = 'https://www.casualvillain.com/Unsounded/'
    startUrl = url + 'comic+index/'
    stripUrl = url + 'comic/ch%s/ch%s_%s.html'
    firstStripUrl = stripUrl % ('01', '01', '01')
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[d:class("back")]'
    latestSearch = '//div[@id="chapter_box"][1]//a[last()]'
    multipleImagesPerStrip = True
    starter = indirectStarter
    style_bg_regex = re.compile(r'background-image: url\((.*pageart/.*)\)')
    help = 'Index format: chapter-page'

    def extract_image_urls(self, url, data):
        urls = []
        with suppress(ValueError):
            urls.extend(super().extract_image_urls(url, data))
        # Include background for multi-image pages
        cssbg = self.extract_css_bg(data)
        if cssbg:
            urls.append(cssbg)
        if not urls:
            raise ValueError(f'No comic found at {url!r}')
        return urls

    def extract_css_bg(self, page) -> str | None:
        comicdivs = self.match(page, '//div[@id="comic"]')
        if comicdivs:
            style = comicdivs[0].attrib.get('style')
            if style:
                hit = self.style_bg_regex.search(style)
                if hit:
                    return hit.group(1)
        return None

    def namer(self, image_url, page_url):
        filename = image_url.rsplit('/', 1)[-1]
        pagename = page_url.rsplit('/', 1)[-1]
        if pagename.split('.', 1)[0] != filename.split('.', 1)[0]:
            filename = pagename.split('_', 1)[0] + '_' + filename
        return filename

    def getPrevUrl(self, url, data):
        # Fix missing navigation links between chapters
        if 'ch13/you_let_me_fall' in url:
            return self.stripUrl % ('13', '13', '85')
        return super().getPrevUrl(url, data)

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

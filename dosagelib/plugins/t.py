# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile, escape, MULTILINE
try:
    from functools import cached_property
except ImportError:
    from cached_property import cached_property

from ..scraper import _BasicScraper, _ParserScraper, ParserScraper
from ..helpers import indirectStarter, joinPathPartsNamer
from ..util import tagre
from .common import (ComicControlScraper, WordPressScraper, WordPressSpliced,
        WordPressNavi, WordPressWebcomic)


class TailsAndTactics(_ParserScraper):
    url = 'http://tailsandtactics.com/comic/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@class="comic-image"]/img'
    prevSearch = '//a[text()=" Back"]'


class TekMage(WordPressNavi):
    url = 'https://tekmagecomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'chapter-1-page-1'


class Tamberlane(WordPressWebcomic):
    baseUrl = 'https://www.tamberlanecomic.com/'
    url = baseUrl + 'latest/'
    stripUrl = baseUrl + 'tamberlane/%s/'
    firstStripUrl = stripUrl % 'page-1'
    imageSearch = '//div[@id="comic-page"]/img/@src'
    prevSearch = '//a[@class="previous-link"]'


class TheBoyWhoFell(ComicControlScraper):
    url = 'https://www.boywhofell.com/'
    firstStripUrl = url + 'comic/ch00p00'


class TheBrads(_ParserScraper):
    url = ('https://web.archive.org/web/20171211154809/'
        'http://bradcolbow.com/archive/C4/')
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'P125'
    imageSearch = '//div[d:class("entry")]//img'
    prevSearch = '//a[d:class("prev")]'
    multipleImagesPerStrip = True
    endOfLife = True


class TheChroniclesOfHuxcyn(WordPressScraper):
    url = 'https://huxcyn.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'opening-001'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        filename = filename.replace('IMG_0504', 'TCoH109')
        filename = filename.replace('tcoh', 'TCoH')
        filename = filename.replace('1599151639.xizana_f3a6458e-8d94-4259-bec3-5a92706fe493_jpeg', 'october.2020.cover')
        filename = filename.replace('huxonsword', 'october.2020.huxonsword')
        filename = filename.replace('New_Canvas100pageswebimage', 'TCoH100')
        if filename[0] == '0':
            filename = 'TCoH' + filename
        elif filename[0] == '3':
            pagenum = int(filename.rsplit('.', 1)[0].split('_', 1)[1].split('_', 1)[0])
            filename = 'TCoH' + str(40 + pagenum) + filename.rsplit('.', 1)[-1]
        return filename


class TheClassMenagerie(_ParserScraper):
    stripUrl = 'http://www.theclassm.com/d/%s.html'
    url = stripUrl % '20050717'
    firstStripUrl = stripUrl % '19990322'
    imageSearch = '//img[@class="ksc"]'
    prevSearch = '//a[@rel="prev"]'
    multipleImagesPerStrip = True
    endOfLife = True


class TheDepths(WordPressWebcomic):
    url = 'https://www.thedepthscomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'page-01'
    imageSearch = '//div[contains(@class, "webcomic-media")]//img'
    adult = True

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        filename = filename.replace('pg', 'page_')
        filename = filename.replace('page_', 'the_depths_')
        filename = filename.replace('-web', '')
        return filename


class TheDevilsPanties(WordPressNavi):
    url = 'https://thedevilspanties.com/'
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '300'
    help = 'Index format: number'


class TheDreamlandChronicles(WordPressScraper):
    url = 'http://www.thedreamlandchronicles.com/'


class TheForgottenOrder(ComicControlScraper):
    url = 'http://www.forgottenordercomic.com/'
    firstStripUrl = url + 'comic/prolouge-01-book-1'


class TheGamerCat(WordPressSpliced):
    url = 'https://thegamercat.com/'
    firstStripUrl = url +  'comic/06102011/'


class TheGentlemansArmchair(WordPressScraper):
    url = 'http://thegentlemansarmchair.com/'


class TheGentleWolf(WordPressScraper):
    url = 'https://thegentlewolf.net/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'tgw-001'

    def namer(self, imageUrl, pageUrl):
        # Fix duplicate filename
        filename = imageUrl.rsplit('/', 1)[-1]
        if pageUrl == self.stripUrl % 'tgw-271':
            filename = filename.replace('272', '271')
        return filename


class TheGlassScientists(ComicControlScraper):
    url = 'https://www.theglassscientists.com/'
    firstStripUrl = url + 'comic/chapter-i'


class TheJunkHyenasDiner(WordPressScraper):
    url = 'http://junkhyenasdiner.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'intro'


class TheLandscaper(_ParserScraper):
    stripUrl = ('https://web.archive.org/web/20171129163510/'
        'http://landscaper.visual-assault.net/comic/%s')
    url = stripUrl % 'latest'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//article[d:class("comic")]//img[1]'
    prevSearch = '//a[contains(text(), "Previous")]'
    endOfLife = True


class TheMelvinChronicles(WordPressScraper):
    url = 'http://melvin.jeaniebottle.com/'


class TheNightBelongsToUs(_ParserScraper):
    url = 'https://tnbtu.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '01-00'
    imageSearch = '//div[@id="spliced-comic"]//img'
    prevSearch = '//a[./img[contains(@src, "nav-prev")]]'
    latestSearch = '//a[contains(@class, "main-link")]'
    starter = indirectStarter
    adult = True


class TheNoob(WordPressScraper):
    url = 'http://thenoobcomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '1'
    help = 'Index format: n (unpadded)'


class TheOldVictorian(_ParserScraper):
    url = 'http://theoldvictorianwebcomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'the-old-victorian-cover'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[contains(@class, "comic-nav-previous")]'

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[-1].replace('_', '-')
        filename = filename.replace('TOV00', 'TOV-00')
        if filename.replace('oldvic', '')[0].isdigit():
            filename = filename.replace('oldvic', 'TOV-00')
        if 'TOV-000' in filename and len(filename) > 12:
            filename = filename[:8] + '-' + filename[8:]
        return filename


class TheOrderOfTheStick(_ParserScraper):
    url = 'https://www.giantitp.com/'
    stripUrl = url + 'comics/oots%s.html'
    firstStripUrl = stripUrl % '0001'
    imageSearch = '//img[contains(@src, "/comics/oots/")]'
    prevSearch = '//a[./img[@alt="Previous Comic"]]'
    latestSearch = '//a[@class="SideBar" and contains(@href, "/comics/oots")]'
    help = 'Index format: n (unpadded)'
    starter = indirectStarter

    def namer(self, image_url, page_url):
        return page_url.rsplit('/', 1)[-1][:-5]


class TheRockCocks(_BasicScraper):
    url = 'http://rockcocks.slipshine.net/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % "page-1-nsfw-track-1-start"
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl, after='id="cc-comic"'))
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after='rel="prev"'))
    adult = True


class TheWhiteboard(_ParserScraper):
    BROKEN_PAGE_MIDDLE = compile(r'</body></html>\n<')
    url = 'http://www.the-whiteboard.com/'
    stripUrl = url + 'auto%s.html'
    firstStripUrl = stripUrl % 'wb001'
    imageSearch = '//img[contains(@src, "auto")]'
    prevSearch = '//a[.//img[contains(@src, "previous")]]'

    def _parse_page(self, data):
        # Ugly hack to fix broken HTML
        data = self.BROKEN_PAGE_MIDDLE.sub('<', data)
        return super(TheWhiteboard, self)._parse_page(data)

    def imageUrlModifier(self, url, data):
        return self.url + url

    def link_modifier(self, fromurl, tourl):
        return self.url + tourl


class TheWotch(WordPressScraper):
    url = 'http://www.thewotch.com/'
    firstStripUrl = url + '?comic=enter-the-wotch'


class ThisIsIndexed(_BasicScraper):
    url = 'http://thisisindexed.com/'
    rurl = escape(url)
    stripUrl = url + 'page/%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/card[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("div", "class", "nav-previous") +
                         tagre("a", "href", r'(%spage/\d+/)[^"]*' % rurl))
    help = 'Index format: number'


class ThreePanelSoul(ComicControlScraper):
    url = 'http://threepanelsoul.com/'
    firstStripUrl = url + 'comic/a-test-comic'


class TinyDickAdventures(_ParserScraper):
    url = 'https://www.lfg.co/'
    stripUrl = url + 'tda/strip/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic-img"]//img'
    prevSearch = '//a[@class="comic-nav-prev"]'
    latestSearch = '//div[@id="feature-tda-footer"]/a[contains(@href, "tda/strip/")]'
    starter = indirectStarter

    def namer(self, imageUrl, pageUrl):
        page = pageUrl.rstrip('/').rsplit('/', 1)[-1]
        ext = imageUrl.rsplit('.', 1)[-1]
        return page + '.' + ext


class ToonHole(ParserScraper):
    url = 'https://toonhole.com/'
    firstStripUrl = url + '2010/01/smart-questions-get-smart-answers/'
    imageSearch = '//img[d:class("wp-post-image")]'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@rel="bookmark"]'
    starter = indirectStarter
    namer = joinPathPartsNamer((), (-3, -2, -1))


class TrippingOverYou(_BasicScraper):
    url = 'http://www.trippingoveryou.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'wiggle-room'
    imageSearch = compile(tagre("img", "src", r'([^"]+/comics/[^"]+)'))
    prevSearch = compile(r'<a class="cc-prev" rel="prev" href="(.+?)">')
    help = 'Index format: stripname'


class TumbleDryComics(WordPressScraper):
    url = 'https://www.tumbledrycomics.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'we-need-to-get-high-jpg'
    textSearch = '//div[@id="comic"]//img/@alt'
    multipleImagesPerStrip = True
    adult = True
    help = 'Index format: name'

    def namer(self, image_url, page_url):
        # Most images have the date they were posted in the filename
        # For those that don't we can get the month and year from the image url
        parts = image_url.rsplit('/', 3)
        year = parts[1]
        month = parts[2]
        filename = parts[3]
        if not filename.startswith(year):
            filename = year + "-" + month + "-" + filename
        return filename


class Turnoff(_ParserScraper):
    name = 'turnoff'
    url = 'https://turnoff.us/'
    imageSearch = '//article[d:class("post-content")]//img'
    prevSearch = '//div[d:class("prev")]//a'
    stripUrl = url + 'geek/%s'
    firstStripUrl = stripUrl % 'tcp-buddies'
    multipleImagesPerStrip = True

    @cached_property
    def comics_order(self):
        # Neither the images nor the pages contain information about dates or indices.
        # However we can extract the order of the images from the JavaScript.
        html = self.session.get(self.url).text
        list_regex = compile(r"""^\s*"/geek/(.*)",\s*$""", flags=MULTILINE)
        return list(reversed(list_regex.findall(html)))

    def namer(self, image_url, page_url):
        comic_name = page_url.split('/')[-1]
        try:
            index = self.comics_order.index(comic_name) + 1
        except ValueError:
            index = len(self.comics_order)
        file_name = image_url.split('/')[-1]
        return "%03d-%s" % (index, file_name)


class TwinDragons(WordPressScraper):
    url = 'http://www.twindragonscomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'the-beginning'
    multipleImagesPerStrip = True


class TwoGuysAndGuy(_BasicScraper):
    url = 'http://www.twogag.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '4'
    imageSearch = compile(tagre('img', 'src', r'(%scomics/\d{4}-\d{2}-\d{2}[^"]*)' % rurl))
    prevSearch = compile(tagre('a', 'href', r'(%sarchives/\d+)' % rurl,
                               after='title="Previous"'))
    help = 'Index format: number'
    adult = True


class Twokinds(_ParserScraper):
    url = 'http://twokinds.keenspot.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//article[d:class("comic")]//img'
    prevSearch = '//a[d:class("navprev")]'
    help = 'Index format: n (unpadded)'


class TwokindsSketches(Twokinds):
    name = 'Twokinds/Sketches'
    imageSearch = '//article[contains(@class, "comic")]/a'


class TwoLumps(_BasicScraper):
    url = 'http://www.twolumps.net/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)', after="prev"))
    help = 'Index format: yyyymmdd'

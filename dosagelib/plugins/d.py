# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import compile, escape

from .. import util
from ..helpers import bounceStarter, indirectStarter, joinPathPartsNamer
from ..scraper import BasicScraper, ParserScraper, _BasicScraper, _ParserScraper
from ..util import tagre
from .common import (
    ComicControlScraper,
    WordPressNavi,
    WordPressScraper,
    WordPressWebcomic,
)


class Damonk(_BasicScraper):
    url = 'http://www.damonk.com/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20060522'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
                         tagre("img", "src", r'/images/previous_day\.gif'))
    help = 'Index format: yyyymmdd'


class DangerouslyChloe(ComicControlScraper):
    url = 'http://www.dangerouslychloe.com/'
    firstStripUrl = url + 'strips-dc/Chapter_1_-_That_damned_girl'


class DarkLegacy(ParserScraper):
    starter = indirectStarter
    url = "https://www.darklegacycomics.com"
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@class="comic narrow"]//img'
    prevSearch = ('//a[@title="Previous - A"]',
                  '//a[@title="Previous"]')
    latestSearch = '//div[@class="comic narrow feed"]//a'
    help = 'Index format: n (unpadded)'


class DarkWhite(WordPressScraper):
    url = 'https://www.darkwhitecomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'chapter-1-sleep'


class DarthsAndDroids(_BasicScraper):
    url = 'http://www.darthsanddroids.net/'
    stripUrl = url + 'episodes/%s.html'
    firstStripUrl = stripUrl % '0001'
    prevSearch = compile(tagre("a", "href", r'(/episodes/\d\d\d\d.html)') +
                         '&lt;PREVIOUS')
    imageSearch = compile(tagre("img", "src", r'(/comics/darths\d\d\d\d\.jpg)'))


class DasLebenIstKeinPonyhof(_ParserScraper):
    baseUrl = 'https://sarahburrini.com/comic/das-leben-ist-kein-ponyhof/'
    url = baseUrl + 'und-nu/'
    firstStripUrl = url + 'mein-erster-webcomic/'
    imageSearch = '//img[d:class("attachment-full")]'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True
    lang = 'de'


class DaughterOfTheLilies(ComicControlScraper):
    url = 'https://www.daughterofthelilies.com/'
    firstStripUrl = url + 'dotl/part-1-a-girl-with-no-face'


class DeadWinter(_BasicScraper):
    url = 'http://deadwinter.cc/'
    stripUrl = url + 'page/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(/static/page/strip/\d+[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') + "Previous")
    help = 'Index format: number'


class Deathbulge(BasicScraper):
    url = 'https://www.deathbulge.com/api/comics'
    imageSearch = compile(r"(/images/comics/[^\.]+\.jpg)")
    prevSearch = compile(r'"previous":(\d+),')
    firstStripUrl = url + '/1'

    def getPrevUrl(self, url, data):
        if data[1] == self.url:
            data = (data[0], data[1] + '/')
        return super().getPrevUrl(url, data)


class DeepFried(_BasicScraper):
    url = 'http://www.whatisdeepfried.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2001/09/16/new-world-out-of-order'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: none'


class DeerMe(_ParserScraper):
    url = 'https://www.deerme.net/'
    firstStripUrl = url + 'a.php?b=comic/c001-image/dm-20031121-001-0001'
    imageSearch = '//div[d:class("ComicImage")]/img'
    prevSearch = '//a[@rel="prev"]'
    nextSearch = '//a[@rel="next"]'
    starter = bounceStarter


class Delve(WordPressScraper):
    url = 'https://thisis.delvecomic.com/NewWP/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'in-too-deep'
    adult = True
    maxLen = len('episode999')

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = util.urlpathsplit(imageUrl)[-1]
        if (pageUrl == self.stripUrl % 'engagement' or
                pageUrl == self.stripUrl % 'losing-it'):
            self.maxLen = self.maxLen - 1
        if ('episode' in filename and
                len(filename) - len('.jpg') > self.maxLen and
                filename[self.maxLen] != '-'):
            filename = filename[:self.maxLen] + '-' + filename[self.maxLen:]
        return filename


class DemolitionSquad(_ParserScraper):
    url = 'http://www.demolitionsquad.de/'
    stripUrl = url + '?comicbeitrag=%s'
    firstStripUrl = stripUrl % '181'
    imageSearch = '//img[contains(@src,"uploads/pics/")]'
    prevSearch = '//img[@name="zuruck"]/..'
    help = 'Index format: number'
    lang = 'de'


class DerTodUndDasMaedchen(_ParserScraper):
    url = ('https://web.archive.org/web/20180106180134/'
        'http://www.cartoontomb.de/deutsch/tod2.php')
    stripUrl = url + '?bild=%s.jpg'
    firstStripUrl = stripUrl % '00_01_01'
    imageSearch = '//img[contains(@src, "images/tod/teil2")]'
    prevSearch = u'//a[text()="zur\u00FCck"]'
    help = 'Index format: nn_nn_nn'
    lang = 'de'


class DesertFox(WordPressWebcomic):
    url = 'https://desertfoxcomics.net/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'origins-1'

    def namer(self, image_url, page_url):
        # Fix inconsistent filenames
        filename = util.urlpathsplit(image_url)[-1]
        filename = filename.replace('Pg', 'Page').replace('Desert-Fox', '')
        if 'origins' in page_url:
            filename = filename.replace('Page-', 'Page-0-')
        return filename


class DieFruehreifen(_BasicScraper):
    url = 'http://www.die-fruehreifen.de/index.php'
    stripUrl = url + '?id=%s&order=DESC'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'([^"]*/strips/[Ff]rueh_?[Ss]trip_\d+.jpg)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?id=\d+&order=DESC)") +
                         tagre("img", "id", r"naechster"))
    help = 'Index format: n (unpadded)'
    lang = 'de'


class DieselSweeties(_ParserScraper):
    url = 'http://dieselsweeties.com/'
    stripUrl = url + 'ics/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@class="xomic"]'
    prevSearch = '//div[@id="prev"]//a[contains(text(), "previous")]'
    latestSearch = prevSearch
    starter = indirectStarter
    help = 'Index format: n (unpadded)'


class DieselSweetiesOld(_ParserScraper):
    url = 'http://dieselsweeties.com/archive/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "/hstrips/")]'
    prevSearch = '//a[contains(@title, "previous")]'
    help = 'Index format: n (unpadded)'
    endOfLife = True

    def starter(self):
        return self.stripUrl % '4000'

    def namer(self, image_url, page_url):
        index = int(util.urlpathsplit(image_url)[-1].split('.')[0])
        return 'sw%02d' % index


class DocRat(WordPressWebcomic):
    url = 'https://www.docrat.com.au/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'begin-with-eye-contact'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = util.urlpathsplit(imageUrl)[-1]
        filename = filename.replace('2006-08-01', 'DR0027')
        filename = filename.replace('2006-07-31', 'DR0026')
        return filename


class DoemainOfOurOwn(ParserScraper):
    url = 'http://www.doemain.com/'
    stripUrl = url + 'html/%s.html'
    firstStripUrl = stripUrl % '1999/1999-04-24'
    imageSearch = '//img[contains(@src, "strips/")]'
    prevSearch = '//a[img[@alt="Previous Strip"]]'
    endOfLife = True
    help = 'Index format: yyyy-mm-dd'

    def namer(self, image_url, page_url):
        # Fix date formatting
        filename = util.urlpathsplit(image_url)[-1]
        if len(filename) > 6 and filename[0:6].isdigit():
            month = filename[0:2]
            day = filename[2:4]
            year = ('19' if filename[4] == '9' else '20') + filename[4:6]
            filename = '%s-%s-%s%s' % (year, month, day, filename[6:])
        return filename


class DoesNotPlayWellWithOthers(WordPressNavi):
    url = 'http://www.doesnotplaywellwithothers.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'pwc-0001'
    adult = True


class DoghouseDiaries(ParserScraper):
    url = 'http://thedoghousediaries.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '34'
    imageSearch = '//img[@class="imgcomic"]'
    textSearch = imageSearch + '/@title'
    prevSearch = '//a[@id="previouslink"]'
    nextSearch = '//a[@id="nextlink"]'
    starter = bounceStarter
    namer = joinPathPartsNamer(pageparts=(-1,))
    help = 'Index format: number'


class DominicDeegan(_ParserScraper):
    url = 'https://www.dominic-deegan.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '0001-20020521'
    imageSearch = '//img[contains(@class, "wp-post-image")]'
    prevSearch = '//a[@title="Prev"]'
    help = 'Index format: ####-yyyymmdd'


class DorkTower(_ParserScraper):
    url = 'http://www.dorktower.com/'
    firstStripUrl = url + '1997/01/01/shadis-magazine-strip-1/'
    imageSearch = '//div[d:class("entry-content")]//a/img'
    prevSearch = '//a[d:class("btn")][text()="Previous"]'


class DoomsdayMyDear(_ParserScraper):
    url = 'http://doomsdaymydear.com/'
    imageSearch = '//img[d:class("attachment-full")]'
    prevSearch = '//a[d:class("previous-webcomic-link")]'


class Draconia(WordPressWebcomic):
    url = 'https://www.draconiachronicles.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'chapter-1-page-1'


class Dracula(_BasicScraper):
    url = 'http://draculacomic.net/'
    stripUrl = url + 'comic.php?comicID=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(r'&nbsp;<a class="archivelink" href="(.+?)">&laquo; Prev</a>')
    help = 'Index format: nnn'


class DreamKeepers(_ParserScraper):
    url = 'http://www.dreamkeeperscomic.com/GNSaga.php'
    stripUrl = url + '?pg=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "GNSagapages")]'
    prevSearch = '//a[@id="prev"]'
    help = 'Index format: n'


class DreamKeepersPrelude(_ParserScraper):
    url = 'http://www.dreamkeeperscomic.com/Prelude.php'
    stripUrl = url + '?pg=%s'
    firstStripUrl = stripUrl % '0001'
    imageSearch = '//div[@class="Preludecomic"]/table//a/img'
    prevSearch = '//a[@id="prev"]'
    help = 'Index format: n'


class DresdenCodak(ParserScraper):
    url = 'http://dresdencodak.com/'
    firstStripUrl = url + '2007/02/08/pom/'
    imageSearch = '//section[d:class("entry-content")]//img[d:class("aligncenter")]'
    prevSearch = '//a[img[contains(@src, "prev")]]'
    latestSearch = '//a[d:class("tc-grid-bg-link")]'
    starter = indirectStarter


class DrFun(_ParserScraper):
    baseUrl = ('https://web.archive.org/web/20180726145737/'
        'http://www.ibiblio.org/Dave/')
    stripUrl = baseUrl + 'ar%s.htm'
    url = stripUrl % '00502'
    firstStripUrl = stripUrl % '00001'
    imageSearch = '//a[contains(@href, "Dr-Fun/df")]'
    multipleImagesPerStrip = True
    prevSearch = '//a[contains(text(), "Previous Week")]'
    endOfLife = True
    help = 'Index format: nnnnn'


class Drive(ParserScraper):
    url = 'http://www.drivecomic.com/'
    firstStripUrl = url + 'comic/act-1-pg-001/'
    imageSearch = ('//div[@id="unspliced-comic"]//img/@data-src-img',
        '//div[@id="unspliced-comic"]//picture//img')
    prevSearch = '//a[d:class("previous-comic")]'


class DrMcNinja(ParserScraper):
    url = ('https://web.archive.org/web/20210322033246/'
        'http://drmcninja.com/')
    stripUrl = url + 'archives/comic/%s/'
    firstStripUrl = stripUrl % '0p1'
    imageSearch = '//div[@id="comic"]/img'
    prevSearch = '//a[d:class("prev")]'
    help = 'Index format: {episode}p{page}'


class Drowtales(_ParserScraper):
    url = 'http://www.drowtales.com/mainarchive.php'
    stripUrl = url + '?sid=%s'
    firstStripUrl = stripUrl % '4192'
    imageSearch = '//div[@id="content_middle"]//img'
    prevSearch = '//a[@id="link_prev_top"]'
    help = 'Index format: number'


class DungeonsAndDenizens(WordPressNavi):
    url = ('https://web.archive.org/web/20160308001834/'
        'http://dungeond.com/')
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2005/08/23/08232005'
    endOfLife = True


class DumbingOfAge(WordPressNavi):
    url = 'http://www.dumbingofage.com/'
    stripUrl = url + '%s/'
    help = 'Index format: yyyy/comic/book-num/seriesname/stripname'

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, bounceStarter, xpath_class
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNaviIn


class DamnLol(_ParserScraper):
    url = 'http://www.damnlol.com/'
    # Classes for next and previous seem to be swapped...
    prevSearch = '//a[%s]' % xpath_class("next")
    nextSearch = '//a[%s]' % xpath_class("previous")
    imageSearch = '//img[@id="post-image"]'
    starter = bounceStarter

    def namer(self, image_url, page_url):
        ext = image_url.rsplit('.', 1)[1]
        path = page_url.rsplit('/', 1)[1][:-5]
        stripname, number = path.rsplit('-', 1)
        return '%s-%s.%s' % (number, stripname, ext)


class Damonk(_BasicScraper):
    url = 'http://www.damonk.com/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20060522'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
                         tagre("img", "src", r'/images/previous_day\.gif'))
    help = 'Index format: yyyymmdd'


class DangerouslyChloe(_ComicControlScraper):
    url = 'http://www.dangerouslychloe.com/'
    firstStripUrl = url + 'strips-dc/Chapter_1_-_That_damned_girl'


class DarkWhite(_WordPressScraper):
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


class DasLebenIstKeinPonyhof(_WPNaviIn):
    url = 'http://sarahburrini.com/wordpress/'
    firstStripUrl = url + 'comic/mein-erster-webcomic/'
    lang = 'de'


class DeadWinter(_BasicScraper):
    url = 'http://deadwinter.cc/'
    stripUrl = url + 'page/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(/static/page/strip/\d+[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') + "Previous")
    help = 'Index format: number'


class Deathbulge(_BasicScraper):
    url = 'http://www.deathbulge.com/api/comics'
    imageSearch = compile(r"(/images/comics/[^\.]+\.jpg)")
    prevSearch = compile(r'"previous":(\d+),')
    firstStripUrl = url + '/1'

    def getPrevUrl(self, url, data):
        if data[1] == self.url:
            data = (data[0], data[1] + '/')
        return _BasicScraper.getPrevUrl(self, url, data)


class DeepFried(_BasicScraper):
    url = 'http://www.whatisdeepfried.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2001/09/16/new-world-out-of-order'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: none'


class DemolitionSquad(_ParserScraper):
    url = 'http://www.demolitionsquad.de/'
    stripUrl = url + '?comicbeitrag=%s'
    firstStripUrl = stripUrl % '181'
    imageSearch = '//img[contains(@src,"uploads/pics/")]'
    prevSearch = '//img[@name="zuruck"]/..'
    help = 'Index format: number'
    lang = 'de'


class DerTodUndDasMaedchen(_ParserScraper):
    url = 'http://www.cartoontomb.de/deutsch/tod2.php'
    stripUrl = url + '?bild=%s.jpg'
    firstStripUrl = stripUrl % '00_01_01'
    imageSearch = '//img[contains(@src, "images/tod/teil2")]'
    prevSearch = u'//a[text()="zur\u00FCck"]'
    help = 'Index format: nn_nn_nn'
    lang = 'de'


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
        index = int(image_url.split('/')[-1].split('.')[0])
        return 'sw%02d' % index


class Dilbert(_ParserScraper):
    url = 'http://dilbert.com/'
    stripUrl = url + 'strip/%s'
    firstStripUrl = stripUrl % '1989-04-16'
    starter = indirectStarter
    prevSearch = '//div[%s]/a' % xpath_class('nav-left')
    imageSearch = '//img[%s]' % xpath_class('img-comic')
    latestSearch = '//a[@class="img-comic-link"]'
    help = 'Index format: yyyy-mm-dd'

    def namer(self, image_url, page_url):
        name = page_url.rsplit("/", 1)[1]
        return "%s" % name


class DocRat(_ParserScraper):
    url = 'http://www.docrat.com.au/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'begin-with-eye-contact'
    imageSearch = '//div[@class="webcomic-image"]//img'
    prevSearch = '//a[contains(@class, "previous-webcomic-link")]'

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1].rsplit('?', 1)[0]
        filename = filename.replace('2006-08-01', 'DR0027')
        filename = filename.replace('2006-07-31', 'DR0026')
        return filename


class DoemainOfOurOwn(_ParserScraper):
    url = 'http://www.doemain.com/'
    stripUrl = url + 'index.cgi/%s'
    imageSearch = '//td/img[contains(@src, "/strips/")]'
    prevSearch = '//a[img[@alt="Previous Strip"]]'
    endOfLife = True
    help = 'Index format: yyyy-mm-dd'


class DoghouseDiaries(_ParserScraper):
    url = 'http://thedoghousediaries.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '34'
    imageSearch = '//img[@class="imgcomic"]'
    textSearch = imageSearch + '/@title'
    prevSearch = '//a[@id="previouslink"]'
    nextSearch = '//a[@id="nextlink"]'
    starter = bounceStarter
    help = 'Index format: number'

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 1)[-1] + '.' + imageUrl.rsplit('.', 1)[-1]


class DominicDeegan(_ParserScraper):
    url = 'http://www.dominic-deegan.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '0001-20020521'
    imageSearch = '//img[contains(@class, "wp-post-image")]'
    prevSearch = '//a[@title="Prev"]'
    endOfLife = True
    help = 'Index format: ####-yyyymmdd'


class DorkTower(_ParserScraper):
    url = 'http://www.dorktower.com/'
    firstStripUrl = url + '1997/01/01/shadis-magazine-strip-1/'
    imageSearch = '//div[%s]//a/img' % xpath_class('entry-content')
    prevSearch = '//a[%s][text()="Previous"]' % xpath_class('btn')


class DoomsdayMyDear(_ParserScraper):
    url = 'http://doomsdaymydear.com/'
    imageSearch = '//img[{}]'.format(xpath_class('attachment-full'))
    prevSearch = '//a[{}]'.format(xpath_class('previous-webcomic-link'))


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


class DresdenCodak(_ParserScraper):
    url = 'http://dresdencodak.com/'
    startUrl = url + 'cat/comic/'
    firstStripUrl = url + '2007/02/08/pom/'
    imageSearch = '//section[%s]//img[%s]' % (
        xpath_class('entry-content'), xpath_class('aligncenter'))
    prevSearch = '//a[img[contains(@src, "prev")]]'
    latestSearch = '//a[%s]' % xpath_class('tc-grid-bg-link')
    starter = indirectStarter

    # Blog and comic are mixed...
    def shouldSkipUrl(self, url, data):
        return not data.xpath(self.imageSearch)


class DrFun(_BasicScraper):
    baseUrl = 'http://www.ibiblio.org/Dave/'
    url = baseUrl + 'ar00502.htm'
    stripUrl = baseUrl + 'ar%s.htm'
    firstStripUrl = stripUrl % '00001'
    imageSearch = compile(tagre("a", "href", r'(Dr-Fun/df\d+/df[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + 'Previous Week,')
    help = 'Index format: nnnnn'
    endOfLife = True


class Drive(_BasicScraper):
    url = 'http://www.drivecomic.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s.html'
    firstStripUrl = stripUrl % '090815'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.drivecomic\.com/strips/main/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/\d+\.html)' % rurl) + "Previous")
    help = 'Index format: yymmdd'


class DrMcNinja(_ParserScraper):
    url = 'http://drmcninja.com/'
    stripUrl = url + 'archives/comic/%s/'
    firstStripUrl = stripUrl % '0p1'
    css = True
    imageSearch = 'div#comic img'
    prevSearch = 'a.prev'
    help = 'Index format: {episode}p{page}'


class Drowtales(_BasicScraper):
    baseUrl = 'http://www.drowtales.com/'
    rurl = escape(baseUrl)
    url = baseUrl + 'mainarchive.php'
    stripUrl = url + '?sid=%s'
    firstStripUrl = stripUrl % '4192'
    imageSearch = (
        compile(tagre("img", "src", r'((%s)?mainarchive/[^"]+)' % rurl)),
        compile(r'background-image:url\((mainarchive/[^\)]+center\.jpg)'),
    )
    prevSearch = compile(tagre("a", "href", r'(\?sid=\d+)', before="link_prev_top"))
    help = 'Index format: number'


class DumbingOfAge(_BasicScraper):
    url = 'http://www.dumbingofage.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    prevSearch = compile(tagre("a", "href", r'(%s\d+/[^"]+)' % rurl, after="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    help = 'Index format: yyyy/comic/book-num/seriesname/stripname'

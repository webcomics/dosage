# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, bounceStarter
from ..util import tagre
from .common import _WordPressScraper, xpath_class


class DailyDose(_ParserScraper):
    url = 'http://dailydoseofcomics.com/'
    starter = indirectStarter
    imageSearch = '//p/a/img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@rel="bookmark"]'


class DamnLol(_ParserScraper):
    url = 'http://www.damnlol.com/'
    prevSearch = '//a[@id="prev"]'
    nextSearch = '//a[@id="next"]'
    imageSearch = '//div[@id="hideFooter"]/img'
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


class DangerouslyChloe(_BasicScraper):
    url = 'http://www.dangerouslychloe.com/'
    stripUrl = url + 'strips-dc/%s'
    firstStripUrl = stripUrl % 'chapter_1_-_that_damned_girl'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-dc/[^"]+)', before="cn[id]prevt"))
    help = 'Index format: name'


class DarthsAndDroids(_BasicScraper):
    url = 'http://www.darthsanddroids.net/'
    stripUrl = url + 'episodes/%s.html'
    firstStripUrl = stripUrl % '0001'
    prevSearch = compile(tagre("a", "href", r'(/episodes/\d\d\d\d.html)') +
                         '&lt;PREVIOUS')
    imageSearch = compile(tagre("img", "src", r'(/comics/darths\d\d\d\d\.jpg)'))


class DasLebenIstKeinPonyhof(_WordPressScraper):
    url = 'http://sarahburrini.com/wordpress/'
    firstStripUrl = url + 'comic/mein-erster-webcomic/'
    multipleImagesPerStrip = True
    lang = 'de'


class DeadWinter(_BasicScraper):
    url = 'http://deadwinter.cc/'
    stripUrl = url + 'page/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(/static/page/strip/\d+[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') + "Previous")
    help = 'Index format: number'


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
    url = 'http://www.dieselsweeties.com/'
    stripUrl = url + 'ics/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@class="xomic"]'
    prevSearch = '//div[@id="prev"]//a[contains(text(), "previous")]'
    nextSearch = '//div[@id="prev"]//a[contains(text(), "next")]'
    starter = bounceStarter
    help = 'Index format: n (unpadded)'


class DieselSweetiesOld(_ParserScraper):
    url = 'http://www.dieselsweeties.com/archive/'
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


class Dilbert(_BasicScraper):
    url = 'http://dilbert.com/'
    stripUrl = url + '/strip/%s'
    firstStripUrl = stripUrl % '1989-04-16'
    starter = indirectStarter
    prevSearch = compile(tagre("a", "href", r'(/strip/\d+-\d+-\d+)', after="Older Strip"))
    imageSearch = compile(tagre("img", "src", r'(http://assets.amuniversal.com/\w+)'))
    latestSearch = compile(tagre("a", "href",
                                 r'(http://dilbert.com/strip/[0-9-]*)',
                                 after="Click to see"))
    help = 'Index format: yyyy-mm-dd'

    def namer(self, image_url, page_url):
        name = page_url.rsplit("/", 1)[1]
        return "%s" % name


class DMFA(_BasicScraper):
    url = 'http://www.missmab.com/'
    stripUrl = url + 'Comics/Vol_%s.php'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(tagre("img", "src", r'((?:Comics/|Vol)[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'((?:Comics/)?Vol[^"]+)') +
                         tagre("img", "src", r'(?:../)?Images/comicprev\.gif'))
    help = 'Index format: nnn (normally, some specials)'


class DoctorCat(_WordPressScraper):
    url = 'http://doctorcatmd.com/'
    firstStripUrl = url + 'comic/doctor-cat'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')


class DoemainOfOurOwn(_BasicScraper):
    url = 'http://www.doemain.com/'
    stripUrl = url + 'index.cgi/%s'
    imageSearch = compile(r"<img border='0' width='\d+' height='\d+' src='(/strips/\d{4}/\d{6}-[^\']+)'")
    prevSearch = compile(r'<a href="(/index\.cgi/\d{4}-\d{2}-\d{2})"><img width="\d+" height="\d+" border="\d+" alt="Previous Strip"')
    help = 'Index format: yyyy-mm-dd'


class DogHouseDiaries(_BasicScraper):
    url = 'http://thedoghousediaries.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '34'
    prevSearch = compile(r"<a id='previouslink' href='(http://thedoghousediaries.com/\d+)'")
    imageSearch = compile(r"<img src='(dhdcomics/[^']+)'")
    help = 'Index format: number'


class DominicDeegan(_BasicScraper):
    url = 'http://www.dominic-deegan.com/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2002-05-21'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(r'"(view.php\?date=[^"]+)".+?prev21')
    help = 'Index format: yyyy-mm-dd'


class DorkTower(_BasicScraper):
    url = 'http://www.dorktower.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1997/01/01/shadis-magazine-strip-1'
    imageSearch = compile(tagre("div", "class", "entry-content") +
                          "\s*<p>\s*" +
                          tagre("img", "src", r'(%sfiles/[0-9]+/[0-9]+/[^"]*Dork[^"]+\.(?:gif|jpg))' % rurl,
                                after=' alt'))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl) + "Previous")
    help = 'Index format: yyyy/mm/dd/stripname-dd-mm-yy'


class Dracula(_BasicScraper):
    url = 'http://draculacomic.net/'
    stripUrl = url + 'comic.php?comicID=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(r'&nbsp;<a class="archivelink" href="(.+?)">&laquo; Prev</a>')
    help = 'Index format: nnn'


class DreamKeepersPrelude(_BasicScraper):
    url = 'http://www.dreamkeeperscomic.com/Prelude.php'
    stripUrl = url + '?pg=%s'
    imageSearch = compile(r'(images/PreludeNew/.+?)"')
    prevSearch = compile(r'(Prelude.php\?pg=.+?)"')
    help = 'Index format: n'


class DresdenCodak(_BasicScraper):
    url = 'http://dresdencodak.com/'
    rurl = escape(url)
    stripUrl = None
    firstStripUrl = url + '2007/02/08/pom/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl) +
                         tagre("img", "src", r"%sm_prev2?\.png" % rurl,
                               quote=""))
    latestSearch = compile(tagre("div", "id", "preview") +
                           tagre("a", "href",
                                 r'(%s\d+/\d+/\d+/[^"]+)' % rurl))
    starter = indirectStarter


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
        compile(tagre("img", "src", r'(%smainarchive/[^"]+)' % rurl)),
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


class DungeonsAndDenizens(_WordPressScraper):
    url = 'http://dungeond.com/'
    firstStripUrl = url + '2005/08/23/08232005/'
    endOfLife = True
    prevSearch = '//a[%s]' % xpath_class('navi-prev')

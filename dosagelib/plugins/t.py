# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape, IGNORECASE
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class TheBrads(_BasicScraper):
    url = 'http://bradcolbow.com/archive/C4/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://s3\.amazonaws\.com/the_brads/the-?brads[-_][^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://bradcolbow\.com/archive/C4/[^"]+)', before="prev"))
    multipleImagesPerStrip = True
    help = 'Index format: a letter and a number'


class TheDevilsPanties(_BasicScraper):
    url = 'http://thedevilspanties.com/'
    stripUrl = url + 'archives/%s'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.thedevilspanties\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archives/\d+)', after="Previous"))
    help = 'Index format: number'


class TheNoob(_BasicScraper):
    url = 'http://www.thenoobcomic.com/index.php'
    stripUrl = url + '?pos=%s'
    imageSearch = compile(tagre("img", "src", r'(/headquarters/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?pos=\d+)', before="comic_nav_previous_button"))
    help = 'Index format: nnnn'


class TheOrderOfTheStick(_BasicScraper):
    baseurl = 'http://www.giantitp.com/'
    url = baseurl + 'comics/oots0863.html'
    stripUrl = baseurl + 'comics/oots%s.html'
    imageSearch = compile(r'<IMG src="(/comics/images/[^"]+)">')
    prevSearch = compile(r'<A href="(/comics/oots\d{4}\.html)"><IMG src="/Images/redesign/ComicNav_Back.gif"')
    help = 'Index format: n (unpadded)'
    starter = indirectStarter(baseurl, compile(r'<A href="(/comics/oots\d{4}\.html)"'))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 1)[-1][:-5]


class TheParkingLotIsFull(_BasicScraper):
    baseurl = 'http://plif.courageunfettered.com/'
    url = baseurl + 'archive/arch2002.htm'
    stripUrl = baseurl + 'archive/arch%s.htm'
    imageSearch = compile(r'<td align="center"><A TARGET=_parent HREF="(wc\d+\..+?)">')
    multipleImagesPerStrip = True
    prevSearch = compile(r'\d{4} -\s+<A HREF="(arch\d{4}\.htm)">\d{4}')
    help = 'Index format: nnn'


class TheWotch(_BasicScraper):
    url = 'http://www.thewotch.com/'
    stripUrl = url + '?date=%s'
    imageSearch = compile(r"<img.+?src='(comics/.+?)'")
    prevSearch = compile(r"<link rel='Previous' href='(/\?date=\d+-\d+-\d+)'")
    help = 'Index format: yyyy-mm-dd'


class ThisIsIndexed(_BasicScraper):
    url = 'http://thisisindexed.com/'
    rurl = escape(url)
    stripUrl = url + 'page/%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/card[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("div", "class", "nav-previous") +
                         tagre("a", "href", r'(%spage/\d+/)' % rurl))
    help = 'Index format: number'


class ThunderAndLightning(_BasicScraper):
    url = 'http://www.talcomic.com/wp/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    prevSearch = compile(tagre("a", "href", r'(%swp/[^"]+)' % rurl, after="prev"))
    imageSearch = compile(tagre("img", "src", r'(%swp/comics/[^"]+)' % rurl))
    help = 'Index format: yyyy/mm/dd/page-nn'

    @classmethod
    def starter(cls):
        return cls.url + '?latestcomic'


class TinyKittenTeeth(_BasicScraper):
    url = 'http://www.tinykittenteeth.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripname (unpadded)'


class ToonHole(_BasicScraper):
    url = 'http://www.toonhole.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/stripname'

    def shouldSkipUrl(self, url):
        return url in (self.stripUrl % "2013/03/if-game-of-thrones-was-animated",)


# XXX disallowed by robots.txt
class _TwoLumps(_BasicScraper):
    url = 'http://www.twolumps.net/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)', after="prev"))
    help = 'Index format: yyyymmdd'


class TwoTwoOneFour(_BasicScraper):
    url = 'http://www.nitrocosm.com/go/2214_classic/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://content\.nitrocosm\.com/[^"]+)', before="gallery_display"))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/)' % rurl, after="Previous"))
    help = 'Index format: n (unpadded)'


class TheWhiteboard(_BasicScraper):
    url = 'http://www.the-whiteboard.com/'
    stripUrl = url + 'auto%s.html'
    imageSearch = compile(r'<img SRC="(autotwb\d{1,4}.+?|autowb\d{1,4}.+?)">', IGNORECASE)
    prevSearch = compile(r'&nbsp<a href="(.+?)">previous</a>', IGNORECASE)
    help = 'Index format: twb or wb + n wg. twb1000'


class HMHigh(_BasicScraper):
    name = 'TheFallenAngel/HMHigh'
    baseurl = 'http://www.thefallenagel.co.uk/'
    url = baseurl + 'hmhigh/'
    rurl = escape(baseurl)
    stripUrl = url + '?id=%s'
    imageSearch = compile(r'<img src="(%shmhigh/img/comic/.+?)"' % rurl)
    prevSearch = compile(r' <a href="(%s.+?)" title=".+?">Prev</a>' % rurl)
    help = 'Index format: nnn'


class TheOuterQuarter(_BasicScraper):
    url = 'http://theouterquarter.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    imageSearch = compile(r'<img src="(%scomics/.+?)"' % rurl)
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: nnn'


class ThreePanelSoul(_BasicScraper):
    url = 'http://threepanelsoul.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class TracyAndTristan(_BasicScraper):
    url = 'http://tandt.thecomicseries.com/'
    rurl = escape(url)
    stripUrl = url + 'comics/%s'
    imageSearch = compile(tagre("img", "src", r'(%simages/comics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+)', after="prev"))
    help = 'Index format: number'

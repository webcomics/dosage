# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function
from re import compile, escape, IGNORECASE

from ..util import tagre
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from .common import _WPNaviIn, _WordPressScraper, xpath_class


class FalconTwin(_BasicScraper):
    url = 'http://www.falcontwin.com/'
    stripUrl = url + 'index.html?strip=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'"(strips/.+?)"')
    prevSearch = compile(r'"prev"><a href="(index.+?)"')
    help = 'Index format: nnn'


class Faneurysm(_WPNaviIn):
    url = 'http://hijinksensue.com/comic/think-only-tree/'
    firstStripUrl = 'http://hijinksensue.com/comic/captains-prerogative/'
    endOfLife = True


class FantasyRealms(_BasicScraper):
    url = 'http://www.fantasyrealmsonline.com/'
    stripUrl = url + 'manga/%s.php'
    imageSearch = compile(r'<img src="(\d{1,4}.\w{3,4})" width="540"', IGNORECASE)
    prevSearch = compile(r'<a href="(.+?)"><img src="../images/nav-back.gif"', IGNORECASE)
    latestSearch = compile(r'<a href="(manga/.+?)"><img src="preview.jpg"', IGNORECASE)
    help = 'Index format: nnn'
    starter = indirectStarter


class FauxPas(_ParserScraper):
    url = 'http://www.ozfoxes.net/cgi/pl-fp1.cgi'
    stripUrl = url + '?%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@name]'
    prevSearch = '//a[img[@alt="Previous"]]'
    help = 'Index format: nnn'


class FireflyCross(_WordPressScraper):
    url = 'http://www.fireflycross.pensandtales.com/'
    firstStripUrl = url + '?comic=05062002'


class FirstWorldProblems(_BasicScraper):
    url = 'http://bradcolbow.com/archive/C5/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'P10'
    imageSearch = compile(tagre("img", "src", r'(http://(?:fwpcomics\.s3\.amazonaws\.com|s3\.amazonaws\.com/fwpcomics)/s1-[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://bradcolbow\.com/archive/C5/[^"]+)', before="prev"))
    multipleImagesPerStrip = True
    help = 'Index format: a letter and a number'


class FlakyPastry(_BasicScraper):
    baseUrl = 'http://flakypastry.runningwithpencils.com/'
    url = baseUrl + 'index.php'
    stripUrl = baseUrl + 'comic.php?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back')
    help = 'Index format: nnnn'


class Flemcomics(_BasicScraper):
    url = 'http://www.flemcomics.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
                         tagre("img", "src", r'/images/previous_day\.jpg'))
    help = 'Index format: yyyymmdd'


class Flipside(_BasicScraper):
    url = 'http://flipside.keenspot.com/comic.php'
    rurl = escape(url)
    stripUrl = url + '?i=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.flipside\.keenspot\.com/comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%s\?i=\d+)' % rurl,
                               after="prev"))
    help = 'Index format: nnnn'


class FonFlatter(_ParserScraper):
    url = 'https://www.fonflatter.de/'
    stripUrl = url + '%s/'
    firstStripUrl = url + '2005/09/20/01-begegnung-mit-batman/'
    lang = 'de'
    imageSearch = r'//img[re:test(@src, "/fred_\d+")]'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy/mm/dd/number-stripname'

    def shouldSkipUrl(self, url, data):
        return url in (
            self.stripUrl % "2006/11/30/adventskalender",
            self.stripUrl % "2006/09/21/danke",
            self.stripUrl % "2006/08/23/zgf-zuweilen-gestellte-fragen",
            self.stripUrl % "2005/10/19/naq-never-asked-questions",
        )


class ForLackOfABetterComic(_BasicScraper):
    url = 'http://forlackofabettercomic.com/'
    rurl = r'http://(?:www\.)?forlackofabettercomic\.com/'
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%simg/comic/\d+[^"]+)' % rurl, after="comicimg"))
    prevSearch = compile(tagre("a", "href", r'(%s\?id\=\d+)' % rurl) + r'Prev')
    help = 'Index format: number'


class Fragile(_ParserScraper):
    url = 'http://www.fragilestory.com/'
    imageSearch = '//div[@id="comic_strip"]/a[@class="nobg"]/img'
    prevSearch = '//div[@id="nav_comic_a"]/a[2]'
    firstStripUrl = url + 'strips/chapter_01'


class FredoAndPidjin(_ParserScraper):
    url = 'http://www.pidjin.net/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/02/19/goofy-monday'
    imageSearch = '//div[%s]//img' % xpath_class("episode")
    multipleImagesPerStrip = True
    prevSearch = '//span[%s]/a' % xpath_class("prev")
    latestSearch = '//section[%s]//a' % xpath_class("latest")
    starter = indirectStarter


class Freefall(_BasicScraper):
    url = 'http://freefall.purrsia.com/default.htm'
    stripUrl = 'http://freefall.purrsia.com/ff%s/fc%s.htm'
    imageSearch = compile(r'<img src="(/ff\d+/.+?.\w{3,4})"')
    prevSearch = compile(r'<A HREF="(/ff\d+/.+?.htm)">Previous</A>')
    help = 'Index format: nnnn/nnnnn'


class FullFrontalNerdity(_BasicScraper):
    url = 'http://ffn.nodwick.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '6'
    imageSearch = compile(tagre("img", "src", r'(%sffnstrips/\d+-\d+-\d+\.[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: number'


class FunInJammies(_BasicScraper):
    url = 'http://www.funinjammies.com/'
    stripUrl = url + 'comic.php?issue=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'(/comic.php.+?)" id.+?prev')
    help = 'Index format: n (unpadded)'

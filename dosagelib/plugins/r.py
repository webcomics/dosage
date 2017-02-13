# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile
from six.moves.urllib.parse import urljoin

from ..helpers import xpath_class
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import _WordPressScraper


class RadioactivePanda(_BasicScraper):
    url = 'http://www.radioactivepanda.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(r'<img src="(/Assets/.*?)".+?"comicimg"')
    prevSearch = compile(r'<a href="(/comic/.*?)".+?previous_btn')
    help = 'Index format: n (no padding)'


class RalfTheDestroyer(_WordPressScraper):
    url = 'http://ralfthedestroyer.com/'


class RaynaOnTheRiver(_WordPressScraper):
    url = 'http://www.catomix.com/rayna/'
    firstStripUrl = url + 'archives/comic/teaser-poster'


class RealLife(_WordPressScraper):
    url = 'http://reallifecomics.com/'
    stripUrl = url + 'comic.php?comic=%s'
    firstStripUrl = stripUrl % 'title-1'
    help = 'Index format: monthname-dd-yyyy'

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


class RedString(_BasicScraper):
    url = 'http://www.redstring.strawberrycomics.com/'
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '434'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/index\.php\?id=\d+)', after="prev"))
    help = 'Index format: nnn'


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

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from ..helpers import bounceStarter
from .common import _WordPressScraper, xpath_class


class ZapComic(_ParserScraper):
    url = 'http://www.zapcomic.com/'
    css = True
    imageSearch = 'img.comic-item'
    prevSearch = 'a.previous-comic-link'


class Zapiro(_BasicScraper):
    url = 'http://www.mg.co.za/zapiro/'
    starter = bounceStarter
    stripUrl = 'http://mg.co.za/cartoon/%s'
    firstStripUrl = stripUrl % 'zapiro_681'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.mg\.co\.za/crop/content/cartoons/[^"]+)'))
    prevSearch = compile(tagre("li", "class", r'nav_older') +
                         tagre("a", "href",
                               r'(http://mg\.co\.za/cartoon/[^"]+)'))
    nextSearch = compile(tagre("li", "class", r'nav_older') +
                         tagre("a", "href",
                               r'(http://mg\.co\.za/cartoon/[^"]+)'))
    help = 'Index format: yyyy-mm-dd-stripname'

    def namer(self, image_url, page_url):
        name = image_url.split('/')[-3]
        return name


class ZenPencils(_WordPressScraper):
    url = 'http://zenpencils.com/'
    multipleImagesPerStrip = True
    firstStripUrl = url + 'comic/1-ralph-waldo-emerson-make-them-cry/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')


class ZombieHunters(_BasicScraper):
    url = 'http://www.thezombiehunters.com/'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/istrip_files/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "id", "prevcomic"))
    help = 'Index format: n(unpadded)'


class Zwarwald(_BasicScraper):
    url = "http://www.zwarwald.de/"
    rurl = escape(url)
    stripUrl = url + 'index.php/page/%s/'
    # anything before page 495 seems to be flash
    firstStripUrl = stripUrl % '495'
    lang = 'de'
    imageSearch = (
        compile(tagre("img", "src", r'(%simages/\d+/\d+/[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(http://wp1163540\.wp190\.webpack\.hosteurope\.de/wordpress/images/\d+/\d+/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php/page/\d+/)' % rurl) +
                         tagre("img", "src",
                               r'http://zwarwald\.de/images/prev\.jpg',
                               quote="'"))
    help = 'Index format: number'

    def shouldSkipUrl(self, url, data):
        """Some pages have flash content."""
        return url in (
            self.stripUrl % "112",
            self.stripUrl % "222",
            self.stripUrl % "223",
            self.stripUrl % "246",
            self.stripUrl % "368",
            self.stripUrl % '495',
        )

    def namer(self, image_url, page_url):
        prefix, year, month, name = image_url.rsplit('/', 3)
        return "%s_%s_%s" % (year, month, name)

# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
from re import compile, escape

from ..scraper import BasicScraper, ParserScraper
from ..util import tagre
from ..helpers import bounceStarter, joinPathPartsNamer
from .common import WordPressNavi


class ZapComic(ParserScraper):
    url = 'http://www.zapcomic.com/'
    css = True
    imageSearch = 'img.comic-item'
    prevSearch = 'a.previous-comic-link'


class Zapiro(ParserScraper):
    url = 'http://mg.co.za/zapiro/'
    starter = bounceStarter
    imageSearch = '//div[@id="cartoon"]/img'
    prevSearch = '//a[d:class("left")]'
    nextSearch = '//a[d:class("right")]'
    namer = joinPathPartsNamer((-1,), ())


class ZenPencils(WordPressNavi):
    url = 'https://web.archive.org/web/20200723091741/https://zenpencils.com/'
    multipleImagesPerStrip = True
    firstStripUrl = url + 'comic/1-ralph-waldo-emerson-make-them-cry/'
    starter = bounceStarter
    prevSearch = '//a[d:class("navi-prev")]'
    nextSearch = '//a[d:class("navi-next")]'
    endOfLife = True


class ZombieHunters(BasicScraper):
    url = 'http://www.thezombiehunters.com/'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/istrip_files/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "id", "prevcomic"))
    help = 'Index format: n(unpadded)'


class Zwarwald(BasicScraper):
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
    namer = joinPathPartsNamer((), (-3, -2, -1))
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

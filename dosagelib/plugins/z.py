# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..util import tagre
from ..helpers import bounceStarter


class ZapComic(_BasicScraper):
    url = 'http://www.zapcomic.com/'
    rurl = escape(url[:-1]) # without trailing slash
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%s\?comic_object\=\d+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s/[^"]+)' % rurl, after="previous-comic-link"))
    help = 'Index format: yyyy/mm/nnn-stripname'


class Zapiro(_BasicScraper):
    url = 'http://www.mg.co.za/zapiro/'
    starter = bounceStarter(url,
      compile(tagre("li", "class", r'nav_older') +
              tagre("a", "href", r'(http://mg\.co\.za/cartoon/[^"]+)')))
    stripUrl = 'http://mg.co.za/cartoon/%s'
    firstStripUrl = stripUrl % 'zapiro_681'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.mg\.co\.za/crop/content/cartoons/[^"]+)'))
    prevSearch = compile(tagre("li", "class", r'nav_older') +
        tagre("a", "href", r'(http://mg\.co\.za/cartoon/[^"]+)'))
    help = 'Index format: yyyy-mm-dd-stripname'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        name = imageUrl.split('/')[-3]
        return name


class ZebraGirl(_BasicScraper):
    url = 'http://www.zebragirl.net/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2000-05-06'
    imageSearch = compile(tagre("img", "src", r"(comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("link", "href", r"(/\?date=[^']+)", quote="'", before='Previous'))
    help = 'Index format: yyyy-mm-dd'


class ZenPencils(_BasicScraper):
    url = 'http://zenpencils.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '1-ralph-waldo-emerson-make-them-cry'
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+/)' % rurl, after="navi-prev"))
    imageSearch = compile(tagre("img", "src", r'(http://zenpencils\.com/comics/\d+-\d+-\d+[^"]+)'))
    help = 'Index format: num-stripname'
    description = u'Inspirational quotes from famous people adapted into cartoons.'


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
        tagre("img", "src", r'http://zwarwald\.de/images/prev\.jpg', quote="'"))
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

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        prefix, year, month, name = imageUrl.rsplit('/', 3)
        return "%s_%s_%s" % (year, month, name)

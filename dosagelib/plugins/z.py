# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre
from ..helpers import bounceStarter


class ZapComic(_BasicScraper):
    url = 'http://www.zapcomic.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.zapcomic\.com\?comic_object=\d+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.zapcomic\.com/[^"]+)', after="previous-comic-link"))
    help = 'Index format: yyyy/mm/nnn-stripname'


class Zapiro(_BasicScraper):
    url = 'http://www.mg.co.za/zapiro/'
    starter = bounceStarter(url,
      compile(tagre("a", "href", r'(http://mg\.co\.za/cartoon/[^"]+)')+"Newer"))
    stripUrl = 'http://mg.co.za/cartoon/%s'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.mg\.co\.za/crop/content/cartoons/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://mg\.co\.za/cartoon/[^"]+)')+"Older")
    help = 'Index format: yyyy-mm-dd-stripname'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        name = imageUrl.split('/')[-3]
        return name


class ZebraGirl(_BasicScraper):
    url = 'http://www.zebragirl.net/'
    stripUrl = url + '?date=%s'
    imageSearch = compile(tagre("img", "src", r"(comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("link", "href", r"(/\?date=[^']+)", quote="'", before='Previous'))
    help = 'Index format: yyyy-mm-dd'


class ZombieHunters(_BasicScraper):
    url = 'http://www.thezombiehunters.com/'
    stripUrl = url + '?strip_id=%s'
    imageSearch = compile(tagre("img", "src", r'(/istrip_files/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "id", "prevcomic"))
    help = 'Index format: n(unpadded)'


class Zwarwald(_BasicScraper):
    url = "http://www.zwarwald.de/"
    stripUrl = url + 'index.php/page/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.zwarwald\.de/images/\d+/\d+/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.zwarwald\.de/index\.php/page/\d+/)') +
        tagre("img", "src", r'http://zwarwald\.de/images/prev\.jpg', quote="'"))
    help = 'Index format: number'
    waitSeconds = 1

    def shouldSkipUrl(self, url):
        return url in (self.stripUrl % "112",)

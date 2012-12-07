# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre
from ..helpers import bounceStarter


class ZapComic(_BasicScraper):
    latestUrl = 'http://www.zapcomic.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.zapcomic\.com\?comic_object=\d+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.zapcomic\.com/[^"]+)', after="previous-comic-link"))
    help = 'Index format: yyyy/mm/nnn-stripname'


class Zapiro(_BasicScraper):
    baseUrl = 'http://www.mg.co.za/zapiro/'
    starter = bounceStarter(baseUrl,
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
    latestUrl = 'http://www.zebragirl.net/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(tagre("img", "src", r"(comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("link", "href", r"(/\?date=[^']+)", quote="'", before='Previous'))
    help = 'Index format: yyyy-mm-dd'


class ZombieHunters(_BasicScraper):
    latestUrl = 'http://www.thezombiehunters.com/'
    stripUrl = latestUrl + '?strip_id=%s'
    imageSearch = compile(tagre("img", "src", r'(/istrip_files/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "id", "prevcomic"))
    help = 'Index format: n(unpadded)'

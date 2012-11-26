# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre
from ..helpers import bounceStarter


class Zapiro(_BasicScraper):
    baseUrl = 'http://www.mg.co.za/zapiro/'
    starter = bounceStarter(baseUrl,
      compile(tagre("a", "href", r'(http://mg\.co\.za/cartoon/[^"]+)')+"Newer"))
    stripUrl = 'http://mg.co.za/cartoon/%s'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.mg\.co\.za/crop/content/cartoons/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://mg\.co\.za/cartoon/[^"]+)')+"Older")
    help = 'Index format: yyyy-mm-dd-stripname'


class ZombieHunters(_BasicScraper):
    latestUrl = 'http://www.thezombiehunters.com/'
    stripUrl = latestUrl + '?strip_id=%s'
    imageSearch = compile(tagre("img", "src", r'(/istrip_files/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "id", "prevcomic"))
    help = 'Index format: n(unpadded)'

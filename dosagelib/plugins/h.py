# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre


class HorribleVille(_BasicScraper):
    latestUrl = 'http://horribleville.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/[^"]+)') + tagre("img", "src", r'/images/previous\.png'))
    help = 'Index format: yyyymmdd'

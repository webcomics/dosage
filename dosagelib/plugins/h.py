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


class HelpDesk(_BasicScraper):
    latestUrl = 'https://www.eviscerati.org/comics?page=78'
    stripUrl = 'https://www.eviscerati.org/comics?page=%s'
    imageSearch = compile(tagre("img", "src", r'(https://www\.eviscerati\.org/files/comics/[^"]+)'))
    prevSearch = compile(tagre("li", "class", r'pager-previous[^"]+') + tagre("a", "href", r'(/comics\?page=%d+)'))
    help = 'Index format: n'


# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class LasLindas(_BasicScraper):
    url = 'http://laslindas.katbox.net/'
    stripUrl = url + 'archive/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://laslindas\.katbox\.net/wp-content/webcomic/las-lindas/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://laslindas\.katbox\.net/archive/[^"]+)', after="previous"))
    help = 'Index format: stripname'


class Lint(_BasicScraper):
    url = 'http://www.purnicellin.com/lint/'
    stripUrl = url + '%s'
    imageSearch = compile(r'<img src="(http://www.purnicellin.com/lint/comics/.+?)"')
    prevSearch = compile(r'\| <a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/num-name'


class LookingForGroup(_BasicScraper):
    url = 'http://www.lfgcomic.com/'
    stripUrl = url + 'page/%s/'
    imageSearch = compile(tagre("meta", "content", r'(http://cdn\.lfgcomic\.com/wp-content/uploads/[^"]+)', before="og:image"))
    prevSearch = compile(tagre("a", "href", r'(http://www\.lfgcomic\.com/page/\d+/)', after="navtop-prev"))
    starter = indirectStarter(url, compile(tagre("a", "href", r'(http://www\.lfgcomic\.com/page/\d+/)', after="feature-previous")))
    nameSearch = compile(r'/page/(\d+)/')
    help = 'Index format: nnn'

    def namer(self, imageUrl, pageUrl):
        return self.nameSearch.search(pageUrl).group(1)


class LittleGamers(_BasicScraper):
    url = 'http://www.little-gamers.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://little-gamers\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.little-gamers.com/[^"]+)', before="comic-nav-prev-link"))
    help = 'Index format: yyyy/mm/dd/name'


class LeastICouldDo(_BasicScraper):
    url = 'http://leasticoulddo.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.leasticoulddo\.com/wp-content/uploads/\d+/\d+/\d{8}\.\w{1,4})'))
    prevSearch = compile(r'<a href="(/comic/\d{8})">Previous</a>')
    help = 'Index format: yyyymmdd'

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class LasLindas(_BasicScraper):
    latestUrl = 'http://laslindas.katbox.net/'
    stripUrl = latestUrl + 'archive/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://laslindas\.katbox\.net/wp-content/webcomic/las-lindas/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://laslindas\.katbox\.net/archive/[^"]+)', after="previous"))
    help = 'Index format: stripname'


class Lint(_BasicScraper):
    latestUrl = 'http://www.purnicellin.com/lint/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'<img src="(http://www.purnicellin.com/lint/comics/.+?)"')
    prevSearch = compile(r'\| <a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/num-name'


class LookingForGroup(_BasicScraper):
    latestUrl = 'http://www.lfgcomic.com/page/latest'
    stripUrl = 'http://www.lfgcomic.com/page/%s'
    imageSearch = compile(r'<img src="(http://newcdn.lfgcomic.com/uploads/comics/.+?)"')
    prevSearch = compile(r'<a href="(/page/\d+)" id="navtop-prev"')
    starter = indirectStarter('http://www.lfgcomic.com/', compile(r'<a href="(/page/\d+)" id="feature-preview"'))
    nameSearch = compile(r'/page/(\d+)')
    help = 'Index format: nnn'

    def namer(self, imageUrl, pageUrl):
        return self.nameSearch.search(pageUrl).group(1)


class LittleGamers(_BasicScraper):
    latestUrl = 'http://www.little-gamers.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://little-gamers\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.little-gamers.com/[^"]+)', before="comic-nav-prev-link"))
    help = 'Index format: yyyy/mm/dd/name'


class LeastICouldDo(_BasicScraper):
    latestUrl = 'http://leasticoulddo.com/'
    stripUrl = latestUrl + 'comic/%s'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.leasticoulddo\.com/wp-content/uploads/\d+/\d+/\d{8}\.\w{1,4})'))
    prevSearch = compile(r'<a href="(/comic/\d{8})">Previous</a>')
    help = 'Index format: yyyymmdd'

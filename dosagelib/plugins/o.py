# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class OctopusPie(_BasicScraper):
    url = 'http://www.octopuspie.com/'
    starter = indirectStarter(url,
        compile(tagre("a", "href", r'(http://www\.octopuspie\.com/[^"]+)') +
                tagre("img", "src", r'http://www\.octopuspie\.com/junk/latest\.png')))
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.octopuspie\.com/strippy/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.octopuspie\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy-mm-dd/nnn-strip-name'


class OddFish(_BasicScraper):
    url = 'http://www.odd-fish.net/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.odd-fish\.net/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.odd-fish\.net/[^"]+)', after="navi-prev"))
    help = 'Index format: stripname'


class OmakeTheater(_BasicScraper):
    url = 'http://omaketheater.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(tagre("img", "src", r'(http://media\.omaketheater\.com/4koma/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://omaketheater\.com/comic/\d+/)', after="prev"))
    starter = indirectStarter(url,
        compile(tagre("a", "href", r'(http://omaketheater\.com/comic/\d+/)')))
    help = 'Index format: number (unpadded)'


class OnTheEdge(_BasicScraper):
    url = 'http://ontheedgecomics.com/'
    stripUrl = 'http://ontheedgecomics.com/comic/%s'
    imageSearch = compile(r'<img src="(http://ontheedgecomics.com/comics/.+?)"')
    prevSearch = compile(r'<a href="([^"]+)" rel="prev">')
    help = 'Index format: nnn (unpadded)'


class OneQuestion(_BasicScraper):
    url = 'http://onequestioncomic.com/'
    stripUrl = url + 'comic.php?strip_id=%s'
    imageSearch = compile(tagre("img", "src", r'(istrip_files/strips/\d+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(comic\.php\?strip_id=\d+)') + tagre("img", "src", r'img/arrow_prev\.jpg'))
    help = 'Index format: n (unpadded)'


class OurHomePlanet(_BasicScraper):
    url = 'http://gdk.gd-kun.net/'
    stripUrl = url + '%s.html'
    imageSearch = compile(r'<img src="(pages/comic.+?)"')
    prevSearch = compile(r'coords="50,18,95,65".+?href="(.+?\.html)".+?alt=')
    help = 'Index format: n (unpadded)'


class OkCancel(_BasicScraper):
    url = 'http://okcancel.com/'
    stripUrl = url + 'comic/%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://okcancel\.com/strips/okcancel\d{8}\.gif)'))
    prevSearch = compile(tagre("div", "class", "previous") + tagre("a", "href", r'(http://okcancel\.com/comic/\d{1,4}\.html)'))
    starter = indirectStarter(url, prevSearch)
    help = 'Index format: yyyymmdd'


class Oglaf(_BasicScraper):
    url = 'http://oglaf.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(/media/comic/[^"]+)', before="strip"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("div", "id", "pvs"))
    help = 'Index format: stripname/nn'


class OverCompensating(_BasicScraper):
    url = 'http://www.overcompensating.com/'
    stripUrl = url + 'posts/%s.html'
    imageSearch = compile(r'<img src="(/comics/.+?)"')
    prevSearch = compile(r'"><a href="(.+?)"[^>]+?>&nbsp;\<\- &nbsp;</a>')
    help = 'Index format: yyyymmdd'

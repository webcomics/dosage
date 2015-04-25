# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..scraper import _ParserScraper
from ..helpers import bounceStarter
from ..util import tagre


class RadioactivePanda(_BasicScraper):
    url = 'http://www.radioactivepanda.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(r'<img src="(/Assets/.*?)".+?"comicimg"')
    prevSearch = compile(r'<a href="(/comic/.*?)".+?previous_btn')
    help = 'Index format: n (no padding)'

class RalfTheDestroyer(_ParserScraper):
    url = 'http://ralfthedestroyer.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = '#comic-1 > a:first-child img'
    prevSearch = 'td.comic_navi_left > a:nth-of-type(2)'
    help = 'Index format: stripname'


class RealLife(_BasicScraper):
    url = 'http://reallifecomics.com/'
    rurl = escape(url)
    stripUrl = url + 'comic.php?comic=%s'
    firstStripUrl = stripUrl % '991115'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'((?:%s)?comic\.php\?comic=[^"]+)' % rurl, after="nav-previous"))
    help = 'Index format: monthname-dd-yyyy)'


class RealmOfAtland(_BasicScraper):
    url = 'http://www.realmofatland.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '1'
    prevSearch = compile(tagre("a", "href", r'(\?p=\d+)', after="cg_back"))
    imageSearch = compile(tagre("img", "src", r'(images/strips/atland\d+.[^"]+)'))
    help = 'Index format: nnn'


class RedMeat(_BasicScraper):
    baseUrl = 'http://www.redmeat.com/redmeat/'
    url = baseUrl + 'current/index.html'
    starter = bounceStarter(url,
        compile(tagre("a", "href", r'(http://www\.redmeat\.com/[^"]*)', after="next")))
    stripUrl = baseUrl + '%s/index.html'
    firstStripUrl = stripUrl % '1996-06-10'
    imageSearch = compile(tagre("img", "src", r'(http://www\.redmeat\.com/imager/b/redmeat/[^"]*\.png)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.redmeat\.com/[^"]*)', after="prev"))
    help = 'Index format: yyyy-mm-dd'


class RedsPlanet(_BasicScraper):
    url = 'http://www.redsplanet.com/comic/'
    rurl = escape(url)
    stripUrl = url + 'rp/%s/'
    firstStripUrl = stripUrl % 'pro/prologue-01'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+_[^"/]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%srp/[^"/]+/[^"/]+/)' % rurl))
    help = 'Index format: chapter/stripname'


class RedString(_BasicScraper):
    url = 'http://www.redstring.strawberrycomics.com/'
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '434'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/index\.php\?id=\d+)', after="prev"))
    help = 'Index format: nnn'


class RomanticallyApocalyptic(_BasicScraper):
    url = 'http://romanticallyapocalyptic.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%sart/\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+[^"]+)' % rurl)+"\s*"+tagre('span', 'class', 'spritePrevious'))
    help = 'Index format: n'
    adult = True


class Roza(_BasicScraper):
    url = 'http://www.junglestudio.com/roza/index.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2007-05-01'
    imageSearch = compile(r'<img src="(pages/.+?)"')
    prevSearch = compile(r'<a href="(index.php\?date=.+?)">[^>].+?navtable_01.gif')
    help = 'Index format: yyyy-mm-dd'


class Ruthe(_BasicScraper):
    url = 'http://ruthe.de/'
    stripUrl = url + 'index.php?pic=%s&sort=datum&order=ASC'
    firstStripUrl = stripUrl % '1'
    lang = 'de'
    imageSearch = compile(tagre("img", "src", r'(/?cartoons/strip_\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/cartoon/\d+/datum/asc/)')+'vorheriger')
    help = 'Index format: number'

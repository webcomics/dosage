# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..scraper import _BasicScraper


class HappyMedium(_BasicScraper):
    latestUrl = 'http://happymedium.fast-bee.com/'
    stripUrl = 'http://happymedium.fast-bee.com/%s'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'com(/.+?)".+?"prev">&#9668')
    help = 'Index format: yyyy/mm/chapter-n-page-n'



class Heliothaumic(_BasicScraper):
    latestUrl = 'http://thaumic.net/'
    stripUrl = 'http://thaumic.net/%s'
    imageSearch = compile(r'<img src="(http://thaumic.net/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://thaumic.net/.+?)">')
    help = 'Index format: yyyy/mm/dd/n(unpadded)-comicname'



class Housd(_BasicScraper):
    latestUrl = 'http://housd.net/archive_page.php?comicID=1284'
    stripUrl = 'http://housd.net/archive_page.php?comicID=%s'
    imageSearch = compile(r'"(.+?/comics/.+?)"')
    prevSearch = compile(r'"(h.+?comicID=.+?)".+?prev')
    help = 'Index format: nnnn'



class HateSong(_BasicScraper):
    latestUrl = 'http://hatesong.com/'
    stripUrl = 'http://hatesong.com/%s/'
    imageSearch = compile(r'src="(http://www.hatesong.com/strips/.+?)"')
    prevSearch = compile(r'<div class="headernav"><a href="(http://hatesong.com/\d{4}/\d{2}/\d{2})')
    help = 'Index format: yyyy/mm/dd'



class HorribleVille(_BasicScraper):
    latestUrl = 'http://horribleville.com/d/20090517.html'
    stripUrl = 'http://horribleville.com/d/%s.html'
    imageSearch = compile(r'src="(/comics/.+?)"')
    prevSearch = compile(r'(\d+\.html)"><img[^>]+?src="/images/previous_day.png"')
    help = 'Index format: yyyy/mm/dd'



class HelpDesk(_BasicScraper):
    latestUrl = 'http://www.ubersoft.net/'
    stripUrl = 'http://www.ubersoft.net/comic/hd/%s/%s/%s'
    imageSearch = compile(r'src="(http://www.ubersoft.net/files/comics/hd/hd\d{8}.png)')
    prevSearch = compile(r'<a href="(/comic/.+?)">(.+?)previous</a>')
    help = 'Index format: yyyy/mm/name'



class HardGraft(_BasicScraper):
    latestUrl = 'http://hard-graft.net/'
    stripUrl = 'http://hard-graft.net/?p=%s'
    imageSearch = compile(r'<img src="(http://hard-graft.net/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)"')
    help = 'Index format: nnn'

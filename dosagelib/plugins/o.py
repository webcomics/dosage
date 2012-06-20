# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE

from ..helpers import _BasicScraper, indirectStarter


class OctopusPie(_BasicScraper):
    starter = indirectStarter('http://www.octopuspie.com/2007-05-14/001-pea-wiggle/',
                              compile(r'<a href="(http://www.octopuspie.com/.+?)"><b>latest comic</b>', IGNORECASE))
    imageUrl = 'http://www.octopuspie.com/%s'
    imageSearch = compile(r'<img src="(http://www.octopuspie.com/strippy/.+?)"')
    prevSearch = compile(r'<link rel=\'prev\'[^>]+?href=\'(http://www.octopuspie.com/.+?)\'')
    help = 'Index format: yyyy-mm-dd/nnn-strip-name'



class OddFish(_BasicScraper):
    latestUrl = 'http://www.odd-fish.net/'
    imageUrl = 'http://www.odd-fish.net/viewing.php?&comic_id=%s'
    imageSearch = compile(r'<img src="(images/\d{1,4}.\w{3,4})" ')
    prevSearch = compile(r'<a href="(.+?)"><img src="http://www.odd-fishing.net/i/older.gif" ')
    help = 'Index format: n (unpadded)'



class OhMyGods(_BasicScraper):
    latestUrl = 'http://ohmygods.co.uk/'
    imageUrl = 'http://ohmygods.co.uk/strips/%s'
    imageSearch = compile(r'<p class="omgs-strip"><img src="(/system/files/.+?)"')
    prevSearch = compile(r'<li class="custom_pager_prev"><a href="(/strips/.+?)"')
    help = 'Index format: yyyy-mm-dd'



class OnTheEdge(_BasicScraper):
    latestUrl = 'http://www.ontheedgecomics.com/'
    imageUrl = 'http://ontheedgecomics.com/comic/ote%s'
    imageSearch = compile(r'<img src="(http://ontheedgecomics.com/comics/.+?)"')
    prevSearch = compile(r'<a href="([^"]+)" rel="prev">')
    help = 'Index format: nnn (unpadded)'



class OneQuestion(_BasicScraper):
    latestUrl = 'http://onequestioncomic.com/'
    imageUrl = 'http://onequestioncomic.com/comics/%s/'
    imageSearch = compile(r'(istrip_files.+?)"')
    prevSearch = compile(r'First.+?"(comic.php.+?)".+?previous.png')
    help = 'Index format: n (unpadded)'



class OurHomePlanet(_BasicScraper):
    latestUrl = 'http://gdk.gd-kun.net/'
    imageUrl = 'http://gdk.gd-kun.net/%s.html'
    imageSearch = compile(r'<img src="(pages/comic.+?)"')
    prevSearch = compile(r'coords="50,18,95,65".+?href="(.+?\.html)".+?alt=')
    help = 'Index format: n (unpadded)'


class OkCancel(_BasicScraper):
    imageUrl = 'http://www.ok-cancel.com/comic/%s.html'
    imageSearch = compile(r'src="(http://www.ok-cancel.com/strips/okcancel\d{8}.gif)"', IGNORECASE)
    prevSearch = compile(r'<div class="previous"><a href="(http://www.ok-cancel.com/comic/\d{1,4}.html)">', IGNORECASE)
    starter = indirectStarter('http://www.ok-cancel.com/', prevSearch)
    help = 'Index format: yyyymmdd'



class Oglaf(_BasicScraper):
    starter = indirectStarter('http://oglaf.com/',
                              compile(r'<a href="(.+?)"><img src="over18.gif"', IGNORECASE))
    imageUrl = 'http://oglaf.com/%s.html'
    imageSearch = compile(r'/><img src="(.+?)"[^>]+?width="760" height="596"', IGNORECASE)
    prevSearch = compile(r'<a href="(.+?)"[^>]+?><img src="prev.gif"', IGNORECASE)
    help = 'Index format: nn'



class OverCompensating(_BasicScraper):
    latestUrl = 'http://www.overcompensating.com/'
    imageUrl = 'http://www.overcompensating.com/posts/%s.html'
    imageSearch = compile(r'<img src="(/comics/.+?)"')
    prevSearch = compile(r'"><a href="(.+?)"[^>]+?>&nbsp;\<\- &nbsp;</a>')
    help = 'Index format: yyyymmdd'

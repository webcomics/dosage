# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..scraper import _BasicScraper
from ..helpers import indirectStarter


class LasLindas(_BasicScraper):
    latestUrl = 'http://www.katbox.net/laslindas/'
    stripUrl = 'http://www.katbox.net/laslindas/index.php?strip_id=%s'
    imageSearch = compile(r'"(istrip_files/strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><[^>]+?alt="Back"')
    help = 'Index format: n (unpadded)'



class LastBlood(_BasicScraper):
    latestUrl = 'http://www.lastblood.net/main/'
    stripUrl = 'http://www.lastblood.net/main/%s'
    imageSearch = compile(r'(/comicfolder/.+?)" alt')
    prevSearch = compile(r'Previous Comic:</small><br />&laquo; <a href="(.+?)">')
    help = 'Index format: yyyy/mm/dd/(page number and name)'



class LesbianPiratesFromOuterSpace(_BasicScraper):
    latestUrl = 'http://rosalarian.com/lesbianpirates/'
    stripUrl = 'http://rosalarian.com/lesbianpirates/?p=%s'
    imageSearch = compile(r'(/lesbianpirates/comics/.+?)"')
    prevSearch = compile(r'/(\?p=.+?)">&laquo')
    help = 'Index format: n'



class Lint(_BasicScraper):
    latestUrl = 'http://www.purnicellin.com/lint/'
    stripUrl = 'http://www.purnicellin.com/lint/%s'
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



class Loserz(_BasicScraper):
    latestUrl = 'http://bukucomics.com/loserz/'
    stripUrl = 'http://bukucomics.com/loserz/go/%s'
    imageSearch = compile(r'<img src="(http://bukucomics.com/loserz/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"> &nbsp;&lt;&nbsp;')
    help = 'Index format: n (unpadded)'



class LittleGamers(_BasicScraper):
    latestUrl = 'http://www.little-gamers.com/'
    stripUrl = 'http://www.little-gamers.com/%s'
    imageSearch = compile(r'<img src="(http://www.little-gamers.com/comics/[^"]+)"')
    prevSearch = compile(r'href="(.+?)"><img id="comic-nav-prev"')
    help = 'Index format: yyyy/mm/dd/name'



class LegoRobot(_BasicScraper):
    latestUrl = 'http://www.legorobotcomics.com/'
    stripUrl = 'http://www.legorobotcomics.com/?id=%s'
    imageSearch = compile(r'id="the_comic" src="(comics/.+?)"')
    prevSearch = compile(r'(\?id=\d+)"><img src="images/back.png"')
    help = 'Index format: nnnn'



class LeastICouldDo(_BasicScraper):
    latestUrl = 'http://www.leasticoulddo.com/'
    stripUrl = 'http://www.leasticoulddo.com/comic/%s'
    imageSearch = compile(r'<img src="(http://cdn.leasticoulddo.com/comics/\d{8}.\w{1,4})" />')
    prevSearch = compile(r'<a href="(/comic/\d{8})">Previous</a>')
    help = 'Index format: yyyymmdd'

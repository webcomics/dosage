# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE, MULTILINE

from ..helpers import _BasicScraper, indirectStarter


class FalconTwin(_BasicScraper):
    latestUrl = 'http://www.falcontwin.com/'
    imageUrl = 'http://www.falcontwin.com/index.html?strip=%s'
    imageSearch = compile(r'"(strips/.+?)"')
    prevSearch = compile(r'"prev"><a href="(index.+?)"')
    help = 'Index format: nnn'


class FauxPas(_BasicScraper):
    latestUrl = 'http://www.ozfoxes.net/cgi/pl-fp1.cgi'
    imageUrl = 'http://www.ozfoxes.net/cgi/pl-fp1.cgi?%s'
    imageSearch = compile(r'<img .*src="(.*fp/fp.*(png|jpg|gif))"')
    prevSearch = compile(r'<a href="(pl-fp1\.cgi\?\d+)">Previous Strip')
    help = 'Index format: nnn'


class FeyWinds(_BasicScraper):
    imageUrl = 'http://kitsune.rydia.net/comic/page.php?id=%s'
    imageSearch = compile(r"(../comic/pages//.+?)'")
    prevSearch = compile(r"(page.php\?id=.+?)'.+?navprevious.png")
    help = 'Index format: n (unpadded)'
    starter = indirectStarter('http://kitsune.rydia.net/index.html',
                              compile(r'(comic/page.php\?id.+?)"'))



class FightCastOrEvade(_BasicScraper):
    latestUrl = 'http://www.fightcastorevade.net/'
    imageUrl = 'http://www.fightcastorevade.net/d/%s'
    imageSearch = compile(r'<img src="(http://www.fightcastorevade.net/comics/.+?)"')
    prevSearch = compile(r'"(.+?/d/.+?)".+?previous')
    help = 'Index format: yyyymmdd.html'



class FilibusterCartoons(_BasicScraper):
    latestUrl = 'http://www.filibustercartoons.com/'
    imageUrl = 'http://www.filibustercartoons.com/index.php/%s'
    imageSearch = compile(r'<img src="(http://www.filibustercartoons.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img src=\'(.+?/arrow-left.gif)\'')
    help = 'Index format: yyyy/mm/dd/name'



class FlakyPastry(_BasicScraper):
    latestUrl = 'http://flakypastry.runningwithpencils.com/index.php'
    imageUrl = 'http://flakypastry.runningwithpencils.com/comic.php\?strip_id=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back')
    help = 'Index format: nnnn'


class Flipside(_BasicScraper):
    latestUrl = 'http://www.flipsidecomics.com/comic.php'
    imageUrl = 'http://www.flipsidecomics.com/comic.php?i=%s'
    imageSearch = compile(r'<IMG SRC="(comic/.+?)"')
    prevSearch = compile(r'<A HREF="(comic.php\?i=\d+?)">&lt')
    help = 'Index format: nnnn'


class Footloose(_BasicScraper):
    latestUrl = 'http://footloosecomic.com/footloose/today.php'
    imageUrl = 'http://footloosecomic.com/footloose/pages.php?page=%s'
    imageSearch = compile(r'<img src="/footloose/(.+?)"')
    prevSearch = compile(r'(?:first.+?[^>]).+?(/footloose/.+?)".+?(?:prev)')
#    prevSearch = compile(r'(?:first.+?[^>]).+?(/footloose/.+?html).+?(?:prev|Prev)')
    help = 'Index format: n (unpadded)'



class FragileGravity(_BasicScraper):
    latestUrl = 'http://www.fragilegravity.com/'
    imageUrl = 'http://www.fragilegravity.com/core.php?archive=%s'
    imageSearch = compile(r'<IMG SRC="(strips/.+?)"')
    prevSearch = compile(r'<A HREF="(.+?)"\nonMouseover="window.status=\'Previous Strip', MULTILINE | IGNORECASE)
    help = 'Index format: yyyymmdd'



class Freefall(_BasicScraper):
    latestUrl = 'http://freefall.purrsia.com/default.htm'
    imageUrl = 'http://freefall.purrsia.com/ff%s/fc%s.htm'
    imageSearch = compile(r'<img src="(/ff\d+/.+?.\w{3,4})"')
    prevSearch = compile(r'<A HREF="(/ff\d+/.+?.htm)">Previous</A>')
    help = 'Index format: nnnn/nnnnn'



class FantasyRealms(_BasicScraper):
    imageUrl = 'http://www.fantasyrealmsonline.com/manga/%s.php'
    imageSearch = compile(r'<img src="(\d{1,4}.\w{3,4})" width="540"', IGNORECASE)
    prevSearch = compile(r'<a href="(.+?)"><img src="../images/nav-back.gif"', IGNORECASE)
    help = 'Index format: nnn'
    starter = indirectStarter('http://www.fantasyrealmsonline.com/',
                              compile(r'<a href="(manga/.+?)"><img src="preview.jpg"', IGNORECASE))



class FullFrontalNerdity(_BasicScraper):
    latestUrl = 'http://nodwick.humor.gamespy.com/ffn/index.php'
    imageUrl = None
    imageSearch = compile(r'<img src="(http://nodwick.humor.gamespy.com/ffn/strips/[^"]*)"', IGNORECASE)
    prevSearch = compile(r'<a href="(index.php\?date=[0-9-]*)"><img src="back.jpg"', IGNORECASE)


class FunInJammies(_BasicScraper):
    latestUrl = 'http://www.funinjammies.com/'
    imageUrl = 'http://www.funinjammies.com/comic.php?issue=%s'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'(/comic.php.+?)" id.+?prev')
    help = 'Index format: n (unpadded)'



class Fallen(_BasicScraper):
    imageUrl = 'http://www.fallencomic.com/pages/part%s/%s-p%s.htm'
    imageSearch = compile(r'<IMG SRC="(page/.+?)"', IGNORECASE)
    prevSearch = compile(r'<A HREF="(.+?)"><FONT FACE="Courier">Back', IGNORECASE)
    help = 'Index format: nn-m (comicNumber-partNumber)'
    starter = indirectStarter('http://www.fallencomic.com/fal-page.htm',
                              compile(r'\(NEW \d{2}/\d{2}/\d{2}\)\s*\n*\s*<a href="(pages/part\d+/\d+-p\d+\.htm)">\d+</a>', MULTILINE))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        num = pageUrl.split('/')[-1].split('-')[0]
        part = pageUrl.split('-')[-1].split('.')[0]
        return '%s-%s' % (part, num)

    def setStrip(self, index):
        index, part = index.split('-')
        self.currentUrl = self.imageUrl % (part, index, part)



class FoxTails(_BasicScraper):
    latestUrl = 'http://www.magickitsune.com/strips/current.html'
    imageUrl = 'http://www.magickitsune.com/strips/%s'
    imageSearch = compile(r'<img src=(img/.+?)[ |>]', IGNORECASE)
    prevSearch = compile(r'(?<=first.gif)*(?<=</td>)*<a.*href=\'(.+?)\'.+?<img.+?src=\'../img/prev.gif\'>', IGNORECASE)
    help = 'Index format: yyyymmdd'

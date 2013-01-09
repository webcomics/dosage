# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..helpers import bounceStarter, queryNamer, indirectStarter
from ..util import tagre


class PandyLand(_BasicScraper):
    latestUrl = 'http://pandyland.net/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://pandyland\.net/comics/[^"]+)'))
    prevSearch =  compile(tagre("a", "href", r'(http://pandyland\.net/\d+/)', after="prev"))
    help = 'Index format: number'


class PartiallyClips(_BasicScraper):
    latestUrl = 'http://partiallyclips.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://partiallyclips\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://partiallyclips\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class PastelDefender(_BasicScraper):
    latestUrl = 'http://www.pasteldefender.com/coverbackcover.html'
    stripUrl = 'http://www.pasteldefender.com/%s.html'
    imageSearch = compile(r'<IMG SRC="(images/.+?)" WIDTH="742"')
    prevSearch = compile(r'<A HREF="([^"]+)"><IMG SRC="images/back\.gif"')
    help = 'Index format: nnn'


class PebbleVersion(_BasicScraper):
    latestUrl = 'http://www.pebbleversion.com/'
    stripUrl = latestUrl + 'Archives/Strip%s.html'
    imageSearch = compile(r'<img src="(ComicStrips/.+?|../ComicStrips/.+?)"')
    prevSearch = compile(r'<a href="((?!.+?">First Comic)Archives/Strip.+?|(?=.+?">Previous Comic)(?!.+?">First Comic)Strip.+?)"')
    help = 'Index format: n (unpadded)'


class PennyAndAggie(_BasicScraper):
    baseUrl = 'http://www.pennyandaggie.com/'
    stripUrl = baseUrl + 'index.php?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.pennyandaggie\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?p=\d+)", quote="'") +
                         tagre("img", "src", r'http://pennyandaggie\.com/images/previous_day\.gif', quote=""))
    starter = indirectStarter(baseUrl, prevSearch)
    help = 'Index format: n (unpadded)'


class PennyArcade(_BasicScraper):
    baseUrl = 'http://penny-arcade.com/comic/'
    starter = bounceStarter(baseUrl,
       compile(tagre("a", "href", r'(http://penny-arcade\.com/comic/[^"]+)', before="btnNext"))
    )
    stripUrl = baseUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://art\.penny-arcade\.com/photos/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://penny-arcade\.com/comic/[^"]+)', before="btnPrev"))
    help = 'Index format: yyyy/mm/dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        dummy, yyyy, mm, dd = pageUrl.rsplit('/', 3)
        return '%04d%02d%02d' % (int(yyyy), int(mm), int(dd))


class PeppermintSaga(_BasicScraper):
    latestUrl = 'http://www.pepsaga.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.pepsaga\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.pepsaga\.com/\?p=\d+)', after="prev"))
    help = 'Index format: number'


class PicPakDog(_BasicScraper):
    latestUrl = 'http://www.picpak.net/'
    stripUrl = latestUrl + 'comics/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.picpak\.net/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.picpak\.net/comics/[^"]+)', after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Pixel(_BasicScraper):
    latestUrl = 'http://pixelcomic.net/'
    stripUrl = latestUrl + '%s.php'
    imageSearch = compile(tagre("img", "src", r'(\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(http://pixelcomic\.net/\d+\.php)', before="prev"))
    help = 'Index format: nnn'


class PiledHigherAndDeeper(_BasicScraper):
    starter = bounceStarter('http://www.phdcomics.com/comics/archive.php', compile(r'<a href=(archive\.php\?comicid=\d+)><img height=52 width=49 src=images/next_button\.gif border=0 align=middle>'))
    stripUrl = 'http://www.phdcomics.com/comics/archive.php?comicid=%s'
    imageSearch = compile(r'<img src=(http://www\.phdcomics\.com/comics/archive/phd\d+s?\.gif)')
    prevSearch = compile(r'<a href=(archive\.php\?comicid=\d+)><img height=52 width=49 src=images/prev_button\.gif border=0 align=middle>')
    help = 'Index format: n (unpadded)'
    namer = queryNamer('comicid', usePageUrl=True)


class Pimpette(_BasicScraper):
    latestUrl = 'http://pimpette.ca/'
    stripUrl = latestUrl + 'index.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)') + "Previous")
    help = 'Index format: yyyymmdd'


class Precocious(_BasicScraper):
    baseUrl = 'http://www.precociouscomic.com/'
    starter = indirectStarter(baseUrl,
      compile(tagre("a", "href", r'(/archive/comic/[^"]+)') + tagre("img", "src", r"/templates/precocious_main/images/next_arrow\.png"))
    )
    stripUrl = baseUrl + 'archive/comic/%s'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/comic/[^"]+)') + tagre("img", "src", r"/templates/precocious_main/images/back_arrow\.png"))
    help = 'Index format: yyyy/mm/dd'


class PvPonline(_BasicScraper):
    latestUrl = 'http://pvponline.com/comic'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://newcdn\.pvponline\.com/img/comic/pvp[^"]+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(http://pvponline\.com/comic/[^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ProperBarn(_BasicScraper):
    latestUrl = 'http://www.nitrocosm.com/go/gag/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://content\.nitrocosm\.com/gag/\d+\.[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.nitrocosm\.com/go/gag/\d+/)', after="nav_btn_previous"))
    help = 'Index format: nnn'


class PunksAndNerds(_BasicScraper):
    latestUrl = 'http://www.punksandnerds.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.punksandnerds\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.punksandnerds\.com/\?p=\d+)', after="navi-prev"))
    help = 'Index format: nnn'


class PunksAndNerdsOld(_BasicScraper):
    latestUrl = 'http://original.punksandnerds.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(r' src="(/comics/.+?)"')
    prevSearch = compile(r'><strong><a href="(.+?)"[^>]+?><img[^>]+?src="/previouscomic.gif">')
    help = 'Index format: yyyymmdd'


class PlanescapeSurvival(_BasicScraper):
    latestUrl = 'http://planescapecomic.com/'
    stripUrl = latestUrl + '%s.html'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img alt="Previous" ')
    help = 'Index format: nnn'

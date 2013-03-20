# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..helpers import bounceStarter, queryNamer, indirectStarter
from ..util import tagre


class PandyLand(_BasicScraper):
    url = 'http://pandyland.net/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://pandyland\.net/comics/[^"]+)'))
    prevSearch =  compile(tagre("a", "href", r'(http://pandyland\.net/\d+/)', after="prev"))
    help = 'Index format: number'


class ParadigmShift(_BasicScraper):
    url = 'http://www.paradigmshiftmanga.com/'
    starter = indirectStarter(url, compile(tagre("a", "href", r'([^"]+)', after="next-comic-link")))
    stripUrl = url + 'ps/%s.html'
    imageSearch = compile(tagre("img", "src", r'([^"]*comics/ps/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="previous-comic-link"))
    help = 'Index format: custom'


class ParallelUniversum(_BasicScraper):
    url = 'http://www.paralleluniversum.net/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '001-der-comic-ist-tot'
    imageSearch = compile(tagre("img", "src", r'(http://www\.paralleluniversum\.net/comics/\d+-\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.paralleluniversum\.net/[^"]+/)') + 
        tagre("span", "class", "prev"))
    help = 'Index format: number-stripname'
    lang = 'de'


class PartiallyClips(_BasicScraper):
    url = 'http://partiallyclips.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://partiallyclips\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://partiallyclips\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class PastelDefender(_BasicScraper):
    url = 'http://www.pasteldefender.com/coverbackcover.html'
    stripUrl = 'http://www.pasteldefender.com/%s.html'
    imageSearch = compile(r'<IMG SRC="(images/.+?)" WIDTH="742"')
    prevSearch = compile(r'<A HREF="([^"]+)"><IMG SRC="images/back\.gif"')
    help = 'Index format: nnn'


class PebbleVersion(_BasicScraper):
    url = 'http://www.pebbleversion.com/'
    stripUrl = url + 'Archives/Strip%s.html'
    imageSearch = compile(r'<img src="(ComicStrips/.+?|../ComicStrips/.+?)"')
    prevSearch = compile(r'<a href="((?!.+?">First Comic)Archives/Strip.+?|(?=.+?">Previous Comic)(?!.+?">First Comic)Strip.+?)"')
    help = 'Index format: n (unpadded)'


class PennyAndAggie(_BasicScraper):
    url = 'http://www.pennyandaggie.com/'
    stripUrl = url + 'index.php?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.pennyandaggie\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?p=\d+)", quote="'") +
                         tagre("img", "src", r'http://pennyandaggie\.com/images/previous_day\.gif', quote=""))
    starter = indirectStarter(url, prevSearch)
    help = 'Index format: n (unpadded)'


class PennyArcade(_BasicScraper):
    url = 'http://penny-arcade.com/comic/'
    starter = bounceStarter(url,
       compile(tagre("a", "href", r'(http://penny-arcade\.com/comic/[^"]+)', before="btnNext"))
    )
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://art\.penny-arcade\.com/photos/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://penny-arcade\.com/comic/[^"]+)', before="btnPrev"))
    help = 'Index format: yyyy/mm/dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        dummy, yyyy, mm, dd = pageUrl.rsplit('/', 3)
        return '%04d%02d%02d' % (int(yyyy), int(mm), int(dd))


class PeppermintSaga(_BasicScraper):
    url = 'http://www.pepsaga.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.pepsaga\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.pepsaga\.com/\?p=\d+)', after="prev"))
    help = 'Index format: number'


class PHDComics(_BasicScraper):
    baseurl = 'http://phdcomics.com/'
    url = baseurl + 'comics.php'
    stripUrl = baseurl + 'comics/archive.php?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://www\.phdcomics\.com/comics/archive/phd[^ ]+)', quote=""))
    prevSearch = compile(tagre("a", "href", r'((?:comics/)?archive\.php\?comicid=\d+)', quote="") +
        tagre("img", "src", r'(?:comics/)?images/prev_button\.gif', quote=""))
    help = 'Index format: number'


class PicPakDog(_BasicScraper):
    url = 'http://www.picpak.net/'
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.picpak\.net/wp-content/uploads/\d+/\d+/\d+-\d+-\d+-[^"]+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.picpak\.net/comic/[^"]+)', after="navi-prev"))
    help = 'Index format: stripname'


class Pixel(_BasicScraper):
    url = 'http://pixelcomic.net/'
    stripUrl = url + '%s.php'
    imageSearch = compile(tagre("img", "src", r'(\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(http://pixelcomic\.net/\d+\.php)', before="prev"))
    help = 'Index format: nnn'


class PiledHigherAndDeeper(_BasicScraper):
    url = 'http://www.phdcomics.com/comics/archive.php'
    starter = bounceStarter(url, compile(r'<a href=(archive\.php\?comicid=\d+)><img height=52 width=49 src=images/next_button\.gif border=0 align=middle>'))
    stripUrl = url + '?comicid=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.phdcomics\.com/comics/archive/phd\d+s?\.gif)', quote=""))
    prevSearch = compile(r'<a href=(archive\.php\?comicid=\d+)><img height=52 width=49 src=images/prev_button\.gif border=0 align=middle>')
    help = 'Index format: n (unpadded)'
    namer = queryNamer('comicid', usePageUrl=True)


class Pimpette(_BasicScraper):
    url = 'http://pimpette.ca/'
    stripUrl = url + 'index.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)') + "Previous")
    help = 'Index format: yyyymmdd'


# Broken navigation: prev link at http://planescapecomic.com/201.html points to same URL.
class _PlanescapeSurvival(_BasicScraper):
    url = 'http://planescapecomic.com/'
    stripUrl = url + '%s.html'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img alt="Previous" ')
    help = 'Index format: nnn'


class PokeyThePenguin(_BasicScraper):
    baseurl = 'http://www.yellow5.com/pokey/archive/'
    url = baseurl + 'index558.html'
    stripUrl = baseurl + 'index%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(pokey\d+[^"]+)'))
    prevSearch = True
    multipleImagesPerStrip = True
    help = 'Index format: number'

    def getPrevUrl(self, url, data, baseUrl):
        """Decrease index.html number."""
        mo = compile(r"index(\d+)\.html").search(url)
        num = int(mo.group(1)) - 1
        prefix = url.rsplit('/', 1)[0]
        return "%s/index%d.html" % (prefix, num)


class Precocious(_BasicScraper):
    url = 'http://www.precociouscomic.com/'
    starter = indirectStarter(url,
      compile(tagre("a", "href", r'(/archive/comic/[^"]+)') + tagre("img", "src", r"/templates/precocious_main/images/next_arrow\.png"))
    )
    stripUrl = url + 'archive/comic/%s'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d+[^"]*\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/comic/[^"]+)') + tagre("img", "src", r"/templates/precocious_main/images/back_arrow\.png"))
    help = 'Index format: yyyy/mm/dd'


class PvPonline(_BasicScraper):
    url = 'http://pvponline.com/comic'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://s3[^"]+\.amazonaws\.com/pvponlinenew/img/comic/\d+/\d+/pvp[^"]+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ProperBarn(_BasicScraper):
    url = 'http://www.nitrocosm.com/go/gag/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://content\.nitrocosm\.com/gag/\d+\.[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.nitrocosm\.com/go/gag/\d+/)', after="nav_btn_previous"))
    help = 'Index format: nnn'


class PunksAndNerds(_BasicScraper):
    url = 'http://www.punksandnerds.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.punksandnerds\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.punksandnerds\.com/\?p=\d+)', after="navi-prev"))
    help = 'Index format: nnn'


class PunksAndNerdsOld(_BasicScraper):
    url = 'http://original.punksandnerds.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(r' src="(/comics/.+?)"')
    prevSearch = compile(r'><strong><a href="(.+?)"[^>]+?><img[^>]+?src="/previouscomic.gif">')
    help = 'Index format: yyyymmdd'

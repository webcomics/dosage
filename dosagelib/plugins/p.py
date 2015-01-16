# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..helpers import bounceStarter, queryNamer, indirectStarter
from ..util import tagre, fetchUrl, getPageContent


class PandyLand(_BasicScraper):
    url = 'http://pandyland.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch =  compile(tagre("a", "href", r'(%s\d+/)' % rurl, after="prev"))
    help = 'Index format: number'


class ParadigmShift(_BasicScraper):
    description = u'A Paranormal Graphic Novel by Dirk I. Tiede'
    url = 'http://www.paradigmshiftmanga.com/'
    starter = indirectStarter(url, compile(tagre("a", "href", r'([^"]+)', after="next-comic-link")))
    stripUrl = url + 'ps/%s.html'
    imageSearch = compile(tagre("img", "src", r'([^"]*comics/ps/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="previous-comic-link"))
    help = 'Index format: custom'


class ParallelUniversum(_BasicScraper):
    url = 'http://www.paralleluniversum.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '001-der-comic-ist-tot'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+/)' % rurl) +
        tagre("span", "class", "prev"))
    help = 'Index format: number-stripname'
    lang = 'de'


class PartiallyClips(_BasicScraper):
    description = u'PartiallyClips - The true stories behind your favorite clip art.'
    url = 'http://partiallyclips.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2001/10/28/screaming-woman'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class PastelDefender(_BasicScraper):
    baseUrl = 'http://www.pasteldefender.com/'
    url = baseUrl + 'coverbackcover.html'
    stripUrl = baseUrl + '%s.html'
    firstStripUrl = stripUrl % 'cover'
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
    url = 'http://pennyandaggie.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.pennyandaggie\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?p\=\d+)", quote="'") +
                         tagre("img", "src", r'%simages/previous_day\.gif' % rurl, quote=""))
    starter = indirectStarter(url, prevSearch)
    help = 'Index format: n (unpadded)'


class PennyArcade(_BasicScraper):
    url = 'http://penny-arcade.com/comic/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1998/11/18'
    imageSearch = compile(tagre("img", "src", r'(http://art\.penny-arcade\.com/photos/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, before="btnPrev"))
    nextSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, before="btnNext"))
    help = 'Index format: yyyy/mm/dd/'

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        if prevUrl:
            dummy, yyyy, mm, dd = prevUrl.rsplit('/', 3)
            try:
                int(dd)
            except ValueError:
                # URL has form yyyy/mm/dd/stripname
                prevUrl = "%s/%s/%s" % (dummy, yyyy, mm)
            return prevUrl

    @classmethod
    def starter(cls):
        """Get bounced start URL."""
        data, baseUrl = getPageContent(cls.url, cls.session)
        url1 = fetchUrl(cls.url, data, baseUrl, cls.prevSearch)
        data, baseUrl = getPageContent(url1, cls.session)
        url2 = fetchUrl(url1, data, baseUrl, cls.nextSearch)
        return cls.prevUrlModifier(url2)

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        p = pageUrl.split('/')
        return '%04d%02d%02d' % (int(p[4]), int(p[5]), int(p[6]))


class PeppermintSaga(_BasicScraper):
    description = u'Sexy Fucking Fantasy Adventure Webcomic - NSFW'
    url = 'http://www.pepsaga.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '3'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: number'
    adult = True


class PHDComics(_BasicScraper):
    baseUrl = 'http://phdcomics.com/'
    url = baseUrl + 'comics.php'
    stripUrl = baseUrl + 'comics/archive.php?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://www\.phdcomics\.com/comics/archive/phd[^ ]+)', quote=""))
    prevSearch = compile(tagre("a", "href", r'((?:comics/)?archive\.php\?comicid=\d+)', quote="") +
        tagre("img", "src", r'(?:comics/)?images/prev_button\.gif', quote=""))
    help = 'Index format: number'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            self.stripUrl % '1669', # video
        )


class PicPakDog(_BasicScraper):
    description = u'A comic by Kim Belding'
    url = 'http://www.picpak.net/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'dogs-cant-spell'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+-[^"]+\.png)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="nav-prev"))
    help = 'Index format: stripname'


class Pixel(_BasicScraper):
    url = 'http://pixelcomic.net/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '000.shtml'
    imageSearch = compile(tagre("img", "src", r'(\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(%s\d+\.(?:php|shtml))' % rurl, before="prev"))
    help = 'Index format: nnn'


class PiledHigherAndDeeper(_BasicScraper):
    url = 'http://www.phdcomics.com/comics.php'
    starter = bounceStarter(url, compile(r'<a href=(archive\.php\?comicid=\d+)>.*<img [^>]*next_button\.gif'))
    stripUrl = url + '?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://www\.phdcomics\.com/comics/archive/phd\d+s\d?\.\w{3,4})', quote=""))
    prevSearch = compile(r'<a href=((comics/)?archive\.php\?comicid=\d+)>.*<img [^>]*prev_button\.gif')
    help = 'Index format: n (unpadded)'
    namer = queryNamer('comicid', usePageUrl=True)


class Pimpette(_BasicScraper):
    url = 'http://pimpette.ca/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '20030905'
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
    baseUrl = 'http://www.yellow5.com/pokey/archive/'
    url = baseUrl + 'index558.html'
    stripUrl = baseUrl + 'index%s.html'
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


class PoorlyDrawnLines(_BasicScraper):
    url = 'http://poorlydrawnlines.com/comic/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'campus-characters/'
    imageSearch = compile(tagre("img", "src", r'(http://poorlydrawnlines\.com/wp-content/uploads/\d+/\d+/[^"]+)'))
    prevSearch = compile(tagre("li", "class", r'previous') + tagre("a", "href", r'(%s[^"]+)' % rurl))
    help = 'Index Format: name'
    description = u'A thrice-weekly webcomic written and illustrated by Reza Farazmand. New comics every Monday, Wednesday, and Friday.'


class Precocious(_BasicScraper):
    url = 'http://www.precociouscomic.com/'
    starter = indirectStarter(url,
      compile(tagre("a", "href", r'(/archive/comic/[^"]+)') + tagre("img", "src", r"/templates/precocious_main/images/next_arrow\.png"))
    )
    stripUrl = url + 'archive/comic/%s'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d+[^"]*\.(?:jpg|gif))'))
    prevSearch = compile(tagre("a", "href", r'(/archive/comic/[^"]+)') + tagre("img", "src", r"/templates/precocious_main/images/back_arrow\.png"))
    help = 'Index format: yyyy/mm/dd'


class ProperBarn(_BasicScraper):
    url = 'http://www.nitrocosm.com/go/gag/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://content\.nitrocosm\.com/gag/\d+\.[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.nitrocosm\.com/go/gag/\d+/)', after="nav_btn_previous"))
    help = 'Index format: nnn'


class PunksAndNerds(_BasicScraper):
    url = 'http://www.punksandnerds.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '15'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="navi-prev"))
    help = 'Index format: nnn'


class PunksAndNerdsOld(_BasicScraper):
    url = 'http://original.punksandnerds.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(r' src="(/comics/.+?)"')
    prevSearch = compile(r'><strong><a href="(.+?)"[^>]+?><img[^>]+?src="/previouscomic.gif">')
    help = 'Index format: yyyymmdd'


class PvPonline(_BasicScraper):
    url = 'http://pvponline.com/comic'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://s3[^"]+\.amazonaws\.com/pvponlinenew/img/comic/\d+/\d+/pvp[^"]+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)', after="left divider"))
    help = 'Index format: yyyy/mm/dd/stripname'

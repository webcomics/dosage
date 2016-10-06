# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import bounceStarter, queryNamer, indirectStarter
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, xpath_class


class PandyLand(_WordPressScraper):
    url = 'http://pandyland.net/'
    firstStripUrl = 'http://pandyland.net/1/'


class ParadigmShift(_BasicScraper):
    url = 'http://www.paradigmshiftmanga.com/'
    starter = indirectStarter
    stripUrl = url + 'ps/%s.html'
    imageSearch = compile(tagre("img", "src", r'([^"]*comics/ps/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)',
                               after="previous-comic-link"))
    latestSearch = compile(tagre("a", "href", r'([^"]+)',
                                 after="next-comic-link"))
    help = 'Index format: custom'


class ParallelUniversum(_BasicScraper):
    url = 'http://www.paralleluniversum.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '001-der-comic-ist-tot'
    imageSearch = compile(tagre("img", "src",
                                r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+/)' % rurl) +
                         tagre("span", "class", "prev"))
    help = 'Index format: number-stripname'
    lang = 'de'


class PartiallyClips(_WordPressScraper):
    url = 'http://partiallyclips.com/'
    firstStripUrl = url + 'comic/screaming-woman/'


class PastelDefender(_BasicScraper):
    baseUrl = 'http://www.pasteldefender.com/'
    url = baseUrl + 'coverbackcover.html'
    stripUrl = baseUrl + '%s.html'
    firstStripUrl = stripUrl % 'cover'
    imageSearch = compile(r'<IMG SRC="(images/.+?)" WIDTH="742"')
    prevSearch = compile(r'<A HREF="([^"]+)"><IMG SRC="images/back\.gif"')
    help = 'Index format: nnn'


class PebbleVersion(_ParserScraper):
    url = 'http://www.pebbleversion.com/'
    stripUrl = url + 'Archives/Strip%s.html'
    imageSearch = "//table/tr[2]//img"
    prevSearch = '//a[text()="Previous Comic"]'
    help = 'Index format: n (unpadded)'


class PennyAndAggie(_BasicScraper):
    url = 'http://pennyandaggie.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.pennyandaggie\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?p\=\d+)", quote="'") +
                         tagre("img", "src", r'%simages/previous_day\.gif' % rurl, quote=""))
    help = 'Index format: n (unpadded)'


class PennyArcade(_ParserScraper):
    url = 'http://www.penny-arcade.com/comic/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1998/11/18'
    imageSearch = '//div[@id="comicFrame"]//img'
    prevSearch = '//a[%s]' % xpath_class('btnPrev')
    nextSearch = '//a[%s]' % xpath_class('btnNext')
    starter = bounceStarter
    help = 'Index format: yyyy/mm/dd'

    def namer(self, image_url, page_url):
        p = page_url.split('/')
        return '%04d%02d%02d' % (int(p[4]), int(p[5]), int(p[6]))


class PeppermintSaga(_BasicScraper):
    url = 'http://www.pepsaga.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '3'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl,
                               after="prev"))
    help = 'Index format: number'
    adult = True


class PHDComics(_ParserScraper):
    baseUrl = 'http://phdcomics.com/'
    url = baseUrl + 'comics.php'
    stripUrl = baseUrl + 'comics/archive.php?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@id="comic"]'
    prevSearch = '//a[img[contains(@src, "prev_button")]]'
    nextSearch = '//a[img[contains(@src, "next_button")]]'
    help = 'Index format: n (unpadded)'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            # video
            self.stripUrl % '1880',
            self.stripUrl % '1669',
        )


class Picklewhistle(_ComicControlScraper):
    url = 'http://www.picklewhistle.com/'


class PicPakDog(_WordPressScraper):
    url = 'http://www.picpak.net/'
    firstStripUrl = url + 'comic/dogs-cant-spell/'


# Keep, because naming is different to PHDComics...
class PiledHigherAndDeeper(PHDComics):
    starter = bounceStarter
    namer = queryNamer('comicid', use_page_url=True)


class Pimpette(_ParserScraper):
    url = 'http://pimpette.ca/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '20030905'
    imageSearch = '//div[@id="strip"]/img'
    prevSearch = '//a[text()="previous"]'
    help = 'Index format: yyyymmdd'


class Pixel(_BasicScraper):
    url = 'http://pixelcomic.net/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '000.shtml'
    imageSearch = compile(tagre("img", "src", r'(\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(%s\d+\.(?:php|shtml))' % rurl,
                               before="prev"))
    help = 'Index format: nnn'


class PlanescapeSurvival(_BasicScraper):
    url = 'http://planescapecomic.com/'
    stripUrl = url + '%s.html'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img alt="Previous" ')
    help = 'Index format: nnn'


class PokeyThePenguin(_ParserScraper):
    url = 'http://www.yellow5.com/pokey/archive/'
    stripUrl = url + 'index%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//p/img'
    latestSearch = '(//a)[last()]'
    multipleImagesPerStrip = True
    starter = indirectStarter
    help = 'Index format: number'

    def getPrevUrl(self, url, data):
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
    prevSearch = compile(tagre("li", "class", r'previous') +
                         tagre("a", "href", r'(%s[^"]+)' % rurl))
    help = 'Index Format: name'


class Precocious(_ParserScraper):
    url = 'http://www.precociouscomic.com/'
    stripUrl = url + 'archive/comic/%s'
    firstStripUrl = stripUrl % '2009/03/09'
    imageSearch = '//img[contains(@src, "/comics/")]'
    prevSearch = '//a[img[contains(@src, "/back_arrow")]]'
    help = 'Index format: yyyy/mm/dd'

class PrinceOfSartar(_WordPressScraper):
    url = 'http://www.princeofsartar.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'introduction-chapter-1'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@class="navi comic-nav-previous navi-prev"]'
    nextSearch = '//a[@class="navi comic-nav-next navi-next"]'
    starter = bounceStarter
    help = 'Index format: name'

    def namer(self, image_url, page_url):
        """Use page URL to contruct a unique name."""
        title = page_url.rsplit('/', 2)[1]
        image_ext = image_url.rsplit('.', 1)[1]
        return '%s.%s' % (title, image_ext)

class PS238(_ParserScraper):
    url = 'http://ps238.nodwick.com/'
    stripUrl = url + 'comic/%s/'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@class="comic-nav-base comic-nav-previous"]'
    help = 'Index format: yyyy-mm-dd'


class PunksAndNerds(_WordPressScraper):
    url = 'http://www.punksandnerds.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '15'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')
    help = 'Index format: nnn'


class PvPonline(_BasicScraper):
    url = 'http://pvponline.com/comic'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://s3[^"]+\.amazonaws\.com/pvponlinenew/img/comic/\d+/\d+/pvp[^"]+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)',
                               after="left divider"))
    help = 'Index format: yyyy/mm/dd/stripname'

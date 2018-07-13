# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import _ComicControlScraper, _WordPressScraper, _WPNavi


class Galaxion(_BasicScraper):
    url = 'http://galaxioncomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1-comic/the-story-so-far/the-story-so-far'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: n-comic/book-n/chapter-n/title-nnn'


class Garanos(_BasicScraper):
    baseUrl = 'http://garanos.alexheberling.com/'
    rurl = escape(baseUrl)
    url = baseUrl + 'pages/page-1/'
    starter = indirectStarter
    stripUrl = baseUrl + 'pages/page-%s'
    imageSearch = compile(
        tagre("img", "src",
              r'(%swp-content/uploads/sites/\d+/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%spages/[^"]+)' % rurl,
                               after="prev"))
    latestSearch = compile(tagre("a", "href", r'(%spages/[^"]+)' % rurl,
                                 after="nav-last"))
    help = 'Index format: n (unpadded)'


class GastroPhobia(_ParserScraper):
    url = 'http://www.gastrophobia.com/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '2008-07-30'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//div[@id="prev"]/a'
    help = 'Index format: yyyy-mm-dd'


class Geeks(_BasicScraper):
    url = 'http://sevenfloorsdown.com/geeks/'
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '10'
    imageSearch = compile(
        r'<img src=\'(http://sevenfloorsdown.com/geeks/comics/.+?)\'')
    prevSearch = compile(r'<a href="(.+?)">&laquo; Previous')
    help = 'Index format: nnn'


class GeeksNextDoor(_BasicScraper):
    url = 'http://www.geeksnextcomic.com/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '2010-10-04'
    imageSearch = compile(tagre("img", "src", r'(images/GND\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\d+-\d+-\d+\.html)') +
                         tagre("img", "src", r'images/nav_prev\.png'))
    help = 'Index format: yyyy-mm-dd'


class GirlGenius(_BasicScraper):
    baseUrl = 'http://www.girlgeniusonline.com/'
    rurl = escape(baseUrl)
    url = baseUrl + 'comic.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20021104'
    imageSearch = compile(
        tagre("img", "src", r"(%sggmain/strips/[^']*)" % rurl, quote="'"))
    prevSearch = compile(tagre("a", "id", "topprev", quote="\"",
                               before=r"(%s[^\"']+)" % rurl))
    multipleImagesPerStrip = True
    help = 'Index format: yyyymmdd'


class GirlsWithSlingshots(_BasicScraper):
    url = 'http://www.girlswithslingshots.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'gws1'
    imageSearch = (
        compile(tagre("img", "src", r'(//www.girlswithslingshots.com/comics/[^"]+)')),
        compile(tagre("img", "src",
                      r'(http://cdn\.girlswithslingshots\.com/comics/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(//www.girlswithslingshots.com/comic/[^"]+)',
                               after="prev"))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Remove random junk from image names."""
        imgname = imageUrl.split('/')[-1]
        if '-' in imgname:
            imgname = imgname.rsplit('-', 1)[1]
        return '%s' % (imgname)

    help = 'Index format: stripname'


class GlassHalfEmpty(_BasicScraper):
    url = 'http://www.defectivity.com/ghe/index.php'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(
        tagre("a", "href", r'(\?strip_id=\d+)') +
        tagre("img", "src", r'\.\./images/arrowbuttons/onback\.jpg'))
    help = 'Index format: nnn'


class GleefulNihilism(_BasicScraper):
    url = 'http://gleefulnihilism.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'amoeba'
    imageSearch = compile(
        tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(
        tagre("a", "href", r'(%scomic/[^"]+)' % rurl) + '&lsaquo;')
    help = 'Index format: stripname'


class GoblinsComic(_ParserScraper):
    url = 'http://www.goblinscomic.org/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    css = True
    imageSearch = '#comic img'
    prevSearch = '.nav-previous > a'
    help = 'Index format: ddmmyyyy'


class GodChild(_WordPressScraper):
    url = 'http://godchild.keenspot.com/'


class GoGetARoomie(_ComicControlScraper):
    url = 'http://www.gogetaroomie.com'


class GoneWithTheBlastwave(_BasicScraper):
    url = 'http://www.blastwave-comic.com/index.php?p=comic&nro=1'
    starter = indirectStarter
    stripUrl = url[:-1] + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<img.+src=".+(/comics/.+?)"')
    prevSearch = compile(r'href="(index.php\?p=comic&amp;nro=\d+)">' +
                         r'<img src="images/page/default/previous')
    latestSearch = compile(r'href="(index.php\?p=comic&amp;nro=\d+)">' +
                           r'<img src="images/page/default/latest')
    help = 'Index format: n'

    def namer(self, image_url, page_url):
        return '%02d' % int(compile(r'nro=(\d+)').search(page_url).group(1))


class GrrlPower(_WPNavi):
    url = 'http://grrlpowercomic.com/'
    firstStripUrl = url + 'archives/48'


class GUComics(_BasicScraper):
    url = 'http://www.gucomics.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '20000710'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d{4}/gu_[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\d+)') +
                         tagre("img", "src", r'/images/nav/prev\.png'))
    help = 'Index format: yyyymmdd'


class GunnerkriggCourt(_BasicScraper):
    url = 'http://www.gunnerkrigg.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(
        tagre("a", "href", r'(\?p=\d+)') +
        tagre("img", "src", "/images/prev_a\.jpg"))
    help = 'Index format: number'


class Gunshow(_BasicScraper):
    url = 'http://gunshowcomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src",
                                r'(http://gunshowcomic\.com/comics/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(
        tagre("a", "href", r'([^"]+)') +
        tagre("img", "src", r'[^"]*menu/small/previous\.gif'))
    help = 'Index format: n'

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class Galaxion(_BasicScraper):
    latestUrl = 'http://galaxioncomics.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://galaxioncomics\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://galaxioncomics\.com/[^"]+)', after="prev"))
    help = 'Index format: n-comic/book-n/chapter-n/title-nnn'


class Garanos(_BasicScraper):
    starter = indirectStarter('http://garanos.alexheberling.com/pages/page-1/',
       compile(tagre("a", "href", r'(http://garanos\.alexheberling\.com/pages/[^"]+)', after="navi-last")))
    stripUrl = 'http://garanos.alexheberling.com/pages/page-%s'
    imageSearch = compile(tagre("img", "src", r'(http://garanos\.alexheberling\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://garanos\.alexheberling\.com/pages/[^"]+)', after="prev"))
    help = 'Index format: n  (unpadded)'


class GUComics(_BasicScraper):
    latestUrl = 'http://www.gucomics.com/comic/'
    stripUrl = latestUrl + '?cdate=%s'
    imageSearch = compile(r'<IMG src="(/comics/\d{4}/gu_.*?)"')
    prevSearch = compile(r'<A href="(/comic/\?cdate=\d+)"><IMG src="/images/cnav_prev')
    help = 'Index format: yyyymmdd'


class GirlGenius(_BasicScraper):
    latestUrl = 'http://girlgeniusonline.com/comic.php'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(r"(/ggmain/strips/.+?)'")
    prevSearch = compile(r"</a> <a href=.+?(/comic.php\?date=.+?)'.+?Previous")
    help = 'Index format: yyyymmdd'


class GirlsWithSlingshots(_BasicScraper):
    latestUrl = 'http://www.girlswithslingshots.com/'
    stripUrl = latestUrl + 'comic/gws-%s/'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.girlswithslingshots\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.girlswithslingshots\.com/comic/[^"]+)', after="prev"))
    help = 'Index format: nnn'


class GleefulNihilism(_BasicScraper):
    latestUrl = 'http://gleefulnihilism.com/'
    stripUrl = latestUrl + 'comics/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://gleefulnihilism\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://gleefulnihilism\.com/comics/[^"]+)') + 'Previous')
    help = 'Index format: yyyy/mm/dd/stripname'


class Goats(_BasicScraper):
    latestUrl = 'http://www.goats.com/'
    stripUrl = latestUrl + 'archive/%s.html'
    imageSearch = compile(r'<img.+?src="(/comix/.+?)"')
    prevSearch = compile(r'<a href="(/archive/\d{6}.html)" class="button" title="go back">')
    help = 'Index format: yymmdd'


class GoneWithTheBlastwave(_BasicScraper):
    starter = indirectStarter('http://www.blastwave-comic.com/index.php?p=comic&nro=1',
                              compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/latest'))
    stripUrl = 'http://www.blastwave-comic.com/index.php?p=comic&nro=%s'
    imageSearch = compile(r'<img.+src=".+(/comics/.+?)"')
    prevSearch = compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/previous')
    help = 'Index format: n'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%02d' % int(compile(r'nro=(\d+)').search(pageUrl).group(1))


class GunnerkrigCourt(_BasicScraper):
    latestUrl = 'http://www.gunnerkrigg.com/index2.php'
    stripUrl = 'http://www.gunnerkrigg.com/archive_page.php?comicID=%s'
    imageSearch = compile(r'<img src="(.+?//comics/.+?)"')
    prevSearch = compile(r'<.+?(/archive_page.php\?comicID=.+?)".+?prev')
    help = 'Index format: n'


class Gunshow(_BasicScraper):
    latestUrl = 'http://gunshowcomic.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://gunshowcomic\.com/comics/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'[^"]*menu/small/previous\.gif'))
    help = 'Index format: n'


class GleefulNihilism(_BasicScraper):
    latestUrl = 'http://gleefulnihilism.com/'
    stripUrl = latestUrl + 'comics/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://gleefulnihilism\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://gleefulnihilism\.com/comics/[^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/strip-name'


class GastroPhobia(_BasicScraper):
    latestUrl = 'http://www.gastrophobia.com/'
    stripUrl = latestUrl + 'index.php?date=%s'
    imageSearch = compile(r'<img src="(http://gastrophobia.com/comix/[^"]+)"[^>]*>(?!<br>)')
    prevSearch = compile(r'<a href="(.+?)"><img src="pix/prev.gif" ')
    help = 'Index format: yyyy-mm-dd'


class Geeks(_BasicScraper):
    latestUrl = 'http://sevenfloorsdown.com/geeks/'
    stripUrl = latestUrl + 'archives/%s'
    imageSearch = compile(r'<img src=\'(http://sevenfloorsdown.com/geeks/comics/.+?)\'')
    prevSearch = compile(r'<a href="(.+?)">&laquo; Previous')
    help = 'Index format: nnn'


class GlassHalfEmpty(_BasicScraper):
    latestUrl = 'http://www.defectivity.com/ghe/index.php'
    stripUrl = latestUrl + '?strip_id=%s'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "src", r'\.\./images/arrowbuttons/onback\.jpg'))
    help = 'Index format: nnn'


class GreystoneInn(_BasicScraper):
    latestUrl = 'http://www.greystoneinn.net/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch=compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch=compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help='Index format: yyyymmdd'

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class Galaxion(_BasicScraper):
    url = 'http://galaxioncomics.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://galaxioncomics\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://galaxioncomics\.com/[^"]+)', after="prev"))
    help = 'Index format: n-comic/book-n/chapter-n/title-nnn'


class Garanos(_BasicScraper):
    url = 'http://garanos.alexheberling.com/pages/page-1/'
    starter = indirectStarter(url,
       compile(tagre("a", "href", r'(http://garanos\.alexheberling\.com/pages/[^"]+)', after="navi-last")))
    stripUrl = 'http://garanos.alexheberling.com/pages/page-%s'
    imageSearch = compile(tagre("img", "src", r'(http://garanos\.alexheberling\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://garanos\.alexheberling\.com/pages/[^"]+)', after="prev"))
    help = 'Index format: n  (unpadded)'


class GastroPhobia(_BasicScraper):
    url = 'http://www.gastrophobia.com/'
    stripUrl = url + 'index.php?date=%s'
    imageSearch = compile(r'<img src="(http://gastrophobia.com/comix/[^"]+)"[^>]*>(?!<br>)')
    prevSearch = compile(r'<a href="(.+?)"><img src="pix/prev.gif" ')
    help = 'Index format: yyyy-mm-dd'


class Geeks(_BasicScraper):
    url = 'http://sevenfloorsdown.com/geeks/'
    stripUrl = url + 'archives/%s'
    imageSearch = compile(r'<img src=\'(http://sevenfloorsdown.com/geeks/comics/.+?)\'')
    prevSearch = compile(r'<a href="(.+?)">&laquo; Previous')
    help = 'Index format: nnn'


class GeeksNextDoor(_BasicScraper):
    url = 'http://www.geeksnextcomic.com/'
    stripUrl = url + '%s.html'
    imageSearch = compile(tagre("img", "src", r'(images/GND\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\d+-\d+-\d+\.html)') +
        tagre("img", "src", r'images/nav_prev\.png'))
    help = 'Index format: yyyy-mm-dd'


class GirlsWithSlingshots(_BasicScraper):
    url = 'http://www.girlswithslingshots.com/'
    stripUrl = url + 'comic/gws-%s/'
    imageSearch = compile(tagre("img", "src", r'(http://(?:www|cdn)\.girlswithslingshots\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.girlswithslingshots\.com/comic/[^"]+)', after="prev"))
    help = 'Index format: nnn'


class GlassHalfEmpty(_BasicScraper):
    url = 'http://www.defectivity.com/ghe/index.php'
    stripUrl = url + '?strip_id=%s'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "src", r'\.\./images/arrowbuttons/onback\.jpg'))
    help = 'Index format: nnn'


class GleefulNihilism(_BasicScraper):
    url = 'http://gleefulnihilism.com/'
    stripUrl = url + 'comics/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://gleefulnihilism\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://gleefulnihilism\.com/comics/[^"]+)') + 'Previous')
    help = 'Index format: yyyy/mm/dd/stripname'


class Goats(_BasicScraper):
    url = 'http://www.goats.com/'
    stripUrl = url + 'archive/%s.html'
    imageSearch = compile(r'<img.+?src="(/comix/.+?)"')
    prevSearch = compile(r'<a href="(/archive/\d{6}.html)" class="button" title="go back">')
    help = 'Index format: yymmdd'


class GoblinsComic(_BasicScraper):
    url = 'http://www.goblinscomic.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '06252005'
    prevSearch = compile(tagre("a", "href", r'(http://www\.goblinscomic\.com/\d+/)', after="prev"))
    imageSearch = compile(tagre("img", "src", r'(http://www\.goblinscomic\.com/comics/\d+\.[^"]+)'))
    help = 'Index format: ddmmyyyy'


class GoneWithTheBlastwave(_BasicScraper):
    url = 'http://www.blastwave-comic.com/index.php?p=comic&nro=1'
    starter = indirectStarter(url,
                              compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/latest'))
    stripUrl = url[:-1] + '%s'
    imageSearch = compile(r'<img.+src=".+(/comics/.+?)"')
    prevSearch = compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/previous')
    help = 'Index format: n'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%02d' % int(compile(r'nro=(\d+)').search(pageUrl).group(1))


class GrrlPower(_BasicScraper):
    url = 'http://www.grrlpowercomic.com/'
    stripUrl = url + 'archives/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.grrlpowercomic\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.grrlpowercomic\.com/archives/\d+)', after="navi-prev"))
    help = 'Index format: number'


class GunnerkrigCourt(_BasicScraper):
    url = 'http://www.gunnerkrigg.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?p=\d+)') + tagre("img", "src", "http://www\.gunnerkrigg\.com/images/prev_a\.jpg"))
    help = 'Index format: number'


class Gunshow(_BasicScraper):
    url = 'http://gunshowcomic.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://gunshowcomic\.com/comics/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'[^"]*menu/small/previous\.gif'))
    help = 'Index format: n'


class GUComics(_BasicScraper):
    url = 'http://www.gucomics.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d{4}/gu_[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\d+)') +
      tagre("img", "src", r'/images/nav/prev\.png'))
    help = 'Index format: yyyymmdd'

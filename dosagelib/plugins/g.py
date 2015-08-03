# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from ..util import tagre


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
    starter = indirectStarter(url,
       compile(tagre("a", "href", r'(%spages/[^"]+)' % rurl, after="nav-last")))
    stripUrl = baseUrl + 'pages/page-%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/sites/\d+/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%spages/[^"]+)' % rurl, after="prev"))
    help = 'Index format: n (unpadded)'


class GastroPhobia(_BasicScraper):
    url = 'http://www.gastrophobia.com/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '2008-07-30'
    imageSearch = compile(r'<img src="(http://gastrophobia.com/comix/[^"]+)"[^>]*>(?!<br>)')
    prevSearch = compile(r'<a href="(.+?)"><img src="pix/prev.gif" ')
    help = 'Index format: yyyy-mm-dd'


class Geeks(_BasicScraper):
    url = 'http://sevenfloorsdown.com/geeks/'
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '10'
    imageSearch = compile(r'<img src=\'(http://sevenfloorsdown.com/geeks/comics/.+?)\'')
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


# 403 error when getting image files, disable for now
class _GeneralProtectionFault(_BasicScraper):
    url = 'http://www.gpf-comics.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s'
    firstStripUrl = stripUrl % '1998/11/02'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl) +
        tagre("img", "alt", "Previous Comic"))
    help = 'Index format: yyyy/mm/dd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Remove random stuff from filename."""
        imageName = imageUrl.split('/')[-1]
        return imageName[:11] + imageName[-4:]


class GirlGenius(_BasicScraper):
    baseUrl = 'http://www.girlgeniusonline.com/'
    rurl = escape(baseUrl)
    url = baseUrl + 'comic.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20021104'
    imageSearch = compile(tagre("img", "src", r"(%sggmain/strips/[^']*)" % rurl, quote="'"))
    prevSearch = compile(tagre("a", "id", "topprev", quote="\"",
                            before=r"(%s[^\"']+)" % rurl))
    multipleImagesPerStrip = True
    help = 'Index format: yyyymmdd'

class GirlsWithSlingshots(_BasicScraper):
    url = 'http://www.girlswithslingshots.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'gws1'
    imageSearch = (
        compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(http://cdn\.girlswithslingshots\.com/comics/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="prev"))
    help = 'Index format: stripname'


class GlassHalfEmpty(_BasicScraper):
    url = 'http://www.defectivity.com/ghe/index.php'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "src", r'\.\./images/arrowbuttons/onback\.jpg'))
    help = 'Index format: nnn'


class GleefulNihilism(_BasicScraper):
    url = 'http://gleefulnihilism.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'amoeba'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl) + '&lsaquo;')
    help = 'Index format: stripname'


class GoblinsComic(_BasicScraper):
    url = 'http://www.goblinscomic.org/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '06252005'
    prevSearch = compile(tagre("a", "href", r'(%s[-\d]+/)' % rurl, after="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+\.[^"]+)' % rurl))
    help = 'Index format: ddmmyyyy'


class GoneWithTheBlastwave(_BasicScraper):
    url = 'http://www.blastwave-comic.com/index.php?p=comic&nro=1'
    starter = indirectStarter(url,
                              compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/latest'))
    stripUrl = url[:-1] + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<img.+src=".+(/comics/.+?)"')
    prevSearch = compile(r'href="(index.php\?p=comic&amp;nro=\d+)"><img src="images/page/default/previous')
    help = 'Index format: n'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%02d' % int(compile(r'nro=(\d+)').search(pageUrl).group(1))


class GrrlPower(_BasicScraper):
    url = 'http://grrlpowercomic.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '48'
    imageSearch = compile(tagre("img", "src", r'(.*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(.*/archives/\d+)', after="navi-prev"))
    help = 'Index format: number'


class GunnerkriggCourt(_BasicScraper):
    url = 'http://www.gunnerkrigg.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?p=\d+)') + tagre("img", "src", "http://www\.gunnerkrigg\.com/images/prev_a\.jpg"))
    help = 'Index format: number'


class Gunshow(_BasicScraper):
    url = 'http://gunshowcomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://gunshowcomic\.com/comics/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'[^"]*menu/small/previous\.gif'))
    help = 'Index format: n'


class GUComics(_BasicScraper):
    url = 'http://www.gucomics.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '20000710'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d{4}/gu_[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\d+)') +
      tagre("img", "src", r'/images/nav/prev\.png'))
    help = 'Index format: yyyymmdd'

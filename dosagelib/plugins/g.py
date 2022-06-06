# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import ComicControlScraper, WordPressScraper, WordPressNavi


class Galaxion(WordPressNavi):
    url = 'http://galaxioncomics.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1-comic/the-story-so-far/the-story-so-far'
    multipleImagesPerStrip = True
    help = 'Index format: n-comic/book-n/chapter-n/title-nnn'


class Garanos(WordPressScraper):
    stripUrl = ('https://web.archive.org/web/20180314181433/'
        'http://garanos.alexheberling.com/pages/%s/')
    url = stripUrl % 'page-487'
    firstStripUrl = stripUrl % 'vol01'
    endOfLife = True


class GastroPhobia(_ParserScraper):
    url = 'http://www.gastrophobia.com/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '2008-07-30'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//div[@id="prev"]/a'
    help = 'Index format: yyyy-mm-dd'


class Geeks(_ParserScraper):
    url = ('https://web.archive.org/web/20190527194921/'
        'http://sevenfloorsdown.com/geeks/')
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '10'
    imageSearch = '//div[@id="comic"]/img'
    prevSearch = '//a[contains(text(), "Previous")]'
    endOfLife = True
    help = 'Index format: nnn'


class GeeksNextDoor(_ParserScraper):
    url = 'http://www.geeksnextcomic.com/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '2007-03-27'  # '2010-10-04'
    imageSearch = '//p/img'
    prevSearch = (
        '//a[img[contains(@src, "/nav_prev")]]',
        '//a[contains(text(), "< prev")]',  # start page is different
    )
    help = 'Index format: yyyy-mm-dd'


class Ginpu(WordPressNavi):
    url = 'https://www.ginpu.us/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'filler-2'

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 3)
        return '%s-%s_%s' % (filename[1], filename[2], filename[3])


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
    url = 'https://girlswithslingshots.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'gws1'
    imageSearch = (
        compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl)),
        compile(tagre("img", "src",
                      r'(http://cdn\.girlswithslingshots\.com/comics/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl,
                               before='rel="prev"'))
    help = 'Index format: stripname'


class GleefulNihilism(WordPressScraper):
    url = ('https://web.archive.org/web/20170911203122/'
        'http://gleefulnihilism.com/')
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'amoeba'
    endOfLife = True
    help = 'Index format: stripname'


class GoblinsComic(ComicControlScraper):
    url = 'http://www.goblinscomic.org/'


class GodChild(WordPressScraper):
    url = 'http://godchild.keenspot.com/'


class GoGetARoomie(ComicControlScraper):
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


class GrrlPower(WordPressScraper):
    url = 'https://grrlpowercomic.com/'
    stripUrl = url + 'archives/comic/%s/'
    firstStripUrl = stripUrl % 'gp0001'

    def __init__(self, name):
        super().__init__(name)
        self.session.add_throttle('grrlpowercomic.com', 1.0, 1.5)


class GuildedAge(WordPressScraper):
    url = 'http://guildedage.net/'
    firstStripUrl = url + 'comic/chapter-1-cover/'


class GUComics(_BasicScraper):
    url = 'http://www.gucomics.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '20000710'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d{4}/gu_[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\d+)') +
                         tagre("img", "src", r'/images/nav/prev\.png'))
    help = 'Index format: yyyymmdd'


class GunnerkriggCourt(_ParserScraper):
    url = 'http://www.gunnerkrigg.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@class="comic_image"]'
    prevSearch = '//a[./img[contains(@src, "prev")]]'
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

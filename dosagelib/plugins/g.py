# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import compile

from ..scraper import _BasicScraper, _ParserScraper, ParserScraper
from ..helpers import indirectStarter
from ..util import tagre, getQueryParams
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


class GastroPhobia(ComicControlScraper):
    url = 'https://gastrophobia.com/'
    firstStripUrl = url + 'comix/the-mane-event'


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
    imageSearch = ('//p/img', '//p/span/img')
    prevSearch = (
        '//a[img[contains(@src, "/nav_prev")]]',
        '//a[contains(text(), "< prev")]',  # start page is different
    )
    help = 'Index format: yyyy-mm-dd'


class GirlGenius(ParserScraper):
    url = 'https://www.girlgeniusonline.com/comic.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20021104'
    imageSearch = '//img[@alt="Comic"]'
    prevSearch = '//a[@id="topprev"]'
    multipleImagesPerStrip = True
    help = 'Index format: yyyymmdd'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return not data.xpath('//div[@id="comicbody"]//img[contains(@src, "comic")]')


class GirlsWithSlingshots(ComicControlScraper):
    url = 'https://girlswithslingshots.com/'
    firstStripUrl = url + 'comic/gws1'


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


class GoneWithTheBlastwave(ParserScraper):
    stripUrl = 'http://www.blastwave-comic.com/index.php?p=comic&nro=%s'
    firstStripUrl = stripUrl % '1'
    url = firstStripUrl
    starter = indirectStarter
    imageSearch = '//*[@id="comic_ruutu"]/center/img'
    prevSearch = '//a[img[contains(@src, "previous")]]'
    latestSearch = '//a[img[contains(@src, "latest")]]'
    help = 'Index format: n'

    def namer(self, image_url, page_url):
        return '%02d' % int(getQueryParams(page_url)['nro'][0])


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


class GUComics(ParserScraper):
    stripUrl = 'https://www.gucomics.com/%s'
    url = stripUrl % 'comic/'
    firstStripUrl = stripUrl % '20000710'
    imageSearch = '//img[contains(@src, "/comics/2")]'
    prevSearch = '//a[img[contains(@alt, "previous")]]'
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

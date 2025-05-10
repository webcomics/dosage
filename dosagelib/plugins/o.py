# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import compile, escape

from ..helpers import bounceStarter, indirectStarter
from ..scraper import ParserScraper, _BasicScraper, _ParserScraper
from ..util import tagre
from .common import WordPressNavi, WordPressScraper


class OccasionalComicsDisorder(WordPressScraper):
    url = 'https://occasionalcomics.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'latest-comic-2'


class OctopusPie(_ParserScraper):
    url = 'http://www.octopuspie.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007-05-14/001-pea-wiggle'
    imageSearch = '//img[@title]'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy-mm-dd/nnn-strip-name'


class OffWhite(ParserScraper):
    baseUrl = 'https://web.archive.org/web/20200627222318/http://off-white.eu/'
    stripUrl = baseUrl + 'comic/%s/'
    firstStripUrl = stripUrl % 'prologue-page-1-2'
    url = firstStripUrl
    imageSearch = '//img[@class="comic-page"]'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[text()="A"]'
    starter = indirectStarter
    endOfLife = True


class Oglaf(_ParserScraper):
    url = 'http://oglaf.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'cumsprite'
    imageSearch = '//img[@id="strip"]'
    prevSearch = '//a[@rel="prev"]'
    nextSearch = '//a[@rel="next"]'
    multipleImagesPerStrip = True
    adult = True

    def extract_image_urls(self, url, data):
        urls = super().extract_image_urls(url, data)
        try:
            nexturl = self.fetchUrls(url, data, self.nextSearch)[0]
            while nexturl.startswith(url):
                data = self.getPage(nexturl)
                urls.extend(super().extract_image_urls(url, data))
                nexturl = self.fetchUrls(url, data, self.nextSearch)[0]
        except ValueError:
            pass
        return urls


class OhJoySexToy(WordPressNavi):
    url = 'http://www.ohjoysextoy.com/'
    firstStripUrl = url + 'introduction/'
    textSearch = '//div[@id="comic"]//img/@alt'
    multipleImagesPerStrip = True
    adult = True


class OkCancel(_BasicScraper):
    url = 'http://okcancel.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%sstrips/okcancel\d{8}\.gif)' % rurl))
    prevSearch = compile(tagre("div", "class", "previous") +
                         tagre("a", "href", r'(%scomic/\d{1,4}\.html)' % rurl))
    help = 'Index format: yyyymmdd'


class OmakeTheater(_ParserScraper):
    url = 'http://omaketheater.com/comic/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    css = True
    imageSearch = ".comicImage img"
    prevSearch = ".previous a"
    help = 'Index format: number (unpadded)'


class OnTheEdge(WordPressScraper):
    url = 'http://ontheedgecomics.com/'
    firstStripUrl = 'http://ontheedgecomics.com/comic/ote0001/'


class OopsComicAdventure(WordPressScraper):
    url = ('https://web.archive.org/web/20190102215141/'
        'http://oopscomicadventure.com/')
    endOfLife = True


class Optipess(WordPressNavi):
    url = 'http://www.optipess.com/'
    firstStripUrl = url + '2008/12/01/jason-friend-of-the-butterflies/'
    textSearch = '//div[@id="comic"]//img/@alt'
    textOptional = True


class OrderOfTheBlackDog(WordPressScraper):
    url = 'http://orderoftheblackdog.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        return '%s.%s' % (pageUrl.rsplit('/', 2)[-2], imageUrl.rsplit('.', 1)[-1])


class OriginalLife(_ParserScraper):
    url = 'https://web.archive.org/web/20200201203404/http://jaynaylor.com/originallife/'
    stripUrl = url + 'archives/%s.html'
    firstStripUrl = stripUrl % '2009/06/001'
    imageSearch = '//img[contains(@src, "/originallife/comic/")]'
    prevSearch = '//a[contains(text(), "Previous")]'
    adult = True
    endOfLife = True


class OurHomePlanet(_ParserScraper):
    url = 'http://www.ourhomeplanet.net/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '01'
    imageSearch = '//a[@rel="next"]/img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: n (unpadded)'


class OutOfPlacers(WordPressScraper):
    url = 'http://www.valsalia.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'prologue/01'
    adult = True


class OverCompensating(ParserScraper):
    stripUrl = 'https://www.wigucomics.com/oc/index.php?comic=%s'
    url = stripUrl % '-1'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//center//img'
    prevSearch = '//a[@alt="go back"]'
    endOfLife = True
    help = 'Index format: number'


class OzyAndMillie(WordPressScraper):
    stripUrl = 'https://ozyandmillie.org/comic/%s/'
    url = stripUrl % 'ozy-and-millie-2131'
    firstStripUrl = stripUrl % 'ozy-and-millie-2'
    endOfLife = True

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
import os
from re import IGNORECASE, compile

from .. import util
from ..helpers import bounceStarter, indirectStarter, joinPathPartsNamer
from ..scraper import ParserScraper, _BasicScraper, _ParserScraper
from ..util import tagre
from .common import (
    ComicControlScraper,
    WordPressNavi,
    WordPressScraper,
    WordPressWebcomic,
)


class EarthsongSaga(_ParserScraper):
    stripUrl = 'http://earthsongsaga.com/vol%s'
    url = stripUrl % '5/epilogue5.php'
    firstStripUrl = stripUrl % '1/vol1cover.php'
    imageSearch = '//img[contains(@src, "images/vol")]'
    prevSearch = ('//a[@title="Previous"]', '//td[@width=98]//a')
    endOfLife = True

    def namer(self, image_url, page_url):
        imgmatch = compile(r'images/vol(\d+)/ch(?:apter)?(\d+)/(.*)\.\w+$',
                           IGNORECASE).search(image_url)
        if imgmatch:
            return 'vol%02d_ch%02d_%s' % (int(imgmatch.group(1)),
                int(imgmatch.group(2)), imgmatch.group(3))
        imgmatch = compile(r'images/vol(\d+)/[^/]*cover[^/]*$',
                           IGNORECASE).search(image_url)
        return 'vol%02dcover' % (int(imgmatch.group(1)))

    def getPrevUrl(self, url, data):
        # Fix wrong navigation links
        if url == self.stripUrl % '1/63.php':
            return self.stripUrl % '1/62.php'
        elif url == self.stripUrl % '2/vol2cover.html':
            return self.stripUrl % '1/121.php'
        elif url == self.stripUrl % '3/1.html':
            return self.stripUrl % '3/ch7cover.html'

        return super().getPrevUrl(url, data)


class EatLiver(_ParserScraper):
    url = 'http://www.eatliver.com/'
    starter = indirectStarter
    multipleImagesPerStrip = True
    imageSearch = '//div[d:class("post-content")]//img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@rel="bookmark"]'


class EatThatToast(WordPressScraper):
    url = 'http://eatthattoast.com/'
    firstStripUrl = url + 'comic/thewizard/'
    textSearch = WordPressScraper.imageSearch + '/@alt'


class EdibleDirt(_BasicScraper):
    url = 'http://eddirt.frozenreality.co.uk/'
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?id=\d+)") +
                         "Previous")
    help = 'Index format: number'


class EdmundFinney(WordPressNavi):
    url = 'http://eqcomics.com/'
    firstStripUrl = url + '2009/03/08/sunday-aliens/'


class ElfOnlyInn(_BasicScraper):
    url = 'http://www.elfonlyinn.net/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20020523'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
                         tagre("img", "src", r'/images/previous_day\.gif'))
    help = 'Index format: yyyymmdd'


class ElGoonishShive(ComicControlScraper):
    url = 'http://www.egscomics.com/'


class ElGoonishShiveNP(ComicControlScraper):
    url = 'http://www.egscomics.com/egsnp.php'


class EmergencyExit(_BasicScraper):
    url = 'http://www.eecomics.net/'
    stripUrl = url + "?strip_id=%s"
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "alt", r"Prior"))
    help = 'Index format: n'


class Erfworld(ParserScraper):
    stripUrl = 'https://archives.erfworld.com/%s'
    url = stripUrl % 'getLatestPage.php'
    firstStripUrl = stripUrl % 'Kickstarter+Stories/1'
    imageSearch = '//div[@class="page_content"]//img'
    textSearch = '//div[@class="page_content"]'
    prevSearch = '//li[@class="previous"]/a'
    nextSearch = '//li[@class="next"]/a'
    multipleImagesPerStrip = True
    textOptional = True
    starter = bounceStarter

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return not self.match(data, self.imageSearch)

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        page = util.urlpathsplit(pageUrl.replace('+', '-'))
        return '_'.join(page[:1] + [filename])

    def getPrevUrl(self, url, data):
        # Fix missing navigation links between books
        if url == self.stripUrl % 'Book+5/1':
            return self.stripUrl % 'Book+4/203'
        elif url == self.stripUrl % 'Book+4/1':
            return self.stripUrl % 'Book+3/145'
        elif url == self.stripUrl % 'Book+3/1':
            return self.stripUrl % 'Book+2/231'
        elif url == self.stripUrl % 'Book+2/1':
            return self.stripUrl % 'Book+1/184'
        elif url == self.stripUrl % 'Book+1/1':
            return self.stripUrl % 'Book+0/81'
        elif url == self.stripUrl % 'Book+0/1':
            return self.stripUrl % 'Kickstarter+Stories/54'
        return super().getPrevUrl(url, data)


class ErmaFelnaEDF(ParserScraper):
    stripUrl = 'https://www.stevegallacci.com/archive/edf/%s'
    firstStripUrl = stripUrl % '0000/00/00'
    url = firstStripUrl
    imageSearch = '//img[@id="comic-container"]'
    prevSearch = '//a[@title="Previous Comic"]'
    latestSearch = '//a[@title="Current Comic"]'
    starter = indirectStarter

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        postDate = '-'.join(util.urlpathsplit(pageUrl)[-3:])
        filename = imageUrl.rsplit('/', 1)[-1]
        return f'{postDate}_{filename}'


class ErrantStory(_BasicScraper):
    url = 'http://www.errantstory.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'<img[^>]+?src="([^"]*?comics/.+?)"')
    prevSearch = compile(r'><a href="(.+?)">&lt;Previous</a>')
    help = 'Index format: yyyy-mm-dd/num'


class Erstwhile(WordPressNavi):
    url = 'http://www.erstwhiletales.com/'
    endOfLife = True


class EverybodyLovesEricRaymond(_ParserScraper):
    url = 'http://geekz.co.uk/lovesraymond/'
    firstStripUrl = url + 'archive/slashdotted'
    imageSearch = '//div[d:class("entry-content")]//img'
    prevSearch = '//a[@rel="prev"]'


class EvilDiva(WordPressScraper):
    url = ('https://web.archive.org/web/20190221223751/'
        'https://www.evildivacomics.com/')
    firstStripUrl = url + 'comic/evil-diva-issue-1-cover/'
    endOfLife = True


class EvilInc(ParserScraper):
    url = 'https://www.evil-inc.com/'
    imageSearch = ('//div[@id="unspliced-comic"]/img',
        '//div[@id="unspliced-comic"]/picture//img')
    prevSearch = '//a[./i[d:class("fa-chevron-left")]]'
    firstStripUrl = url + 'comic/monday-3/'


class Evilish(ParserScraper):
    url = ('https://web.archive.org/web/20220125053115/'
        'http://evilish.pensandtales.com/')
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20020630'
    imageSearch = '//img[@alt="Today\'s Comics"]'
    prevSearch = '//a[img[@alt="Previous Comic"]]'
    endOfLife = True
    help = 'Index format: yyyymmdd'


class Evon(WordPressScraper):
    url = 'http://evoncomics.com/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'chapter-1'
    adult = True


class ExorcismAcademy(WordPressWebcomic):
    url = 'https://ea.asmodrawscomics.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'title-page'
    multipleImagesPerStrip = True
    adult = True
    namer = joinPathPartsNamer(imageparts=range(-3, 0))


class ExploitationNow(WordPressNavi):
    url = 'http://www.exploitationnow.com/'
    firstStripUrl = url + '2000-07-07/9'
    endOfLife = True


class Exvulnerum(_ParserScraper):
    url = 'https://zules.com/exvulnerum/'
    stripUrl = url + 'comic.php?page=%s'
    firstStripUrl = stripUrl.replace('comic', 'newprologue') % '1'
    imageSearch = ('//img[contains(@src, "pages/")]',
                   '//img[contains(@src, "newprologue/")]')
    prevSearch = '//a[./img[contains(@src, "nav_prev")]]'


class ExtraFabulousComics(WordPressScraper):
    url = 'https://extrafabulouscomics.com/'
    firstStripUrl = url + 'comic/buttfly/'
    starter = bounceStarter
    multipleImagesPerStrip = True

    def namer(self, image_url, page_url):
        imagename = os.path.basename(image_url)
        pagepart = compile(r'/comic/([^/]+)/$').search(page_url).group(1)
        return '_'.join((pagepart, imagename))

    def shouldSkipUrl(self, url, data):
        return self.match(data, '//div[@id="comic"]//iframe')


class ExtraLife(_BasicScraper):
    url = 'http://www.myextralife.com/'
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.myextralife\.com/wp-content/uploads/[^"]+)', before="comic"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', before="prev_comic"))
    help = 'Index format: stripname'


class ExtraOrdinary(_ParserScraper):
    url = 'https://www.exocomics.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '01'
    prevSearch = '//a[d:class("prev")]'
    imageSearch = '//img[d:class("image-style-main-comic")]'
    help = 'Index format: number'

# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2021 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import bounceStarter, indirectStarter
from ..util import tagre
from .common import ComicControlScraper, WordPressScraper, WordPressNaviIn


class Lackadaisy(_ParserScraper):
    url = 'https://www.lackadaisy.com/comic.php'
    stripUrl = url + '?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="content"]/img'
    prevSearch = '//div[@class="prev"]/a'
    nextSearch = '//div[@class="next"]/a'
    help = 'Index format: n'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        # Use comic id for filename
        num = pageUrl.rsplit('=', 1)[-1]
        ext = imageUrl.rsplit('.', 1)[-1]
        return 'lackadaisy_%s.%s' % (num, ext)


class LastResort(WordPressScraper):
    url = 'http://www.lastres0rt.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'that-sound-you-hear-is-a-shattered-stereotype'


class LazJonesAndTheMayfieldRegulators(_ParserScraper):
    baseUrl = 'https://www.lazjones.com/'
    url = baseUrl + 'regulators'
    stripUrl = baseUrl + 'comic/%s'
    firstStripUrl = stripUrl % 'chapter1_00'
    imageSearch = '//img[contains(@src, "comic/pages/")]'
    prevSearch = '//a[contains(text(), "Previous")]'


class LazJonesAndTheMayfieldRegulatorsSideStories(LazJonesAndTheMayfieldRegulators):
    name = 'LazJonesAndTheMayfieldRegulators/SideStories'
    baseUrl = 'https://www.lazjones.com/'
    url = baseUrl + 'comics'
    stripUrl = baseUrl + 'comic/%s'
    firstStripUrl = stripUrl % 'journal01'

    def getPrevUrl(self, url, data):
        # Fix broken navigation links
        if url == self.url and data.xpath(self.prevSearch + '/@href')[0] == self.stripUrl % 'summer00':
            return self.stripUrl % 'summer21'
        return super(LazJonesAndTheMayfieldRegulators, self).getPrevUrl(url, data)


class LeastICouldDo(_ParserScraper):
    url = 'https://leasticoulddo.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '20030210'
    imageSearch = '//div[@id="content-comic"]//img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@id="latest-comic"]'
    starter = indirectStarter
    help = 'Index format: yyyymmdd'


class LetsSpeakEnglish(ComicControlScraper):
    url = 'http://www.marycagle.com'


class LifeAintNoPonyFarm(WordPressScraper):
    url = ('https://web.archive.org/web/20181221154155/'
        'http://sarahburrini.com/en/')
    firstStripUrl = url + 'comic/my-first-webcomic/'
    multipleImagesPerStrip = True
    endOfLife = True


class LifeAsRendered(_ParserScraper):
    # Reverse navigation doesn't work properly, so search forward instead
    stripUrl = 'https://kittyredden.com/LAR/%s/'
    url = stripUrl % '0100'
    firstStripUrl = stripUrl % '05extra'
    imageSearch = '//figure[@class="wp-block-image"]//img'
    prevSearch = '//a[img[@alt="Next"]]'
    textSearch = '//div[@class="entry-content"]//text()'
    adult = True
    endOfLife = True
    nav = {
        '0140': '0200',
        '0272': '02ss00',
        '02SS14': '0300',
        '0367': '03ss00',
        '03ss10': '0400',
        '0408': '0409',
        '0409': '0410',
        '0421': '0422',
        '0449': '0450',
        '0458': '0460',
        '0460': '04ss00',
        '04ss00': '04ss01',
        '04ss10': '0500',
        '0500': '0501',
        '0508': '0509',
        '0558': '0559',
        '0577': '05extra',
    }

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        return filename.replace('ReN', 'N').replace('N01P', 'A02S')

    def fetchUrls(self, url, data, urlSearch):
        # Fix missing image link
        if 'LAR/0403' in url and urlSearch == self.imageSearch:
            return [self.stripUrl.rstrip('/') % 'A04/A04P03.png']
        return super(LifeAsRendered, self).fetchUrls(url, data, urlSearch)

    def getPrevUrl(self, url, data):
        # Fix broken navigation links
        page = url.rstrip('/').rsplit('/', 1)[-1]
        if page in self.nav:
            return self.stripUrl % self.nav[page]
        return super(LifeAsRendered, self).getPrevUrl(url, data)

    def fetchText(self, url, data, textSearch, optional):
        # Save final summary text
        if url == self.firstStripUrl:
            url = self.stripUrl % 'the-end'
            data = self.getPage(url)
            return super(LifeAsRendered, self).fetchText(url, data, textSearch, optional)
        return None


class LilithsWord(ComicControlScraper):
    url = 'http://www.lilithword.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'prologue-page-00'

    def namer(self, imageUrl, pageUrl):
        return imageUrl.rsplit('/', 1)[-1].split('-', 1)[1]


class LittleGamers(_BasicScraper):
    url = 'http://www.little-gamers.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2000/12/01/99'
    imageSearch = compile(tagre("img", "src", r'(http://little-gamers\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.little-gamers\.com/[^"]+)', before="comic-nav-prev-link"))
    help = 'Index format: yyyy/mm/dd/name'


class LittleTales(_ParserScraper):
    url = 'http://www.little-tales.com/'
    stripUrl = url + 'index.php?Strip=%s'
    firstStripUrl = stripUrl % '1'
    url = stripUrl % '450'
    imageSearch = '//img[contains(@src, "strips/")]'
    prevSearch = '//a[./img[@alt="BACK"]]'
    nextSearch = '//a[./img[@alt="FORWARD"]]'
    starter = bounceStarter
    nav = {
        '517': '515',
        '449': '447',
    }

    def namer(self, imageUrl, pageUrl):
        page = pageUrl.rsplit('=', 1)[-1]
        ext = imageUrl.rsplit('.', 1)[-1]
        return page + '.' + ext

    def getPrevUrl(self, url, data):
        # Skip missing pages with broken navigation links
        page = url.rsplit('=', 1)[1]
        if page in self.nav:
            return self.stripUrl % self.nav[page]
        return super(LittleTales, self).getPrevUrl(url, data)


class LoadingArtist(_ParserScraper):
    url = 'https://loadingartist.com/'
    firstStripUrl = url + 'comic/born/'
    imageSearch = '//div[d:class("main-image-container")]//img'
    prevSearch = '//div[d:class("left-nav")]//a'
    latestSearch = '//nav//a[text()="Comic"]'
    starter = indirectStarter


class LoFiJinks(WordPressNaviIn):
    baseUrl = 'https://hijinksensue.com/comic/'
    url = baseUrl + 'learning-to-love-again/'
    firstStripUrl = baseUrl + 'lo-fijinks-everything-i-know-anout-james-camerons-avatar-movie/'
    endOfLife = True


class LookingForGroup(_ParserScraper):
    url = 'https://www.lfg.co/'
    stripUrl = url + 'page/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic-img"]//img'
    prevSearch = '//a[@class="comic-nav-prev"]'
    latestSearch = '//div[@id="feature-lfg-footer"]/a[contains(@href, "page/")]'
    starter = indirectStarter
    help = 'Index format: nnn'

    def namer(self, imageUrl, pageUrl):
        page = pageUrl.rstrip('/').rsplit('/', 1)[-1]
        return page.replace('2967', '647')

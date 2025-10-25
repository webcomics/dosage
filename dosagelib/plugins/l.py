# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from .. import util
from ..helpers import bounceStarter, indirectStarter
from ..scraper import ParserScraper, _ParserScraper
from .common import ComicControlScraper, WordPressScraper


class Lancer(WordPressScraper):
    url = 'https://lancercomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'chapter-1-cover'


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
        if url == self.url and self.match(data, self.prevSearch + '/@href')[0] == self.stripUrl % 'summer00':
            return self.stripUrl % 'summer21'
        return super(LazJonesAndTheMayfieldRegulators, self).getPrevUrl(url, data)


class LeastICouldDo(ParserScraper):
    @property
    def url(self):
        """Find today's strip (or most recent non-Sunday)"""
        import datetime
        today = datetime.date.today()
        
        # If today is Sunday, go back to Saturday
        if today.weekday() == 6:  # Sunday
            today = today - datetime.timedelta(days=1)
        
        today_str = today.strftime('%Y%m%d')
        return f'https://leasticoulddo.com/comic/{today_str}'
    
    stripUrl = 'https://leasticoulddo.com/comic/%s'
    firstStripUrl = stripUrl % '20030210'
    imageSearch = '//div[contains(@class, "elementor-widget-image")]//img[contains(@src, "licd") and contains(@src, "desktop-scaled")]'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyymmdd'


class LeastICouldDoBeginnings(_ParserScraper):
    @property
    def url(self):
        """Find the most recent Sunday for Beginnings strips"""
        import datetime
        today = datetime.date.today()
        
        # Find the most recent Sunday (0=Monday, 6=Sunday)
        days_since_sunday = (today.weekday() + 1) % 7
        if days_since_sunday == 0:  # Today is Sunday
            most_recent_sunday = today
        else:
            most_recent_sunday = today - datetime.timedelta(days=days_since_sunday)
        
        sunday_str = most_recent_sunday.strftime('%Y%m%d')
        return f'https://leasticoulddo.com/comic/{sunday_str}'
    
    stripUrl = 'https://leasticoulddo.com/comic/%s'
    firstStripUrl = stripUrl % '20081109'  # First Sunday Beginnings strip  
    imageSearch = '//div[contains(@class, "elementor-widget-image")]//img[contains(@src, "beg") and contains(@src, "desktop-scaled")]'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyymmdd (Sunday "Beginnings" strips)'
    

class LetsSpeakEnglish(ComicControlScraper):
    url = 'http://www.marycagle.com'


class LifeAintNoPonyFarm(WordPressScraper):
    url = ('https://web.archive.org/web/20181221154155/'
        'http://sarahburrini.com/en/')
    firstStripUrl = url + 'comic/my-first-webcomic/'
    multipleImagesPerStrip = True
    endOfLife = True


class LifeAsRendered(ParserScraper):
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

    def extract_image_urls(self, url, data):
        # Fix missing image link
        if 'LAR/0403' in url:
            return [self.stripUrl.rstrip('/') % 'A04/A04P03.png']
        return super().extract_image_urls(url, data)

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


class LittleGamers(ParserScraper):
    url = 'https://www.little-gamers.com/'
    firstStripUrl = url + '2000/12/01/99'
    imageSearch = '//div[d:class("comic")]//img'
    prevSearch = ('//a[@id="previous"]',
        '//div[d:class("comic-navigation")]//a[text()="previous"]')


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


class LoFiJinks(WordPressScraper):
    baseUrl = 'https://hijinksensue.com/comic/'
    url = baseUrl + 'learning-to-love-again/'
    firstStripUrl = baseUrl + 'lo-fijinks-everything-i-know-anout-james-camerons-avatar-movie/'
    endOfLife = True


class LookingForGroup(ParserScraper):
    url = 'https://www.lfg.co/'
    stripUrl = url + 'page/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic-img"]//img'
    prevSearch = '//a[d:class("comic-nav-prev")]'
    latestSearch = '//div[@id="feature-lfg-footer"]/a[contains(@href, "page/")]'
    starter = indirectStarter
    help = 'Index format: nnn'

    def namer(self, imageUrl, pageUrl):
        page = util.urlpathsplit(pageUrl)[-1]
        return page.replace('2967', '647')

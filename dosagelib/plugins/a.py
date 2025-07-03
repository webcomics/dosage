# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import MULTILINE, compile

from ..helpers import bounceStarter, indirectStarter, joinPathPartsNamer
from ..scraper import ParserScraper, _BasicScraper, _ParserScraper
from ..util import tagre
from .common import WordPressNavi, WordPressScraper, WordPressWebcomic


class AbstruseGoose(ParserScraper):
    url = 'https://web.archive.org/web/20230930172141/https://abstrusegoose.com/'
    starter = bounceStarter
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "/strips/")]'
    textSearch = imageSearch + '/@title'
    textOptional = True
    prevSearch = '//a[contains(text(), "Previous")]'
    nextSearch = '//a[contains(text(), "Next")]'
    help = 'Index format: n (unpadded)'

    def namer(self, imageurl, pageurl):
        index = int(pageurl.rsplit('/', 1)[1])
        name = imageurl.rsplit('/', 1)[1]
        return 'c%03d-%s' % (index, name)


class AbsurdNotions(_BasicScraper):
    baseUrl = 'http://www.absurdnotions.org/'
    url = baseUrl + 'page129.html'
    stripUrl = baseUrl + 'page%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src', r'(an[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre('a', 'href', r'([^"]+)') +
                         tagre('img', 'src', r'nprev\.gif'))
    help = 'Index format: n (unpadded)'


class Achewood(ParserScraper):
    baseUrl = 'https://achewood.com/'
    stripUrl = baseUrl + '%s/title.html'
    url = stripUrl % '2016/12/25'
    firstStripUrl = stripUrl % '2001/10/01'
    imageSearch = '//img[d:class("comicImage")]'
    prevSearch = '//a[d:class("comic_prev")]'
    namer = joinPathPartsNamer(pageparts=range(0, 3))
    help = 'Index format: yyyy/mm/dd'
    endOfLife = True


class AdventuresOfFifne(_ParserScraper):
    stripUrl = 'http://fifine.purrsia.com/%s.html'
    url = stripUrl % 'COMICS'
    firstStripUrl = stripUrl % 'Fifine01'
    imageSearch = '//img[contains(@src, "jpg")]'
    prevSearch = '//a[text()="PREVIOUS"]'
    multipleImagesPerStrip = True
    endOfLife = True

    def namer(self, imageUrl, pageUrl):
        # Prepend chapter number to image filename
        filename = imageUrl.rsplit('/', 1)[-1]
        if filename[0] == 'p':
            filename = filename.replace('p', '1_p')
        filename = filename.replace('TIL', '2_TIL')
        filename = filename.replace('NS', '3_NS')
        filename = filename.replace('LG', '4_LG')
        filename = filename.replace('WM', '5_WM')
        return filename

    def getPrevUrl(self, url, data):
        # Fix broken navigation links
        if url == self.stripUrl % 'lg06':
            return self.stripUrl % 'lg05'
        return super(AdventuresOfFifne, self).getPrevUrl(url, data)


class AfterStrife(WordPressNavi):
    baseUrl = 'http://afterstrife.com/'
    stripUrl = baseUrl + '?p=%s'
    url = stripUrl % '262'
    firstStripUrl = stripUrl % '1'
    help = 'Index format: nnn'
    endOfLife = True


class AGirlAndHerFed(_ParserScraper):
    url = 'https://agirlandherfed.com/'
    stripUrl = url + '1.%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic-image"]/img'
    prevSearch = '//div[@id="comic-nav"]/a[.//img[contains(@src, "back")]]'
    help = 'Index format: nnn'


class AhoiPolloi(_ParserScraper):
    url = 'https://ahoipolloi.blogger.de/'
    stripUrl = url + '?day=%s'
    firstStripUrl = stripUrl % '20060306'
    multipleImagesPerStrip = True
    lang = 'de'
    imageSearch = '//img[contains(@src, "/static/antville/ahoipolloi/")]'
    prevSearch = '//a[contains(@href, "/?day=")]'
    help = 'Index format: yyyymmdd'


class AirForceBlues(WordPressScraper):
    url = 'https://web.archive.org/web/20210102113825/http://farvatoons.com/'
    firstStripUrl = url + 'comic/in-texas-there-are-texans/'


class ALessonIsLearned(_BasicScraper):
    url = 'http://www.alessonislearned.com/'
    prevSearch = compile(tagre("a", "href", r"(index\.php\?comic=\d+)",
                               quote="'") + r"[^>]+previous")
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(cmx/lesson\d+\.[a-z]+)"))
    help = 'Index format: nnn'


class Alice(WordPressScraper):
    url = 'https://web.archive.org/web/20210115132313/http://www.alicecomics.com/'
    latestSearch = '//a[text()="Latest Alice!"]'
    starter = indirectStarter
    endOfLife = True


class AlienLovesPredator(ParserScraper):
    url = ('https://web.archive.org/web/20161207230717/'
        'http://alienlovespredator.com/')
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2004/10/12/unavoidable-delay'
    imageSearch = '//div[@id="comic"]//p//img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy/mm/dd/name'
    endOfLife = True


class AlienShores(WordPressScraper):
    url = 'http://alienshores.com/alienshores_band/'
    firstStripUrl = url + 'AScomic/updated-cover/'


class AllTheGrowingThings(WordPressScraper):
    url = ('https://web.archive.org/web/20160611212229/'
        'http://growingthings.typodmary.com/')
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'all-the-growing-things'
    endOfLife = True


class AlphaLuna(ParserScraper):
    url = 'https://alphalunacomic.net/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'
    imageSearch = '//main[@id="comic"]//img'
    prevSearch = '//a[@rel="prev"]'


class AlphaLunaSpanish(ParserScraper):
    name = 'AlphaLuna/Spanish'
    lang = 'es'
    url = 'https://alphalunacomic.net/spanish/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'
    imageSearch = '//main[@id="comic"]//img'
    prevSearch = '//a[@rel="prev"]'


class Altermeta(_ParserScraper):
    url = 'http://altermeta.net/'
    stripUrl = url + 'archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[./img[contains(@src, "back")]]'
    nextSearch = '//a[./img[contains(@src, "forward")]]'
    starter = bounceStarter
    help = 'Index format: n (unpadded)'

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rsplit('=', 1)[-1] + '_' + imageUrl.rsplit('/', 1)[-1]


class AltermetaOld(_ParserScraper):
    url = Altermeta.url + 'oldarchive/index.php'
    stripUrl = Altermeta.url + 'oldarchive/archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[text()="Back"]'
    help = 'Index format: n (unpadded)'


class AmazingSuperPowers(WordPressNavi):
    url = 'https://www.amazingsuperpowers.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/09/heredity'
    imageSearch = '//div[d:class("comicpane")]/img'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            # video
            self.stripUrl % '2013/05/orbital-deathray-kickstarter',
        )


class AmbersNoBrainers(_ParserScraper):
    baseUrl = 'https://foxyverse.com/'
    url = baseUrl + 'comics/'
    stripUrl = baseUrl + 'ambers-no-brainers-%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "Page")]'
    latestSearch = '//a[contains(@href, "ambers-no-brainers")]'
    starter = indirectStarter

    def getPrevUrl(self, url, data):
        # Replace missing navigation links
        pageNum = int(url.rstrip('/').rsplit('-', 1)[-1])
        return self.stripUrl % str(pageNum - 1)


class Amya(WordPressScraper):
    url = 'http://www.amyachronicles.com/'


class Angband(ParserScraper):
    url = 'http://angband.calamarain.net/'
    stripUrl = url + '%s'
    imageSearch = '//img'
    multipleImagesPerStrip = True
    endOfLife = True

    def starter(self):
        page = self.getPage(self.url)
        self.pages = self.match(page, '//p/a[not(contains(@href, "cast"))]/@href')
        self.firstStripUrl = self.pages[0]
        return self.pages[-1]

    def getPrevUrl(self, url, data):
        return self.pages[self.pages.index(url) - 1]


class Annyseed(_ParserScraper):
    baseUrl = ('https://web.archive.org/web/20190511031451/'
        'http://www.mirrorwoodcomics.com/')
    stripUrl = baseUrl + 'Annyseed%s.htm'
    url = stripUrl % 'Latest'
    firstStripUrl = stripUrl % '000'
    imageSearch = '//div/img[contains(@src, "Annyseed")]'
    prevSearch = '//a[img[@name="Previousbtn"]]'
    endOfLife = True
    help = 'Index format: nnn'
    FIX_RE = compile(r'Annyseed/Finished%20For%20Print/')

    def imageUrlModifier(self, image_url, data):
        return self.FIX_RE.sub('', image_url)

    def link_modifier(self, fromurl, tourl):
        """Fix circular link."""
        if 'Annyseed150' in fromurl and 'Annyseed150' in tourl:
            return self.stripUrl % '149'
        return tourl


class AntiheroForHire(ParserScraper):
    stripUrl = 'https://www.giantrobot.club/antihero-for-hire/%s'
    firstStripUrl = stripUrl % '2016/6/8/entrance-vigil'
    url = firstStripUrl
    imageSearch = '//div[@class="image-wrapper"]//img[not(@class="thumb-image")]'
    multipleImagesPerStrip = True
    endOfLife = True

    def starter(self):
        # Build list of chapters for navigation
        page = self.getPage(self.url)
        self.chapters = self.match(page, '//ul[d:class("archive-group-list")]//a[d:class("archive-item-link")]/@href')
        return self.chapters[0]

    def getPrevUrl(self, url, data):
        # Retrieve previous chapter from list
        index = self.chapters.index(url) + 1
        return self.chapters[index] if index < len(self.chapters) else None


class AppleGeeks(_BasicScraper):
    url = 'http://www.applegeeks.com/'
    stripUrl = url + 'comics/viewcomic.php?issue=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'((?:/comics/)?issue\d+\.jpg)'))
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    allow_errors = (404,)
    help = 'Index format: n (unpadded)'


class ARedTailsDream(_BasicScraper):
    baseUrl = 'http://www.minnasundberg.fi/'
    stripUrl = baseUrl + 'comic/page%s.php'
    firstStripUrl = stripUrl % '00'
    url = baseUrl + 'comic/recent.php'
    imageSearch = compile(tagre('img', 'src', r'(chapter.+?/eng[^"]*)'))
    prevSearch = compile(tagre('a', 'href', r'(page\d+\.php)') +
                         tagre("img", "src", r'.*?aprev.*?'))
    help = 'Index format: nn'


class ArtificialIncident(WordPressWebcomic):
    url = 'https://www.artificialincident.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'issue-one-life-changing'


class AstronomyPOTD(ParserScraper):
    baseUrl = 'http://apod.nasa.gov/apod/'
    url = baseUrl + 'astropix.html'
    starter = bounceStarter
    stripUrl = baseUrl + 'ap%s.html'
    firstStripUrl = stripUrl % '061012'
    imageSearch = '//a/img'
    multipleImagesPerStrip = True
    prevSearch = '//a[text()="<"]'
    nextSearch = '//a[text()=">"]'
    help = 'Index format: yymmdd'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return self.match(data, '//iframe')  # videos

    def namer(self, image_url, page_url):
        return '%s-%s' % (page_url.split('/')[-1].split('.')[0][2:],
                          image_url.split('/')[-1].split('.')[0])


class ATaleOfTails(WordPressScraper):
    url = 'http://www.feretta.net/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'a-tale-of-tails-1-0'
    adult = True


class Awaken(ParserScraper):
    url = "https://www.awakencomic.com/"
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'comic-cover'
    imageSearch = '//div[@id="cc-comicbody"]//img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: chapter-n-page-n (unpadded)'


class AwkwardZombie(ParserScraper):
    url = 'https://www.awkwardzombie.com/'
    stripUrl = url + 'awkward-zombie/%s'
    firstStripUrl = stripUrl % 'coin-battle'
    imageSearch = '//div[@id="cc-comicbody"]//img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: variable :('


class AxeCop(WordPressScraper):
    url = 'http://axecop.com/comic/season-two/'

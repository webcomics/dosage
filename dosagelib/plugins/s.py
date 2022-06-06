# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from re import compile, escape, IGNORECASE, sub
from os.path import splitext

from ..scraper import _BasicScraper, _ParserScraper, ParserScraper
from ..helpers import indirectStarter, bounceStarter, joinPathPartsNamer
from ..util import tagre
from .common import ComicControlScraper, WordPressScraper, WordPressNavi, WordPressWebcomic


class SabrinaOnline(_BasicScraper):
    url = 'http://sabrina-online.com/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '1996-01'
    imageSearch = (compile(tagre("a", "href", r'(strips/[^"]*)')),
                   compile(tagre("img", "src", r'(pages/[^"]*)')))
    prevSearch = compile(tagre("a", "href", r"(\d\d\d\d-\d\d.html)") +
                         tagre("img", "src", "b_back.gif"))
    help = 'Index format: yyyy-qq'
    adult = True
    multipleImagesPerStrip = True

    def starter(self):
        """Pick last one in a list of archive pages."""
        archive = self.url + 'archive.html'
        data = self.getPage(archive)
        search = compile(tagre("a", "href", r"(\d\d\d\d-\d\d.html)"))
        archivepages = self.fetchUrls(archive, data, search)
        return archivepages[-1]


class SafelyEndangered(WordPressNavi):
    url = 'http://www.safelyendangered.com/'
    firstStripUrl = url + 'comic/ignored/'


class SaffronAndSage(WordPressScraper):
    url = 'https://www.saffroncomic.com/'
    firstStripUrl = url + 'comic/p0001/'


class SailorsunOrg(WordPressScraper):
    url = 'https://sailorsun.org/'

    def shouldSkipUrl(self, url, data):
        return 'sailorsun-org-credits' in url  # video


class SamAndFuzzy(_ParserScraper):
    url = 'http://www.samandfuzzy.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@class="comic-image"]'
    prevSearch = '//li[@class="prev-page"]/a'
    help = 'Index format: n (unpadded)'


class SandraOnTheRocks(ComicControlScraper):
    url = 'https://pixietrixcomix.com/sandra-on-the-rocks/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'start-by-running'
    endOfLife = True
    help = 'Index format: name'


class Savestate(WordPressNavi):
    url = 'http://www.savestatecomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2014/02/pokemon-bank'


class ScandinaviaAndTheWorld(_ParserScraper):
    url = 'https://satwcomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'sweden-denmark-and-norway'
    starter = indirectStarter
    imageSearch = '//img[@itemprop="image"]'
    prevSearch = '//a[@accesskey="p"]'
    latestSearch = '//a[text()="View latest comic"]'
    textSearch = '//span[@itemprop="articleBody"]'
    help = 'Index format: stripname'


class ScaryGoRound(_ParserScraper):
    url = 'http://www.scarygoround.com/sgr/ar.php'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20020604'
    imageSearch = '//img[contains(@src, "/strips/")]'
    prevSearch = '//a[contains(text(), "Previous")]'
    endOfLife = True
    help = 'Index format: yyyymmdd'


class ScenesFromAMultiverse(_BasicScraper):
    url = 'http://amultiverse.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2010/06/14/parenthood'
    imageSearch = (
        compile(tagre("div", "id", "comic") + r"\s*" +
            tagre("img", "src",
                r'(.*amultiverse.com/wp-content/uploads/\d+/\d+/[^"]+)')),
        compile(tagre("div", "id", "comic") + r"\s*" +
            tagre("a", "href", r'[^"]*') +
            tagre("img", "src",
                r'(.*amultiverse.com/wp-content/uploads/\d+/\d+/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(%scomic/\d+\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class SchlockMercenary(_ParserScraper):
    url = 'http://www.schlockmercenary.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2000-06-12'
    imageSearch = '//div[@class="strip-image-wrapper"]/img'
    prevSearch = '//a[@class="previous-strip"]'
    multipleImagesPerStrip = True
    endOfLife = True
    help = 'Index format: yyyy-mm-dd'


class SchoolBites(_ParserScraper):
    url = ('https://web.archive.org/web/20170215065523/'
        'http://schoolbites.net/')
    stripUrl = url + 'd/%s.html'
    imageSearch = '//img[d:class("ksc")]'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True
    help = 'Index format: yyyymmdd'


class Schuelert(_ParserScraper):
    url = ('https://web.archive.org/web/20190103022830/'
        'http://www.schuelert.de/')
    stripUrl = url + 'index.php?paged=%s'
    firstStripUrl = stripUrl % '3'
    imageSearch = '//img[contains(@src, "wp-content")]'
    prevSearch = '//span[d:class("prevlink")]/a'
    multipleImagesPerStrip = True
    endOfLife = True
    lang = 'de'


class Science(_ParserScraper):
    stripUrl = ('https://web.archive.org/web/20180616152753/'
        'http://sci-ence.org/%s/')
    url = stripUrl % 'new-york-comic-con-2013'
    firstStripUrl = stripUrl % 'periodic-table-element-ass'
    prevSearch = '//a[d:class("navi-prev")]'
    imageSearch = '//div[@class="comicpane"]//img'
    endOfLife = True


class SequentialArt(_ParserScraper):
    url = 'https://www.collectedcurios.com/sequentialart.php'
    stripUrl = url + '?s=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[d:class("w3-image")]'
    prevSearch = '//a[@id="backOne"]'
    help = 'Index format: name'


class SexyLosers(_ParserScraper):
    adult = True
    url = 'https://www.sexylosers.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '003'
    imageSearch = '//div[@class="entry-content"]//img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@rel="bookmark"]'
    help = 'Index format: nnn'
    starter = indirectStarter
    namer = joinPathPartsNamer((-2,), (-1,), '-')


class ShadesOfGray(_ParserScraper):
    url = 'https://www.theduckwebcomics.com/Shades_of_Gray/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '4820502'
    imageSearch = '//div[@id="comic"]/img'
    prevSearch = '//a[img[@class="arrow_prev"]]'
    nextSearch = '//a[img[@class="arrow_next"]]'
    starter = bounceStarter
    endOfLife = True

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rstrip('/').rsplit('/', 1)[-1]


class Sharksplode(WordPressScraper):
    url = 'http://sharksplode.com/'
    textSearch = '//div[@id="comic"]//img/@alt'
    allow_errors = (403,)


class Sheldon(_BasicScraper):
    url = 'http://www.sheldoncomics.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s.html'
    firstStripUrl = stripUrl % '011130'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.sheldoncomics\.com/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/\d+\.html)' % rurl,
                               after="sidenav-prev"))
    help = 'Index format: yymmdd'


class Shifters(WordPressNavi):
    url = 'http://shiftersonline.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'shifters-redux-promo'


class ShipInABottle(WordPressScraper):
    url = 'http://shipinbottle.pepsaga.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '281'
    adult = True
    help = 'Index format: number'


class Shortpacked(_ParserScraper):
    url = 'http://www.shortpacked.com/index.php'
    stripUrl = url + '?id=%s'
    css = True
    imageSearch = 'img#comic'
    prevSearch = 'a.prev'
    help = 'Index format: nnn'


class ShotgunShuffle(WordPressScraper):
    url = 'http://shotgunshuffle.com/'
    firstStripUrl = url + 'comic/pilot/'


class SinFest(ParserScraper):
    END_HTML_TAG = compile(r'</html>')

    url = 'https://sinfest.xyz/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2000-01-17'
    imageSearch = '//img[contains(@src, "btphp/comics/")]'
    textSearch = imageSearch + '/@alt'
    prevSearch = '//a[d:class("prev")]'
    help = 'Index format: yyyy-mm-dd'

    # Remove HTML end tag confusing our parser
    def _parse_page(self, data):
        data = self.END_HTML_TAG.sub('', data)
        return super()._parse_page(data)


class SisterClaire(ComicControlScraper):
    url = 'https://www.sisterclaire.com/comic/'
    firstStripUrl = url + 'book-one'


class SixGunMage(ComicControlScraper):
    url = 'http://www.6gunmage.com/comic/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '6-gun-mage-kickoff'


class SixPackOfOtters(WordPressWebcomic):
    url = 'http://sixpackofotters.com/'
    stripUrl = url + 'pages/%s/'
    firstStripUrl = stripUrl % 'chapter-01-tandem'


class SkinDeep(WordPressWebcomic):
    url = 'http://www.skindeepcomic.com/'
    stripUrl = url + 'archive/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'


class SleeplessDomain(ComicControlScraper):
    url = 'http://www.sleeplessdomain.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'chapter-1-cover'
    starter = bounceStarter

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 1)[-1] + '.' + imageUrl.rsplit('.', 1)[-1]


class SlightlyDamned(ComicControlScraper):
    url = 'http://www.sdamned.com/'
    firstStripUrl = url + 'comic/prologue'

    def namer(self, imageurl, pageurl):
        """Clean up mixed filename formats."""
        filename = pageurl.rsplit('/', 1)[-1]
        if filename == '':
            filename = imageurl.rsplit('-', 1)[-1]
        else:
            filename = 'SD' + filename + '.' + imageurl.rsplit('.', 1)[-1]
        return filename


class SluggyFreelance(_ParserScraper):
    url = 'http://sluggy.com/'
    stripUrl = 'http://archives.sluggy.com/book.php?chapter=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[d:class("comic_content")]/img/@data-src'
    prevSearch = '//div[d:class("previous")]/a'
    latestSearch = '//a[d:class("archives_link")]'
    starter = indirectStarter
    multipleImagesPerStrip = True
    help = 'Index format: chapter'

    def namer(self, imageurl, pageurl):
        # Remove random noise from filename
        return imageurl.rsplit('/', 1)[-1].split('.pagespeed', 1)[0]


class SMBC(ComicControlScraper):
    url = 'https://www.smbc-comics.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '2002-09-05'
    imageSearch = ('//img[@id="cc-comic"]', '//div[@id="aftercomic"]/img')
    textSearch = '//img[@id="cc-comic"]/@title'
    multipleImagesPerStrip = True

    def namer(self, imageUrl, pageUrl):
        # Remove random noise from filename
        filename = imageUrl.rsplit('/', 1)[-1]
        if '-' in filename and len(filename.rsplit('-', 1)[-1]) > 12:
            filename = filename.rsplit('-', 1)[-1]
        elif len(filename) > 22 and filename[0] == '1':
            filename = filename[10:]
        return filename


class SnowFlame(WordPressScraper):
    url = ('https://web.archive.org/web/20160905071051/'
        'http://www.snowflamecomic.com/')
    stripUrl = url + '?comic=snowflame-%s-%s'
    firstStripUrl = stripUrl % ('01', '01')
    starter = bounceStarter
    endOfLife = True
    help = 'Index format: chapter-page'

    def getIndexStripUrl(self, index):
        return self.stripUrl % tuple(index.split('-'))

    def namer(self, image_url, page_url):
        prefix, filename = image_url.rsplit('/', 1)
        ro = compile(r'snowflame-([^-]+)-([^-]+)')
        mo = ro.search(page_url)
        chapter = mo.group(1)
        page = mo.group(2)
        return "%s-%s-%s" % (chapter, page, filename)


class SodiumEyes(WordPressScraper):
    url = 'https://web.archive.org/web/20200220041406/http://sodiumeyes.com/'
    starter = indirectStarter
    endOfLife = True


class SomethingPositive(_ParserScraper):
    url = 'https://www.somethingpositive.net/'
    stripUrl = url + 'sp%s.shtml'
    imageSearch = r'//img[re:test(@src, "/sp\d+")]'
    prevSearch = ('//a[contains(text(), "Previous")]',
        '//a[img[contains(@src, "previous")]]')
    multipleImagesPerStrip = True
    help = 'Index format: mmddyyyy'


class Sorcery101(WordPressWebcomic):
    baseUrl = 'https://kelmcdonald.com/sorcery-101/'
    stripUrl = baseUrl + '%s/'
    url = stripUrl % 'sorcery101-ch-01'
    firstStripUrl = url
    starter = indirectStarter
    help = 'Index format: stripname'


class SpaceFurries(_ParserScraper):
    url = 'http://www.spacefurrs.org/'
    firstStripUrl = url
    multipleImagesPerStrip = True
    adult = True
    endOfLife = True

    def fetchUrls(self, url, data, urlSearch):
        # Website requires JS, so build the list of image URLs manually
        imageUrls = []
        currentPage = int(data.xpath('//input[@name="pagnum"]')[0].get('value'))
        for page in reversed(range(1, currentPage + 1)):
            imageUrls.append(self.url + 'comics/' + str(page) + '.jpg')
        return imageUrls


class SpaceJunkArlia(_ParserScraper):
    url = 'http://spacejunkarlia.com/'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//div[d:class("content")]/img'
    prevSearch = '//a[text()="<"]'
    help = 'Index format: number'


class SpaceTrawler(_ParserScraper):
    url = 'https://www.baldwinpage.com/spacetrawler/'
    firstStripUrl = url + '2010/01/01/spacetrawler-4/'
    imageSearch = '//img[d:class("size-full")]'
    prevSearch = '//a[@rel="prev"]'


class Spamusement(_BasicScraper):
    url = 'http://spamusement.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php/comics/view/%s'
    imageSearch = compile(r'<img src="(%sgfx/\d+\..+?)"' % rurl, IGNORECASE)
    prevSearch = compile(r'<a href="(%sindex.php/comics/view/.+?)">' % rurl,
                         IGNORECASE)
    latestSearch = prevSearch
    help = 'Index format: n (unpadded)'
    starter = indirectStarter


class SpareParts(_BasicScraper):
    baseUrl = 'http://www.sparepartscomics.com/'
    url = baseUrl + 'comics/?date=20080328'
    stripUrl = baseUrl + 'comics/index.php?date=%s'
    firstStripUrl = stripUrl % '20031022'
    imageSearch = compile(tagre("img", "src", r'(http://www\.sparepartscomics\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)',
                               quote="'") + "Previous Comic")
    help = 'Index format: yyyymmdd'


class Spinnerette(ComicControlScraper):
    url = 'http://www.spinnyverse.com'


class SPQRBlues(WordPressScraper):
    url = 'http://spqrblues.com/IV/'


class SSDD(_ParserScraper):
    url = 'http://www.poisonedminds.com/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '19980927'
    imageSearch = ('//img[contains(@src, "/comics/")]',
                   '//source[contains(@src, "/video/")]')
    prevSearch = '//a[@rel="prev"]'
    multipleImagesPerStrip = True
    adult = True
    help = 'Index format: yyyymmdd'

    def shouldSkipUrl(self, url, data):
        # Skip news, flash animation, and non-comic pages.
        return url in (
            # News post
            self.stripUrl % '20060712',
            self.stripUrl % '20060719',
            self.stripUrl % '20071225',
            self.stripUrl % '20110321',
            self.stripUrl % '20110830',
            self.stripUrl % '20110929',
            self.stripUrl % '20180927',

            # Flash animation
            self.stripUrl % '20180401',
            self.stripUrl % '20170429',
            self.stripUrl % '20041203',

            # Comic missing
            self.stripUrl % '20070402',
            self.stripUrl % '20060413',
            self.stripUrl % '20060412',
            self.stripUrl % '20060202',
            self.stripUrl % '20051026',
            self.stripUrl % '20050805',
            self.stripUrl % '20050530',
            self.stripUrl % '20050526',
            self.stripUrl % '20050525',
            self.stripUrl % '20050524',
            self.stripUrl % '20050523',
            self.stripUrl % '20050504',
            self.stripUrl % '20040705',
            self.stripUrl % '20030418',
            self.stripUrl % '20030214',
        )


class StandStillStaySilent(_ParserScraper):
    baseUrl = 'http://sssscomic.com/'
    url = baseUrl + 'comic2.php'
    stripUrl = baseUrl + 'comic%s.php?page=%s'
    firstStripUrl = stripUrl % ('', '1')
    imageSearch = '//img[@class="comicnormal"]'
    prevSearch = '//a[./img[contains(@src, "nav_prev")]]'

    def namer(self, imageUrl, pageUrl):
        chapter = '2' if ('adv2_comicpages' in imageUrl) else '1'
        return '%s-%s' % (chapter, imageUrl.rsplit('/', 1)[-1].replace('page_', ''))


class StarCrossdDestiny(_ParserScraper):
    baseUrl = ('https://web.archive.org/web/20190918132321/'
        'http://starcrossd.net/')
    url = baseUrl + 'comic.html'
    stripUrl = baseUrl + 'archives/%s.html'
    firstStripUrl = stripUrl % '00000001'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[text()="prev"]'
    endOfLife = True
    help = 'Index format: nnnnnnnn'

    def namer(self, image_url, page_url):
        if image_url.find('ch1') == -1:
            # At first all images were stored in a strips/ directory but
            # that was changed with the introduction of book2
            image_url = sub('(?:strips)|(?:images)', 'book1', image_url)
        elif not image_url.find('strips') == -1:
            image_url = image_url.replace('strips/', '')
        directory, filename = image_url.split('/')[-2:]
        filename, extension = splitext(filename)
        return directory + '-' + filename


class StarfireAgency(WordPressWebcomic):
    url = 'https://poecatcomix.com/starfire-agency-static/'
    stripUrl = 'https://poecatcomix.com/starfire-agency/%s/'
    firstStripUrl = stripUrl % '2005-09-201'
    imageSearch = '//div[contains(@class, "webcomic-media")]//img'

    def starter(self):
        # Build list of chapters for naming
        indexPage = self.getPage(self.url)
        self.chapters = indexPage.xpath('//a[./img[contains(@class, "attachment-large")]]/@href')
        latestPage = self.chapters[0]
        self.chapters = self.chapters[1:]
        self.currentChapter = len(self.chapters)
        return latestPage

    def namer(self, imageUrl, pageUrl):
        page = pageUrl.rstrip('/').rsplit('/', 1)[-1]
        page = page.replace('3page00', 'cover3').replace('6429', 'cover7').replace('sfa-6-5-cover', 'cover6')
        page = page.replace('sfa01', 'page01').replace('sfa03', 'page03').replace('sfa04', 'page04')
        page = page.replace('sfa24', 'page24').replace('sfa07', 'page')
        filename = 'sfa%d-%s.%s' % (self.currentChapter, page, imageUrl.rsplit('.', 1)[-1])
        if pageUrl in self.chapters:
            self.currentChapter = self.currentChapter - 1
        return filename


class StarTrip(ComicControlScraper):
    url = 'https://www.startripcomic.com/'


class StationV3(_ParserScraper):
    url = 'http://www.stationv3.com/'
    stripUrl = url + 'd3/%s.html'
    firstStripUrl = stripUrl % '20170101'
    imageSearch = '//img[contains(@src,"/comics3/")]'
    prevSearch = '//a[img[contains(@src,"/previous2")]]'
    help = 'Index format: yyyymmdd'


class StickyDillyBuns(ComicControlScraper):
    url = 'https://pixietrixcomix.com/sticky-dilly-buns/'
    firstStripUrl = url + 'awesome-leading-man'
    endOfLife = True


class StreetFighter(ComicControlScraper):
    url = 'http://www.streetfightercomics.com'


class StringTheory(WordPressNavi):
    url = 'http://www.stringtheorycomic.com/'
    firstStripUrl = url + 'comics/chapterone/chapterone/'


class StrongFemaleProtagonist(_ParserScraper):
    url = 'http://strongfemaleprotagonist.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = 'article p img'
    prevSearch = 'a.page-nav__item--left'
    help = 'Index format: issue-?/page-??'

    def shouldSkipUrl(self, url, data):
        """Skip hiatus & non-comic pages."""
        return url in (
            self.stripUrl % 'guest-art/tuesday',
            self.stripUrl % 'guest-art/friday',
            self.stripUrl % 'guest-art/wednesday',
            self.stripUrl % 'issue-5/newspaper',
            self.stripUrl % 'issue-5/hiatus-1',
            self.stripUrl % 'issue-5/hiatus-2',
            self.stripUrl % 'issue-1/no-page',
        )


class StupidFox(_ParserScraper):
    url = 'http://stupidfox.net/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'hello'
    imageSearch = '//div[@class="comicmid"]//img'
    prevSearch = '//a[@accesskey="p"]'

    def namer(self, imageUrl, pageUrl):
        page = self.getPage(pageUrl)
        title = page.xpath(self.imageSearch + '/@title')[0].replace(' - ', '-').replace(' ', '-')
        return title + '.' + imageUrl.rsplit('.', 1)[-1]


class SuburbanJungle(_ParserScraper):
    url = 'http://suburbanjungleclassic.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '10'
    imageSearch = '//div[@id="comic"]/img'
    prevSearch = '//div[@class="nav-previous"]/a'


class SuburbanJungleRoughHousing(WordPressScraper):
    url = 'http://roughhouse.suburbanjungle.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'rough-housing-issue-1-cover'


class Supercell(_ParserScraper):
    baseUrl = 'https://www.supercellcomic.com/'
    url = baseUrl + 'latest.html'
    stripUrl = baseUrl + 'pages/%s.html'
    firstStripUrl = stripUrl % '0001'
    imageSearch = '//img[@class="comicStretch"]'
    prevSearch = '//div[@class="comicnav"]/a[./img[contains(@src, "comnav_02")]]'


class SupernormalStep(ComicControlScraper):
    url = 'http://supernormalstep.com/'


class SurvivingTheWorld(_ParserScraper):
    url = 'http://survivingtheworld.net/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % 'Lesson1'
    imageSearch = (
        '//div[@class="img"]/img',      # When there's one image per strip
        '//div[@class="img"]/p/img',    # When there's multiple images per strip
        '//td/img',                     # Special case for Lesson1296.html
    )
    prevSearch = (
        '//li[@class="previous"]/a',
        '//td/a',                       # Special case for Lesson1296.html
    )
    multipleImagesPerStrip = True
    help = 'Index format: name'


class SwordsAndSausages(_ParserScraper):
    url = 'https://www.tigerknight.com/ss'
    stripUrl = url + '/%s'
    firstStripUrl = stripUrl % '1-1'
    imageSearch = '//img[d:class("comic-image")]'
    prevSearch = '//a[./span[contains(text(), "Previous")]]'
    multipleImagesPerStrip = True

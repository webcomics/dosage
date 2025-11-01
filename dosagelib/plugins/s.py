# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import IGNORECASE, compile, escape, sub

from .. import util
from ..helpers import bounceStarter, indirectStarter, joinPathPartsNamer
from ..scraper import ParserScraper, _BasicScraper, _ParserScraper
from ..util import tagre
from .common import (
    ComicControlScraper,
    WordPressNavi,
    WordPressScraper,
    WordPressSpliced,
    WordPressWebcomic,
)


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
    url = 'https://satwcomic.com/sweden-denmark-and-norway'
    firstStripUrl = url
    starter = indirectStarter
    imageSearch = '//img[@itemprop="image"]'
    prevSearch = '//a[@accesskey="p"]'
    latestSearch = '//a[contains(@title, "Latest")]'
    textSearch = '//span[@itemprop="articleBody"]'


class ScaryGoRound(_ParserScraper):
    url = ('https://web.archive.org/web/20190327203330/'
        'https://www.scarygoround.com/sgr/ar.php')
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


class SchlockMercenary(ParserScraper):
    url = 'https://www.schlockmercenary.com/'
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
    namer = joinPathPartsNamer(pageparts=(-1,), imageparts=(-1,), joinchar='-')


class ShadesOfGray(ParserScraper):
    url = 'https://www.theduckwebcomics.com/Shades_of_Gray/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '4820502'
    imageSearch = '//div[@id="comic"]/img'
    prevSearch = '//a[img[@class="arrow_prev"]]'
    nextSearch = '//a[img[@class="arrow_next"]]'
    starter = bounceStarter
    namer = joinPathPartsNamer(pageparts=(-1,))
    endOfLife = True


class Sharksplode(WordPressScraper):
    url = 'http://sharksplode.com/'
    textSearch = '//div[@id="comic"]//img/@alt'
    allow_errors = (403,)


class Sheldon(ParserScraper):
    url = 'https://www.sheldoncomics.com/'
    firstStripUrl = url + 'comic/well-who-is-this/'
    imageSearch = '//div[@id="comic"]//img/@data-src-img'
    prevSearch = '//a[img[d:class("left")]]'


class Shifters(ParserScraper):
    baseUrl = 'https://shiftersonline.com/'
    url = baseUrl + 'series/shifters-redux/'
    stripUrl = baseUrl + 'comic/%s/'
    firstStripUrl = stripUrl % 'chapter-1-pg-1'
    imageSearch = '//div[@id="spliced-comic"]//span[@class="default-lang"]//img'
    prevSearch = '//a[@class="previous-comic"]'
    latestSearch = '//div[@id="comic-archive-list"]//a'
    starter = indirectStarter
    namer = joinPathPartsNamer(pageparts=(-1,))


class ShiftersOnGossamerWings(Shifters):
    name = 'Shifters/OnGossamerWings'
    baseUrl = 'https://shiftersonline.com/'
    url = baseUrl + 'series/shifters-on-gossamer-wings/'
    stripUrl = baseUrl + 'comic/%s/'
    firstStripUrl = stripUrl % 'on-gossamer-wings-cover'


class ShiftersTheBeastWithin(Shifters):
    name = 'Shifters/TheBeastWithin'
    baseUrl = 'https://shiftersonline.com/'
    url = baseUrl + 'series/shifters-the-beast-within/'
    stripUrl = baseUrl + 'comic/%s/'
    firstStripUrl = stripUrl % 'awakenings-pg-1'
    endOfLife = True

    def namer(self, imageUrl, pageUrl):
        filename = util.urlpathsplit(pageUrl)[-1]
        if filename.startswith('the-company-of-dragons'):
            filename = 'in-' + filename
        # Prepend chapter number to filename
        chapters = [
            'awakenings',
            'lifting-the-veil',
            'tears-of-blood',
            'on-the-lam',
            'shades-of-intrigue',
            'catfight',
            'out-of-control',
            'damage-control',
            'wolfs-clothing',
            'strange-dreams',
            'blood-bonds',
            'the-other-team',
            'get-ferrah',
            'the-price-of-power',
            'dogfight',
            'surfacing',
            'in-the-company-of-dragons',
            'filler',
        ]
        for chapter in chapters:
            if filename.startswith(chapter):
                filename = 'chapter-' + str(chapters.index(chapter) + 1) + '-' + filename
        return filename


class ShipInABottle(WordPressScraper):
    url = 'http://shipinbottle.pepsaga.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '281'
    adult = True
    help = 'Index format: number'


class Shortpacked(ComicControlScraper):
    url = 'https://www.shortpacked.com/comic/'
    firstStripUrl = url + 'just-a-toy-store'


class ShotgunShuffle(WordPressSpliced):
    # Currently down, use archive.org in the meantime (08-2023)
    url = ('https://web.archive.org/web/20230131163842/'
        'https://shotgunshuffle.com/')
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
    url = 'https://www.skindeepcomic.com/'
    stripUrl = url + 'archive/%s/'
    firstStripUrl = stripUrl % 'issue-1-cover'
    imageSearch = '//div[d:class("webcomic-image")]//noscript/img'
    starter = bounceStarter
    namer = joinPathPartsNamer(pageparts=(-1,))


class SleeplessDomain(ComicControlScraper):
    url = 'http://www.sleeplessdomain.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'chapter-1-cover'
    starter = bounceStarter
    namer = joinPathPartsNamer(pageparts=(-1,))


class SlightlyDamned(ComicControlScraper):
    url = 'http://www.sdamned.com/'
    firstStripUrl = url + 'comic/prologue'
    starter = bounceStarter

    def namer(self, imageurl, pageurl):
        """Clean up mixed filename formats."""
        return 'SD' + util.urlpathsplit(pageurl)[-1]


class SluggyFreelance(ParserScraper):
    url = 'https://sluggy.com/'
    stripUrl = 'https://archives.sluggy.com/book.php?chapter=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[d:class("comic_content")]/img/@data-src'
    prevSearch = '//div[d:class("previous")]/a'
    latestSearch = '//a[d:class("archives_link")]'
    starter = indirectStarter
    multipleImagesPerStrip = True
    help = 'Index format: chapter'

    def namer(self, imageurl, pageurl):
        # Remove random noise from filename
        return util.urlpathsplit(imageurl)[-1].split('.', 1)[0]


class SMBC(ComicControlScraper):
    url = 'https://www.smbc-comics.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '2002-09-05'
    imageSearch = ('//img[@id="cc-comic"]', '//div[@id="aftercomic"]/img')
    textSearch = '//img[@id="cc-comic"]/@title'
    multipleImagesPerStrip = True

    def namer(self, image_url, page_url):
        # Remove random noise from filename
        filename = util.urlpathsplit(image_url)[-1]
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
        filename = util.urlpathsplit(image_url)[-1]
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


class SpaceFurries(ParserScraper):
    url = 'https://www.spacefurrs.org/'
    firstStripUrl = url
    multipleImagesPerStrip = True
    adult = True
    endOfLife = True

    def extract_image_urls(self, url, data):
        # Website requires JS, so build the list of image URLs manually
        imageurls = []
        current = int(self.match(data, '//input[@name="pagnum"]')[0].get('value'))
        for page in reversed(range(1, current + 1)):
            imageurls.append(self.url + 'comics/' + str(page) + '.jpg')
        return imageurls


class SpaceJunkArlia(ParserScraper):
    url = ('https://web.archive.org/web/20220121133701/'
        'http://spacejunkarlia.com/')
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = '//div[d:class("content")]/img'
    prevSearch = '//a[text()="<"]'
    endOfLife = True
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

    def namer(self, image_url, page_url):
        chapter = '2' if ('adv2_comicpages' in image_url) else '1'
        return '%s-%s' % (chapter, util.urlpathsplit(image_url)[-1].replace('page_', ''))


class StarCrossdDestiny(ParserScraper):
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
        directory, filename = util.urlpathsplit(image_url)[-2:]
        return directory + '-' + filename


class StarfireAgency(ParserScraper):
    url = 'https://poecatcomix.com/starfirecomic/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'sfa-issue-1-cover'
    imageSearch = '//img[@class="scale-with-grid wp-post-image"]'
    prevSearch = '//a[d:class("fixed-nav-prev")]'
    latestSearch = '//div[@class="post-title"]//a'
    starter = indirectStarter
    adult = True
    namer = joinPathPartsNamer(pageparts=(-1,))


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


class StrongFemaleProtagonist(ParserScraper):
    url = 'https://strongfemaleprotagonist.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'issue-1/page-0'
    imageSearch = '//article/p/img'
    prevSearch = '//a[d:class("page-nav__item--left")]'
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


class StupidFox(ParserScraper):
    url = 'http://stupidfox.net/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'hello'
    imageSearch = '//div[d:class("comicmid")]//img'
    prevSearch = '//a[@accesskey="p"]'

    def namer(self, imageUrl, pageUrl):
        page = self.getPage(pageUrl)
        title = self.match(page, self.imageSearch + '/@title')[0].replace(' - ',
            '-').replace(' ', '-')
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


class SwordsComic(ParserScraper):
    url = 'https://swordscomic.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'cover'
    imageSearch = '//div[@class="page-image-wrapper"]//img'
    prevSearch = '//a[@class="navigation-button navigation-previous"]'
    help = 'Index format: Swordsnnn (unpadded)'

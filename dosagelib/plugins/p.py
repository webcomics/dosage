# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import compile, escape

from ..helpers import bounceStarter, indirectStarter, joinPathPartsNamer, queryNamer
from ..scraper import ParserScraper, _BasicScraper, _ParserScraper
from ..util import tagre
from .common import ComicControlScraper, WordPressNavi, WordPressScraper


class PandyLand(_ParserScraper):
    url = ('https://web.archive.org/web/20200122163307/'
        'http:/pandyland.net/')
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[d:class("comic")]/img'
    prevSearch = '//a[contains(text(), "previous")]'
    help = 'Index format: number'
    endOfLife = True


class ParadigmShift(_BasicScraper):
    url = 'http://www.paradigmshiftmanga.com/'
    starter = indirectStarter
    stripUrl = url + 'ps/%s.html'
    imageSearch = compile(tagre("img", "src", r'([^"]*comics/ps/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)',
                               after="previous-comic-link"))
    latestSearch = compile(tagre("a", "href", r'([^"]+)',
                                 after="next-comic-link"))
    help = 'Index format: custom'


class ParallelUniversum(WordPressScraper):
    url = 'https://www.paralleluniversum.net/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '001-der-comic-ist-tot'
    prevSearch = '//a[@rel="prev"]'
    lang = 'de'


class ParaNatural(ComicControlScraper):
    url = 'https://www.paranatural.net/'
    firstStripUrl = url + 'comic/chapter-1'


class PartiallyClips(WordPressScraper):
    url = ('https://web.archive.org/web/20180509161332/'
        'http://partiallyclips.com/')
    firstStripUrl = url + 'comic/screaming-woman/'
    endOfLife = True


class PastelDefender(_BasicScraper):
    baseUrl = 'http://www.pasteldefender.com/'
    url = baseUrl + 'coverbackcover.html'
    stripUrl = baseUrl + '%s.html'
    firstStripUrl = stripUrl % 'cover'
    imageSearch = compile(r'<IMG SRC="(images/.+?)" WIDTH="742"')
    prevSearch = compile(r'<A HREF="([^"]+)"><IMG SRC="images/back\.gif"')
    help = 'Index format: nnn'


class PeanutBerrySundae(_ParserScraper):
    baseUrl = 'https://foxyverse.com/'
    url = baseUrl + 'comics/'
    stripUrl = baseUrl + 'peanut-berry-sundae-%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = ('//img[contains(@src, "Page")]',
                   '//img[contains(@src, "page")]')
    latestSearch = '//a[contains(@href, "peanut-berry-sundae")]'
    starter = indirectStarter
    adult = True

    def getPrevUrl(self, url, data):
        # Replace missing navigation links
        pageNum = int(url.replace('-70-2', '-71').rstrip('/').rsplit('-', 1)[-1])
        url = self.stripUrl % str(pageNum - 1)
        return url.replace('-71', '-70-2')


class PebbleVersion(_ParserScraper):
    url = 'http://www.pebbleversion.com/'
    stripUrl = url + 'Archives/Strip%s.html'
    imageSearch = "//table/tr[2]//img"
    prevSearch = '//a[text()="Previous Comic"]'
    help = 'Index format: n (unpadded)'


class PennyAndAggie(ComicControlScraper):
    url = 'https://pixietrixcomix.com/penny-and-aggie'
    stripUrl = url + '/%s'
    firstStripUrl = stripUrl % '2004-09-06'
    endOfLife = True
    help = 'Index format: yyyy-mm-dd'


class PennyArcade(_ParserScraper):
    url = 'https://www.penny-arcade.com/comic/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1998/11/18/the-sin-of-long-load-times'
    imageSearch = '//div[d:class("comic-panel")]//img'
    prevSearch = '//a[d:class("older")]'
    nextSearch = '//a[d:class("newer")]'
    multipleImagesPerStrip = True
    starter = bounceStarter
    help = 'Index format: yyyy/mm/dd'


class PeppermintSaga(WordPressScraper):
    url = 'http://www.pepsaga.com/'
    stripUrl = url + 'comics/%s/'
    firstStripUrl = stripUrl % 'the-sword-of-truth-vol1'
    adult = True


class PeppermintSagaBGR(WordPressScraper):
    url = 'http://bgr.pepsaga.com/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % '04172011'
    adult = True


class PeterAndCompany(_ParserScraper):
    url = 'http://peterandcompany.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '20050101'
    imageSearch = ('//div[@id="page"]//img',
                   '//div[@id="strip"]//img[contains(@src, "strips/")]')
    prevSearch = '//a[./img[contains(@src, "nav_previous")]]'


class PeterAndWhitney(_ParserScraper):
    url = 'http://peterandwhitney.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '20160502'
    imageSearch = '//div[@id="page"]//img'
    prevSearch = '//a[./img[contains(@src, "nav_previous")]]'


class PHDComics(ParserScraper):
    BROKEN_COMMENT_END = compile(r'--!>')

    baseUrl = 'http://phdcomics.com/'
    url = baseUrl + 'comics.php'
    stripUrl = baseUrl + 'comics/archive.php?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = ('//img[@id="comic2"]',
        r'//img[d:class("img-responsive") and re:test(@name, "comic\d+")]')
    multipleImagesPerStrip = True
    prevSearch = '//a[img[contains(@src, "prev_button")]]'
    nextSearch = '//a[img[contains(@src, "next_button")]]'
    help = 'Index format: n (unpadded)'

    # Ugly hack :(
    def _parse_page(self, data):
        data = self.BROKEN_COMMENT_END.sub('-->', data)
        return super(PHDComics, self)._parse_page(data)

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            # video
            self.stripUrl % '1880',
            self.stripUrl % '1669',
        ) or self.match(data, '//img[@id="comic" and contains(@src, "phd083123s")]')


class Picklewhistle(ComicControlScraper):
    url = 'http://www.picklewhistle.com/'


class PicPakDog(WordPressScraper):
    url = 'http://www.picpak.net/'
    firstStripUrl = url + 'comic/dogs-cant-spell/'


# Keep, because naming is different to PHDComics...
class PiledHigherAndDeeper(PHDComics):
    starter = bounceStarter
    namer = queryNamer('comicid', use_page_url=True)


class Pixel(_BasicScraper):
    url = 'http://pixelcomic.net/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '000.shtml'
    imageSearch = compile(tagre("img", "src", r'(\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(%s\d+\.(?:php|shtml))' % rurl,
                               before="prev"))
    help = 'Index format: nnn'


class PlanescapeSurvival(_BasicScraper):
    url = 'http://planescapecomic.com/'
    stripUrl = url + '%s.html'
    imageSearch = compile(r'src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img alt="Previous" ')
    help = 'Index format: nnn'


class PlushAndBlood(ParserScraper):
    url = 'http://www.plushandblood.com/Comic.php'
    stripUrl = url + '?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "comics/")]'
    prevSearch = '//a[contains(text(), "PREV")]'


class PokeyThePenguin(_ParserScraper):
    url = 'http://www.yellow5.com/pokey/archive/'
    stripUrl = url + 'index%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//p/img'
    latestSearch = '(//a)[last()]'
    multipleImagesPerStrip = True
    starter = indirectStarter
    help = 'Index format: number'

    def getPrevUrl(self, url, data):
        """Decrease index.html number."""
        mo = compile(r"index(\d+)\.html").search(url)
        num = int(mo.group(1)) - 1
        prefix = url.rsplit('/', 1)[0]
        return "%s/index%d.html" % (prefix, num)


class PoorlyDrawnLines(ParserScraper):
    url = 'https://poorlydrawnlines.com/'
    stripUrl = url + 'comic/%s/'
    multipleImagesPerStrip = True
    firstStripUrl = stripUrl % 'hardly-essayists'
    imageSearch = '//div[d:class("entry-content")]//noscript/img'
    prevSearch = '//a[@rel="prev"]'
    namer = joinPathPartsNamer(imageparts=range(-3, 0))

    def shouldSkipUrl(self, url, _data):
        """Skip pages without a comic."""
        skipUrls = [self.stripUrl % s for s in (
            'hope-it-all-works-out-new-book-coming-this-fall',
            'poorly-drawn-lines-animated-series',
            'poorly-drawn-lines-episode-two',
            'watch-poorly-drawn-lines-on-hulu',
        )]
        return url in skipUrls

    def getPrevUrl(self, url: str, data):
        """Skip missing comics which redirect back to home page"""
        if url == self.stripUrl % '8198':
            return self.stripUrl % 'excited-2'
        elif url == self.stripUrl % '8186':
            return self.stripUrl % 'to-hell-2'
        elif url == self.stripUrl % '8177':
            return self.stripUrl % 'feel-real'
        elif url == self.stripUrl % '2056':
            return self.stripUrl % 'stereotype'

        return super().getPrevUrl(url, data)


class PoppyOPossum(WordPressScraper):
    baseUrl = 'https://www.poppy-opossum.com/'
    url = baseUrl + '?latest'
    stripUrl = baseUrl + 'comic/%s'
    firstStripUrl = stripUrl % 'a-story'


class PowerNap(_ParserScraper):
    url = 'https://www.powernapcomic.com/powernap/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20110617'
    imageSearch = '//center/img'
    prevSearch = '//a[./img[contains(@src, "previous")]]'
    endOfLife = True

    def imageUrlModifier(self, url, data):
        return url.replace('\n', '').strip()

    def link_modifier(self, fromurl, tourl):
        return tourl.replace('\n', '').strip()


class Precocious(_ParserScraper):
    url = 'http://www.precociouscomic.com/'
    stripUrl = url + 'archive/comic/%s'
    firstStripUrl = stripUrl % '2009/03/09'
    imageSearch = '//img[contains(@src, "/comics/")]'
    prevSearch = '//a[img[contains(@src, "/back_arrow")]]'
    help = 'Index format: yyyy/mm/dd'


class PrinceOfSartar(WordPressNavi):
    url = 'http://www.princeofsartar.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'introduction-chapter-1'
    nextSearch = '//a[d:class("navi-next")]'
    starter = bounceStarter
    namer = joinPathPartsNamer(pageparts=(-1,))
    help = 'Index format: name'


class ProphecyOfTheCircle(WordPressNavi):
    url = 'https://www.prophecyofthecircle.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'prologue'

    def namer(self, imageUrl, pageUrl):
        # Fix duplicate filenames
        filename = imageUrl.rsplit('/', 1)[-1]
        if '2015/12/jamet101' in imageUrl:
            filename = filename.replace('101', '10')
        elif '2012-02-20-jahrd156' in imageUrl:
            filename = filename.replace('156', '157')
        elif '2011-10-02-jahrd137' in imageUrl:
            filename = filename.replace('137', '137-1')
        # Fix inconsistent filenames
        if filename[0] == '2':
            filename = filename[11:]
        if len(filename) >= 9 and filename[8].isdigit():
            filename = filename[:8] + '-' + filename[8:]
        return filename


class Prototype(_ParserScraper):
    stripUrl = 'https://web.archive.org/web/20201030035444/http://planetprototype.com/%s/'
    firstStripUrl = stripUrl % '2018/03/30/vol-1-ch-1-front-cover'
    url = firstStripUrl
    imageSearch = '//img[contains(@class, "wp-post-image")]'
    prevSearch = '//a[.//text()="Previous"]'
    latestSearch = '//a[.//text()="Latest"]'
    starter = indirectStarter
    endOfLife = True


class PS238(_ParserScraper):
    url = 'http://ps238.nodwick.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '12072006'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@class="comic-nav-base comic-nav-previous"]'
    help = 'Index format: yyyy-mm-dd'


class PvPOnline(ParserScraper):
    baseUrl = 'https://www.toonhoundstudios.com/'
    stripUrl = baseUrl + 'comic/%s/?sid=372'
    url = stripUrl % 'pvp-2022-09-16'
    firstStripUrl = stripUrl % '19980504'
    imageSearch = '//div[@id="spliced-comic"]//img/@data-src-img'
    prevSearch = '//a[d:class("prev")]'
    endOfLife = True

    def namer(self, image_url, page_url):
        return 'pvp' + image_url.rsplit('/', 1)[-1]

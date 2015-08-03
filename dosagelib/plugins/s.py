# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape, IGNORECASE, sub
from os.path import splitext, basename
from datetime import datetime
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter, bounceStarter
from ..util import tagre, getPageContent


class SabrinaOnline(_BasicScraper):
    url = 'http://sabrina-online.com/'
    imageSearch = compile(tagre("a", "href", r'(strips/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r"(\d\d\d\d-\d\d.html)") +
        tagre("img", "src", "b_back.gif"))
    help = 'Index format: n (unpadded)'
    adult = True
    multipleImagesPerStrip = True

    @classmethod
    def starter(cls):
        """Pick last one in a list of archive pages."""
        archive = cls.url + 'archive.html'
        data = getPageContent(archive, cls.session)
        search = compile(tagre("a", "href", r"(\d\d\d\d-\d\d.html)"))
        archivepages = search.findall(data)
        return cls.url + archivepages[-1]


class SafelyEndangered(_BasicScraper):
    url = 'http://www.safelyendangered.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl =  stripUrl % 'ignored'
    imageSearch = compile(tagre("img", "src", r'(http://www\.safelyendangered\.com/wp-content/uploads/\d+/\d+/[^"]+\.[a-z]+).*'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="navi navi-prev"))
    textSearch = compile(tagre("img", "title", r'([^"]+)', before=r'http://www\.safelyendangered\.com/wp-content/uploads'))
    help = 'Index format: yyyy/mm/stripname'


class SamAndFuzzy(_BasicScraper):
    url = 'http://www.samandfuzzy.com/'
    stripUrl = 'http://samandfuzzy.com/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'(/comics/.+?)" alt')
    prevSearch = compile(r'"><a href="(.+?)"><img src="imgint/nav_prev.gif"')
    help = 'Index format: nnnn'


class SandraOnTheRocks(_BasicScraper):
    url = 'http://www.sandraontherocks.com/'
    stripUrl = url + 'strips-sotr/%s'
    firstStripUrl = stripUrl % 'start_by_running'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-sotr/[^"]+)', before="cn[id]prev"))
    help = 'Index format: name'


class ScandinaviaAndTheWorld(_ParserScraper):
    url = 'http://satwcomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'sweden-denmark-and-norway'
    starter = indirectStarter(url, '//a[text()="View latest comic"]')
    imageSearch = '//img[@itemprop="image"]'
    prevSearch = '//a[@accesskey="p"]'
    textSearch = '//span[@itemprop="articleBody"]'
    help = 'Index format: stripname'


class ScaryGoRound(_BasicScraper):
    url = 'http://www.scarygoround.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20090918'
    imageSearch = compile(tagre("img", "src", r'(strips/\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(\?date=\d+)') + "Previous")
    help = 'Index format: n (unpadded)'


class ScenesFromAMultiverse(_BasicScraper):
    url = 'http://amultiverse.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2010/06/14/parenthood'
    imageSearch = (
      compile(tagre("div", "id", "comic") + r"\s*" +
        tagre("img", "src", r'(.*amultiverse.com/wp-content/uploads/\d+/\d+/[^"]+)')),
      compile(tagre("div", "id", "comic") + r"\s*" + tagre("a", "href", r'[^"]*') +
        tagre("img", "src", r'(.*amultiverse.com/wp-content/uploads/\d+/\d+/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(%scomic/\d+\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class SchlockMercenary(_BasicScraper):
    url = 'http://www.schlockmercenary.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2000-06-12'
    imageSearch = compile(tagre("img", "src", r'(http://static\.schlockmercenary\.com/comics/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(/\d+-\d+-\d+)', quote="'", after="nav-previous"))
    help = 'Index format: yyyy-mm-dd'


class SchoolBites(_BasicScraper):
    url = 'http://schoolbites.net/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.schoolbites\.net/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://schoolbites\.net/d/\d+\.html)', after="prev"))
    help = 'Index format: yyyymmdd'


class Schuelert(_BasicScraper):
    url = 'http://www.schuelert.de/'
    rurl = escape(url)
    stripUrl = url + 'index.php?paged=%s'
    firstStripUrl = stripUrl % '5'
    imageSearch = compile(tagre("img", "src", r"(%swp-content/[^']+)" % rurl, quote="'"))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php\?paged=\d+)' % rurl) + "&laquo;")
    multipleImagesPerStrip = True
    help = 'Index format: none'
    lang = 'de'


class Science(_BasicScraper):
    url = 'http://sci-ence.org/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'periodic-table-element-ass'
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+/)' % rurl, after="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    help = 'Index format: stripname'


class SequentialArt(_BasicScraper):
    url = 'http://www.collectedcurios.com/sequentialart.php'
    stripUrl = url + '?s=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'([^"]+)', before="strip"))
    prevSearch = compile(tagre("a", "href", r'(/sequentialart\.php\?s=\d+)')
      + tagre("img", "src", "Nav_BackOne\.gif"))
    help = 'Index format: name'


class SexyLosers(_BasicScraper):
    adult = True
    url = 'http://www.sexylosers.com/'
    stripUrl = url + '%s.html'
    imageSearch = compile(r'<img src\s*=\s*"\s*(comics/[\w\.]+?)"', IGNORECASE)
    prevSearch = compile(r'<a href="(/\d{3}\.\w+?)"><font color = FFAAAA><<', IGNORECASE)
    help = 'Index format: nnn'
    starter = indirectStarter(url,
                              compile(r'SEXY LOSERS <A HREF="(.+?)">Latest SL Comic \(#\d+\)</A>', IGNORECASE))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = pageUrl.split('/')[-1].split('.')[0]
        title = imageUrl.split('/')[-1].split('.')[0]
        return index + '-' + title


class Sheldon(_BasicScraper):
    url = 'http://www.sheldoncomics.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s.html'
    firstStripUrl = stripUrl % '011130'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.sheldoncomics\.com/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/\d+\.html)' % rurl, after="sidenav-prev"))
    help = 'Index format: yymmdd'


class ShermansLagoon(_BasicScraper):
    url = 'http://shermanslagoon.com/'
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % '/december-29-2003/'
    imageSearch = compile(tagre("img", "src", r'(http://safr\.kingfeatures\.com/idn/etv/zone/xml/content\.php\?file=.+?)'))
    prevSearch = compile(r'id="previouscomic" class="button white"><a href="(%scomics/[a-z0-9-]+/)"' % url)
    help = 'Index format: monthname-day-year'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        name = pageUrl.rsplit('/', 3)[2]
        if name == "shermanslagoon.com":
            import datetime
            name = datetime.date.today().strftime("%B-%d-%Y").lower()
        # name is monthname-day-year
        month, day, year = name.split('-')
        return "%s-%s-%s" % (year, month, day)


class Shivae(_BasicScraper):
    url = 'http://shivae.net/'
    rurl = escape(url)
    stripUrl = url + 'blog/%s/'
    firstStripUrl = stripUrl % '2007/09/21/09212007'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/blogs\.dir/\d+/files/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sblog/[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Shortpacked(_ParserScraper):
    url = 'http://www.shortpacked.com/index.php'
    stripUrl = url + '?id=%s'
    css = True
    imageSearch = 'img#comic'
    prevSearch = 'a.prev'
    help = 'Index format: nnn'


class ShotgunShuffle(_BasicScraper):
    url = 'http://shotgunshuffle.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl =  stripUrl % 'pilot/'
    imageSearch = compile(tagre("img", "src", r'(http://shotgunshuffle.com/wp-content/uploads/\d+/\d+/\d+-[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="navi navi-prev"))
    help = 'Index format: stripname'


class SinFest(_BasicScraper):
    name = 'KeenSpot/SinFest'
    url = 'http://www.sinfest.net/'
    stripUrl = url + 'view.php?date=%s'
    imageSearch = compile(tagre("img","src", r'(btphp/comics/.+)', after="alt"))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date=.+)') + '\\s*' + tagre("img", "src", r'\.\./images/prev\.gif'))
    help = 'Index format: yyyy-mm-dd'


# XXX disallowed by robots.txt
class _Sketchesnatched(_BasicScraper):
    url = 'http://sketchesnatched.blogspot.com/'
    stripUrl = url + 'search?updated-max=%s%%2B01:00&max-results=1'
    firstStripUrl = stripUrl % '2011-01-27T08:32:00'
    imageSearch = compile(tagre("meta", "content", r"(http://\d+\.bp\.blogspot\.com/[^']+)",
        after=r'image_url', quote="'"))
    prevSearch = compile(tagre("a", "href", r"(http://sketchesnatched\.blogspot\.[a-z]+/search[^']+)",
        before=r"blog-pager-older-link", quote="'"))
    help = 'Index format: yyyy-mm-ddThh:mm:ss'


class SkinDeep(_BasicScraper):
    url = 'http://www.skindeepcomic.com/'
    stripUrl = url + 'archive/%s/'
    imageSearch = compile(r'<span class="webcomic-object[^>]*><img src="([^"]*)"')
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="previous-webcomic-link"))
    help = 'Index format: custom'


class SleeplessDomain(_ParserScraper):
    url = 'http://www.sleeplessdomain.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'chapter-1-cover'
    css = True
    imageSearch = 'img#cc-comic'
    prevSearch = 'div.nav a.prev'
    starter = bounceStarter(url, 'div.nav a.next')
    help = 'Index format: chapter-X-page-Y (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Image file name is UNIX time stamp & something for most of the comics..."""
        start = ''
        tsmatch = compile(r'/(\d+)-').search(imageUrl)
        if tsmatch:
            start = datetime.utcfromtimestamp(int(tsmatch.group(1))).strftime("%Y-%m-%d")
        else:
            # There were only chapter 1, page 4 and 5 not matching when writing
            # this...
            start = '2015-04-11x'
        return start + "-" + pageUrl.rsplit('/', 1)[-1]


class SluggyFreelance(_BasicScraper):
    url = 'http://www.sluggy.com/'
    stripUrl = url + 'comics/archives/daily/%s'
    imageSearch = compile(r'<img src="(/images/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?><span class="ui-icon ui-icon-seek-prev">')
    multipleImagesPerStrip = True
    help = 'Index format: yymmdd'


class SMBC(_ParserScraper):
    url = 'http://www.smbc-comics.com/'
    rurl = escape(url)
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '1'
    multipleImagesPerStrip = True
    imageSearch = ['//img[@id="comic"]', '//div[@id="aftercomic"]/img']
    prevSearch = '//a[@class="prev"]'
    help = 'Index format: nnnn'
    textSearch = '//img[@id="comic"]/@title'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Remove random noise from name."""
        return imageUrl.rsplit('-', 1)[-1]

    def shouldSkipUrl(self, url, data):
        """Skip promo or missing update pages."""
        return url in (
            self.stripUrl % '2865',
            self.stripUrl % '2653',
            self.stripUrl % '2424',
            self.stripUrl % '2226',
            self.stripUrl % '2069',
            self.stripUrl % '1895',
            self.stripUrl % '1896',
            self.stripUrl % '1589',
        )


class SnowFlakes(_BasicScraper):
    url = 'http://www.snowflakescomic.com/'
    stripUrl = url + '?id=%s&sl=%s'
    firstStripUrl = stripUrl % ('103', '1')
    endOfLife = True
    imageSearch = (
        compile(tagre("img", "src", r'(comics/[^"]+)')),
        compile(tagre("img", "src", r'(http://www.snowflakescomic.com/comics/[^"]+)')),
    )
    prevSearch = compile(tagre("a", "href", r'(/\?id=\d+\&sl=\d)', quote="") +
        tagre("img", "src", r'images/nav_prior-ON\.gif'))
    help = 'Index format: number'

    @classmethod
    def starter(cls):
        return cls.stripUrl % ('530', '5')

    def getIndexStripUrl(self, index):
        return self.stripUrl % (index, index[0])

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Use strip index number for image name."""
        index = int(compile(r'id=(\d+)').search(pageUrl).group(1))
        ext = imageUrl.rsplit('.', 1)[1]
        return "SnowFlakes-%d.%s" % (index, ext)

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            self.stripUrl % ('279', '2'), # no comic
            self.stripUrl % ('278', '2'), # no comic
            self.stripUrl % ('277', '2'), # no comic
            self.stripUrl % ('276', '2'), # no comic
            self.stripUrl % ('275', '2'), # no comic
            self.stripUrl % ('214', '2'), # no comic
        )


class SnowFlame(_BasicScraper):
    url = 'http://www.snowflamecomic.com/'
    rurl = escape(url)
    stripUrl = url + '?comic=snowflame-%s-%s'
    firstStripUrl = stripUrl % ('01', '01')
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl, after="Snow[Ff]lame "))
    prevSearch = compile(tagre("span", "class", "mininav-prev") +
        tagre("a", "href", r'(%s\?comic=snowflame[^"]+)' % rurl))
    starter = bounceStarter(url,
        compile(tagre("span", "class", "mininav-next") +
        tagre("a", "href", r'(%s\?comic=snowflame[^"]+)' % rurl)))
    help = 'Index format: chapter-page'

    def getIndexStripUrl(self, index):
        return self.stripUrl % tuple(index.split('-'))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        prefix, filename = imageUrl.rsplit('/', 1)
        ro = compile(r'snowflame-([^-]+)-([^-]+)')
        mo = ro.search(pageUrl)
        chapter = mo.group(1)
        page = mo.group(2)
        return "%s-%s-%s" % (chapter, page, filename)


class SodiumEyes(_BasicScraper):
    url = 'http://sodiumeyes.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/11/08/damning-evidence'
    imageSearch = compile(tagre("img", "src", r'(%scomic/[^ ]+)' % rurl, quote=""))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Sorcery101(_BasicScraper):
    baseUrl = 'http://www.sorcery101.net/'
    url = baseUrl + 'sorcery-101/'
    rurl = escape(baseUrl)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%ssorcery-101/[^"]+)' % rurl, after="previous-"))
    help = 'Index format: stripname'


class SpaceTrawler(_BasicScraper):
    url = 'http://spacetrawler.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2010/01/01/spacetrawler-4'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Spamusement(_BasicScraper):
    url = 'http://spamusement.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php/comics/view/%s'
    imageSearch = compile(r'<img src="(%sgfx/\d+\..+?)"' % rurl, IGNORECASE)
    prevSearch = compile(r'<a href="(%sindex.php/comics/view/.+?)">' % rurl, IGNORECASE)
    help = 'Index format: n (unpadded)'
    starter = indirectStarter(url, prevSearch)


class SpareParts(_BasicScraper):
    baseUrl = 'http://www.sparepartscomics.com/'
    url = baseUrl + 'comics/?date=20080328'
    stripUrl = baseUrl + 'comics/index.php?date=%s'
    firstStripUrl = stripUrl % '20031022'
    imageSearch = compile(tagre("img", "src", r'(http://www\.sparepartscomics\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)', quote="'") + "Previous Comic")
    help = 'Index format: yyyymmdd'


class StandStillStaySilent(_ParserScraper):
    url = 'http://www.sssscomic.com/comic.php'
    rurl = escape(url)
    stripUrl = url + '?page=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[@class="comicnormal"]'
    prevSearch = '//a//div[@id="navprev"]'
    help = 'Index Format: number'


class StationV3(_ParserScraper):
    url = 'http://www.stationv3.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = '//img[contains(@src,"/comics2/")]'
    prevSearch = '//a[img[contains(@src,"/previous2")]]'

    help = 'Index format: yyyymmdd'


class StickyDillyBuns(_BasicScraper):
    url = 'http://www.stickydillybuns.com/'
    stripUrl = url + 'strips-sdb/%s'
    firstStripUrl = stripUrl % 'awesome_leading_man'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-sdb/[^"]+)', before="cn[id]prev"))
    help = 'Index format: name'


class Stubble(_BasicScraper):
    url = 'http://stubblecomics.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '4'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="navi-prev"))
    help = 'Index format: number'


class StuffNoOneToldMe(_BasicScraper):
    url = 'http://www.snotm.com/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '2010/05/01'
    olderHref = r"(http://www\.snotm\.com/\d+/\d+/[^']+\.html)"
    starter = indirectStarter(url,
        compile(tagre("a", "href", olderHref, quote="'")))
    imageSearch = (
        compile(tagre("img", "src", r'(http://i\.imgur\.com/[^"]+)') + r"(?:</a>|<br />)"),
        compile(tagre("img", "src", r'(http://\d+\.bp\.blogspot\.com/[^"]+)') + r"(?:(?:&nbsp;)?</a>|<span |<br />)"),
        compile(tagre("img", "src", r'(https://lh\d+\.googleusercontent\.com/[^"]+)') + r"</a>"),
    )
    prevSearch = compile(tagre("a", "href", olderHref, quote="'", before="older-link"))
    multipleImagesPerStrip = True
    help = 'Index format: yyyy/mm/stripname'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Use page URL to construct meaningful image name."""
        parts, year, month, stripname = pageUrl.rsplit('/', 3)
        stripname = stripname.rsplit('.', 1)[0]
        parts, imagename = imageUrl.rsplit('/', 1)
        return '%s-%s-%s-%s' % (year, month, stripname, imagename)

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            self.stripUrl % '2012/08/self-rant', # no comic
            self.stripUrl % '2012/06/if-you-wonder-where-ive-been', # video
            self.stripUrl % '2011/10/i-didnt-make-this-nor-have-anything-to', # video
            self.stripUrl % '2010/12/first-snotm-fans-in-sao-paulo', # no comic
            self.stripUrl % '2010/11/ear-infection', # no comic
        )


class StrawberryDeathCake(_BasicScraper):
    url = 'http://strawberrydeathcake.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/webcomic/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'


class StrongFemaleProtagonist(_ParserScraper):
    url = 'http://strongfemaleprotagonist.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = 'article p:first-child img'
    prevSearch = 'div.nav-previous > a'
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
        )

class SuburbanTribe(_BasicScraper):
    url = 'http://www.pixelwhip.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: nnnn'


class SomethingPositive(_BasicScraper):
    url = 'http://www.somethingpositive.net/'
    stripUrl = url + 'sp%s.shtml'
    imageSearch = (
        compile(tagre("img", "src", r'(sp\d+\.png)')),
        compile(tagre("img", "src", r'(twither\.gif)')),
    )
    prevSearch = compile(tagre("a", "href", r'(sp\d+\.shtml)') +
      "(?:" + tagre("img", "src", r'images/previous\.gif') + "|Previous)")
    help = 'Index format: mmddyyyy'


class StarCrossdDestiny(_BasicScraper):
    baseUrl = 'http://www.starcrossd.net/'
    rurl = escape(baseUrl)
    url = baseUrl + 'comic.html'
    stripUrl = baseUrl + 'archives/%s.html'
    firstStripUrl = stripUrl % '00000001'
    imageSearch = compile(tagre("img", "src", r'(http://(?:www\.)?starcrossd\.net/(?:ch1|strips|book2)/[^"]+)'))
    prevSearch = compile(r'<a href="(%s(?:ch1/)?archives/\d+\.html)"[^>]*"[^"]*"[^>]*>prev' % rurl, IGNORECASE)
    help = 'Index format: nnnnnnnn'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        if imageUrl.find('ch1') == -1:
            # At first all images were stored in a strips/ directory but that was changed with the introduction of book2
            imageUrl = sub('(?:strips)|(?:images)','book1',imageUrl)
        elif not imageUrl.find('strips') == -1:
            imageUrl = imageUrl.replace('strips/','')
        directory, filename = imageUrl.split('/')[-2:]
        filename, extension = splitext(filename)
        return directory + '-' + filename


# XXX disallowed by robots.txt
class _StrangeCandy(_BasicScraper):
    url = 'http://www.strangecandy.net/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') + tagre("img", "alt", "Previous comic"))
    help = 'Index format: yyyyddmm'


class SupernormalStep(_BasicScraper):
    url = 'http://supernormalstep.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '8'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: number'

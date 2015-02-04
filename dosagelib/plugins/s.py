# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape, IGNORECASE, sub
from os.path import splitext
from ..scraper import _BasicScraper
from ..helpers import indirectStarter, bounceStarter
from ..util import tagre, getPageContent


class SabrinaOnline(_BasicScraper):
    description = u'Skunks, computers and porn'
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
        data = getPageContent(archive, cls.session)[0]
        search = compile(tagre("a", "href", r"(\d\d\d\d-\d\d.html)"))
        archivepages = search.findall(data)
        return cls.url + archivepages[-1]

class SafelyEndangered(_BasicScraper):
    description = u''
    url = 'http://www.safelyendangered.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl =  stripUrl % 'ignored'
    imageSearch = compile(tagre("img", "src", r'(http://www\.safelyendangered\.com/wp-content/uploads/\d+/\d+/[^"]+\.[a-z]+).*'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="navi navi-prev"))
    textSearch = compile(tagre("img", "title", r'([^"]+)', before=r'http://www\.safelyendangered\.com/wp-content/uploads'))
    help = 'Index format: yyyy/mm/stripname'

class SailorsunOrg(_BasicScraper):
    url = 'http://sailorsun.org/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '21'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: n (unpadded)'


class SamAndFuzzy(_BasicScraper):
    description = u"Serial about a cab driver and his bear-like friend by Sam Logan. Offers a reader's guide, forum, and frequently asked questions."
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

class ScandinaviaAndTheWorld(_BasicScraper):
    description = u'Scandinavia and the World'
    url = 'http://satwcomic.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'sweden-denmark-and-norway'
    imageSearch = compile(tagre("img", "src", r'(%sart/[^"/]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"/]+)' % rurl)+"\s*"+tagre('span', 'class', 'spritePrevious'))
    help = 'Index format: stripname'

class ScaryGoRound(_BasicScraper):
    url = 'http://www.scarygoround.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20090918'
    imageSearch = compile(tagre("img", "src", r'(strips/\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(\?date=\d+)') + "Previous")
    help = 'Index format: n (unpadded)'


class ScenesFromAMultiverse(_BasicScraper):
    description = u'SFAM Guest Month wraps up today with a contribution by Meredith Gran of Octopus Pie that is sure to tickle and delight even the grumpiest of codgers.'
    url = 'http://amultiverse.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2010/06/14/parenthood'
    imageSearch = (
      compile(tagre("div", "id", "comic") + r"\s*" +
        tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl)),
      compile(tagre("div", "id", "comic") + r"\s*" + tagre("a", "href", r'[^"]*') +
        tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl)),
    )
    prevSearch = compile(tagre("a", "href", r'(%scomic/\d+\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class SchlockMercenary(_BasicScraper):
    description = u'2 days ago ... Travel the galaxy. Meet new and fascinating life-forms.'
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
    description = u'A comic about science, technology, skepticism, geekery, video games, atheism, and more.'


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


# XXX site has been hacked
class _ShadowGirls(_BasicScraper):
    description = u"It's like H.P. Lovecraft meets the Gilmore Girls!"
    url = 'http://www.shadowgirlscomic.com/'
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % 'book-1/chapter-1-broken-dreams/welcome'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*)', after='navi-prev'))
    help = 'Index format: custom'
    starter = indirectStarter(url, compile(tagre("a", "href", r'([^"]*/comics/[^"]+)')))


class Sheldon(_BasicScraper):
    description = u'The story of a software company tycoon billionaire ten-year-old, his grampa, his duck, his pug and a lizard.'
    url = 'http://www.sheldoncomics.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s.html'
    firstStripUrl = stripUrl % '011130'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.sheldoncomics\.com/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/\d+\.html)' % rurl, after="sidenav-prev"))
    help = 'Index format: yymmdd'


class ShermansLagoon(_BasicScraper):
    description = u"Sherman's Lagoon by Jim Toomey"
    url = 'http://shermanslagoon.com/'
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % '/december-29-2003/'
    imageSearch = compile(tagre("img", "src", r'(http://safr\.kingfeatures\.com/idn/test/zone/xml/content\.php\?file=.+?)'))
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


# XXX disallowed by robots.txt
class _Shortpacked(_BasicScraper):
    url = 'http://www.shortpacked.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/comic/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/comic/book-nn/mm-name1/name2'


class ShotgunShuffle(_BasicScraper):
    description = u'adventures of the Seven Buckingham sisters, a fat cat, an irritable roommate, a dirty hippy'
    url = 'http://shotgunshuffle.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl =  stripUrl % 'pilot/'
    imageSearch = compile(tagre("img", "src", r'(http://shotgunshuffle.com/wp-content/uploads/\d+/\d+/\d+-[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="navi navi-prev"))
    help = 'Index format: stripname'


class SinFest(_BasicScraper):
    description = u'Strip dealing with contemporary issues and religion. Created by Tatsuya Ishida.'
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
    description = u"Artwork by Massimo Carnevale"


class SkinDeep(_BasicScraper):
    url = 'http://www.skindeepcomic.com/'
    stripUrl = url + 'archive/%s/'
    imageSearch = compile(r'<span class="webcomic-object[^>]*><img src="([^"]*)"')
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="previous-webcomic-link"))
    help = 'Index format: custom'


class SlightlyDamned(_BasicScraper):
    url = 'http://www.sdamned.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2004/03/03142004'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/number'


class SluggyFreelance(_BasicScraper):
    url = 'http://www.sluggy.com/'
    stripUrl = url + 'comics/archives/daily/%s'
    imageSearch = compile(r'<img src="(/images/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?><span class="ui-icon ui-icon-seek-prev">')
    multipleImagesPerStrip = True
    help = 'Index format: yymmdd'


class SMBC(_BasicScraper):
    description = u"Saturday Morning Breakfast Cereal"
    url = 'http://www.smbc-comics.com/'
    rurl = escape(url)
    stripUrl = url + '?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(%scomics/\d{8}(?:\w2?|-\d)?\.\w{3})\s*" % rurl, quote="'"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)#comic', after="backRollover"))
    help = 'Index format: nnnn'

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
    description = u'Snowflakes - A comic by James Ashby, Chris Jones and Zach Weiner.'
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
    description = u'The fan-comic series featuring "The Man Powered by Cocaine"'
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
    description = u'Welcome to the site of Kel McDonald, professional comic illustrator and writer.'
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
    description = u'Spamusement! Poorly-drawn cartoons inspired by actual spam subject lines!'
    url = 'http://spamusement.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php/comics/view/%s'
    imageSearch = compile(r'<img src="(%sgfx/\d+\..+?)"' % rurl, IGNORECASE)
    prevSearch = compile(r'<a href="(%sindex.php/comics/view/.+?)">' % rurl, IGNORECASE)
    help = 'Index format: n (unpadded)'
    starter = indirectStarter(url, prevSearch)


class SpareParts(_BasicScraper):
    description = u'Spare Parts by Terrence and Isabel Marks!'
    baseUrl = 'http://www.sparepartscomics.com/'
    url = baseUrl + 'comics/?date=20080328'
    stripUrl = baseUrl + 'comics/index.php?date=%s'
    firstStripUrl = stripUrl % '20031022'
    imageSearch = compile(tagre("img", "src", r'(http://www\.sparepartscomics\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)', quote="'") + "Previous Comic")
    help = 'Index format: yyyymmdd'


class Spinnerette(_BasicScraper):
    url = 'http://www.spinnyverse.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '2010/02/09/02092010'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)', after="comic"))
    prevSearch = compile(tagre("a", "href", r'(/index\.php\?id=[^"]+)', after="prev"))
    help = 'Index format: number'


class SPQRBlues(_BasicScraper):
    description = u"You can skip the next comic if you'd like to pass over the rest of this (very mildly) mature theme. I've tried to clarify the legalities as pointed out in the comments."
    url = 'http://spqrblues.com/IV/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '1467'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+\.png)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: number'


class StandStillStaySilent(_BasicScraper):
    url = 'http://www.sssscomic.com/comic.php'
    rurl = escape(url)
    stripUrl = url + '?page=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(comicpages/[^"]+)', before="comicnormal"))
    prevSearch = compile(tagre("a", "href", r"([^']+)", quote="'") + tagre("div", "id", r'navprev'))
    help = 'Index Format: number'
    description = u'"Stand Still. Stay Silent" is a post-apocalyptic adventure story with a rather light tone and careless pace.'


# XXX disallowed by robots.txt
class _StationV3(_BasicScraper):
    url = 'http://www.stationv3.com/'
    rurl = escape(url)
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sd/\d+\.html)' % rurl) +
      tagre("img", "src", r'http://www\.stationv3\.com/images/previous\.gif'))
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
    description = u"Everyday's life advices in the shape of witty and humorous cartoons."
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
    description = u"Update2 I'm alive and still working on the comic, but progress has been slow. I'm inching my way through sketches. Update-A little break from the comic."
    url = 'http://strawberrydeathcake.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/webcomic/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'


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
    description = u'Furturistic fantasy. A group of outcasts fight to survive in a world that shuns them as freaks.'
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
    description = u'Supernormal Step - Magic, Face Punching, and a Robot or Two'
    url = 'http://supernormalstep.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '8'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: number'

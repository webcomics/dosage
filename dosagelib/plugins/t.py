# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape, IGNORECASE
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre, fetchUrl, getPageContent


class TheBrads(_BasicScraper):
    description = u'ArchiveFirst World Problems Comic - By Brad Colbow'
    url = 'http://bradcolbow.com/archive/C4/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'P125'
    imageSearch = compile(tagre("img", "src", r'(http://s3\.amazonaws\.com/the_brads/the-?brads[-_][^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://bradcolbow\.com/archive/C4/[^"]+)', before="prev"))
    multipleImagesPerStrip = True
    help = 'Index format: a letter and a number'


class TheDevilsPanties(_BasicScraper):
    description = u"It's not Satanic Porn"
    url = 'http://thedevilspanties.com/'
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '300'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.thedevilspanties\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archives/\d+)', after="Previous"))
    help = 'Index format: number'


class TheDreamlandChronicles(_BasicScraper):
    description = u'The Dreamland Chronicles'
    url = 'http://www.thedreamlandchronicles.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'page-1'
    rurl = escape(url)
    imageSearch = compile(tagre("img", "src", r'(http://www\.thedreamlandchronicles\.com/wp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]*)' % rurl, after='navi-prev"'))
    help = 'Index format: page-n or chapter-n'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Remove trailing digit from day number."""
        name = imageUrl.split('/')[-1]
        base, ext = name.split('.', 1)
        bp = base.split('-')
        if len(bp[2]) == 3:
            bp[2] = bp[2][:-1]
        return "%s-%s-%s.%s" % (bp[0], bp[1], bp[2], ext)

class TheGamerCat(_BasicScraper):
    description = u"The Gamer Cat"
    url = 'http://www.thegamercat.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2011/06/06102011'
    imageSearch = compile(tagre("img", "src", r'(%swordpress/comics/[^"/]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/[^"/]+/)' % rurl , after="navi navi-prev"))
    help = 'Index format: yyyy/mm/mmddyyyy'


class TheGentlemansArmchair(_BasicScraper):
    url = 'http://thegentlemansarmchair.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'dora-the-explorer/'
    imageSearch =  compile(tagre("div", "id", r'comic') + "\s*.*\s*" + tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after='navi-prev'))
    textSearch = compile(r'<h3 class="comic-post-widget-title">(.+)</h3>')
    help = 'Index Format: name'


class TheLandscaper(_BasicScraper):
    url = 'http://landscaper.visual-assault.net/comic/latest'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/comics/comic/comic_page/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)')+'&lsaquo; Previous')
    help = 'Index format: name'

class TheNoob(_BasicScraper):
    url = 'http://www.thenoobcomic.com/index.php'
    stripUrl = url + '?pos=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/headquarters/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?pos=\d+)', before="comic_nav_previous_button"))
    help = 'Index format: nnnn'


class TheOrderOfTheStick(_BasicScraper):
    baseUrl = 'http://www.giantitp.com/'
    url = baseUrl + 'comics/oots0863.html'
    stripUrl = baseUrl + 'comics/oots%s.html'
    firstStripUrl = stripUrl % '0001'
    imageSearch = compile(r'<IMG src="(/comics/images/[^"]+)">')
    prevSearch = compile(r'<A href="(/comics/oots\d{4}\.html)"><IMG src="/Images/redesign/ComicNav_Back.gif"')
    help = 'Index format: n (unpadded)'
    starter = indirectStarter(baseUrl, compile(r'<A href="(/comics/oots\d{4}\.html)"'))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 1)[-1][:-5]


class TheParkingLotIsFull(_BasicScraper):
    baseUrl = 'http://plif.courageunfettered.com/'
    url = baseUrl + 'archive/arch2002.htm'
    stripUrl = baseUrl + 'archive/arch%s.htm'
    firstStripUrl = stripUrl % '1998'
    imageSearch = compile(r'<td align="center"><A TARGET=_parent HREF="(wc\d+\..+?)">')
    multipleImagesPerStrip = True
    prevSearch = compile(r'\d{4} -\s+<A HREF="(arch\d{4}\.htm)">\d{4}')
    help = 'Index format: nnn'


class TheWotch(_BasicScraper):
    url = 'http://www.thewotch.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2002-11-21'
    imageSearch = compile(r"<img.+?src='(comics/.+?)'")
    prevSearch = compile(r"<link rel='Previous' href='(/\?date=\d+-\d+-\d+)'")
    help = 'Index format: yyyy-mm-dd'


class ThisIsIndexed(_BasicScraper):
    url = 'http://thisisindexed.com/'
    rurl = escape(url)
    stripUrl = url + 'page/%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/card[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("div", "class", "nav-previous") +
                         tagre("a", "href", r'(%spage/\d+/)[^"]*' % rurl))
    help = 'Index format: number'


class ThunderAndLightning(_BasicScraper):
    url = 'http://www.talcomic.com/wp/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    help = 'Index format: yyyy/mm/dd/page-nn'

    @classmethod
    def starter(cls):
        return cls.url + '?latestcomic'


class TinyKittenTeeth(_BasicScraper):
    url = 'http://www.tinykittenteeth.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/01/26/gene-kelly'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripname (unpadded)'


class ToonHole(_BasicScraper):
    url = 'http://www.toonhole.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/12/toon-hole-coming-soon-2010'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/stripname'

    def shouldSkipUrl(self, url, data):
        return url in (self.stripUrl % "2013/03/if-game-of-thrones-was-animated",)


# XXX disallowed by robots.txt
class _TwoLumps(_BasicScraper):
    url = 'http://www.twolumps.net/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)', after="prev"))
    help = 'Index format: yyyymmdd'


class TwoTwoOneFour(_BasicScraper):
    description = u'Artwork, comics, graphic novels, music, articles, and various silliness by Troy McQuinn'
    url = 'http://www.nitrocosm.com/go/2214_classic/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://content\.nitrocosm\.com/[^"]+)', before="gallery_display"))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/)' % rurl, after="Previous"))
    help = 'Index format: n (unpadded)'


class TheWhiteboard(_BasicScraper):
    description = u'The Whiteboard, a somewhat paintball-related webcomic by "Doc" Nickel'
    url = 'http://www.the-whiteboard.com/'
    stripUrl = url + 'auto%s.html'
    imageSearch = compile(r'<img SRC="(autotwb\d{1,4}.+?|autowb\d{1,4}.+?)">', IGNORECASE)
    prevSearch = compile(r'&nbsp<a href="(.+?)">previous</a>', IGNORECASE)
    help = 'Index format: twb or wb + n wg. twb1000'


class TheOuterQuarter(_BasicScraper):
    url = 'http://theouterquarter.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'oq-the-first-take/4'
    imageSearch = compile(r'<img src="(%scomics/.+?)"' % rurl)
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: nnn'


class TheThinHLine(_BasicScraper):
    description = u'the thin H line. Proudly mediocre. NSFW.'
    url = 'http://thinhline.tumblr.com/'
    rurl = escape(url)
    stripUrl = url + 'post/%s'
    firstStripUrl = stripUrl % '3517345105'
    imageSearch = compile(tagre('img', 'data-src', r'([^"]+media.tumblr.com/[^"]+)', before='content-image'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + '&gt;</a>')
    starter = indirectStarter(url, compile(tagre("a", "href", r'([^"]+)', after='class="timestamp"')))
    adult = True

    indirectImageSearch = compile(tagre('a', 'href', r'(%simage/\d+)' % rurl))

    def getComicStrip(self, url, data, baseUrl):
        """The comic strip image is in a separate page."""
        pageUrl = fetchUrl(url, data, baseUrl, self.indirectImageSearch)
        pageData, pageBaseUrl = getPageContent(pageUrl, self.session)
        return super(TheThinHLine, self).getComicStrip(pageUrl, pageData, pageBaseUrl)

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Use page URL sequence which is apparently increasing."""
        num = pageUrl.split('/')[-1]
        ext = imageUrl.rsplit('.', 1)[1]
        return "thethinhline-%s.%s" % (num, ext)


class ThreePanelSoul(_BasicScraper):
    url = 'http://threepanelsoul.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/05/11/a-test-comic'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class TracyAndTristan(_BasicScraper):
    url = 'http://tandt.thecomicseries.com/'
    rurl = escape(url)
    stripUrl = url + 'comics/%s'
    imageSearch = compile(tagre("img", "src", r'(%simages/comics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+)', after="prev"))
    help = 'Index format: number'


class TwoGuysAndGuy(_BasicScraper):
    description = u"Two Guys and Guy"
    url = 'http://www.twogag.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '4'
    imageSearch = compile(tagre('img', 'src', r'(%scomics/\d{4}-\d{2}-\d{2}[^"]*)' % rurl))
    prevSearch = compile(tagre('a', 'href', r'(%sarchives/\d+)' % rurl, after='title="Previous"'))
    help = 'Index format: number'
    adult = True

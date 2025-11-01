# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import compile, escape

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


class Namesake(ComicControlScraper):
    url = 'http://namesakecomic.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'the-journey-begins'


class NatalieDee(_BasicScraper):
    url = 'http://www.nataliedee.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '022806'
    imageSearch = compile(tagre("img", "src", r'(%s\d+/[^"]+)' % rurl,
                                before="overflow"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "&lt;&lt; Yesterday")
    help = 'Index format: mmddyy'
    namer = joinPathPartsNamer(imageparts=range(-2, 0), joinchar='-')


class Nedroid(WordPressScraper):
    url = 'http://nedroid.com/'
    prevSearch = '//a[@rel="prev"]'


class NeoCTC(_ParserScraper):
    url = 'http://www.hirezfox.com/neoctc/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20071205'
    imageSearch = '//img[contains(@src, "neoctc/comics")]'
    prevSearch = '//a[./img[@alt="Previous Day"]]'
    multipleImagesPerStrip = True


class NeoEarth(_BasicScraper):
    url = 'http://www.neo-earth.com/NE/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '2007-03-23'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'


class NerfNow(WordPressScraper):
    url = 'https://www.nerfnow.com/'
    prevSearch = '//li[@id="nav_previous"]/a'


class Newshounds(_ParserScraper):
    stripUrl = 'http://www.newshounds.com/%s.html'
    url = stripUrl % 'nh2/20140929'
    firstStripUrl = stripUrl % 'nh1/19971101'
    imageSearch = '//img[@class="ksc"]'
    prevSearch = '//a[./img[@alt="Previous comic"]]'
    endOfLife = True

    def getPrevUrl(self, url, data):
        # Add navigation link between comic and graphic novel
        if url == self.stripUrl % 'nh2/20070201':
            return self.stripUrl % 'nh1/20061208'
        return super(Newshounds, self).getPrevUrl(url, data)


class NewWorld(WordPressScraper):
    url = ('https://web.archive.org/web/20190718012133/'
        'http://www.tfsnewworld.com/')
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/08/30/63'
    prevSearch = '//a[@rel="prev"]'
    endOfLife = True
    help = 'Index format: yyyy/mm/dd/stripn'


class NeverSatisfied(ComicControlScraper):
    url = 'https://www.neversatisfiedcomic.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'never-satisfied'


class NichtLustig(_BasicScraper):
    url = 'https://joscha.com/'
    starter = bounceStarter
    stripUrl = url + 'nichtlustig/%s/'
    firstStripUrl = stripUrl % '000501'
    lang = 'de'
    imageSearch = compile(tagre("img", "src", r'(https://joscha.com/data/media/cartoons/[0-9a-f-_]+.png)'))
    prevSearch = compile(tagre("a", "href", r'(https://joscha.com/nichtlustig/\d+/)', after="next"))
    nextSearch = compile(tagre("a", "href", r'(https://joscha.com/nichtlustig/\d+/)', after="prev"))
    namer = joinPathPartsNamer(pageparts=(-1,))
    help = 'Index format: yymmdd'


class Nicky510(WordPressNavi):
    url = ('https://web.archive.org/web/20160510215718/'
        'http://www.nickyitis.com/')
    endOfLife = True


class Nightshift(ParserScraper):
    url = 'https://poecatcomix.com/nightshiftcomic/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'ns-issue-1-cover'
    imageSearch = '//img[@class="scale-with-grid wp-post-image"]'
    prevSearch = '//a[d:class("fixed-nav-prev")]'
    latestSearch = '//div[@class="post-title"]//a'
    starter = indirectStarter
    adult = True
    namer = joinPathPartsNamer(pageparts=(-2,))


class Nimona(_ParserScraper):
    url = ('https://web.archive.org/web/20141008095502/'
        'http://gingerhaze.com/nimona/')
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % "page-1"
    imageSearch = '//div[d:class("field-name-field-comic-page")]//img'
    prevSearch = '//a[img[contains(@src, "/comicdrop_prev_label")]]'
    endOfLife = True


class NineToNine(_ParserScraper):
    url = 'https://www.tigerknight.com/99'
    stripUrl = url + '/%s'
    firstStripUrl = stripUrl % '2014-01-01'
    imageSearch = '//img[d:class("comic-image")]'
    prevSearch = '//a[./span[contains(text(), "Previous")]]'
    multipleImagesPerStrip = True


class NobodyScores(_BasicScraper):
    url = 'http://nobodyscores.loosenutstudio.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '4'
    imageSearch = compile(tagre("img", "src", r'(%scomix/[^"]+)' % rurl))
    multipleImagesPerStrip = True
    prevSearch = compile(r'<a href="(%sindex.php.+?)">the one before </a>' % rurl)
    help = 'Index format: nnn'


class NoNeedForBushido(_ParserScraper):
    url = 'http://nn4b.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = '//div[@id="comic-image"]//img'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: nnn'


class NonPlayerCharacter(ParserScraper):
    url = 'https://www.lfg.co/'
    stripUrl = url + 'npc/comic/%s/'
    firstStripUrl = stripUrl % '1-1'
    imageSearch = '//div[@id="comic-img"]//img'
    prevSearch = '//a[@class="comic-nav-prev"]'
    latestSearch = '//div[@id="feature-npc-footer"]/a[contains(@href, "npc/comic/")]'
    starter = indirectStarter
    namer = joinPathPartsNamer(pageparts=(-1,))


class NotAVillain(WordPressWebcomic):
    url = 'https://navcomic.com/'
    stripUrl = url + 'not-a-villain/%s/'
    firstStripUrl = stripUrl % 'v1-001'

    def namer(self, image_url, page_url):
        filename = util.urlpathsplit(image_url)[-1]
        # Fix filenames missing "Page"
        if filename[2].isdigit():
            filename = filename[0] + '-Page' + filename[2:]
        # Fix filenames of early comics
        filename = filename.replace('Page-', '1-Page')
        if filename.startswith('0-Page'):
            filename = '1' + filename[1:]
        return filename


class NotInventedHere(_ParserScraper):
    url = 'http://notinventedhe.re/'
    stripUrl = url + 'on/%s'
    firstStripUrl = stripUrl % '2009-9-21'
    imageSearch = '//div[@id="comic-content"]//img'
    prevSearch = '//a[@id="nav-previous"]'
    help = 'Index format: yyyy-m-d'


class Nukees(_BasicScraper):
    url = 'http://www.nukees.com/'
    stripUrl = url + 'd/%s'
    firstStripUrl = stripUrl % '19970121'
    imageSearch = compile(r'"comic".+?"(/comics/.+?)"')
    prevSearch = compile(r'"(/d/.+?)".+?previous')
    help = 'Index format: yyyymmdd.html'

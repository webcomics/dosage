# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from re import compile, escape

from ..helpers import bounceStarter, indirectStarter
from ..scraper import BasicScraper, ParserScraper
from ..util import tagre
from .common import ComicControlScraper, WordPressNaviIn, WordPressScraper


class Hackles(ParserScraper):
    url = ('https://web.archive.org/web/20220128022158/'
        'http://hackles.org/')
    stripUrl = url + 'cgi-bin/archives.pl?request=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//img[contains(@src, "strips/")]'
    prevSearch = '//a[text()="< previous"]'
    endOfLife = True


class HagarTheHorrible(BasicScraper):
    url = 'http://www.hagarthehorrible.net/'
    stripUrl = 'http://www.hagardunor.net/comicstrips_us.php?serietype=9&colortype=1&serieno=%s'
    firstStripUrl = stripUrl % '1'
    multipleImagesPerStrip = True
    imageSearch = compile(tagre("img", "src", r'(stripus\d+/(?:Hagar_The_Horrible_?|h)\d+[^ >]+)', quote=""))
    prevUrl = r'(comicstrips_us\.php\?serietype\=9\&colortype\=1\&serieno\=\d+)'
    prevSearch = compile(tagre("a", "href", prevUrl, after="Previous"))
    help = 'Index format: number'

    def starter(self):
        """Return last gallery link."""
        url = 'http://www.hagardunor.net/comics.php'
        data = self.getPage(url)
        pattern = compile(tagre("a", "href", self.prevUrl))
        return self.fetchUrls(url, data, pattern)[-1]


class HarkAVagrant(BasicScraper):
    url = 'http://www.harkavagrant.com/'
    rurl = escape(url)
    starter = bounceStarter
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%s[^"]+)' % rurl,
                                after='BORDER'))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php\?id=\d+)' % rurl) +
                         tagre("img", "src", "buttonprevious.png"))
    nextSearch = compile(tagre("a", "href", r'(%sindex\.php\?id=\d+)' % rurl) +
                         tagre("img", "src", "buttonnext.png"))
    help = 'Index format: number'

    def namer(self, image_url, page_url):
        filename = image_url.rsplit('/', 1)[1]
        num = page_url.rsplit('=', 1)[1]
        return '%s-%s' % (num, filename)


class HavocInc(WordPressScraper):
    url = 'http://www.radiocomix.com/havoc-inc/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'havoc-cover'


class HeadlessBliss(ComicControlScraper):
    url = 'http://headlessbliss.com/'


class Hellkats(ParserScraper):
    url = 'https://poecatcomix.com/hellkatscomic/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'hellkats-issue-1-cover'
    imageSearch = '//img[@class="scale-with-grid wp-post-image"]'
    prevSearch = '//a[d:class("fixed-nav-prev")]'
    latestSearch = '//div[@class="post-title"]//a'
    starter = indirectStarter
    adult = True

    def namer(self, imageUrl, pageUrl):
        return pageUrl.rsplit('/', 2)[1] + '.' + imageUrl.rsplit('.', 1)[-1]


class HeyFox(WordPressScraper):
    url = 'http://www.steamclaw.com/heyfox/'
    stripUrl = url + 'archives/comic/%s'
    firstStripUrl = stripUrl % '11092004'
    adult = True


class HeyKitty(WordPressScraper):
    url = 'http://heykittycomic.com/'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % 'it-begins'


class Hipsters(WordPressScraper):
    url = 'http://www.hipsters-comic.com/'
    firstStripUrl = 'http://www.hipsters-comic.com/comic/hip01/'


class HijinksEnsue(WordPressNaviIn):
    url = 'http://hijinksensue.com/'
    latestSearch = '//a[text()="Latest HijiNKS ENSUE"]'
    firstStripUrl = 'http://hijinksensue.com/comic/who-is-your-daddy-and-what-does-he-do/'
    starter = indirectStarter


class HijinksEnsueClassic(WordPressNaviIn):
    url = 'http://hijinksensue.com/comic/open-your-eyes/'
    firstStripUrl = 'http://hijinksensue.com/comic/a-soul-as-black-as-eyeliner/'
    endOfLife = True


class HijinksEnsueConvention(WordPressNaviIn):
    url = 'http://hijinksensue.com/comic/emerald-city-comicon-2015-fancy-sketches-part-4/'
    firstStripUrl = 'http://hijinksensue.com/comic/whatever-dad-im-outta-here/'
    endOfLife = True


class HijinksEnsuePhoto(WordPressNaviIn):
    url = 'http://hijinksensue.com/comic/emerald-city-comicon-2015-fancy-photo-comic-part-2/'
    firstStripUrl = 'http://hijinksensue.com/comic/san-diego-comic-con-fancy-picto-comic-pt-1/'
    endOfLife = True


class HowToBeAWerewolf(ComicControlScraper):
    url = 'http://howtobeawerewolf.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'coming-february-3rd'

    def namer(self, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[-1]
        if filename[0].isdigit():
            filename = filename.split('-', 1)[1]
        return filename

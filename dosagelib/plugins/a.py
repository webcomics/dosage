# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape, MULTILINE
from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import regexNamer, bounceStarter, indirectStarter


class AbleAndBaker(_BasicScraper):
    description = u"Able and Baker: Hatin' and Dictatin'"
    url = 'http://www.jimburgessdesign.com/comics/index.php'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src', r'(comics/.+)'))
    prevSearch = compile(tagre('a', 'href', r'(.+\d+)') + '.+?previous.gif')
    help = 'Index format: nnn'


class AbsurdNotions(_BasicScraper):
    baseUrl = 'http://www.absurdnotions.org/'
    url = baseUrl + 'page129.html'
    stripUrl = baseUrl + 'page%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src', r'(an[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre('a', 'href', r'([^"]+)') + tagre('img', 'src', 'nprev\.gif'))
    help = 'Index format: n (unpadded)'


class AbstruseGoose(_BasicScraper):
    url = 'http://abstrusegoose.com/'
    rurl = escape(url)
    starter = bounceStarter(url, compile(tagre('a', 'href', r'(%s\d+)' % rurl)+"Next &raquo;"))
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src', r'(http://abstrusegoose\.com/strips/[^<>"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(%s\d+)' % rurl) + r'&laquo; Previous')
    nextSearch = compile(tagre('a', 'href', r'(%s\d+)' % rurl) + r'Next &raquo;')
    help = 'Index format: n (unpadded)'
    textSearch = compile(tagre("img", "title", r'([^"]+)'))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').split('/')[-1])
        name = imageUrl.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)


class AcademyVale(_BasicScraper):
    description = u'Academy Vale'
    url = 'http://www.imagerie.com/vale/'
    stripUrl = url + 'avarch.cgi?%s'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(tagre('img', 'src', r'(avale\d{4}-\d{2}\.gif)'))
    prevSearch = compile(tagre('a', 'href', r'(avarch[^">]+)', quote="") + tagre('img', 'src', 'AVNavBack\.gif'))
    help = 'Index format: nnn'


class Achewood(_BasicScraper):
    url = 'http://www.achewood.com/'
    stripUrl = url + 'index.php?date=%s'
    firstStripUrl = stripUrl % '00000000'
    imageSearch = compile(tagre("img", "src", r'(/comic\.php\?date=\d+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)', after="Previous"))
    help = 'Index format: mmddyyyy'
    namer = regexNamer(compile(r'date=(\d+)'))


class AfterStrife(_BasicScraper):
    baseUrl = 'http://afterstrife.com/'
    rurl = escape(baseUrl)
    stripUrl = baseUrl + '?p=%s'
    url = stripUrl % '262'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<img src="(%sstrips/.+?)"' % rurl)
    prevSearch = compile(r'<a href="(.+?)" class="navi navi-prev"')
    help = 'Index format: nnn'


class AGirlAndHerFed(_BasicScraper):
    description = u'A Girl and Her Fed'
    url = 'http://www.agirlandherfed.com/'
    starter = bounceStarter(url,
      compile(r'<a href="([^"]+)">[^>]+Back'))
    stripUrl = url + '1.%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(img/strip/[^"]+\.jpg)'))
    prevSearch = compile(r'<a href="([^"]+)">[^>]+Back')
    help = 'Index format: nnn'


class AhoiPolloi(_BasicScraper):
    description = u'ahoi polloi - ein f\xfcllhorn voller f\xfchlh\xf6rner'
    url = 'http://ahoipolloi.blogger.de/'
    stripUrl = url + '?day=%s'
    firstStripUrl = stripUrl % '20060306'
    multipleImagesPerStrip = True
    lang = 'de'
    imageSearch = compile(tagre('img', 'src', r'(/static/antville/ahoipolloi/images/[^"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(http://ahoipolloi\.blogger\.de/\?day=\d+)'))
    help = 'Index format: yyyymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.rsplit('/', 1)[1]


class AirForceBlues(_BasicScraper):
    description = u'Air Force Blues | By A. May -'
    url = 'http://www.afblues.com/'
    stripUrl = url + 'wordpress/%s/'
    firstStripUrl = stripUrl % '1997/09/07/need-a-clue-do-ya'
    imageSearch = compile(tagre("img", "src", r'(http://www\.afblues\.com/wordpress/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='Previous'))
    help = 'Index format: yyyy/mm/dd/stripname'


class ALessonIsLearned(_BasicScraper):
    description = u'A Lesson Is Learned But The Damage Is Irreversible'
    url = 'http://www.alessonislearned.com/'
    prevSearch = compile(tagre("a", "href", r"(index\.php\?comic=\d+)", quote="'")+r"[^>]+previous")
    starter = indirectStarter(url, prevSearch)
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(cmx/lesson\d+\.[a-z]+)"))
    help = 'Index format: nnn'


class Alice(_BasicScraper):
    description = u'The little webcomic with the BIG imagination'
    url = 'http://alice.alicecomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%salicecomics/[^"]+)' % rurl, after="previous"))
    help = 'Index format: name'


class AlienLovesPredator(_BasicScraper):
    description = u'Abe (the Alien) and Preston (the Predator) represent in NYC'
    url = 'http://alienlovespredator.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2004/10/12/unavoidable-delay'
    imageSearch = compile(tagre("img", "src", r'([^"]+)', after='border="1" alt="" width="750"'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class AlienShores(_BasicScraper):
    description = u'A webcomic about four guys forming a band. They find that being a band is more than just playing the music.'
    baseUrl = 'http://alienshores.com/'
    rurl = escape(baseUrl)
    url = baseUrl + 'alienshores_band/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(%salienshores_band/wp-content/uploads/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/p<nn>/'


class AllTheGrowingThings(_BasicScraper):
    description = u'All The Growing Things - A Tale of Gardens, monsters, and old ladies'
    url = 'http://growingthings.typodmary.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/04/21/all-the-growing-things'
    imageSearch = compile(tagre("img", "src", r'(%sfiles/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name'


class AlphaLuna(_BasicScraper):
    description = u'Luna, a young girl discovers what lies in her soul: a werewolf beast and a destiny. An adventure manga story for werecreatures fans.'
    url = 'http://www.alphaluna.net/'
    stripUrl = url + 'issue-%s/'
    firstStripUrl = stripUrl % '1/cover'
    imageSearch = compile(tagre("a", "href", r'[^"]*/(?:issue-|support/upcoming)[^"]+') + tagre("img", "src", r'([^"]*/PAGINAS/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "alt", "Prev"))
    help = 'Index format: issue/page (e.g. 4/05)'


class AlphaLunaSpanish(AlphaLuna):
    name = 'AlphaLuna/Spanish'
    lang = 'es'
    url = 'http://alphaluna.net/spanish/'
    stripUrl = url + 'issue-%s/'
    firstStripUrl = stripUrl % '1/portada'


class AlsoBagels(_BasicScraper):
    description = u'Also, Bagels - A Comic of Inept Redundancy'
    url = 'http://alsobagels.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php/comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php/comic/[^"]+)' % rurl, after="Previous"))
    help = 'Index format: strip-name'


class Altermeta(_BasicScraper):
    url = 'http://altermeta.net/'
    rurl = escape(url)
    stripUrl = url + 'archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'<img src="(comics/[^"]+)" />')
    prevSearch = compile(r'<a href="([^"]+)"><img src="%stemplate/default/images/sasha/back\.png' % rurl)
    help = 'Index format: n (unpadded)'


class AltermetaOld(Altermeta):
    url = Altermeta.url + 'oldarchive/index.php'
    stripUrl = Altermeta.url + 'oldarchive/archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    prevSearch = compile(r'<a href="([^"]+)">Back')


class AmazingSuperPowers(_BasicScraper):
    url = 'http://www.amazingsuperpowers.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/09/heredity'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/name'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            # video
            self.stripUrl % '2013/05/orbital-deathray-kickstarter',
        )


class Amya(_BasicScraper):
    description = u'A Graphic Novel'
    url = 'http://www.amyachronicles.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '117'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchives/\d+)' % rurl, after="Previous"))
    help = 'Index format: n'


class Angband(_BasicScraper):
    description = u'Angband - Tales From The Pit'
    url = 'http://angband.calamarain.net/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2005-12-30'
    imageSearch = compile(tagre("img", "src", r'(comics/Scroll[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date\=[^"]+)')+"Previous")
    help = 'Index format: yyyy-mm-dd'


class Angels2200(_BasicScraper):
    description = u'Angels 2200'
    url = 'http://www.janahoffmann.com/angels/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.janahoffmann\.com/angels/comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"&laquo; Previous")
    help = 'Index format: yyyy/mm/dd/part-<n>-comic-<n>'


class Annyseed(_BasicScraper):
    baseUrl = 'http://www.colourofivy.com/'
    rurl = escape(baseUrl)
    url = baseUrl + 'annyseed_webcomic_latest.htm'
    stripUrl = baseUrl + 'annyseed_webcomic%s.htm'
    imageSearch = compile(tagre("img", "src", r'(Annyseed[^"]+)'))
    prevSearch = compile(r'<a href="(%s[^"]+)"><img src="Last.gif"' % rurl)
    help = 'Index format: nnn'


class Antics(_BasicScraper):
    url = 'http://www.anticscomic.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '3'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after='prev'))
    help = 'Index format: number'


class AppleGeeks(_BasicScraper):
    description = u'AppleGeeks 3.0'
    url = 'http://www.applegeeks.com/'
    stripUrl = url + 'comics/viewcomic.php?issue=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'((?:/comics/)?issue\d+\.jpg)'))
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    help = 'Index format: n (unpadded)'


class ARedTailsDream(_BasicScraper):
    description = u"Finnish mythology meets teen boy and his dog"
    baseUrl = 'http://www.minnasundberg.fi/'
    stripUrl = baseUrl + 'comic/page%s.php'
    firstStripUrl = stripUrl % '00'
    url = baseUrl + 'comic/recent.php'
    imageSearch = compile(tagre('img', 'src', r'(chapter.+?/eng[^"]*)'))
    prevSearch = compile(tagre('a', 'href', r'(page\d+\.php)') +
      tagre("img", "src", r'.*?aprev.*?'))
    help = 'Index format: nn'


class ASofterWorld(_BasicScraper):
    url = 'http://www.asofterworld.com/'
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("p", "id", "thecomic") + r'\s*' +
      tagre("img", "src", r'(http://www\.asofterworld\.com/clean/[^"]+)'))
    prevSearch = compile(tagre("a", "href", "(index\.php\?id=\d+)")+'< back')
    help = 'Index format: n (unpadded)'


class AstronomyPOTD(_BasicScraper):
    description = u'A different astronomy and space science related image is featured each day, along with a brief explanation.'
    baseUrl = 'http://antwrp.gsfc.nasa.gov/apod/'
    url = baseUrl + 'astropix.html'
    starter = bounceStarter(url,
        compile(tagre("a", "href", r'(ap\d{6}\.html)') + "&gt;</a>"))
    stripUrl = baseUrl + 'ap%s.html'
    firstStripUrl = stripUrl % '061012'
    imageSearch = compile(tagre("a", "href", r'(image/\d{4}/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(ap\d{6}\.html)') + "&lt;</a>")
    help = 'Index format: yymmdd'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            self.stripUrl % '130217', # video
            self.stripUrl % '130218', # video
            self.stripUrl % '130226', # video
            self.stripUrl % '130424', # video
        )

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%s-%s' % (pageUrl.split('/')[-1].split('.')[0][2:],
                          imageUrl.split('/')[-1].split('.')[0])


class ASkeweredParadise(_BasicScraper):
    url = 'http://aspcomics.net/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(tagre("img", "src", r'(http://aspcomics\.net/sites/default/files[^"]*/asp\d+\.jpg)[^"]+'))
    prevSearch = compile(tagre("a", "href", "(/comic/\d+)")+r"[^>]+Previous")
    help = 'Index format: nnn'


class AxeCop(_BasicScraper):
    description = u'Axe Cop'
    url = 'http://axecop.com/'
    rurl = escape(url)
    starter = bounceStarter(url,
        (
          compile(tagre("a", "href", r'(%scomic/page-\d+-[^"]+/)' % rurl, after="navi-next")),
          compile(tagre("a", "href", r'(%scomic/[^"]+/)' % rurl, after="navi-next")),
        )
    )
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(http://mainsite\.axecop\.wpengine\.com/wp-content/uploads/sites/\d+/\d+/\d+/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+/)' % rurl, after="navi-prev"))
    help = 'Index format: usually stripname'

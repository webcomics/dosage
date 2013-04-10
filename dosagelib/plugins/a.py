# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape, MULTILINE
from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import regexNamer, bounceStarter, indirectStarter


class AbleAndBaker(_BasicScraper):
    url = 'http://www.jimburgessdesign.com/comics/index.php'
    stripUrl = url + '?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre('img', 'src', r'(comics/.+)'))
    prevSearch = compile(tagre('a', 'href', r'(.+\d+)') + '.+?previous.gif')
    help = 'Index format: nnn'


class AbsurdNotions(_BasicScraper):
    baseurl = 'http://www.absurdnotions.org/'
    url = baseurl + 'page129.html'
    stripUrl = baseurl + 'page%s.html'
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
    imageSearch = compile(tagre('img', 'src', r'(%sstrips/[^<>"]+)' % rurl))
    prevSearch = compile(tagre('a', 'href', r'(%s\d+)' % rurl) + r'&laquo; Previous</a>')
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').split('/')[-1])
        name = imageUrl.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)


class AcademyVale(_BasicScraper):
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


class AetheriaEpics(_BasicScraper):
    url = 'http://aetheria-epics.schala.net/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '00001'
    imageSearch = compile(tagre("img", "src", r'(\d{5}\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(\d{5}\.html)') + "Previous")
    help = 'Index format: nnn'


class AfterStrife(_BasicScraper):
    url = 'http://afterstrife.com/?p=262'
    stripUrl = 'http://afterstrife.com/?p=%s'
    imageSearch = compile(r'<img src="(http://afterstrife.com/strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" class="navi navi-prev"')
    help = 'Index format: nnn'


class AGirlAndHerFed(_BasicScraper):
    url = 'http://www.agirlandherfed.com/'
    starter = bounceStarter(url,
      compile(r'<a href="([^"]+)">[^>]+Back'))
    stripUrl = url + '1.%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(img/strip/[^"]+\.jpg)'))
    prevSearch = compile(r'<a href="([^"]+)">[^>]+Back')
    help = 'Index format: nnn'


class AhoiPolloi(_BasicScraper):
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
    url = 'http://www.afblues.com/'
    stripUrl = url + 'wordpress/%s/'
    firstStripUrl = stripUrl % '1997/09/07/need-a-clue-do-ya'
    imageSearch = compile(tagre("img", "src", r'(http://www\.afblues\.com/wordpress/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='Previous'))
    help = 'Index format: yyyy/mm/dd/stripname'


class ALessonIsLearned(_BasicScraper):
    url = 'http://www.alessonislearned.com/'
    prevSearch = compile(tagre("a", "href", r"(index\.php\?comic=\d+)", quote="'")+r"[^>]+previous")
    starter = indirectStarter(url, prevSearch)
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r"(cmx/lesson\d+\.[a-z]+)"))
    help = 'Index format: nnn'


class Alice(_BasicScraper):
    url = 'http://alice.alicecomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%salicecomics/[^"]+)' % rurl, after="previous"))
    help = 'Index format: name'


class AlienLovesPredator(_BasicScraper):
    url = 'http://alienlovespredator.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2004/10/12/unavoidable-delay'
    imageSearch = compile(tagre("img", "src", r'([^"]+)', after='border="1" alt="" width="750"'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class AlienShores(_BasicScraper):
    url = 'http://alienshores.com/alienshores_band/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://alienshores\.com/alienshores_band/wp-content/uploads/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://alienshores\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/p<nn>/'


class ALLCAPS(_BasicScraper):
    url = 'http://www.allcapscomix.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/08/welcome-to-all-caps'
    imageSearch = compile(tagre("img", "src", r'(http://www\.allcapscomix\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+r"[^<]+Previous</a>")
    help = 'Index format: yyyy/mm/strip-name'


class AllTheGrowingThings(_BasicScraper):
    url = 'http://growingthings.typodmary.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/04/21/all-the-growing-things'
    imageSearch = compile(tagre("img", "src", r'(%sfiles/comics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name'


class AlphaLuna(_BasicScraper):
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
    url = 'http://alsobagels.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php/comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php/comic/[^"]+)' % rurl, after="Previous"))
    help = 'Index format: strip-name'


class Altermeta(_BasicScraper):
    url = 'http://altermeta.net/'
    stripUrl = url + 'archive.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'<img src="(comics/[^"]+)" />')
    prevSearch = compile(r'<a href="([^"]+)"><img src="http://altermeta\.net/template/default/images/sasha/back\.png')
    help = 'Index format: n (unpadded)'


class AltermetaOld(Altermeta):
    url = 'http://altermeta.net/oldarchive/index.php'
    stripUrl = 'http://altermeta.net/oldarchive/archive.php?comic=%s'
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


class Amya(_BasicScraper):
    url = 'http://www.amyachronicles.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/%s'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchives/\d+)' % rurl, after="Previous"))
    help = 'Index format: n'


class Angband(_BasicScraper):
    url = 'http://angband.calamarain.net/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2005-12-30'
    imageSearch = compile(tagre("img", "src", r'(comics/Scroll[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date\=[^"]+)')+"Previous")
    help = 'Index format: yyyy-mm-dd'


class Angels2200(_BasicScraper):
    url = 'http://www.janahoffmann.com/angels/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.janahoffmann\.com/angels/comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"&laquo; Previous")
    help = 'Index format: yyyy/mm/dd/part-<n>-comic-<n>'


class Annyseed(_BasicScraper):
    url = 'http://www.colourofivy.com/annyseed_webcomic_latest.htm'
    stripUrl = 'http://www.colourofivy.com/annyseed_webcomic%s.htm'
    imageSearch = compile(tagre("img", "src", r'(Annyseed[^"]+)'))
    prevSearch = compile(r'<a href="(http://www\.colourofivy\.com/[^"]+)"><img src="Last.gif"')
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
    url = 'http://www.applegeeks.com/'
    stripUrl = url + 'comics/viewcomic.php?issue=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'((?:/comics/)?issue\d+\.jpg)'))
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    help = 'Index format: n (unpadded)'


class ASofterWorld(_BasicScraper):
    url = 'http://www.asofterworld.com/'
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("p", "id", "thecomic") + r'\s*' +
      tagre("img", "src", r'(http://www\.asofterworld\.com/clean/[^"]+)'))
    prevSearch = compile(tagre("a", "href", "(index\.php\?id=\d+)")+'< back')
    help = 'Index format: n (unpadded)'


class AstronomyPOTD(_BasicScraper):
    baseurl = 'http://antwrp.gsfc.nasa.gov/apod/'
    url = baseurl + 'astropix.html'
    starter = bounceStarter(url,
        compile(tagre("a", "href", r'(ap\d{6}\.html)') + "&gt;</a>"))
    stripUrl = baseurl + 'ap%s.html'
    firstStripUrl = stripUrl % '061012'
    imageSearch = compile(tagre("a", "href", r'(image/\d{4}/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(ap\d{6}\.html)') + "&lt;</a>")
    help = 'Index format: yymmdd'

    def shouldSkipUrl(self, url):
        """Skip pages without images."""
        return url in (
            self.stripUrl % '130217', # video
            self.stripUrl % '130218', # video
            self.stripUrl % '130226', # video
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
    url = 'http://axecop.com/'
    rurl = escape(url)
    starter = indirectStarter(url,
        compile(tagre("a", "href", r'(%sindex\.php/acepisodes/read/episode_\d+/)' % rurl)))
    stripUrl = url + 'index.php/acepisodes/read/%s/'
    firstStripUrl = stripUrl % 'episode_0'
    imageSearch = compile(tagre("img", "src", r'(%simages/uploads/(?:axecop|AXE-COP|acmarried|nightmonster)[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php/acepisodes/read/[^"]+)' % rurl) +
        tagre("img", "src", r'http://axecop\.com/acimages/buttons/page_left\.png'))
    help = 'Index format: stripname'

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, MULTILINE
from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import regexNamer, bounceStarter, indirectStarter


class AbleAndBaker(_BasicScraper):
    url = 'http://www.jimburgessdesign.com/comics/index.php'
    stripUrl = url + '?comic=%s'
    imageSearch = compile(tagre('img', 'src', r'(comics/.+)'))
    prevSearch = compile(tagre('a', 'href', r'(.+\d+)') + '.+?previous.gif')
    help = 'Index format: nnn'


class AbsurdNotions(_BasicScraper):
    url = 'http://www.absurdnotions.org/page129.html'
    stripUrl = 'http://www.absurdnotions.org/page%s.html'
    imageSearch = compile(tagre('img', 'src', r'(an[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre('a', 'href', r'([^"]+)') + tagre('img', 'src', 'nprev\.gif'))
    help = 'Index format: n (unpadded)'


class AbstruseGoose(_BasicScraper):
    url = 'http://abstrusegoose.com/'
    starter = bounceStarter(url,
       compile(tagre('a', 'href', r'(http://abstrusegoose\.com/\d+)')+"Next &raquo;"))
    stripUrl = url + '%s'
    imageSearch = compile(tagre('img', 'src', r'(http://abstrusegoose\.com/strips/[^<>"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(http://abstrusegoose\.com/\d+)') + r'&laquo; Previous</a>')
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').split('/')[-1])
        name = imageUrl.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)


class AcademyVale(_BasicScraper):
    url = 'http://www.imagerie.com/vale/'
    stripUrl = url + 'avarch.cgi?%s'
    imageSearch = compile(tagre('img', 'src', r'(avale\d{4}-\d{2}\.gif)'))
    prevSearch = compile(tagre('a', 'href', r'(avarch[^">]+)', quote="") + tagre('img', 'src', 'AVNavBack\.gif'))
    help = 'Index format: nnn'


class AhoiPolloi(_BasicScraper):
    url = 'http://ahoipolloi.blogger.de/'
    stripUrl = url + '?day=%s'
    firstStripUrl = stripUrl % '20060305'
    multipleImagesPerStrip = True
    imageSearch = compile(tagre('img', 'src', r'(/static/antville/ahoipolloi/images/[^"]+)'))
    prevSearch = compile(tagre('a', 'href', r'(http://ahoipolloi\.blogger\.de/\?day=\d+)'))
    help = 'Index format: yyyymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return imageUrl.rsplit('/', 1)[1]


class ALessonIsLearned(_BasicScraper):
    url = 'http://www.alessonislearned.com/'
    prevSearch = compile(tagre("a", "href", r"(index\.php\?comic=\d+)", quote="'")+r"[^>]+previous")
    starter = indirectStarter(url, prevSearch)
    stripUrl = url + 'index.php?comic=%s'
    imageSearch = compile(tagre("img", "src", r"(cmx/lesson\d+\.[a-z]+)"))
    help = 'Index format: nnn'


class Alice(_BasicScraper):
    url = 'http://alice.alicecomics.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://alice\.alicecomics\.com/wp-content/webcomic/alicecomics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://alice\.alicecomics\.com/archive/[^"]+)', after="previous"))
    help = 'Index format: name'


class AlienLovesPredator(_BasicScraper):
    url = 'http://alienlovespredator.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'([^"]+)', after='border="1" alt="" width="750"'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name/'


class AlphaLuna(_BasicScraper):
    url = 'http://www.alphaluna.net/'
    stripUrl = url + 'issue-%s/'
    imageSearch = compile(tagre("a", "href", r'[^"]*/(?:issue-|support/upcoming)[^"]+') + tagre("img", "src", r'([^"]*/PAGINAS/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "alt", "Prev"))
    help = 'Index format: issue/page (e.g. 4/05)'


class AlphaLunaSpanish(AlphaLuna):
    name = 'AlphaLuna/Spanish'
    url = 'http://alphaluna.net/spanish/'
    stripUrl = url + 'issue-%s/'


class Altermeta(_BasicScraper):
    url = 'http://altermeta.net/'
    stripUrl = url + 'archive.php?comic=%s'
    imageSearch = compile(r'<img src="(comics/[^"]+)" />')
    prevSearch = compile(r'<a href="([^"]+)"><img src="http://altermeta\.net/template/default/images/sasha/back\.png')
    help = 'Index format: n (unpadded)'


class AltermetaOld(Altermeta):
    url = 'http://altermeta.net/oldarchive/index.php'
    stripUrl = 'http://altermeta.net/oldarchive/archive.php?comic=%s'
    prevSearch = compile(r'<a href="([^"]+)">Back')


class AmazingSuperPowers(_BasicScraper):
    url = 'http://www.amazingsuperpowers.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.amazingsuperpowers\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.amazingsuperpowers\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/name'


class Angels2200(_BasicScraper):
    url = 'http://www.janahoffmann.com/angels/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.janahoffmann\.com/angels/comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"&laquo; Previous")
    help = 'Index format: yyyy/mm/dd/part-<n>-comic-<n>'


class Antics(_BasicScraper):
    url = 'http://www.anticscomic.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.anticscomic\.com/comics/\d+-\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.anticscomic\.com/\?p=\d+)', after='prev'))
    help = 'Index format: number'


class AppleGeeks(_BasicScraper):
    url = 'http://www.applegeeks.com/'
    stripUrl = url + 'comics/viewcomic.php?issue=%s'
    imageSearch = compile(tagre("img", "src", r'((?:/comics/)?issue\d+\.jpg)'))
    prevSearch = compile(r'<div class="caption">Previous Comic</div>\s*<p><a href="([^"]+)">', MULTILINE)
    help = 'Index format: n (unpadded)'


class Achewood(_BasicScraper):
    url = 'http://www.achewood.com/'
    stripUrl = url + 'index.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(/comic\.php\?date=\d+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)', after="Previous"))
    help = 'Index format: mmddyyyy'
    namer = regexNamer(compile(r'date=(\d+)'))


class ASofterWorld(_BasicScraper):
    url = 'http://www.asofterworld.com/'
    stripUrl = url + 'index.php?id=%s'
    imageSearch = compile(tagre("p", "id", "thecomic") + r'\s*' +
      tagre("img", "src", r'(http://www\.asofterworld\.com/clean/[^"]+)'))
    prevSearch = compile(tagre("a", "href", "(index\.php\?id=\d+)")+'< back')
    help = 'Index format: n (unpadded)'


class AstronomyPOTD(_BasicScraper):
    url = 'http://antwrp.gsfc.nasa.gov/apod/astropix.html'
    starter = bounceStarter(url,
        compile(tagre("a", "href", r'(ap\d{6}\.html)') + "&gt;</a>"))
    stripUrl = 'http://antwrp.gsfc.nasa.gov/apod/ap%s.html'
    imageSearch = compile(tagre("a", "href", r'(image/\d{4}/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(ap\d{6}\.html)') + "&lt;</a>")
    help = 'Index format: yymmdd'

    def shouldSkipUrl(self, url):
        """Skip pages without images."""
        return url in (
            'http://antwrp.gsfc.nasa.gov/apod/ap130217.html', # video
            'http://antwrp.gsfc.nasa.gov/apod/ap130218.html', # video
            'http://antwrp.gsfc.nasa.gov/apod/ap130226.html', # video
        )

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%s-%s' % (pageUrl.split('/')[-1].split('.')[0][2:],
                          imageUrl.split('/')[-1].split('.')[0])


class AfterStrife(_BasicScraper):
    url = 'http://afterstrife.com/?p=262'
    stripUrl = 'http://afterstrife.com/?p=%s'
    imageSearch = compile(r'<img src="(http://afterstrife.com/strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" class="navi navi-prev"')
    help = 'Index format: nnn'


class ALLCAPS(_BasicScraper):
    url = 'http://www.allcapscomix.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.allcapscomix\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+r"[^<]+Previous</a>")
    help = 'Index format: yyyy/mm/strip-name'


class ASkeweredParadise(_BasicScraper):
    url = 'http://aspcomics.net/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(tagre("img", "src", r'(http://aspcomics\.net/sites/default/files[^"]*/asp\d+\.jpg)[^"]+'))
    prevSearch = compile(tagre("a", "href", "(/comic/\d+)")+r"[^>]+Previous")
    help = 'Index format: nnn'


class AGirlAndHerFed(_BasicScraper):
    url = 'http://www.agirlandherfed.com/'
    starter = bounceStarter(url,
      compile(r'<a href="([^"]+)">[^>]+Back'))
    stripUrl = url + '1.%s.html'
    imageSearch = compile(tagre("img", "src", r'(img/strip/[^"]+\.jpg)'))
    prevSearch = compile(r'<a href="([^"]+)">[^>]+Back')
    help = 'Index format: nnn'


class AetheriaEpics(_BasicScraper):
    url = 'http://aetheria-epics.schala.net/'
    stripUrl = url + '%s.html'
    imageSearch = compile(tagre("img", "src", r'(\d{5}\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(\d{5}\.html)') + "Previous")
    help = 'Index format: nnn'


class AirForceBlues(_BasicScraper):
    url = 'http://www.afblues.com/'
    stripUrl = url + 'wordpress/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.afblues\.com/wordpress/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='Previous'))
    help = 'Index format: yyyy/mm/dd/name/'


class AlienShores(_BasicScraper):
    url = 'http://alienshores.com/alienshores_band/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://alienshores\.com/alienshores_band/wp-content/uploads/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://alienshores\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/p<nn>/'


class AllTheGrowingThings(_BasicScraper):
    url = 'http://growingthings.typodmary.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://growingthings\.typodmary\.com/files/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://growingthings\.typodmary\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name'


class Amya(_BasicScraper):
    url = 'http://www.amyachronicles.com/'
    stripUrl = url + 'archives/%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.amyachronicles\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.amyachronicles\.com/archives/\d+)', after="Previous"))
    help = 'Index format: n'


class Angband(_BasicScraper):
    url = 'http://angband.calamarain.net/'
    stripUrl = url + 'view.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/Scroll[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?date\=[^"]+)')+"Previous")
    help = 'Index format: yyyy-mm-dd'


class AlsoBagels(_BasicScraper):
    url = 'http://alsobagels.com/'
    stripUrl = url + 'index.php/comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://alsobagels\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://alsobagels\.com/index\.php/comic/[^"]+)', after="Previous"))
    help = 'Index format: strip-name'


class Annyseed(_BasicScraper):
    url = 'http://www.colourofivy.com/annyseed_webcomic_latest.htm'
    stripUrl = 'http://www.colourofivy.com/annyseed_webcomic%s.htm'
    imageSearch = compile(tagre("img", "src", r'(Annyseed[^"]+)'))
    prevSearch = compile(r'<a href="(http://www\.colourofivy\.com/[^"]+)"><img src="Last.gif"')
    help = 'Index format: nnn'


class AxeCop(_BasicScraper):
    url = 'http://axecop.com/'
    starter = indirectStarter(url, compile(tagre("a", "href", r'(http://axecop\.com/index\.php/acepisodes/read/episode_\d+/)')))
    stripUrl = url + 'index.php/acepisodes/read/%s/'
    firstStripUrl = stripUrl % 'episode_0'
    imageSearch = compile(tagre("img", "src", r'(http://axecop\.com/images/uploads/(?:axecop|AXE-COP|acmarried|nightmonster)[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://axecop\.com/index\.php/acepisodes/read/[^"]+)') +
        tagre("img", "src", r'http://axecop\.com/acimages/buttons/page_left\.png'))
    help = 'Index format: stripname'

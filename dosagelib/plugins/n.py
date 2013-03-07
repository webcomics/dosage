# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..helpers import indirectStarter, bounceStarter
from ..util import tagre


class Namesake(_BasicScraper):
    url = 'http://namesakecomic.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(tagre("img", "src", r'([^"]*/wp-content/uploads/[^"]+)', after='title='))
    prevSearch = compile(tagre("a", "href", r'([^"]*/comic/[^"]+)', after='navi-prev'))
    help = 'Index format: name'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imgmatch = compile(r'uploads/(\d+)/(\d+)/(.+)$').search(imageUrl)
        return '-'.join(imgmatch.groups())


class NamirDeiter(_BasicScraper):
    url = 'http://www.namirdeiter.com/'
    stripUrl = url + 'comics/index.php?date=%s'
    imageSearch = compile(tagre("img", "src", r"'?(http://www\.namirdeiter\.com/comics/\d+\.jpg)'?", quote=""))
    prevSearch = compile(tagre("a", "href", r'(http://www\.namirdeiter\.com/comics/index\.php\?date=\d+)', quote="'")+"Previous")
    help = 'Index format: yyyymmdd'


class Nedroid(_BasicScraper):
    url = 'http://nedroid.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://nedroid\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://nedroid\.com/\d+/\d+/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class NeoEarth(_BasicScraper):
    url = 'http://www.neo-earth.com/NE/'
    stripUrl = url + 'index.php?date=%s'
    imageSearch = compile(r'<img src="(strips/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">Previous</a>')
    help = 'Index format: yyyy-mm-dd'


class NewAdventuresOfBobbin(_BasicScraper):
    url = 'http://www.bobbin-comic.com/bobbin_strips/'
    imageSearch = compile(tagre("a", "href", r'(\d+\.gif)'))
    multipleImagesPerStrip = True
    help = 'Index format: none'


class NewWorld(_BasicScraper):
    url = 'http://www.tfsnewworld.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'<img src="(http://www.tfsnewworld.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/stripn'


class Nicky510(_BasicScraper):
    url = 'http://www.nickyitis.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.nickyitis\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.nickyitis\.com/comic/[^"]+)', after="Previous"))
    help = 'Index format: stripname'


class NekkoAndJoruba(_BasicScraper):
    url = 'http://www.nekkoandjoruba.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(r'<img src="(http://www.nekkoandjoruba.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)">&lsaquo;</a>')
    help = 'Index format: nnn'


class NekoTheKitty(_BasicScraper):
    url = 'http://www.nekothekitty.net/'
    stripUrl = url + 'comics/%s'
    starter = bounceStarter(url, compile(tagre("a", "href", r'(http://www\.nekothekitty\.net/comics/[^"]+)') +
      tagre("img", "src", r'http://www\.nekothekitty\.net/files/smallnext.png')))
    imageSearch = compile(tagre("img", "src", r'(http://(?:img\d+|www)\.smackjeeves\.com/images/uploaded/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.nekothekitty\.net/comics/[^"]+)') +
      tagre("img", "src", r'http://www\.nekothekitty\.net/files/smallprev.png'))
    help = 'Index format: n/n-name'


class NichtLustig(_BasicScraper):
    url = 'http://www.nichtlustig.de/main.html'
    stripUrl = 'http://static.nichtlustig.de/toondb/%s.html'
    imageSearch = compile('background-image:url\((http://static\.nichtlustig\.de/comics/full/\d+\.jpg)')
    prevSearch = compile(tagre("a", "href", r'(http://static\.nichtlustig\.de/toondb/\d+\.html)'))
    help = 'Index format: yymmdd'
    starter = indirectStarter(url,
                              compile(tagre("a", "href", r'([^"]*toondb/\d+\.html)')))


class Nnewts(_BasicScraper):
    url = 'http://nnewts.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'nnewts-page-1'
    imageSearch = compile(tagre("img", "src", r'(http://nnewts\.com/newty/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://nnewts\.com/(?:nnewts-)?page-\d+/)', after="navi-prev"))
    help = 'Index format: page-number'


class Nodwick(_BasicScraper):
    url = 'http://comic.nodwick.com/'
    stripUrl = url + "?p=%s"
    imageSearch = compile(tagre("img", "src", r'(http://comic\.nodwick\.com/nodwickstrips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://comic\.nodwick\.com/\?p=\d+)', after="prev"))
    help = 'Index format: stripnumber'


class NobodyScores(_BasicScraper):
    url = 'http://nobodyscores.loosenutstudio.com/'
    stripUrl = url + 'index.php?id=%s'
    imageSearch = compile(tagre("img", "src", r'(http://nobodyscores\.loosenutstudio\.com/comix/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(r'<a href="(http://nobodyscores\.loosenutstudio\.com/index.php.+?)">the one before </a>')
    help = 'Index format: nnn'


class NoNeedForBushido(_BasicScraper):
    url = 'http://noneedforbushido.com/latest/'
    stripUrl = 'http://noneedforbushido.com/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://noneedforbushido\.com/comics/comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://noneedforbushido\.com/[^"]+)', after="previous-comic-link"))
    help = 'Index format: yyyy/comic/nnn'


class Nukees(_BasicScraper):
    url = 'http://www.nukees.com/'
    stripUrl = url + 'd/%s'
    imageSearch = compile(r'"comic".+?"(/comics/.+?)"')
    prevSearch = compile(r'"(/d/.+?)".+?previous')
    help = 'Index format: yyyymmdd.html'

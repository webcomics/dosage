# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, MULTILINE, IGNORECASE, sub
from os.path import splitext
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class SailorsunOrg(_BasicScraper):
    latestUrl = 'http://sailorsun.org/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://sailorsun\.org/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://sailorsun\.org/\?p=\d+)', after="prev"))
    help = 'Index format: n (unpadded)'


class SamAndFuzzy(_BasicScraper):
    latestUrl = 'http://www.samandfuzzy.com/'
    stripUrl = 'http://samandfuzzy.com/%s'
    imageSearch = compile(r'(/comics/.+?)" alt')
    prevSearch = compile(r'"><a href="(.+?)"><img src="imgint/nav_prev.gif"')
    help = 'Index format: nnnn'


class SarahZero(_BasicScraper):
    latestUrl = 'http://www.sarahzero.com/'
    stripUrl = latestUrl + 'sz_%s.html'
    imageSearch = compile(tagre("img", "src", r'(z_(?:spreads|decoy)/sz_[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(sz_\d+\.html)') + tagre("img", "src", r'z_site/sz_05_nav\.gif'))
    help = 'Index format: nnnn'


class ScaryGoRound(_BasicScraper):
    latestUrl = 'http://www.scarygoround.com/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(tagre("img", "src", r'(strips/\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(\?date=\d+)') + "Previous")
    help = 'Index format: n (unpadded)'


class SchlockMercenary(_BasicScraper):
    latestUrl = 'http://www.schlockmercenary.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://static\.schlockmercenary\.com/comics/[^"]+)'))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(/\d+-\d+-\d+)', quote="'", after="nav-previous"))
    help = 'Index format: yyyy-mm-dd'


class SchoolBites(_BasicScraper):
    latestUrl = 'http://schoolbites.net/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.schoolbites\.net/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://schoolbites\.net/d/\d+\.html)', after="prev"))
    help = 'Index format: yyyymmdd'


class Sheldon(_BasicScraper):
    latestUrl = 'http://www.sheldoncomics.com/'
    stripUrl = latestUrl + 'archive/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/\d+\.html)', after="sidenav-prev"))
    help = 'Index format: yymmdd'


class Shivae(_BasicScraper):
    latestUrl = 'http://shivae.net/'
    stripUrl = latestUrl + 'blog/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://shivae\.net/files/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://shivae\.net/blog/[^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripname'


# XXX disallowed by robots.txt
class _Shortpacked(_BasicScraper):
    latestUrl = 'http://www.shortpacked.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.shortpacked\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.shortpacked\.com/\d+/comic/[^"]+)', after="prev"))
    help = 'Index format: yyyy/comic/book-nn/mm-name1/name2'


class SinFest(_BasicScraper):
    name = 'KeenSpot/SinFest'
    latestUrl = 'http://www.sinfest.net/'
    stripUrl = latestUrl + 'archive_page.php?comicID=%s'
    imageSearch = compile(r'<img src=".+?(/comikaze/comics/.+?)"')
    prevSearch = compile(r'(/archive_page.php\?comicID=.+?)".+?prev_a')
    help = 'Index format: n (unpadded)'


class SlightlyDamned(_BasicScraper):
    latestUrl = 'http://www.sdamned.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.sdamned\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.sdamned\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/number'


class SluggyFreelance(_BasicScraper):
    latestUrl = 'http://www.sluggy.com/'
    stripUrl = latestUrl + 'comics/archives/daily/%s'
    imageSearch = compile(r'<img src="(/images/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?><span class="ui-icon ui-icon-seek-prev">')
    help = 'Index format: yymmdd'


class SodiumEyes(_BasicScraper):
    latestUrl = 'http://sodiumeyes.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://sodiumeyes\.com/comic/[^ ]+)', quote=""))
    prevSearch = compile(tagre("a", "href", r'(http://sodiumeyes\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Sorcery101(_BasicScraper):
    baseUrl = 'http://www.sorcery101.net/'
    latestUrl = baseUrl + 'sorcery-101/'
    stripUrl = baseUrl + 'sorcery101/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.sorcery101\.net/comics/sorcery101/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.sorcery101\.net/sorcery101/[^"]+)', after="previous-comic-link"))
    help = 'Index format: stripname'


class SpareParts(_BasicScraper):
    baseUrl = 'http://www.sparepartscomics.com/'
    latestUrl = baseUrl + 'comics/?date=20080328'
    stripUrl = baseUrl + 'comics/index.php?date=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.sparepartscomics\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php\?date=\d+)', quote="'") + "Previous Comic")
    help = 'Index format: yyyymmdd'


class SPQRBlues(_BasicScraper):
    latestUrl = 'http://spqrblues.com/IV/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://spqrblues\.com/IV/comics/\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(http://spqrblues\.com/IV/\?p=\d+)', after="prev"))
    help = 'Index format: number'


# XXX disallowed by robots.txt
class _StationV3(_BasicScraper):
    latestUrl = 'http://www.stationv3.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://www\.stationv3\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.stationv3\.com/d/\d+\.html)') +
      tagre("img", "src", r'http://www\.stationv3\.com/images/previous\.gif'))
    help = 'Index format: yyyymmdd'


class Stubble(_BasicScraper):
    latestUrl = 'http://stubblecomics.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://stubblecomics\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://stubblecomics\.com/\?p=\d+)', after="navi-prev"))
    help = 'Index format: number'


class StrawberryDeathCake(_BasicScraper):
    latestUrl = 'http://strawberrydeathcake.com/'
    stripUrl = latestUrl + 'archive/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://strawberrydeathcake\.com/wp-content/webcomic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://strawberrydeathcake\.com/archive/[^"]+)', after="previous"))
    help = 'Index format: stripname'


class SuburbanTribe(_BasicScraper):
    latestUrl = 'http://www.pixelwhip.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.pixelwhip\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.pixelwhip\.com/\?p=\d+)', after="prev"))
    help = 'Index format: nnnn'


class SomethingPositive(_BasicScraper):
    latestUrl = 'http://www.somethingpositive.net/'
    stripUrl = latestUrl + 'sp%s.shtml'
    imageSearch = compile(tagre("img", "src", r'(sp\d+\.png)'))
    prevSearch = compile(tagre("a", "href", r'(sp\d+\.shtml)') +
      "(?:" + tagre("img", "src", r'images/previous\.gif') + "|Previous)")
    help = 'Index format: mmddyyyy'


class SexyLosers(_BasicScraper):
    adult = True
    stripUrl = 'http://www.sexylosers.com/%s.html'
    imageSearch = compile(r'<img src\s*=\s*"\s*(comics/[\w\.]+?)"', IGNORECASE)
    prevSearch = compile(r'<a href="(/\d{3}\.\w+?)"><font color = FFAAAA><<', IGNORECASE)
    help = 'Index format: nnn'
    starter = indirectStarter('http://www.sexylosers.com/',
                              compile(r'SEXY LOSERS <A HREF="(.+?)">Latest SL Comic \(#\d+\)</A>', IGNORECASE))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = pageUrl.split('/')[-1].split('.')[0]
        title = imageUrl.split('/')[-1].split('.')[0]
        return index + '-' + title


class StarCrossdDestiny(_BasicScraper):
    latestUrl = 'http://www.starcrossd.net/comic.html'
    stripUrl = 'http://www.starcrossd.net/archives/%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://www\.starcrossd\.net/(?:ch1|strips|book2)/[^"]+)'))
    prevSearch = compile(r'<a href="(http://www\.starcrossd\.net/(?:ch1/)?archives/\d+\.html)"[^>]*"[^"]*"[^>]*>prev', IGNORECASE)
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


class Spamusement(_BasicScraper):
    stripUrl = 'http://spamusement.com/index.php/comics/view/%s'
    imageSearch = compile(r'<img src="(http://spamusement.com/gfx/\d+\..+?)"', IGNORECASE)
    prevSearch = compile(r'<a href="(http://spamusement.com/index.php/comics/view/.+?)">', IGNORECASE)
    help = 'Index format: n (unpadded)'

    starter = indirectStarter('http://spamusement.com/', prevSearch)


# XXX disallowed by robots.txt
class _StrangeCandy(_BasicScraper):
    latestUrl = 'http://www.strangecandy.net/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/\d+\.jpg)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') + tagre("img", "alt", "Previous comic"))
    help = 'Index format: yyyyddmm'


class SMBC(_BasicScraper):
    latestUrl = 'http://www.smbc-comics.com/'
    stripUrl = latestUrl + 'index.php?db=comics&id=%s'
    imageSearch = compile(r'<img src=\'(.+?\d{8}.\w{1,4})\'>')
    prevSearch = compile(r'131,13,216,84"\n\s+href="(.+?)#comic"\n>', MULTILINE)
    help = 'Index format: nnnn'

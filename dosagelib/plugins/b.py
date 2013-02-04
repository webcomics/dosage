# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile

from ..util import tagre
from ..scraper import _BasicScraper
from ..helpers import indirectStarter


class Bardsworth(_BasicScraper):
    url = 'http://www.bardsworth.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.bardsworth\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.bardsworth\.com/[^"]+)', after="prev"))
    help = 'Index format: nnn'


class BetterDays(_BasicScraper):
    url = 'http://jaynaylor.com/betterdays/'
    stripUrl = url + 'archives/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/betterdays/comic/[^>]+)', quote=""))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + '&laquo; Previous')
    help = 'Index format: yyyy/mm/<your guess>'


class BiggerThanCheeses(_BasicScraper):
    url = 'http://www.biggercheese.com/'
    stripUrl = url + 'index.php?comic=%s'
    imageSearch = compile(r'src="(comics/.+?)" alt')
    prevSearch = compile(r'"(index.php\?comic=.+?)".+?_back')
    help = 'Index format: n (unpadded)'


class BizarreUprising(_BasicScraper):
    url = 'http://www.bizarreuprising.com/'
    stripUrl = url + 'view/%s'
    imageSearch = compile(tagre("img", "src", r'(comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view/\d+/[^"]+)') + tagre("img", "src", r'images/b_prev\.gif'))
    help = 'Index format: n/name'


class Blip(_BasicScraper):
    url = 'http://blipcomic.com/'
    stripUrl = url + 'index.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First.+?"(index.php\?strip_id=.+?)".+?prev')
    help = 'Index format: n'


class BlueCrashKit(_BasicScraper):
    url = 'http://www.bluecrashkit.com/cheese/'
    stripUrl = url + 'node/%s'
    imageSearch = compile(r'(/cheese/files/comics/.+?)"')
    prevSearch = compile(r'(/cheese/node/.+?)".+?previous')
    help = 'Index format: non'


class BMovieComic(_BasicScraper):
    url = 'http://www.bmoviecomic.com/'
    stripUrl = url + '?cid=%s'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?Prev')
    help = 'Index format: n'


### With BratHalla there is no 'previous' link at comic 360
### You will need to use
### mainline -c BratHalla:360-backup-dad-unstable-plans/
### to get earlier comics
class BratHalla(_BasicScraper):
    url = 'http://brat-halla.com/'
    stripUrl = url + 'comic/%s'
    imageSearch = compile(r"(/comics/.+?)' target='_blank")
    prevSearch = compile(r'headernav2".+?"(http.+?)"')
    help = 'Index format: non'


class Brink(_BasicScraper):
    url = 'http://paperfangs.com/brink/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://paperfangs\.com/brink/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://paperfangs\.com/brink/[^"]+)', after="prev"))
    help = 'Index format: n'


class BoredAndEvil(_BasicScraper):
    url = 'http://www.boredandevil.com/'
    stripUrl = url + '?date=%s'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(r'First Comic.+<a href="(.+?)".+previous-on.gif')
    starter = indirectStarter(url, prevSearch)
    help = 'Index format: yyyy-mm-dd'


class BoyOnAStickAndSlither(_BasicScraper):
    url = 'http://www.boasas.com/'
    stripUrl = url + 'page/%s'
    imageSearch = compile(tagre("img", "src", r'(http://\d+\.media\.tumblr\.com/[^"]+_1280\.png)'))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') + "<span>Next page")
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.rsplit('/')[-1]


class ButternutSquash(_BasicScraper):
    url = 'http://www.butternutsquash.net/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.butternutsquash\.net/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.butternutsquash\.net/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'


class BlankIt(_BasicScraper):
    url = 'http://blankitcomics.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://blankitcomics\.com/bicomics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='rel="prev"'))
    help = 'Index format: yyyy/mm/dd/name'


class BobWhite(_BasicScraper):
    url = 'http://www.bobwhitecomics.com/'
    stripUrl = url + '?webcomic_post=%s'
    imageSearch = compile(tagre("img", "src", r"(http://www\.bobwhitecomics\.com/wp/wp-content/webcomic/untitled/\d+.jpg)"))
    prevSearch = compile(tagre("a", "href", "(http://www\.bobwhitecomics\.com/\?webcomic_post=\d+)")+r'[^"]+Previous')
    help = 'Index format: yyyymmdd'


class BigFatWhale(_BasicScraper):
    url = 'http://www.bigfatwhale.com/'
    stripUrl = url + 'archives/bfw_%s.htm'
    imageSearch = compile(tagre("img", "src", r'(archives/bfw_[^"]+|bfw_[^"]+)'))
    prevSearch = compile(r' HREF="(.+?)" TARGET="_top" TITLE="Previous Cartoon"')
    help = 'Index format: nnn'


class BadassMuthas(_BasicScraper):
    url = 'http://badassmuthas.com/pages/comic.php'
    stripUrl = url + '?%s'
    imageSearch = compile(tagre("img", "src", r'(/images/comicsissue[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", r'/images/comicsbuttonBack\.gif'))
    help = 'Index format: nnn'


class BrightlyWound(_BasicScraper):
    baseUrl = 'http://www.brightlywound.com/'
    url = baseUrl + '?comic=137'
    stripUrl = baseUrl + '?comic=%s'
    imageSearch = compile(tagre("img", "src", r"(comic/[^']+)", quote="'"))
    prevSearch = compile(r'<div id=\'navback\'><a href=\'(\?comic\=\d+)\'><img src=\'images/previous.png\'')
    help = 'Index format: nnn'


class BlueCrashKit(_BasicScraper):
    url = 'http://robhamm.com/bluecrashkit/'
    stripUrl = url + 'comics/blue-crash-kit/%s'
    imageSearch = compile(tagre("img", "src", r'(http://robhamm\.com/bluecrashkit/sites/default/files/comics/[^"]+)'))
    prevSearch = compile(r'<li class="previous"><a href="([^"]+)">')
    help = 'Index format: yyyy-mm-dd'


class BloodBound(_BasicScraper):
    url = 'http://bloodboundcomic.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://bloodboundcomic\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://bloodboundcomic\.com/[^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/name'


class BookOfBiff(_BasicScraper):
    url = 'http://www.thebookofbiff.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'([^"]+/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripnum-strip-name'


class BillyTheDunce(_BasicScraper):
    url = 'http://www.duncepress.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.duncepress\.com/comics/[^"]+)'))
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.duncepress.com/[^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/strip-name'


class BackwaterPlanet(_BasicScraper):
    url = 'http://www.backwaterplanet.com/current.htm'
    stripUrl = 'http://www.backwaterplanet.com/archive/bwp%s.htm'
    imageSearch = compile(r'<img src="(/images/comic/bwp.+?)">')
    prevSearch = compile(r'<a href="(/archive/bwp.+?)"><img src="(images/Previous.jpg|/images/Previous.jpg)"')
    help = 'Index format: yymmdd'


class Baroquen(_BasicScraper):
    url = 'http://www.baroquencomics.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.baroquencomics\.com/Comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.baroquencomics\.com/[^"]+)', after='prev'))
    help = 'Index format: yyyy/mm/dd/strip-name'


class BetweenFailures(_BasicScraper):
    url = 'http://betweenfailures.com/'
    stripUrl = url + 'archives/archive/%s'
    imageSearch = compile(tagre("img", "src", r'(http://betweenfailures\.com/wp-content/webcomic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://betweenfailures\.com/archives/archive/[^"]+)', after="previous"))
    help = 'Index format: stripnum-strip-name'

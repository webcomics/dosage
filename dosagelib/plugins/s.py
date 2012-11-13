# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, MULTILINE, IGNORECASE, sub
from os.path import splitext

from ..scraper import _BasicScraper
from ..helpers import bounceStarter, indirectStarter


class SailorsunOrg(_BasicScraper):
    latestUrl = 'http://www.sailorsun.org/'
    stripUrl = 'http://www.sailorsun.org/browse.php?comicID=%s'
    imageSearch = compile(r'(comics/.+?)"')
    prevSearch = compile(r'/(browse.php.+?)".+?/prev.gif')
    help = 'Index format: n (unpadded)'



class SamAndFuzzy(_BasicScraper):
    latestUrl = 'http://www.samandfuzzy.com/'
    stripUrl = 'http://samandfuzzy.com/%s'
    imageSearch = compile(r'(/comics/.+?)" alt')
    prevSearch = compile(r'"><a href="(.+?)"><img src="imgint/nav_prev.gif"')
    help = 'Index format: nnnn'



class SarahZero(_BasicScraper):
    latestUrl = 'http://www.sarahzero.com/'
    stripUrl = 'http://www.sarahzero.com/sz_%s.html'
    imageSearch = compile(r'<img src="(z_(?:(?:spreads)|(?:temp)).+?)" alt=""')
    prevSearch = compile(r'onmouseout="changeImages\(\'sz_05_nav\',\'z_site/sz_05_nav.gif\'\);return true" href="(sz_.+?)">')
    help = 'Index format: nnnn'



class ScaryGoRound(_BasicScraper):
    latestUrl = 'http://www.scarygoround.com/'
    stripUrl = 'http://www.scarygoround.com/?date=%s'
    imageSearch = compile(r'<img src="(strips/\d{8}\..{3})"')
    prevSearch = compile(r'f><a href="(.+?)"><img src="site-images/previous.png"')
    help = 'Index format: n (unpadded)'



class SchoolBites(_BasicScraper):
    latestUrl = 'http://www.schoolbites.net/'
    stripUrl = 'http://www.schoolbites.net/d/%s.html'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'first_day.+?(/d/.+?.html).+?/previous_day.gif')
    help = 'Index format: yyyymmdd'


class SinFest(_BasicScraper):
    name = 'KeenSpot/SinFest'
    latestUrl = 'http://www.sinfest.net/'
    stripUrl = 'http://www.sinfest.net/archive_page.php?comicID=%s'
    imageSearch = compile(r'<img src=".+?(/comikaze/comics/.+?)"')
    prevSearch = compile(r'(/archive_page.php\?comicID=.+?)".+?prev_a')
    help = 'Index format: n (unpadded)'


class SlightlyDamned(_BasicScraper):
    latestUrl = 'http://raizap.com/sdamned/index.php'
    stripUrl = 'http://raizap.com/sdamned/pages.php\?comicID=%s'
    imageSearch = compile(r'"(.+?comics2/.+?)"')
    prevSearch = compile(r'</a>.+?(pages.php\?comicID=.+?)".+?back1')
    help = 'Index format: n (unpadded)'



class SluggyFreelance(_BasicScraper):
    latestUrl = 'http://www.sluggy.com/'
    stripUrl = 'http://www.sluggy.com/comics/archives/daily/%s'
    imageSearch = compile(r'<img src="(/images/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?><span class="ui-icon ui-icon-seek-prev">')
    help = 'Index format: yymmdd'



class SodiumEyes(_BasicScraper):
    stripUrl = 'http://sodiumeyes.com/%s'
    imageSearch = compile(r'(/comic/.+?)"')
    prevSearch = compile(r'"http://sodiumeyes.com/(.+?/)"><.+?comic-prev')
    help = 'Index format: nnn'
    starter = indirectStarter('http://sodiumeyes.com/',
                              compile(r'<a href="http://sodiumeyes.com/(\d\d\d\d.+?/)">'))



class SpareParts(_BasicScraper):
    latestUrl = 'http://www.sparepartscomics.com/'
    stripUrl = 'http://www.sparepartscomics.com/comics/\\?date=s%'
    imageSearch = compile(r'(/comics/2.+?)[" ]')
    prevSearch = compile(r'(/comics/.+?|index.php\?.+?)".+?Prev')
    help = 'Index format: yyyymmdd'



class Stubble(_BasicScraper):
    latestUrl = 'http://www.stubblecomics.com/d/20051230.html'
    stripUrl = 'http://www.stubblecomics.com/d/%s.html'
    imageSearch = compile(r'"(/comics/.*?)"')
    prevSearch = compile(r'"(.*?)".*?backarrow')
    help = 'Index format: yyyymmdd'



class StrawberryDeathCake(_BasicScraper):
    latestUrl = 'http://rainchildstudios.com/strawberry/'
    stripUrl = 'http://rainchildstudios.com/strawberry/?p=%s'
    imageSearch = compile(r'/(comics/.+?)"')
    prevSearch = compile(r'strawberry/(\?p=.+?)".+?span class="prev"')
    help = 'Index format: n (good luck)'



class SuburbanTribe(_BasicScraper):
    latestUrl = 'http://www.pixelwhip.com/'
    stripUrl = 'http://www.pixelwhip.com/?p%s'
    imageSearch = compile(r'<img src="(http://www.pixelwhip.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: nnnn'



class SuccubusJustice(_BasicScraper):
    latestUrl = 'http://www.succubus-justice.com/Com%20main%20frame.htm'
    stripUrl = 'http://www.succubus-justice.com/%s%%20frame.htm'
    imageSearch = compile(r'<p align="center"><img src="(/\d+.\w{3,4})"')
    prevSearch = compile(r'<a href="(/[\w%]+\.htm|[\w%]+\.htm)"[^>]+?><img src="124.gif"')
    help = 'Index format: nnn'



class Supafine(_BasicScraper):
    latestUrl = 'http://www.supafine.com/comics/classic.php'
    stripUrl = 'http://www.supafine.com/comics/classic.php?comicID=%s'
    imageSearch = compile(r'<img src="(http://www.supafine.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(http://www.supafine.com/comics/classic.php\?.+?)"><img src="http://supafine.com/comikaze/images/previous.gif" ')
    help = 'Index format: nnn'



class SomethingPositive(_BasicScraper):
    latestUrl = 'http://www.somethingpositive.net/'
    stripUrl = 'http://www.somethingpositive.net/sp%s.shtml'
    imageSearch = compile(r'<img src="(/arch/sp\d+.\w{3,4}|/sp\d+.\w{3,4})"')
    prevSearch = compile(r'<a \n?href="(sp\d{8}\.shtml)">(<font size=1\nface=".+?"\nSTYLE=".+?">Previous|<img src="images2/previous|<img src="images/previous.gif")', MULTILINE | IGNORECASE)
    help = 'Index format: mmddyyyy'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]



class SexyLosers(_BasicScraper):
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



def smackJeeves(names):
    # XXX mature content can be viewed directly with:
    # http://www.smackjeeves.com/mature.php?ref=<percent-encoded-url>
    class _SJScraper(_BasicScraper):
        stripUrl = property(lambda self: self.baseUrl + self.shortName)
        imageSearch = compile(r'<img src="(http://www\.smackjeeves\.com/images/uploaded/comics/[^"]*)"', IGNORECASE)
        prevSearch = compile(r'<a href="(/comics/\d+/[^"]*)"><img[^>]*alt="< Previous"', IGNORECASE)
        help = 'Index format: nnnn (some increasing number)'

        @classmethod
        def namer(cls, imageUrl, pageUrl):
            return pageUrl.split('/')[-2]


    def makeScraper(shortName):
        baseUrl = 'http://%s.smackjeeves.com/comics/' % shortName
        return type('SmackJeeves_%s' % shortName,
            (_SJScraper,),
            dict(
            name='SmackJeeves/' + shortName,
            baseUrl=baseUrl,
            starter=bounceStarter(baseUrl, compile(r'<a href="(/comics/\d+/[^"]*)"><img[^>]*alt="Next >"', IGNORECASE)))
        )
    return dict((name, makeScraper(name)) for name in names)


globals().update(smackJeeves([
    '20galaxies',
    'axe13',
    'beartholomew',
    'bliss',
    'durian',
    'heard',
    'mpmcomic',
    'nlmo-project',
    'paranoidloyd',
    'thatdreamagain',
    'wowcomics',
    ]))



class StarCrossdDestiny(_BasicScraper):
    latestUrl = 'http://www.starcrossd.net/comic.html'
    stripUrl = 'http://www.starcrossd.net/archives/%s.html'
    imageSearch = compile(r'<img src="(http://www\.starcrossd\.net/(?:ch1|strips|book2)/[^"]+)">')
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



class SGVY(_BasicScraper):
    stripUrl = 'http://www.sgvy.com/Edda%s/Issue%s/Page%s.html'
    imageSearch = compile(r'"comic" src="((?:\.\./)+images/sgvy/sgvy-[-\w\d]+\.\w+)"')
    prevSearch = compile(r'<a href="((?:\.\./)+(?:Edda\d+|Holiday)/(?:Issue\d+/Page\d+|Cover)\.html)">Prev</a>')
    help = 'Index format: edda-issue-page'

    starter = indirectStarter('http://www.sgvy.com/', compile(r'<a href="(archives/(?:Edda\d+|Holiday)/(?:Issue\d+/Page\d+|Cover)\.html)">'))

    def setStrip(self, index):
        self.currentUrl = self.stripUrl % tuple(map(int, index.split('-')))


class Spamusement(_BasicScraper):
    stripUrl = 'http://spamusement.com/index.php/comics/view/%s'
    imageSearch = compile(r'<img src="(http://spamusement.com/gfx/\d+\..+?)"', IGNORECASE)
    prevSearch = compile(r'<a href="(http://spamusement.com/index.php/comics/view/.+?)">', IGNORECASE)
    help = 'Index format: n (unpadded)'

    starter = indirectStarter('http://spamusement.com/', prevSearch)



def snafuComics():
    class _SnafuComics(_BasicScraper):
        imageSearch = compile(r'<img src=http://\w+\.snafu-comics\.com/(comics/\d{6}_\w*\.\w{3,4})')
        prevSearch = compile(r'<a href="(\?comic_id=\d+)">Previous</a>')
        help = 'Index format: n (unpadded)'

        @property
        def stripUrl(self):
            return self.latestUrl + 'index.php?strip_id=%s'

    comics = {
        'Grim': 'grim',
        'KOF': 'kof',
        'PowerPuffGirls': 'ppg',
        'Snafu': 'www',
        'Tin': 'tin',
        'TW': 'tw',
        'Sugar': 'sugar',
        'SF': 'sf',
        'Titan': 'titan',
        'EA': 'ea',
        'Zim': 'zim',
        'Soul': 'soul',
        'FT': 'ft',
        'Bunnywith': 'bunnywith',
        'Braindead': 'braindead',
        }

    url = 'http://%s.snafu-comics.com/'
    return dict((name, type('SnafuComics_%s' % name,
                            (_SnafuComics,),
                             dict(name='SnafuComics/' + name,
                             latestUrl=url % host)))
                for name, host in comics.items())

globals().update(snafuComics())



class SosiaalisestiRajoittuneet(_BasicScraper):
    latestUrl = 'http://sosiaalisestirajoittuneet.fi/index_nocomment.php'
    stripUrl = 'http://sosiaalisestirajoittuneet.fi/index_nocomment.php?date=%s'
    imageSearch = compile(r'<img src="(strips/web/\d+.jpg)" alt=".*?"   />')
    prevSearch = compile(r'<a href="(index_nocomment\.php\?date=\d+)"><img\s+src="images/active_edellinen\.gif"', MULTILINE)



class StrangeCandy(_BasicScraper):
    latestUrl = 'http://www.strangecandy.net/'
    stripUrl = 'http://www.strangecandy.net/d/%s.html'
    imageSearch = compile(r'src="(http://www.strangecandy.net/comics/\d{8}.\w{1,4})"')
    prevSearch = compile(r'<a href="(http://www.strangecandy.net/d/\d{8}.html)"><img[^>]+?src="http://www.strangecandy.net/images/previous_day.gif"')
    help = 'Index format: yyyyddmm'



class SMBC(_BasicScraper):
    latestUrl = 'http://www.smbc-comics.com/'
    stripUrl = 'http://www.smbc-comics.com/index.php?db=comics&id=%s'
    imageSearch = compile(r'<img src=\'(.+?\d{8}.\w{1,4})\'>')
    prevSearch = compile(r'131,13,216,84"\n\s+href="(.+?)#comic"\n>', MULTILINE)
    help = 'Index format: nnnn'



class SomethingLikeLife(_BasicScraper):
    latestUrl = 'http://www.pulledpunches.com/'
    stripUrl = 'http://www.pulledpunches.com/?p=%s'
    imageSearch = compile(r'<img src="(http://www.pulledpunches.com/comics/[^"]*)"')
    prevSearch = compile(r'</a> <a href="(http://www.pulledpunches.com/\?p=[^"]*)"><img src="back1.gif"')
    help = 'Index format: nn'



class StickEmUpComics(_BasicScraper):
    latestUrl = 'http://stickemupcomics.com/'
    stripUrl = 'http://stickemupcomics.com/%s'
    imageSearch = compile(r'<img src="(http://stickemupcomics.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><span class="prev">')
    help = 'Index format: yyyy/mm/dd/stripname'



class SexDemonBag(_BasicScraper):
    latestUrl = 'http://www.sexdemonbag.com/'
    stripUrl = 'http://www.sexdemonbag.com/?p=%s'
    imageSearch = compile(r'<img src="(http://www.sexdemonbag.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)">')
    help = 'Index format: nnn'

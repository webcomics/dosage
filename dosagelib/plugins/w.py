# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile, IGNORECASE, DOTALL

from ..scraper import _BasicScraper
from ..helpers import queryNamer, bounceStarter


class WayfarersMoon(_BasicScraper):
    latestUrl = 'http://www.wayfarersmoon.com/'
    imageUrl = 'http://www.wayfarersmoon.com/index.php\?page=%s'
    imageSearch = compile(r'<img src="(/admin.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back.gif')
    help = 'Index format: nn'


class WhiteNinja(_BasicScraper):
    latestUrl = 'http://www.whiteninjacomics.com/comics.shtml'
    imageUrl = 'http://www.whiteninjacomics.com/comics/%s.shtml'
    imageSearch = compile(r'<img src=(/images/comics/(?!t-).+?\.gif) border=0')
    prevSearch = compile(r'(/comics/.+?shtml).+?previous')
    help = 'Index format: s (comic name)'


class WhiteNoise(_BasicScraper):
    latestUrl = 'http://www.wncomic.com/archive.php'
    imageUrl = 'http://www.wncomic.com/archive_comments.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'First .+?"(archive.+?)".+?top_back')
    help = 'Index format: n'



class WhyTheLongFace(_BasicScraper):
    latestUrl = 'http://www.absurdnotions.org/wtlf200709.html'
    imageUrl = 'http://www.absurdnotions.org/wtlf%s.html'
    imageSearch = compile(r'<img src="(http://www.absurdnotions.org/wtlf.+?|lf\d+.\w{1,4})"', IGNORECASE)
    prevSearch = compile(r'HREF="(.+?)"><IMG SRC="nprev.gif" ')
    help = 'Index format: yyyymm'



class Wigu(_BasicScraper):
    latestUrl = 'http://www.wigu.com/wigu/'
    imageUrl = 'http://www.wigu.com/wigu/?date=%s'
    imageSearch = compile(r'<img src="(strips/\d{8}\..+?)" alt=""')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>< PREV COMIC</a> ')
    help = 'Index format: yyyymmdd'



class WiguTV(_BasicScraper):
    latestUrl = 'http://jjrowland.com/'
    imageUrl = 'http://jjrowland.com/archive/%s.html'
    imageSearch = compile(r'"(/comics/.+?)"')
    prevSearch = compile(r'<a href="(/archive/.+?)"[^>]+?>&nbsp;')
    help = 'Index format: yyyymmdd'



class WotNow(_BasicScraper):
    latestUrl = 'http://shadowburn.binmode.com/wotnow/'
    imageUrl = 'http://shadowburn.binmode.com/wotnow/comic.php?comic_id=%s'
    imageSearch = compile(r'<IMG SRC="(comics/.+?)"')
    prevSearch = compile(r'<A HREF="(.+?)"><IMG SRC="images/b_prev.gif" ')
    help = 'Index format: n (unpadded)'



class WorldOfWarcraftEh(_BasicScraper):
    latestUrl = 'http://woweh.com/'
    imageUrl = 'http://woweh.com/?p='
    imageSearch = compile(r'http://woweh.com/(comics/.+?)"')
    prevSearch = compile(r'woweh.com/(\?p=.+:?)".+:?="prev')
    help = 'Index format: non'


class Wulffmorgenthaler(_BasicScraper):
    latestUrl = 'http://www.wulffmorgenthaler.com/'
    imageUrl = 'http://www.wulffmorgenthaler.com/Default.aspx?id=%s'
    imageSearch = compile(r'img id="ctl00_content_Strip1_imgStrip".+?class="strip" src="(striphandler\.ashx\?stripid=[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})"')
    prevSearch = compile(r'<a href="(/default\.aspx\?id=[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})" id="ctl00_content_Strip1_aPrev">')
    help = 'Index format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx (GUID)'
    namer = queryNamer('stripid')


def webcomicsNation():
    class _WebcomicsNation(_BasicScraper):
        imageSearch = compile(r'<a name="strip\d*?">.*?<img[^>]+?src="([^"]*?memberimages/.+?)"', IGNORECASE + DOTALL)
        prevSearch = compile(r'href="([^"]*?whichbutton=prev[^"]*?)"', IGNORECASE)
        help = 'Index format: nnnn (non-contiguous)'

        @property
        def imageUrl(self):
            return self.baseUrl + '?view=archive&amp;chapter=%s'

    comics = {
        'AgnesQuill': 'daveroman/agnes/',
        'Elvenbaath': 'tdotodot2k/elvenbaath/',
        'IrrationalFears': 'uvernon/irrationalfears/',
        'KismetHuntersMoon': 'laylalawlor/huntersmoon/',
        'SaikoAndLavender': 'gc/saiko/',
        'MyMuse': 'gc/muse/',
        'NekkoAndJoruba': 'nekkoandjoruba/nekkoandjoruba/',
        'JaxEpoch': 'johngreen/quicken/',
        'QuantumRockOfAges': 'DreamchildNYC/quantum/',
        'ClownSamurai' : 'qsamurai/clownsamurai/',
        }

    return dict((name, type('WebcomicsNation_%s' % name,
                (_WebcomicsNation,),
                dict(name='WebcomicsNation/' + name,
                latestUrl='http://www.webcomicsnation.com/' + subpath)))
                for name, subpath in comics.items())


globals().update(webcomicsNation())



class WhiteNoise(_BasicScraper):
    latestUrl = 'http://www.wncomic.com/archive.php'
    imageUrl = 'http://www.wncomic.com/archive_comments.php?strip_id=%s'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="images/top_back.jpg" ')
    help = 'Index format: n'



class WapsiSquare(_BasicScraper):
    latestUrl = 'http://wapsisquare.com/'
    imageUrl = 'http://wapsisquare.com/comic/%s'
    imageSearch = compile(r'<img src="(http://wapsisquare.com/comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>Previous</a>')
    help = 'Index format: strip-name'



class WrongWay(_BasicScraper):
    latestUrl = 'http://www.wrongwaycomics.com/'
    imageUrl = 'http://www.wrongwaycomics.com/%s.html'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r' <a class="comicNav" href="(.+?)" onmouseover="previousLinkIn\(\)"')
    help = 'Index format: nnn'



class WeCanSleepTomorrow(_BasicScraper):
    latestUrl = 'http://wecansleeptomorrow.com/'
    imageUrl = 'http://wecansleeptomorrow.com/2009/12/07/smothered/'
    imageSearch = compile(r'<img src="(http://wecansleeptomorrow.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)">')
    help = 'Index format: yyyy/mm/dd/stripname'



class _WLP(_BasicScraper):
    imageSearch=compile(r'SRC="(http://www.wlpcomics.com/adult/.+?|http://www.wlpcomics.com/general/.+?)"', IGNORECASE)
    prevSearch=compile(r'</a> <A HREF="(\w+.html)">Previous Page</a>', IGNORECASE)
    help='Index format: nnn'


    @property
    def baseUrl(self):
        return 'http://www.wlpcomics.com/%s' % (self.path,)


    @property
    def imageUrl(self):
        return self.baseUrl + '%s.html'


    def namer(self, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]


    def starter(self):
        # XXX: ergh
        meth = bounceStarter(self.baseUrl, compile(r'</a> <A HREF="(\w+.html)">Next Page</a>', IGNORECASE))
        return meth.__get__(self, type(self))()



class ChichiChan(_WLP):
    name = 'WLP/ChichiChan'
    path = 'adult/chichi/'



class ChocolateMilkMaid(_WLP):
    name = 'WLP/ChocolateMilkMaid'
    path = 'adult/cm/'



class MaidAttack(_WLP):
    name = 'WLP/MaidAttack'
    path = 'general/maidattack/'



class ShadowChasers(_WLP):
    name = 'WLP/ShadowChasers'
    path = 'general/shadowchasers/'



class Stellar(_WLP):
    name = 'WLP/Stellar'
    path = 'adult/stellar/'



class Wondermark(_BasicScraper):
    latestUrl = 'http://wondermark.com'
    imageUrl = 'http://wondermark.com/%s/'
    imageSearch = compile(r'<img src="(http://wondermark.com/c/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" rel="prev">')
    help = 'Index format: nnn'

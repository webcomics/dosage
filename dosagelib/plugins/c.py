# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile

from ..scraper import _BasicScraper
from ..helpers import bounceStarter
from ..util import tagre


class CaptainSNES(_BasicScraper):
    latestUrl = 'http://www.captainsnes.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(r"<img src='(http://www\.captainsnes\.com/comics/[^']+)'")
    prevSearch = compile(r'<a href="(http://www\.captainsnes\.com/[^"]+)"><span class="prev">')
    multipleImagesPerStrip = True
    help = 'Index format: yyyy/mm/dd/nnn-stripname'


class CaseyAndAndy(_BasicScraper):
    latestUrl = 'http://www.galactanet.com/comic/'
    stripUrl = latestUrl + 'view.php?strip=%s'
    imageSearch = compile(tagre("img", "src", r'(Strip\d+\.gif)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?strip=\d+)')
     + tagre("img", "src", r'previous\.gif'))
    help = 'Index format: number'


class CaribbeanBlue(_BasicScraper):
    latestUrl = 'http://cblue.katbox.net/'
    stripUrl = latestUrl + 'archive/%s'
    imageSearch = compile(tagre("img", "src", r'(http://cblue\.katbox\.net/wp-content/webcomic/cblue/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://cblue\.katbox\.net/archive/[^"]+)', after="previous"))
    help = 'Index format: nnn-stripname'


class Catalyst(_BasicScraper):
    baseUrl = "http://catalyst.spiderforest.com/"
    latestUrl = baseUrl + "comic.php?comic_id=415"
    stripUrl = baseUrl + "comic.php?comic_id=%s"
    imageSearch = compile(tagre("img", "src", r'(http://catalyst\.spiderforest\.com/comics/[^"]+)'))
    prevSearch = compile("<center>" + tagre("a", "href", r'(http://catalyst\.spiderforest\.com/comic\.php\?comic_id=\d+)'))
    help = 'Index format: number'


class Catena(_BasicScraper):
    latestUrl = 'http://catenamanor.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://catenamanor\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='rel="prev"'))
    help = 'Index format: yyyy/mm/dd/<name>'


class ChasingTheSunset(_BasicScraper):
    latestUrl = 'http://www.fantasycomic.com/'
    stripUrl = latestUrl + 'index.php?p=c%s'
    imageSearch = compile(r'(/cmsimg/.+?)".+?comic-img')
    prevSearch = compile(r'<a href="(.+?)" title="" ><img src="(images/eye-prev.png|images/cn-prev.png)"')
    help = 'Index format: n'


class CheckerboardNightmare(_BasicScraper):
    latestUrl = 'http://www.checkerboardnightmare.com/'
    stripUrl = latestUrl + 'd/%s.shtml'
    imageSearch=compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch=compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help='Index format: yyyymmdd'


class Chisuji(_BasicScraper):
    latestUrl = 'http://www.chisuji.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'<img src="(http://www.chisuji.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.chisuji.com/.+?)">')
    help = 'Index format: yyyy/mm/dd/strip-name'


class ChugworthAcademy(_BasicScraper):
    latestUrl = 'http://chugworth.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'<img src="(.+?)" alt="Comic')
    prevSearch = compile(r'<a href="(http://chugworth.com/\?p=\d{1,4})"[^>]+?title="Previous">')
    help = 'Index format: n (unpadded)'


class ChugworthAcademyArchive(_BasicScraper):
    latestUrl = 'http://chugworth.com/archive/?strip_id=422'
    stripUrl = 'http://chugworth.com/archive/?strip_id=%s'
    imageSearch = compile(r'<img src=(comics/\d+.+?.\w{1,4})')
    prevSearch = compile(r'<a href=\'(.+?)\'><img src=\'images/previous.gif')
    help = 'Index format: nnn'


class CigarroAndCerveja(_BasicScraper):
    latestUrl = 'http://www.cigarro.ca/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r"(/comics/.+?)'")
    prevSearch = compile(r'(/\?p=.+?)">&laq')
    help = 'Index format: non'


class Comedity(_BasicScraper):
    latestUrl = 'http://www.comedity.com/'
    stripUrl = latestUrl + 'index.php?strip_id=%s'
    imageSearch = compile(r'<img src="(Comedity_files/.+?)"')
    prevSearch = compile(r'<a href="(/?index.php\?strip_id=\d+?)"> *<img alt=\"Prior Strip')
    help = 'Index format: n (no padding)'


class Commissioned(_BasicScraper):
    latestUrl = 'http://www.commissionedcomic.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.commissionedcomic\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.commissionedcomic\.com/\?p=\d+)', after="prev"))
    help = 'Index format: n'


class Concession(_BasicScraper):
    latestUrl = 'http://concessioncomic.com/'
    stripUrl = latestUrl + 'index.php?pid=%s'
    imageSearch = compile(tagre("img", "src", r'(http://concessioncomic\.com/comics/[^"]+)', after="Comic"))
    prevSearch = compile(tagre("a", "href", r'(http://concessioncomic\.com/index\.php\?pid=\d+)', after="nav-prev"))
    help = 'Index format: number'


class CoolCatStudio(_BasicScraper):
    latestUrl = 'http://www.coolcatstudio.com/'
    stripUrl = latestUrl + 'strips-cat/ccs%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.coolcatstudio\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.coolcatstudio\.com/strips-cat/[^"]+)', before="prev"))
    help = 'Index format: yyyymmdd'


class CourtingDisaster(_BasicScraper):
    latestUrl = 'http://www.courting-disaster.com/'
    stripUrl = latestUrl + 'archive/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/\d+\.html)') + tagre("img", "src", r'/images/previous\.gif'))
    help = 'Index format: yyyymmdd'


class CrapIDrewOnMyLunchBreak(_BasicScraper):
    latestUrl = 'http://crap.jinwicked.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://crap\.jinwicked\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class CtrlAltDel(_BasicScraper):
    latestUrl = 'http://www.cad-comic.com/cad/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://v\.cdn\.cad-comic\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="nav-back"))
    help = 'Index format: yyyymmdd'


class CtrlAltDelSillies(CtrlAltDel):
    name = 'CtrlAltDel/Sillies'
    latestUrl = 'http://www.cad-comic.com/sillies/'
    stripUrl = latestUrl + '%s'


class Curvy(_BasicScraper):
    latestUrl = 'http://www.c.urvy.org/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(tagre("img", "src", r'(/c/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\?date=\d+)') + tagre("img", "src", "/nav/prev\.png"))
    help = 'Index format: yyyymmdd'


class CatAndGirl(_BasicScraper):
    latestUrl = 'http://catandgirl.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://catandgirl\.com/archive/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+r"[^<]+Previous</a>")
    help = 'Index format: n (unpadded)'


class CyanideAndHappiness(_BasicScraper):
    _latestUrl = 'http://www.explosm.net/comics/'
    starter = bounceStarter(_latestUrl, compile(tagre("a", "href", r"(/comics/\d+/)", before="next")))
    stripUrl = _latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://(?:www\.)?explosm\.net/db/files/[^"]+)', before="a daily webcomic"))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+/)', before="prev"))
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imgname = imageUrl.split('/')[-1]
        imgnum = pageUrl.split('/')[-2]
        return '%s_%s' % (imgnum, imgname)


class CrimsonDark(_BasicScraper):
    latestUrl = 'http://www.davidcsimon.com/crimsondark/'
    stripUrl = latestUrl + 'index.php?view=comic&strip_id=%s'
    imageSearch = compile(r'src="(.+?strips/.+?)"')
    prevSearch = compile(r'<a href=[\'"](/crimsondark/index\.php\?view=comic&amp;strip_id=\d+)[\'"]><img src=[\'"]themes/cdtheme/images/active_prev.png[\'"]')
    help = 'Index format: n (unpadded)'


class CatsAndCameras(_BasicScraper):
    latestUrl = 'http://catsncameras.com/cnc/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'<img src="(http://catsncameras.com/cnc/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://catsncameras.com/cnc/.+?)">')
    help = 'Index format: nnn'


class CowboyJedi(_BasicScraper):
    latestUrl = 'http://www.cowboyjedi.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.cowboyjedi.\com/comics/[^"]+)'))
    prevSearch = compile(r'<a href="(http://www.cowboyjedi.com/.+?)" class="navi navi-prev"')
    help = 'Index format: yyyy/mm/dd/strip-name'


class CasuallyKayla(_BasicScraper):
    latestUrl = 'http://casuallykayla.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://casuallykayla\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("div", "class", r'nav-previous') + tagre("a", "href", r'([^"]+)'))
    help = 'Index format: nnn'


class Collar6(_BasicScraper):
    latestUrl = 'http://collar6.com/'
    stripUrl = latestUrl + 'archive/%s'
    imageSearch = compile(tagre("img", "src", r'(http://collar6\.com/wp-content/webcomic/collar6/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://collar6\.com/archive/[^"]+)', after="previous"))
    help = 'Index format: <name>'


class Chester5000XYV(_BasicScraper):
    latestUrl = 'http://jessfink.com/Chester5000XYV/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://jessfink\.com/Chester5000XYV/comics/[^"]+)'))
    prevSearch = compile(r'<a href="(.+?)"><span class="prev">')
    help = 'Index format: nnn'


class Champ2010(_BasicScraper):
    # the latest URL is hard coded since the comic is discontinued
    latestUrl = 'http://jedcollins.com/champ2010/champ-12-30-10.html'
    stripUrl = 'http://jedcollins.com/champ2010/%s.html'
    imageSearch = compile(tagre("img", "src", r'(http://jedcollins\.com/champ2010/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://jedcollins\.com/champ2010/[^"]+)', after="Previous"))
    help = 'Index format: yy-dd-mm'


class Chucklebrain(_BasicScraper):
    latestUrl = 'http://www.chucklebrain.com/main.php'
    stripUrl = latestUrl + '?img=%s'
    imageSearch = compile(tagre("img", "src", r'(/images/strip[^"]+)'))
    prevSearch = compile(r'<a href=\'(/main.php\?img\=\d+)\'><img src=\'/images/previous.jpg\'')
    help = 'Index format: nnn'


class CompanyY(_BasicScraper):
    latestUrl = 'http://company-y.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://company-y\.com/comics/[^"]+)'))
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://company-y.com/.+?)"')
    help = 'Index format: yyyy/mm/dd/strip-name'


class CorydonCafe(_BasicScraper):
    starter = bounceStarter('http://corydoncafe.com/', compile(tagre("a", "href", r"(http://corydoncafe\.com/\d+/[^']+)", after="next", quote="'")))
    stripUrl = 'http://corydoncafe.com/%s.php'
    imageSearch = compile(tagre("img", "src", r"(\./[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r"(http://corydoncafe\.com/\d+/[^']+)", after="prev", quote="'"))
    help = 'Index format: yyyy/stripname'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]


class CraftedFables(_BasicScraper):
    latestUrl = 'http://www.craftedfables.com/'
    stripUrl = 'http://www.caf-fiends.net/craftedfables/?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.caf-fiends\.net/craftedfables/comics/[^"]+)'))
    prevSearch = compile(r'<a href="(http://www.caf-fiends.net/craftedfables/.+?)"><span class="prev">')
    help = 'Index format: nnn'

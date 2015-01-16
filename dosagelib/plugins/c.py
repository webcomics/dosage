# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape

from ..scraper import _BasicScraper
from ..helpers import bounceStarter, indirectStarter
from ..util import tagre


class Caggage(_BasicScraper):
    url = 'http://caggagecomic.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/%s'
    firstStripUrl = stripUrl % '77'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchives/\d+)' % rurl, after="prev"))
    help = 'Index format: number'

class CampComic(_BasicScraper):
    url = 'http://campcomic.com/comic/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '6'
    imageSearch = compile(tagre("img", "src", r'(http://hw1\.pa-cdn\.com/camp/assets/img/katie/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, before="btn btnPrev"))
    help = 'Index Format: number'
    description = u'Camp Weedonwantcha is a place where kids get dropped off for the summer and are never picked up again.'

class CaptainSNES(_BasicScraper):
    description = u'Captain SNES'
    url = 'http://www.captainsnes.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2001/07/10/the-mistake'
    imageSearch = compile(tagre("img", "src", r"(%scomics/[^']+)" % rurl, quote="'"))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl) + tagre("span", "class", "prev"))
    multipleImagesPerStrip = True
    help = 'Index format: yyyy/mm/dd/nnn-stripname'


class Carciphona(_BasicScraper):
    description = u'Fantasy webcomic by Shilin. In an era where magic is forbidden, a sorceress struggles to restore her once peaceful life.'
    url = 'http://carciphona.com/'
    stripUrl = url + 'view.php?page=%s&chapter=%s'
    imageSearch = compile(tagre("div", "style", r'background-image:url\((_pages[^)]*)\)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?[^"]*)', after="prevarea"))
    latestSearch = compile(tagre("a", "href", r'(view\.php\?page=[0-9]+[^"]*)'))
    help = 'Index format: None'
    starter = indirectStarter(url, latestSearch)

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        ip = imageUrl.split('/')
        return "volume_%s_page_%s" % (ip[-2], ip[-1])


class CaseyAndAndy(_BasicScraper):
    description = u'Casey and Andy'
    url = 'http://www.galactanet.com/comic/'
    stripUrl = url + 'view.php?strip=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(Strip\d+\.gif)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?strip=\d+)')
     + tagre("img", "src", r'previous\.gif'))
    help = 'Index format: number'


class CasuallyKayla(_BasicScraper):
    description = u'Casually Kayla: Keeping it as Casual as possible'
    url = 'http://casuallykayla.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '89'
    imageSearch = compile(tagre("img", "src", r'(http://casuallykayla\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("div", "class", r'nav-previous') + tagre("a", "href", r'([^"]+)'))
    help = 'Index format: nnn'


class Catalyst(_BasicScraper):
    baseUrl = "http://catalyst.spiderforest.com/"
    rurl = escape(baseUrl)
    url = baseUrl + "comic.php?comic_id=415"
    stripUrl = baseUrl + "comic.php?comic_id=%s"
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'((?:%s)?comics/[^"]+)' % rurl))
    prevSearch = compile("<center>" + tagre("a", "href", r'(%scomic\.php\?comic_id=\d+)' % rurl))
    help = 'Index format: number'


class CatAndGirl(_BasicScraper):
    description = u'Cat and Girl'
    url = 'http://catandgirl.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '1602'
    imageSearch = compile(tagre("img", "src", r'(%sarchive/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+r"[^<]+Previous</a>")
    help = 'Index format: n (unpadded)'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            self.stripUrl % '4299',
        )


class Catena(_BasicScraper):
    url = 'http://catenamanor.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/06/17/the-start-of-it-all'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='rel="prev"'))
    help = 'Index format: yyyy/mm/dd/<name>'


class CatsAndCameras(_BasicScraper):
    description = u'Just when you thought it was safe to go to the photographer'
    url = 'http://catsncameras.com/cnc/'
    rurl = escape(url)
    stripUrl = url + '?comic=%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("span", "class", r'mininav-prev') +
        tagre("a", "href", r'(%s[^"]+)' % rurl))
    help = 'Index format: stripname'


class ChainsawSuit(_BasicScraper):
    description = u'internet humor, fresh-cut'
    url = 'http://chainsawsuit.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/03/12/strip-338'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomic/\d+/\d+/\d+/[^"]+)' % rurl) +
        tagre("img", "alt", r'previous'))
    help = 'Index format: yyyy/mm/dd/stripname'


class Champ2010(_BasicScraper):
    description = u'Champ2010 - an almost daily journal comic from jed collins who is not drinking this year. webcomic'
    baseUrl = 'http://jedcollins.com/champ2010/'
    rurl = escape(baseUrl)
    # the latest URL is hard coded since the comic is discontinued
    url = baseUrl + 'champ-12-30-10.html'
    stripUrl = baseUrl + '%s.html'
    firstStripUrl = stripUrl % 'champ1-1-10-fuck'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="Previous"))
    help = 'Index format: yy-dd-mm'


class ChannelAte(_BasicScraper):
    description = u'Comics and Cartoons by Ryan Hudson'
    url = 'http://www.channelate.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class ChasingTheSunset(_BasicScraper):
    description = u'Chasing the Sunset | Fantasy Webcomic | Elves, Pixies and a blue dragon with orange stripes.'
    url = 'http://www.fantasycomic.com/'
    stripUrl = url + 'index.php?p=c%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'(/cmsimg/.+?)".+?comic-img')
    prevSearch = compile(r'<a href="(.+?)" title="" ><img src="(images/eye-prev.png|images/cn-prev.png)"')
    help = 'Index format: n'


class CheckerboardNightmare(_BasicScraper):
    description = u'Checkerboard Nightmare by Kristofer Straub - A Webcomics Institution'
    url = 'http://www.checkerboardnightmare.com/'
    stripUrl = url + 'd/%s.shtml'
    firstStripUrl = stripUrl % '20001110'
    imageSearch=compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch=compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help='Index format: yyyymmdd'


class Chester5000XYV(_BasicScraper):
    url = 'http://jessfink.com/Chester5000XYV/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '34'
    imageSearch = compile(tagre("img", "src", r'(http://jessfink\.com/Chester5000XYV/comics/[^"]+)'))
    prevSearch = compile(r'<a href="(.+?)"><span class="prev">')
    help = 'Index format: nnn'


class Chisuji(_BasicScraper):
    url = 'http://www.chisuji.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/05/02/chisujiposter01'
    imageSearch = compile(r'<img src="(http://www.chisuji.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(http://www.chisuji.com/.+?)">')
    help = 'Index format: yyyy/mm/dd/strip-name'


class CigarroAndCerveja(_BasicScraper):
    description = u'Cigarro & Cerveja'
    url = 'http://www.cigarro.ca/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(r"(/comics/.+?)'")
    prevSearch = compile(r'(/\?p=.+?)">&laq')
    help = 'Index format: non'


class Collar6(_BasicScraper):
    description = u'Collar 6'
    url = 'http://collar6.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s'
    firstStripUrl = stripUrl % 'collar-6-187'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/webcomic/collar6/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/[^"]+)' % rurl, after="previous"))
    help = 'Index format: <name>'


class Comedity(_BasicScraper):
    description = u'Comedity 2.0'
    url = 'http://www.comedity.com/'
    stripUrl = url + 'index.php?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<img src="(Comedity_files/.+?)"')
    prevSearch = compile(r'<a href="(/?index.php\?strip_id=\d+?)"> *<img alt=\"Prior Strip')
    help = 'Index format: n (no padding)'


class Commissioned(_BasicScraper):
    url = 'http://www.commissionedcomic.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '139'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: n'


class CompanyY(_BasicScraper):
    description = u'Company-Y'
    url = 'http://company-y.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/08/14/coming-soon'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("div", "class", r"nav-previous") +
        tagre("a", "href", r'(%s[^"]+)' % rurl))
    help = 'Index format: yyyy/mm/dd/strip-name'


class Concession(_BasicScraper):
    url = 'http://concessioncomic.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?pid=%s'
    firstStripUrl = stripUrl % '20060701'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl, after="Comic"))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php\?pid=\d+)' % rurl, after="nav-prev"))
    help = 'Index format: number'


class CoolCatStudio(_BasicScraper):
    url = 'http://www.coolcatstudio.com/'
    rurl = escape(url)
    stripUrl = url + 'strips-cat/%s'
    firstStripUrl = stripUrl % 'first'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sstrips-cat/[^"]+)' % rurl, before="prev"))
    help = 'Index format: ccsyyyymmdd'


class CorydonCafe(_BasicScraper):
    description = u'Corydon Cafe humorous online comic archive of abstruse awesomeness created by a starving artist'
    url = 'http://corydoncafe.com/'
    starter = indirectStarter(url,
        compile(tagre("a", "href", r'(\./\d+/[^"]+)')))
    stripUrl = url + '%s.php'
    imageSearch = compile(tagre("img", "src", r"(\./[^']+)", quote="'"))
    prevSearch = compile(tagre("a", "href", r"(http://corydoncafe\.com/\d+/[^']+)", after="prev", quote="'"))
    help = 'Index format: yyyy/stripname'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]


class CourtingDisaster(_BasicScraper):
    description = u'Courting Disaster by Brad Guigar - A Daily Webcomic'
    url = 'http://www.courting-disaster.com/'
    stripUrl = url + 'archive/%s.html'
    firstStripUrl = stripUrl % '20050112'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/archive/\d+\.html)') + tagre("img", "src", r'/images/previous\.gif'))
    help = 'Index format: yyyymmdd'


class CowboyJedi(_BasicScraper):
    description = u'A Long Time Ago In A Webcomic Updated Weekly...'
    url = 'http://www.cowboyjedi.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/08/10/a-new-webcomic'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/strip-name'


class CrapIDrewOnMyLunchBreak(_BasicScraper):
    description = u'A semi-biographical web comic about the struggles and occasional humour of daily life, pets, friends, and more. Currently completing the missing archive comics with your help.'
    url = 'http://crap.jinwicked.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/07/30/jin-and-josh-decide-to-move'
    imageSearch = compile(tagre("img", "src", r'(http://crap\.jinwicked\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class CtrlAltDel(_BasicScraper):
    url = 'http://www.cad-comic.com/cad/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(http://v\.cdn\.cad-comic\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="nav-back"))
    help = 'Index format: yyyymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Remove random junk from image names."""
        imgname = imageUrl.split('/')[-1]
        imgbase = imgname.rsplit('-', 1)[0]
        imgext = imgname.rsplit('.', 1)[1]
        return '%s.%s' % (imgbase, imgext)


class CtrlAltDelSillies(CtrlAltDel):
    name = 'CtrlAltDel/Sillies'
    url = 'http://www.cad-comic.com/sillies/'
    stripUrl = url + '%s'


class CrimsonDark(_BasicScraper):
    description = u'A Sci-Fi webcomic set in space in the distant future.'
    url = 'http://www.davidcsimon.com/crimsondark/'
    stripUrl = url + 'index.php?view=comic&strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'src="(.+?strips/.+?)"')
    prevSearch = compile(r'<a href=[\'"](/crimsondark/index\.php\?view=comic&amp;strip_id=\d+)[\'"]><img src=[\'"]themes/cdtheme/images/active_prev.png[\'"]')
    help = 'Index format: n (unpadded)'


class CraftedFables(_BasicScraper):
    description = u'Caf-Fiends'
    url = 'http://www.craftedfables.com/'
    baseUrl = 'http://www.caf-fiends.net/'
    rurl = escape(baseUrl)
    stripUrl = baseUrl + 'craftedfables/?p=%s'
    imageSearch = compile(tagre("img", "src", r'(%scraftedfables/comics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scraftedfables/[^"]+)' % rurl) +
        tagre("span", "class", r"prev"))
    help = 'Index format: nnn'


class CucumberQuest(_BasicScraper):
    description = u'Cucumber Quest'
    url = 'http://cucumber.gigidigi.com/'
    rurl = escape(url)
    stripUrl = url + 'cq/%s/'
    firstStripUrl = stripUrl % 'page-1'
    starter = indirectStarter(url + 'recent.html',
        compile(r'window\.location="(/cq/[^"]+/)"'))
    imageSearch = (
        compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/ch\d+[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/bonus[^"]+)' % rurl)),
    )
    prevSearch = compile(tagre("a", "href", r'(%scq/[^"]+/)' % rurl, after="previous"))
    help = 'Index format: stripname'


class Curtailed(_BasicScraper):
    description = u''
    url = 'http://curtailedcomic.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2012/04/08/sneeze'
    rurl = escape(url)
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/[0-9]+/[^"]*)' % rurl))
    prevSearch = compile('<a href="([^"]*)" class="comic-nav-base comic-nav-previous"')
    help = 'Index format: yyyy/mm/dd/stripname'


class Curvy(_BasicScraper):
    description = u'An erotic sci-fi adventure comic for adults.'
    url = 'http://www.c.urvy.org/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20080329'
    imageSearch = compile(tagre("img", "src", r'(/c/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/\?date=\d+)') +
        tagre("img", "src", "/nav/prev\.png"))
    help = 'Index format: yyyymmdd'
    starter = bounceStarter(url,
        compile(tagre("a", "href", r'(/\?date=\d+)') +
            tagre("img", "src", "/nav/next\.png")))

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return url in (
            self.stripUrl % '20130402',
        )


class CyanideAndHappiness(_BasicScraper):
    url = 'http://www.explosm.net/comics/'
    starter = bounceStarter(url, compile(tagre("a", "href", r"(/comics/\d+/)", after="next-comic")))
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '15'
    imageSearch = compile(tagre("img", "src", r'(//files.explosm.net/comics/[^"]+)', before="main-comic"))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+/)', after="previous-comic"))
    help = 'Index format: n (unpadded)'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return "/comics/play-button.png" in data

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imgname = imageUrl.split('/')[-1]
        # only get the first 100 chars for the image name
        imgname = imgname[:100]
        imgnum = pageUrl.split('/')[-2]
        return '%s_%s' % (imgnum, imgname)

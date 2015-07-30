# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
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

class CaptainSNES(_BasicScraper):
    url = 'http://www.captainsnes.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2001/07/10/the-mistake'
    imageSearch = compile(tagre("img", "src", r"(%scomics/[^']+)" % rurl, quote="'"))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl) + tagre("span", "class", "prev"))
    multipleImagesPerStrip = True
    help = 'Index format: yyyy/mm/dd/nnn-stripname'


class Carciphona(_BasicScraper):
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
    url = 'http://www.galactanet.com/comic/'
    stripUrl = url + 'view.php?strip=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(Strip\d+\.gif)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?strip=\d+)')
     + tagre("img", "src", r'previous\.gif'))
    help = 'Index format: number'


class CasuallyKayla(_BasicScraper):
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

class CatVersusHuman(_ParserScraper):
    url = 'http://www.catversushuman.com'
    multipleImagesPerStrip = True
    imageSearch = '//div[@class="post-body entry-content"]//img'
    prevSearch = '//a[@class="blog-pager-older-link"]'


class ChainsawSuit(_ParserScraper):
    url = 'http://chainsawsuit.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/03/12/strip-338'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//img[@alt="previous"]/..'
    help = 'Index format: yyyy/mm/dd/stripname'


class Champ2010(_BasicScraper):
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
    url = 'http://www.channelate.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class ChasingTheSunset(_BasicScraper):
    url = 'http://www.fantasycomic.com/'
    stripUrl = url + 'index.php?p=c%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'(/cmsimg/.+?)".+?comic-img')
    prevSearch = compile(r'<a href="(.+?)" title="" ><img src="(images/eye-prev.png|images/cn-prev.png)"')
    help = 'Index format: n'


class CheckerboardNightmare(_ParserScraper):
    url = 'http://www.checkerboardnightmare.com/'
    stripUrl = url + 'd/%s'
    firstStripUrl = stripUrl % '20001110.html'
    imageSearch = '//td[@colspan="4"]//img'
    prevSearch = '//td[2]/a'
    help = 'Index format: yyyymmdd'


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


class CigarroAndCerveja(_ParserScraper):
    url = 'http://www.cigarro.ca/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'reacquaintance'
    imageSearch = '//div[@id="comic"]//img',
    prevSearch = '//a[contains(text()," Prev")]',

class Collar6(_BasicScraper):
    url = 'http://collar6.com/'
    rurl = escape(url)
    stripUrl = url + 'archive/%s'
    firstStripUrl = stripUrl % 'collar-6-187'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/webcomic/collar6/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchive/[^"]+)' % rurl, after="previous"))
    help = 'Index format: <name>'


class Comedity(_BasicScraper):
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


class CorydonCafe(_ParserScraper):
    url = 'http://corydoncafe.com/'
    starter = indirectStarter(url, '//ul//a')
    stripUrl = url + '%s.php'
    imageSearch = "//center[2]//img"
    prevSearch = '//a[@title="prev"]'
    help = 'Index format: yyyy/stripname'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.split('/')[-1].split('.')[0]


class CrapIDrewOnMyLunchBreak(_BasicScraper):
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
    url = 'http://www.davidcsimon.com/crimsondark/'
    stripUrl = url + 'index.php?view=comic&strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'src="(.+?strips/.+?)"')
    prevSearch = compile(r'<a href=[\'"](/crimsondark/index\.php\?view=comic&amp;strip_id=\d+)[\'"]><img src=[\'"]themes/cdtheme/images/active_prev.png[\'"]')
    help = 'Index format: n (unpadded)'


class CucumberQuest(_BasicScraper):
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
    url = 'http://curtailedcomic.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2012/04/08/sneeze'
    rurl = escape(url)
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/[0-9]+/[^"]*)' % rurl))
    prevSearch = compile('<a href="([^"]*)" class="comic-nav-base comic-nav-previous"')
    help = 'Index format: yyyy/mm/dd/stripname'


class Curvy(_ParserScraper):
    url = 'http://www.c.urvy.org/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20080329'
    imageSearch = '//div[@id="theActualComic"]//img'
    prevSearch = '//div[@class="aNavbar"]//p[2]/a'
    help = 'Index format: yyyymmdd'


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
        return "/comics/play-button.png" in data[0]

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imgname = imageUrl.split('/')[-1]
        # only get the first 100 chars for the image name
        imgname = imgname[:100]
        imgnum = pageUrl.split('/')[-2]
        return '%s_%s' % (imgnum, imgname)

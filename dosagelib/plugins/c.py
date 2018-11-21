# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2018 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from ..util import tagre
from .common import _TumblrScraper, _WordPressScraper, _WPNavi


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
    imageSearch = compile(tagre("img", "src", r"(%scomics/[^']+)" % rurl,
                                quote="'"))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl) +
                         tagre("span", "class", "prev"))
    multipleImagesPerStrip = True
    help = 'Index format: yyyy/mm/dd/nnn-stripname'


class Carciphona(_BasicScraper):
    url = 'http://carciphona.com/'
    multipleImagesPerStrip = True
    imageSearch = compile(tagre("div", "style", r'background-image:url\((_pages[^)]*)\)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?[^"]*)', after="prevarea"))
    latestSearch = compile(tagre("a", "href", r'(read\.php\#chapter=[^"]*&page=[0-9]*[^"]*)'))
    starter = indirectStarter

    def namer(self, image_url, page_url):
        ip = image_url.split('/')
        return "volume_%s_page_%s" % (ip[-2], ip[-1])


class CaseyAndAndy(_BasicScraper):
    url = 'http://www.galactanet.com/comic/'
    stripUrl = url + 'view.php?strip=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(Strip\d+\.gif)'))
    prevSearch = compile(tagre("a", "href", r'(view\.php\?strip=\d+)') +
                         tagre("img", "src", r'previous\.gif'))
    help = 'Index format: number'


class CasuallyKayla(_BasicScraper):
    url = 'http://casuallykayla.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '89'
    imageSearch = compile(tagre("img", "src",
                                r'(http://casuallykayla\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("div", "class", r'nav-previous') +
                         tagre("a", "href", r'([^"]+)'))
    help = 'Index format: nnn'


class Catalyst(_BasicScraper):
    baseUrl = "http://catalyst.spiderforest.com/"
    rurl = escape(baseUrl)
    url = baseUrl + "comic.php?comic_id=415"
    stripUrl = baseUrl + "comic.php?comic_id=%s"
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'((?:%s)?comics/[^"]+)' % rurl))
    prevSearch = compile("<center>" +
                         tagre("a", "href",
                               r'(%scomic\.php\?comic_id=\d+)' % rurl))
    help = 'Index format: number'


class CatAndGirl(_ParserScraper):
    url = 'http://catandgirl.com/'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@rel="prev"]'


class Catena(_WordPressScraper):
    url = 'http://catenamanor.com/'


class CatsAndCameras(_WordPressScraper):
    url = 'http://catsncameras.com/'


class CatVersusHuman(_ParserScraper):
    url = 'http://www.catversushuman.com'
    imageSearch = '//div[@class="post-body entry-content"]//img'
    prevSearch = '//a[@id="Blog1_blog-pager-older-link"]'
    latestSearch = '//a[@rel="bookmark"]'
    starter = indirectStarter


class ChainsawSuit(_WordPressScraper):
    url = 'http://chainsawsuit.com/comic/'
    stripUrl = url + 'archive/%s/'
    firstStripUrl = stripUrl % '2008/03/12/strip-338'
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
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl,
                               after="Previous"))
    help = 'Index format: yy-dd-mm'


class ChannelAte(_WPNavi):
    url = 'http://www.channelate.com/'


class ChasingTheSunset(_BasicScraper):
    url = 'http://www.fantasycomic.com/'
    stripUrl = url + 'index.php?p=c%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'(/cmsimg/.+?)".+?comic-img')
    prevSearch = compile(r'<a href="(.+?)" title="" ><img src="(images/eye-prev.png|images/cn-prev.png)"')
    help = 'Index format: n'


class Chester5000XYV(_WordPressScraper):
    url = 'http://jessfink.com/Chester5000XYV/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '34'
    prevSearch = '//a[@rel="prev"]'
    adult = True
    help = 'Index format: n (unpadded)'

    def link_modifier(self, fromurl, tourl):
        """Bugfix for link to blog"""
        if tourl == self.stripUrl % '714':
            return self.stripUrl % '710'
        return tourl


class Chisuji(_WordPressScraper):
    url = 'http://www.chisuji.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '266'
    prevSearch = '//div[@class="nav-previous"]/a'
    help = 'Index format: nnn'


class CigarroAndCerveja(_ParserScraper):
    url = 'http://www.cigarro.ca/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'reacquaintance'
    imageSearch = '//div[@id="comic"]//img',
    prevSearch = '//a[contains(text()," Prev")]',


class Collar6(_TumblrScraper):
    url = 'http://collar6.tumblr.com/'
    firstStripUrl = url + 'post/138117470810/the-very-first-strip-from-when-i-thought-it-was'
    imageSearch = '//figure[@class="photo-hires-item"]//img'
    prevSearch = '//a[@class="previous-button"]'
    latestSearch = '//li[@class="timestamp"]/a'
    adult = True


class Comedity(_BasicScraper):
    url = 'http://www.comedity.com/'
    stripUrl = url + 'index.php?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<img src="(Comedity_files/.+?)"')
    prevSearch = compile(r'<a href="(/?index.php\?strip_id=\d+?)"> *<img alt=\"Prior Strip')
    help = 'Index format: n (no padding)'


class CommitStrip(_ParserScraper):
    baseUrl = 'https://www.commitstrip.com/en/'
    url = baseUrl + '?setLocale=1'  # ensure the language cookie is set
    stripUrl = baseUrl + '%s/'
    firstStripUrl = 'http://www.commitstrip.com/en/2012/02/22/interview/'  # non-TLS!

    latestSearch = '//section//a'
    starter = indirectStarter
    imageSearch = '//article/div//img'
    prevSearch = '//span[@class="nav-previous"]/a'
    help = 'Index format: yyyy/mm/dd/strip-name'

    def namer(self, image_url, page_url):
        parts = page_url.rstrip('/').rsplit('/')[-4:]
        return '-'.join(parts)


class CommitStripFr(CommitStrip):
    baseUrl = 'https://www.commitstrip.com/fr/'
    url = baseUrl + '?setLocale=1'  # ensure the language cookie is set
    stripUrl = baseUrl + '%s/'
    firstStripUrl = 'http://www.commitstrip.com/fr/2012/02/22/interview/'  # non-TLS!
    lang = 'fr'


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


class CorydonCafe(_ParserScraper):
    url = 'http://corydoncafe.com/'
    imageSearch = "//center[2]//img"
    prevSearch = '//a[@title="prev"]'
    multipleImagesPerStrip = True


class CourtingDisaster(_WordPressScraper):
    url = 'http://www.courting-disaster.com/'
    firstStripUrl = 'http://www.courting-disaster.com/comic/courting-disaster-17/'


class CraftedFables(_WordPressScraper):
    url = 'http://www.caf-fiends.net/comicpress/'
    prevSearch = '//a[@rel="prev"]'


class CrapIDrewOnMyLunchBreak(_BasicScraper):
    url = 'http://crap.jinwicked.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/07/30/jin-and-josh-decide-to-move'
    imageSearch = compile(tagre("img", "src", r'(http://crap\.jinwicked\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


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
    startUrl = url + 'recent.html'
    starter = indirectStarter
    imageSearch = (
        compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/ch\d+[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/bonus[^"]+)' % rurl)),
    )
    prevSearch = compile(tagre("a", "href", r'(%scq/[^"]+/)' % rurl, after="previous"))
    latestSearch = compile(r'window\.location="(/cq/[^"]+/)"')
    help = 'Index format: stripname'


class Curtailed(_WordPressScraper):
    url = 'http://curtailedcomic.com/'
    firstStripUrl = url + 'comic/001-sneeze/'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return 'comic/sitrep-1' in url


class Curvy(_ParserScraper):
    url = 'http://www.c.urvy.org/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20080329'
    imageSearch = '//div[@id="theActualComic"]//img'
    prevSearch = '//div[@class="aNavbar"]//p[2]/a'
    help = 'Index format: yyyymmdd'


class CtrlAltDel(_BasicScraper):
    url = 'http://cad-comic.com/'
    stripUrl = url + '%s'
    startUrl='http://cad-comic.com/'
    latestSearch = compile('"url": *"([^"]*)')
    imageSearch = compile(tagre("img", "src", r'(https://cad-comic\.com/wp-content/uploads/[^"]+png)'))
    prevSearch = compile(tagre("a", "href", r'(https:[^"]+)', after="prev"))
    help = 'Index format: yyyymmdd'
   
    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Remove random junk from image names."""
        imgname = imageUrl.split('/')[-1]
        imgbase = imgname.rsplit('_', 1)[1]
        parts = imgbase.split('.')
        return 'cad-%s.%s' % (parts[0], parts[-1])


class CyanideAndHappiness(_BasicScraper):
    url = 'http://www.explosm.net/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '15'
    imageSearch = compile(tagre("img", "src", r'(//files.explosm.net/comics/[^"]+)', before="main-comic"))
    prevSearch = compile(tagre("a", "href", r'(/comics/\d+/)', after="nav-previous"))
    nextSearch = compile(tagre("a", "href", r"(/comics/\d+/)", after="nav-next"))
    help = 'Index format: n (unpadded)'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return "/comics/play-button.png" in data[0]

    def namer(self, image_url, page_url):
        imgname = image_url.split('/')[-1]
        # only get the first 100 chars for the image name
        imgname = imgname[:100]
        imgnum = page_url.split('/')[-2]
        return '%s_%s' % (imgnum, imgname)

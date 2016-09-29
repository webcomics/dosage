# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape, IGNORECASE

from ..helpers import indirectStarter
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from .common import _WordPressScraper, WP_LATEST_SEARCH, xpath_class


class EarthsongSaga(_ParserScraper):
    url = 'http://earthsongsaga.com/index.php'
    starter = indirectStarter
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@title="Previous"]'
    latestSearch = '//div[@id="leftmenu"]/span[1]/a[1]'

    def fetchUrls(self, url, data, urlSearch):
        urls = super(EarthsongSaga, self).fetchUrls(url, data, urlSearch)
        return [x.replace('earthsongsaga.com/../',
                          'earthsongsaga.com/') for x in urls]

    def namer(self, image_url, page_url):
        imgmatch = compile(r'images/vol(\d+)/ch(\d+)/(\d+)\.\w+$',
                           IGNORECASE).search(image_url)
        if not imgmatch:
            imgmatch = compile(r'images/vol(\d+)/ch(\d+)/ch(\d+)cover\.\w+$',
                               IGNORECASE).search(image_url)
            suffix = "cover"
        else:
            suffix = ""
        return 'vol%02d_ch%02d_%02d%s' % (
          int(imgmatch.group(1)), int(imgmatch.group(2)),
          int(imgmatch.group(3)), suffix)


class EasilyAmused(_WordPressScraper):
    url = 'http://www.flowerlarkstudios.com/comic/college-daze/ea01/'
    firstStripUrl = url
    latestSearch = WP_LATEST_SEARCH
    starter = indirectStarter


class EatLiver(_ParserScraper):
    url = 'http://www.eatliver.com/'
    starter = indirectStarter
    multipleImagesPerStrip = True
    imageSearch = '//div[%s]//img' % xpath_class('post-content')
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@rel="bookmark"]'


class EatThatToast(_BasicScraper):
    url = 'http://eatthattoast.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'thewizard/'
    imageSearch = compile(tagre("div", "id", r'comic') + "\s*.*\s*" + tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl,
                               after='comic-nav-base comic-nav-previous'))
    textSearch = compile(tagre("div", "id", r'comic') + "\s*.*\s*" +
                         tagre("img", "alt", r'([^"]+)'))
    help = 'Index Format: name'


class EdibleDirt(_BasicScraper):
    url = 'http://eddirt.frozenreality.co.uk/'
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r"(index\.php\?id=\d+)") +
                         "Previous")
    help = 'Index format: number'


class EdmundFinney(_WordPressScraper):
    url = 'http://eqcomics.com/'
    firstStripUrl = url + '2009/03/08/sunday-aliens/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')


class EerieCuties(_BasicScraper):
    url = 'http://www.eeriecuties.com/'
    stripUrl = url + 'strips-ec/%s'
    imageSearch = compile(tagre("img", "src", r'(http://ace\.eeriecuties\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', before="prev"))
    help = 'Index format: stripname'


class ElfOnlyInn(_BasicScraper):
    url = 'http://www.elfonlyinn.net/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20020523'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/\d+\.html)') +
                         tagre("img", "src", r'/images/previous_day\.gif'))
    help = 'Index format: yyyymmdd'


class ElGoonishShive(_BasicScraper):
    name = 'KeenSpot/ElGoonishShive'
    url = 'http://www.egscomics.com/'
    stripUrl = url + 'index.php?id=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)',
                                after="comic"))
    prevSearch = compile(tagre("a", "href", r'(/index\.php\?id=\d+)',
                               after="prev"))
    help = 'Index format: number'


class ElGoonishShiveNP(_BasicScraper):
    name = 'KeenSpot/ElGoonishShiveNP'
    url = 'http://www.egscomics.com/egsnp.php'
    stripUrl = url + '?id=%s'
    imageSearch = compile(tagre("img", "src", r'(comics/[^"]+)',
                                after="comic"))
    prevSearch = compile(tagre("a", "href", r'(/egsnp\.php\?id=\d+)',
                               after="prev"))
    help = 'Index format: number'


class EmergencyExit(_BasicScraper):
    url = 'http://www.eecomics.net/'
    stripUrl = url + "?strip_id=%s"
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(\?strip_id=\d+)') + tagre("img", "alt", r"Prior"))
    help = 'Index format: n'


class ErrantStory(_BasicScraper):
    url = 'http://www.errantstory.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'<img[^>]+?src="([^"]*?comics/.+?)"')
    prevSearch = compile(r'><a href="(.+?)">&lt;Previous</a>')
    help = 'Index format: yyyy-mm-dd/num'


class Erstwhile(_WordPressScraper):
    url = 'http://www.erstwhiletales.com/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')
    endOfLife = True


class Eryl(_WordPressScraper):
    url = 'http://www.flowerlarkstudios.com/comic/prologue-migration/page-i/'
    firstStripUrl = url
    latestSearch = WP_LATEST_SEARCH
    starter = indirectStarter


class EverybodyLovesEricRaymond(_BasicScraper):
    url = 'http://geekz.co.uk/lovesraymond/'
    stripUrl = url + 'archive/%s'
    firstStripUrl = stripUrl % 'slashdotted'
    imageSearch = compile(r'<img src="((?:http://geekz.co.uk)?/lovesraymond/wp-content(?:/images)/ep\d+\w?\.jpg)"', IGNORECASE)
    prevSearch = compile(r'&laquo; <a href="(http://geekz.co.uk/lovesraymond/archive/[^/"]*)">')
    help = 'Index format: name-of-old-comic'


# Seems to be GeoBlocked from Europe?
class EvilDiva(_BasicScraper):
    url = 'http://www.evildivacomics.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '145'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(r'http.+?com/(.+?)".+?"prev')
    help = 'Index format: n (unpadded)'


class EvilInc(_WordPressScraper):
    url = 'http://evil-inc.com/'
    firstStripUrl = url + 'comic/monday-3/'


class Evilish(_ParserScraper):
    url = 'http://evilish.pensandtales.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20020630'
    imageSearch = '//img[@alt="Today\'s Comics"]'
    prevSearch = '//a[img[@alt="Previous Comic"]]'
    endOfLife = True
    help = 'Index format: yyyymmdd'


class Exiern(_BasicScraper):
    url = 'http://www.exiern.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2005/09/06/so-far'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ExploitationNow(_WordPressScraper):
    url = 'http://www.exploitationnow.com/'
    firstStripUrl = url + '2000-07-07/9'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')
    endOfLife = True


class ExtraLife(_BasicScraper):
    url = 'http://www.myextralife.com/'
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(http://www\.myextralife\.com/wp-content/uploads/[^"]+)', before="comic"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', before="prev_comic"))
    help = 'Index format: stripname'


class ExtraOrdinary(_BasicScraper):
    url = 'http://www.exocomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '01'
    prevSearch = compile(tagre("a", "href", r'(%s\d+)' % rurl, before="prev"))
    imageSearch = compile(tagre("img", "src", r'(%scomics/comics/\d+\.[^"]+)' % rurl))
    help = 'Index format: number'


class EyeOfRamalach(_BasicScraper):
    url = 'http://theeye.katbox.net/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/[^"]+)' % rurl, after="data-webcomic-parent"))
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import bounceStarter, indirectStarter, xpath_class
from ..util import tagre
from .common import (_ComicControlScraper, _WordPressScraper, _WPNaviIn,
                     WP_LATEST_SEARCH)


class Lackadaisy(_BasicScraper):
    baseUrl = 'http://lackadaisy.foxprints.com/'
    url = baseUrl + 'comic.php'
    stripUrl = baseUrl + 'comic.php?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://www\.lackadaisy\.com/comic/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r"(/comic\.php\?comicid=[0-9]+)") +
                         "Previous")
    nextSearch = compile(tagre("a", "href", r"(/comic.php\?comicid=[0-9]+)") +
                         "Next")
    help = 'Index format: n'
    starter = bounceStarter

    def namer(self, image_url, page_url):
        """Use comic id for filename."""
        num = page_url.rsplit('=', 1)[-1]
        ext = image_url.rsplit('.', 1)[-1]
        return 'lackadaisy_%s.%s' % (num, ext)


class Laiyu(_WordPressScraper):
    url = 'http://www.flowerlarkstudios.com/comicpage/preliminary-concepts/welcome/'
    firstStripUrl = url
    latestSearch = WP_LATEST_SEARCH
    starter = indirectStarter


class LasLindas(_BasicScraper):
    url = 'http://laslindas.katbox.net/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/[^"]+)' % rurl, after="attachment-full"))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'


class LeastICouldDo(_ParserScraper):
    url = 'http://www.leasticoulddo.com/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '20030210'
    imageSearch = '//div[@id="content-comic"]//img'
    prevSearch = '//a[@rel="prev"]'
    latestSearch = '//a[@id="latest-comic"]'
    starter = indirectStarter
    help = 'Index format: yyyymmdd'


class LetsSpeakEnglish(_ComicControlScraper):
    url = 'http://www.marycagle.com'


class LifeAintNoPonyFarm(_WordPressScraper):
    url = 'http://sarahburrini.com/en/'
    firstStripUrl = url + 'comic/my-first-webcomic/'
    multipleImagesPerStrip = True


class LittleGamers(_BasicScraper):
    url = 'http://www.little-gamers.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2000/12/01/99'
    imageSearch = compile(tagre("img", "src", r'(http://little-gamers\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.little-gamers\.com/[^"]+)', before="comic-nav-prev-link"))
    help = 'Index format: yyyy/mm/dd/name'


class LoadingArtist(_ParserScraper):
    url = 'http://www.loadingartist.com/latest'
    imageSearch = '//div[@class="comic"]//img'
    prevSearch = "//a[contains(concat(' ', @class, ' '), ' prev ')]"


class LoFiJinks(_WPNaviIn):
    url = 'http://hijinksensue.com/comic/learning-to-love-again/'
    firstStripUrl = 'http://hijinksensue.com/comic/lo-fijinks-everything-i-know-anout-james-camerons-avatar-movie/'
    endOfLife = True


class LookingForGroup(_ParserScraper):
    url = 'http://www.lfg.co/latest-comic/'
    stripUrl = 'http://www.lfg.co/page/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = '//div[@id="comic-img"]//img'
    prevSearch = '//a[%s]' % xpath_class('comic-nav-prev')
    help = 'Index format: nnn'

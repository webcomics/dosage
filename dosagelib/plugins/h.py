# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..scraper import _BasicScraper
from ..util import tagre
from ..helpers import bounceStarter, indirectStarter
from .common import _WordPressScraper, _WPNaviIn


class HagarTheHorrible(_BasicScraper):
    url = 'http://www.hagarthehorrible.net/'
    stripUrl = 'http://www.hagardunor.net/comicstrips_us.php?serietype=9&colortype=1&serieno=%s'
    firstStripUrl = stripUrl % '1'
    multipleImagesPerStrip = True
    imageSearch = compile(tagre("img", "src", r'(stripus\d+/(?:Hagar_The_Horrible_?|h)\d+[^ >]+)', quote=""))
    prevUrl = r'(comicstrips_us\.php\?serietype\=9\&colortype\=1\&serieno\=\d+)'
    prevSearch = compile(tagre("a", "href", prevUrl, after="Previous"))
    help = 'Index format: number'

    def starter(self):
        """Return last gallery link."""
        url = 'http://www.hagardunor.net/comics.php'
        data = self.getPage(url)
        pattern = compile(tagre("a", "href", self.prevUrl))
        for starturl in self.fetchUrls(url, data, pattern):
            pass
        return starturl


# "Hiatus", navigation missing
class _HappyJar(_WordPressScraper):
    url = 'http://www.happyjar.com/'


class HarkAVagrant(_BasicScraper):
    url = 'http://www.harkavagrant.com/'
    rurl = escape(url)
    starter = bounceStarter
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%s[^"]+)' % rurl,
                                after='BORDER'))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php\?id=\d+)' % rurl) +
                         tagre("img", "src", "buttonprevious.png"))
    nextSearch = compile(tagre("a", "href", r'(%sindex\.php\?id=\d+)' % rurl) +
                         tagre("img", "src", "buttonnext.png"))
    help = 'Index format: number'

    def namer(self, image_url, page_url):
        filename = image_url.rsplit('/', 1)[1]
        num = page_url.rsplit('=', 1)[1]
        return '%s-%s' % (num, filename)


class Hipsters(_WordPressScraper):
    url = 'http://www.hipsters-comic.com/'
    firstStripUrl = 'http://www.hipsters-comic.com/comic/hip01/'


class HijinksEnsue(_WPNaviIn):
    url = 'http://hijinksensue.com/'
    latestSearch = '//a[text()="Latest HijiNKS ENSUE"]'
    firstStripUrl = 'http://hijinksensue.com/comic/who-is-your-daddy-and-what-does-he-do/'
    starter = indirectStarter


class HijinksEnsueClassic(_WPNaviIn):
    url = 'http://hijinksensue.com/comic/open-your-eyes/'
    firstStripUrl = 'http://hijinksensue.com/comic/a-soul-as-black-as-eyeliner/'
    endOfLife = True


class HijinksEnsueConvention(_WPNaviIn):
    url = 'http://hijinksensue.com/comic/emerald-city-comicon-2015-fancy-sketches-part-4/'
    firstStripUrl = 'http://hijinksensue.com/comic/whatever-dad-im-outta-here/'
    endOfLife = True


class HijinksEnsuePhoto(_WPNaviIn):
    url = 'http://hijinksensue.com/comic/emerald-city-comicon-2015-fancy-photo-comic-part-2/'
    firstStripUrl = 'http://hijinksensue.com/comic/san-diego-comic-con-fancy-picto-comic-pt-1/'
    endOfLife = True

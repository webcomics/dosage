# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from re import compile, escape

from ..util import tagre
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from .common import (_ComicControlScraper, _WordPressScraper, WP_PREV_SEARCH,
                     xpath_class)


class BadassMuthas(_BasicScraper):
    url = 'http://badassmuthas.com/pages/comic.php'
    stripUrl = url + '?%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/images/comicsissue[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') +
                         tagre("img", "src", r'/images/comicsbuttonBack\.gif'))
    help = 'Index format: nnn'


class BadMachinery(_BasicScraper):
    url = 'http://scarygoround.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '20090918'
    imageSearch = compile(tagre("img", "src", r'(strips/\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(\?date=\d+)') + 'Previous')
    help = 'Index format: yyyymmdd'


class BalderDash(_ComicControlScraper):
    url = 'http://www.balderdashcomic.com/'


class Bardsworth(_WordPressScraper):
    url = 'http://www.bardsworth.com/'
    latestSearch = '//a[@rel="bookmark"]'
    starter = indirectStarter


class Baroquen(_BasicScraper):
    url = 'http://www.baroquencomics.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2008/11/05/raise-the-curtains'
    imageSearch = compile(tagre("img", "src", r'(%sComics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after='prev'))
    help = 'Index format: yyyy/mm/dd/strip-name'


class Bearmageddon(_WordPressScraper):
    url = 'http://bearmageddon.com/'
    firstStripUrl = url + '2011/08/01/page-1/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev')


class Beetlebum(_BasicScraper):
    url = 'http://blog.beetlebum.de/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2006/03/10/quiz-fur-ruskiphile'
    starter = indirectStarter
    multipleImagesPerStrip = True
    imageSearch = compile(tagre('img', 'src', r'(http://blog\.beetlebum\.de/wp-content/uploads/[^"]+)'))
    prevSearch = compile(tagre('a', 'href',
                               r'(%s\d{4}/\d{2}/\d{2}/[^"]*)' % rurl,
                               after='prev'))
    latestSearch = compile(tagre('a', 'href',
                                 r'(%s\d{4}/\d{2}/\d{2}/[^"]+)' % rurl,
                                 after='bookmark'))
    help = 'Index format: yyyy/mm/dd/striptitle'
    lang = 'de'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        indexes = tuple(pageUrl.rstrip('/').split('/')[-4:])
        name = '%s-%s-%s-%s' % indexes
        name = name + '_' + imageUrl.split('/')[-1]
        return name


class BetterDays(_BasicScraper):
    url = 'http://jaynaylor.com/betterdays/'
    stripUrl = url + 'archives/%s.html'
    firstStripUrl = stripUrl % '2003/04/post-2'
    imageSearch = compile(tagre("img", "src", r'(/betterdays/comic/[^>]+)', quote=""))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + '&laquo; Previous')
    help = 'Index format: yyyy/mm/<your guess>'


class BetweenFailures(_BasicScraper):
    url = 'http://betweenfailures.com/'
    rurl = escape(url)
    stripUrl = url + 'comics1/%s'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomics1/[^"]+)' % rurl,
                               after="previous"))
    help = 'Index format: stripname'


class BiggerThanCheeses(_BasicScraper):
    url = 'http://www.biggercheese.com/'
    stripUrl = url + 'index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'src="(comics/.+?)" alt')
    prevSearch = compile(r'"(index.php\?comic=.+?)".+?_back')
    help = 'Index format: n (unpadded)'


class BillyTheDunce(_BasicScraper):
    url = 'http://www.duncepress.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/06/an-introduction-of-sorts'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(r'<div class="nav-previous"><a href="(%s[^"]+)" rel="prev">' % rurl)
    help = 'Index format: yyyy/mm/stripname'


class BizarreUprising(_BasicScraper):
    url = 'http://www.bizarreuprising.com/'
    stripUrl = url + 'view/%s'
    firstStripUrl = stripUrl % '1/awakening-splash'
    imageSearch = compile(tagre("img", "src", r'(comic/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(view/\d+/[^"]+)') +
                         tagre("img", "src", r'images/b_prev\.gif'))
    help = 'Index format: n/name'


class BlankIt(_BasicScraper):
    url = 'http://blankitcomics.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '0001'
    imageSearch = compile(tagre("img", "src",
                                r'(http://blankitcomics\.com/bicomics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after='rel="prev"'))
    help = 'Index format: stripname'


class BloodBound(_WordPressScraper):
    url = 'http://bloodboundcomic.com/'
    firstStripUrl = 'http://bloodboundcomic.com/comic/06112006/'


class BloomingFaeries(_ParserScraper):
    adult = True
    url = 'http://www.bloomingfaeries.com/'
    firstStripUrl = url + 'comic/public/pit-stop/'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = WP_PREV_SEARCH

    @classmethod
    def namer(cls, image_url, page_url):
        return "_".join(image_url.rsplit('/', 3)[1:])


class BMovieComic(_BasicScraper):
    url = 'http://www.bmoviecomic.com/'
    stripUrl = url + '?cid=%s'
    firstStripUrl = stripUrl % '8'
    imageSearch = compile(r'"(comics/.+?)"')
    prevSearch = compile(r'(\?cid=.+?)".+?Prev')
    help = 'Index format: n'


class BookOfBiff(_BasicScraper):
    url = 'http://thebookofbiff.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/01/02/4'
    imageSearch = compile(tagre("img", "src", r'([^"]+/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: yyyy/mm/dd/stripnum-stripname'


class BoredAndEvil(_BasicScraper):
    url = 'http://www.boredandevil.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2004-06-07'
    imageSearch = compile(tagre("img", "src", r'(strips/[^"]+)'))
    prevSearch = compile(r'First Comic.+<a href="(.+?)".+previous-on.gif')
    latestSearch = prevSearch
    starter = indirectStarter
    help = 'Index format: yyyy-mm-dd'


class BoyOnAStickAndSlither(_BasicScraper):
    url = 'http://www.boasas.com/'
    stripUrl = url + 'page/%s'
    firstStripUrl = stripUrl % '2'
    imageSearch = compile(tagre("img", "src", r'(http://\d+\.media\.tumblr\.com/[^"]+_1280\.png)'))
    prevSearch = compile(tagre("a", "href", r'(/page/\d+)') +
                         "<span>Next page")
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return pageUrl.rsplit('/')[-1]


class BratHalla(_WordPressScraper):
    url = 'http://brat-halla.com/'


class Brink(_BasicScraper):
    url = 'http://paperfangs.com/brink/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '5'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: number'


class BroodHollow(_WordPressScraper):
    url = 'http://broodhollow.chainsawsuit.com/'
    firstStripUrl = 'http://broodhollow.chainsawsuit.com/page/2012/10/06/book-1-curious-little-thing'


class Buni(_WordPressScraper):
    url = 'http://www.bunicomic.com/'


class BusinessCat(_WordPressScraper):
    url = 'http://www.businesscat.happyjar.com/'
    prevSearch = '//a[%s]' % xpath_class('navi-prev-in')


class ButtercupFestival(_ParserScraper):
    url = 'http://www.buttercupfestival.com/'
    stripUrl = url + '%s.htm'
    firstStripUrl = stripUrl % '2-1'
    imageSearch = '//center/img'
    prevSearch = '//a[text()="previous"]'
    help = 'Index format: 2-number'


class ButternutSquash(_BasicScraper):
    url = 'http://www.butternutsquash.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2003/04/16/meet-da-punks'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/strip-name-author-name'


class ButterSafe(_BasicScraper):
    url = 'http://buttersafe.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/04/03/breakfast-sad-turtle'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+\d+/\d+/\d+/[^"]+)' % rurl,
                               after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'

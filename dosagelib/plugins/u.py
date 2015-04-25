# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape

from ..scraper import _BasicScraper
from ..helpers import bounceStarter, indirectStarter
from ..util import getQueryParams, tagre

class Underling(_BasicScraper):
    url = 'http://underlingcomic.com/'
    stripUrl = url
    rurl = escape(url)
    firstStripUrl = stripUrl + 'page-one/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]*)' % rurl))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after = r'class="[^"]*navi-prev'))
    help = 'Index format: nnn'


class Undertow(_BasicScraper):
    url = 'http://undertow.dreamshards.org/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'([^"]+\.jpg)'))
    prevSearch = compile(r'href="(.+?)".+?teynpoint')
    help = 'Index format: good luck !'
    starter = indirectStarter(url,
                              compile(r'href="(.+?)".+?Most recent page'))


class UnicornJelly(_BasicScraper):
    baseUrl = 'http://unicornjelly.com/'
    url = baseUrl + 'uni666.html'
    stripUrl = baseUrl + 'uni%s.html'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(r'</TABLE>(?:<FONT COLOR="BLACK">)?<IMG SRC="(images/[^"]+)" WIDTH=')
    prevSearch = compile(r'<A HREF="(uni\d{3}[bcs]?\.html)">(<FONT COLOR="BLACK">)?<IMG SRC="images/back00\.gif"')
    help = 'Index format: nnn'


class Unsounded(_BasicScraper):
    url = 'http://www.casualvillain.com/Unsounded/'
    stripUrl = url + 'comic/ch%s/ch%s_%s.html'
    firstStripUrl = stripUrl % ('01', '01', '01')
    rurl = escape(url)
    imageSearch = compile(tagre("img", "src", r'(pageart/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*)', after='class="back'))
    starter = indirectStarter(url,
       compile(tagre("a", "href", r'(%scomic/[^"]*)' % rurl) +
           tagre("img", "src", r"%simages/newpages\.png" % rurl)))
    help = 'Index format: chapter-number'

    def getIndexStripUrl(self, index):
        """Get comic strip URL from index."""
        chapter, num = index.split('-')
        return self.stripUrl % (chapter, chapter, num)


# XXX disallowed by robots.txt
class _UserFriendly(_BasicScraper):
    url = 'http://ars.userfriendly.org/cartoons/?mode=classic'
    stripUrl = url + '&id=%s'
    starter = bounceStarter(url, compile(r'<area shape="rect" href="(/cartoons/\?id=\d{8}&mode=classic)" coords="[\d, ]+?" alt="">'))
    imageSearch = compile(r'<img border="0" src="\s*(http://www.userfriendly.org/cartoons/archives/\d{2}\w{3}/.+?\.gif)"')
    prevSearch = compile(r'<area shape="rect" href="(/cartoons/\?id=\d{8}&mode=classic)" coords="[\d, ]+?" alt="Previous Cartoon">')
    help = 'Index format: yyyymmdd'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return 'uf%s' % (getQueryParams(pageUrl)['id'][0][2:],)

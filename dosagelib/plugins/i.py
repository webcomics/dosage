# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..util import tagre


class IAmArg(_BasicScraper):
    description = u'An Internet comic of non sequitur Geekiness. Updates Monday, Wednesday and Friday'
    url = 'http://iamarg.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2011/05/08/05082011'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class ICanBarelyDraw(_BasicScraper):
    url = 'http://www.icanbarelydraw.com/comic/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '39'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+-[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+)' % rurl))
    help = 'Index format: number'
    description = u'Webcomic featuring technology, romance, and odd behavior'


class IDreamOfAJeanieBottle(_BasicScraper):
    url = 'http://jeaniebottle.com/'
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '15'
    imageSearch = compile(r'(/comics/.+?)"')
    prevSearch = compile(tagre("a", "href", r'(http://jeaniebottle\.com/\?p=\d+)', after="prev"))
    help = 'Index format: n (unpadded)'


class InternetWebcomic(_BasicScraper):
    description = u"Internet Webcomic"
    url = 'http://www.internet-webcomic.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '30'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"/]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="navi navi-prev"))
    help = 'Index format: n'


class IrregularWebcomic(_BasicScraper):
    url = 'http://www.irregularwebcomic.net/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<img .*src="(.*comics/.*(png|jpg|gif))".*>')
    prevSearch = compile(r'<a href="(/\d+\.html|/cgi-bin/comic\.pl\?comic=\d+)">Previous ')
    help = 'Index format: nnn'


class ItsWalky(_BasicScraper):
    url = 'http://www.itswalky.com/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '19970908'
    imageSearch = compile(tagre("img", "src", r'(/comic[s|/][^"]+)'))
    prevSearch = compile(tagre("a", "href", r'[^"]*(/d/\d+\.s?html)')+r"[^>]+/images/(?:nav_02|previous_day)\.gif")
    help = 'Index format: yyyymmdd'

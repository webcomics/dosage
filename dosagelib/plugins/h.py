# -*- coding: iso-8859-1 -*-
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre
from ..helpers import bounceStarter


class HagarTheHorrible(_BasicScraper):
    url = 'http://www.hagarthehorrible.net/'
    stripUrl = 'http://www.hagardunor.net/comicstrips_us.php?serietype=9&colortype=1&serieno=%s'
    firstStripUrl = stripUrl % '1'
    multipleImagesPerStrip = True
    imageSearch = compile(tagre("img", "src", r'(stripus\d+/(?:Hagar_The_Horrible_?|h)\d+[^ >]+)', quote=""))
    prevUrl = r'(comicstrips_us\.php\?serietype\=9\&colortype\=1\&serieno\=\d+)'
    prevSearch = compile(tagre("a", "href", prevUrl, after="Previous"))
    help = 'Index format: number'

    @classmethod
    def starter(cls):
        """Return last gallery link."""
        url = 'http://www.hagardunor.net/comics.php'
        data = cls.getPage(url)
        pattern = compile(tagre("a", "href", cls.prevUrl))
        for starturl in cls.fetchUrls(url, data, pattern):
            pass
        return starturl


class HarkAVagrant(_BasicScraper):
    url = 'http://www.harkavagrant.com/'
    rurl = escape(url)
    starter = bounceStarter(url,
        compile(tagre("a", "href", r'(%sindex\.php\?id=\d+)' % rurl) +
        tagre("img", "src", "buttonnext.png")))
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%s[^"]+)' % rurl, after='BORDER'))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php\?id=\d+)' % rurl) +
        tagre("img", "src", "buttonprevious.png"))
    help = 'Index format: number'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[1]
        num = pageUrl.rsplit('=', 1)[1]
        return '%s-%s' % (num, filename)


class HorribleVille(_BasicScraper):
    url = 'http://horribleville.com/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20051220'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/[^"]+)') + tagre("img", "src", r'/images/previous\.png'))
    help = 'Index format: yyyymmdd'

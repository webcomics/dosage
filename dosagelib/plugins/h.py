# -*- coding: iso-8859-1 -*-
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..util import tagre, getPageContent, fetchUrls
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
        content = getPageContent(url, cls.session)[0]
        pattern = compile(tagre("a", "href", cls.prevUrl))
        for starturl in fetchUrls(url, content, url, pattern):
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


class HijinksEnsue(_BasicScraper):
    description = u'HijiNKS ENSUE is a geek pop culture webcomic that makes fun of the latest news in tv, movies, Sci-Fi, technology and the Internet'
    url = 'http://hijinksensue.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007/05/11/a-soul-as-black-as-eyeliner'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class Hipsters(_BasicScraper):
    description = u'a weekly webcomic series by Adrian vom Baur - Hipsters vs. Vampires - Hipsters vs. Dinosaurs - Hipsters vs. Robots'
    url = 'http://www.hipsters-comic.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2010/08/hip01'
    imageSearch = compile(tagre("img", "src", r'(%scomics/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/dd/stripname'


class HorribleVille(_BasicScraper):
    url = 'http://horribleville.com/'
    stripUrl = url + 'd/%s.html'
    firstStripUrl = stripUrl % '20051220'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/[^"]+)') + tagre("img", "src", r'/images/previous\.png'))
    help = 'Index format: yyyymmdd'

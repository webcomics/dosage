# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile
from ..scraper import _BasicScraper
from ..util import tagre, getPageContent, fetchUrls
from ..helpers import bounceStarter


class HagarTheHorrible(_BasicScraper):
    url = 'http://www.hagarthehorrible.net/'
    stripUrl = 'http://www.hagardunor.net/comicstrips_us.php?serietype=9&colortype=1&serieno=%s'
    firstStripUrl = stripUrl % '1'
    multipleImagesPerStrip = True
    imageSearch = compile(tagre("img", "src", r'(stripus\d+/Hagar_The_Horrible_\d+[^ >]+)', quote=""))
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
    starter = bounceStarter(url,
        compile(tagre("a", "href", r'(http://www\.harkavagrant\.com/index\.php\?id=\d+)') +
        tagre("img", "src", "buttonnext.png")))
    stripUrl = url + 'index.php?id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://www.harkavagrant.com/[^"]+)', after='BORDER'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.harkavagrant\.com/index\.php\?id=\d+)') +
        tagre("img", "src", "buttonprevious.png"))
    help = 'Index format: number'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        filename = imageUrl.rsplit('/', 1)[1]
        num = pageUrl.rsplit('=', 1)[1]
        return '%s-%s' % (num, filename)


class HijinksEnsue(_BasicScraper):
    url = 'http://hijinksensue.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://hijinksensue\.com/comics/\d+-\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://hijinksensue\.com/\d+/\d+/\d+/[^"]+)', after="navi-prev"))
    help = 'Index format: yyyy/mm/dd/name'


class Hipsters(_BasicScraper):
    url = 'http://www.hipsters-comic.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2010/08/hip01'
    imageSearch = compile(tagre("img", "src", r'(http://www\.hipsters-comic\.com/comics/\d+-\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.hipsters-comic\.com/\d+/\d+/[^"]+)', after="prev"))
    help = 'Index format: yyyy/dd/stripname'


class HorribleVille(_BasicScraper):
    url = 'http://horribleville.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/d/[^"]+)') + tagre("img", "src", r'/images/previous\.png'))
    help = 'Index format: yyyymmdd'

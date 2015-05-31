# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape, IGNORECASE

from ..scraper import _BasicScraper, _ParserScraper
from ..util import tagre


class MacHall(_BasicScraper):
    url = 'http://www.machall.com/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2000-11-07'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img[^>]+?src=\'drop_shadow/previous.gif\'>')
    help = 'Index format: yyyy-mm-dd'


class MadamAndEve(_BasicScraper):
    url = 'http://www.madamandeve.co.za/'
    stripUrl = None
    imageSearch = compile(tagre('img', 'src', r'(/cartoons/me\d{6}\.(gif|jpg))'))
    multipleImagesPerStrip = True


class Magellan(_ParserScraper):
    description = u'A comic strip about Superheroes and Not-Superheroes'
    url = 'http://magellanverse.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = '#comic-1 > a:first-child img'
    prevSearch = '.nav-previous > a'
    help = 'Index format: stripname'

	
class MagickChicks(_BasicScraper):
    url = 'http://www.magickchicks.com/'
    stripUrl = url + 'strips-mc/%s'
    firstStripUrl = stripUrl % 'tis_but_a_trifle'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-mc/[^"]+)', before="cn[id]prevt"))
    help = 'Index format: name'


class ManlyGuysDoingManlyThings(_ParserScraper):
    url = 'http://thepunchlineismachismo.com/'
    stripUrl = url + 'archives/comic/%s'
    firstStripUrl = stripUrl % '02222010'
    css = True
    imageSearch = "#comic img"
    prevSearch = ".comic-nav-previous"
    help = 'Index format: ddmmyyyy'


class MareInternum(_ParserScraper):
    description = u'Mare Internum is an online science fiction graphic novel about the isolated inhabitants of the planet Mars. '
    url = 'http://marecomic.com/'
    stripUrl = url + 'comics/ch%s'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@class="comic-nav-base comic-nav-previous"]'
    help = 'Index format: <chapter>-page-<pagenum>'


class Marilith(_BasicScraper):
    url = 'http://www.marilith.com/'
    stripUrl = url + 'archive.php?date=%s'
    firstStripUrl = stripUrl % '20041215'
    imageSearch = compile(r'<img src="(comics/.+?)" border')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class MarriedToTheSea(_BasicScraper):
    url = 'http://www.marriedtothesea.com/'
    rurl = escape(url)
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '022806'
    imageSearch = compile(tagre("img", "src", r'(%s\d+/[^"]+)' % rurl, before="overflow"))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "&lt;&lt; Yesterday")
    help = 'Index format: mmddyy'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        unused, date, filename = imageUrl.rsplit('/', 2)
        return '%s-%s' % (date, filename)

class MaxOveracts(_ParserScraper):
    url = 'http://occasionalcomics.com/'
    stripUrl = url + '%s/'
    css = True
    imageSearch = '#comic img'
    prevSearch = '.nav-previous > a'
    help = 'Index format: nnn'


class MegaTokyo(_BasicScraper):
    url = 'http://megatokyo.com/'
    stripUrl = url + 'strip/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'"(strips/.+?)"', IGNORECASE)
    prevSearch = compile(r'"(./strip/\d+?)">Prev')
    help = 'Index format: nnnn'


class MenageA3(_BasicScraper):
    adult = True
    url = 'http://www.ma3comic.com/'
    stripUrl = url + 'strips-ma3/%s'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-ma3/[^"]+)', before="cn[id]prev"))
    help = 'Index format: name'


class Misfile(_BasicScraper):
    url = 'http://www.misfile.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2004-02-22'
    imageSearch = compile(tagre("img", "src", r"(comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("link", "href", r"([^']+)", quote="'", before="Previous"))
    help = 'Index format: yyyy-mm-dd'


class Moonsticks(_ParserScraper):
    url = "http://moonsticks.org/"
    stripUrl = url
    imageSearch = "//div[@class='entry']//img"
    prevSearch = u"//a[text()='« Previous']"
    help = 'Index format: stripname'


class MonsieurLeChien(_BasicScraper):
    url = 'http://www.monsieur-le-chien.fr/'
    stripUrl = url + 'index.php?planche=%s'
    firstStripUrl = stripUrl % '2'
    lang = 'fr'
    imageSearch = compile(tagre("img", "src", r'(i/planches/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", "i/precedent.gif"))
    help = 'Index format: n'


class MrLovenstein(_BasicScraper):
    url = 'http://www.mrlovenstein.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s#comic'
    firstStripUrl = stripUrl % '1'
    imageSearch =  (
        #captures rollover comic
        compile(tagre("div", "class", r'comic_image') + "\s*.*\s*" + tagre("div", "style", r'display: none;') + "\s*.*\s*" + tagre("img", "src", r'(/images/comics/[^"]+)')),
        #captures standard comic
        compile(tagre("img", "src", r'(/images/comics/[^"]+)', before="comic_main_image")),
    )
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + tagre("img", "src", "/images/nav_left.png"))
    textSearch = compile(r'<meta name="description" content="(.+?)" />')
    help = 'Index Format: n'


class MyCartoons(_BasicScraper):
    url = 'http://mycartoons.de/'
    rurl = escape(url)
    stripUrl = url + 'page/%s'
    imageSearch = (
        compile(tagre("img", "src", r'(%swp-content/cartoons/(?:[^"]+/)?\d+-\d+-\d+[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(%scartoons/[^"]+/\d+-\d+-\d+[^"]+)' % rurl)),
    )
    prevSearch = compile(tagre("a", "href", r'(%spage/[^"]+)' % rurl) + "&laquo;")
    help = 'Index format: number'
    lang = 'de'


class MysteriesOfTheArcana(_ParserScraper):
    url = 'http://mysteriesofthearcana.com/'
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[@class="navprevious"]'
    help = 'Index format: n (unpadded)'

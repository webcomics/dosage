# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre


# broken links - disable for now
class _MadamAndEve(_BasicScraper):
    url = 'http://www.madamandeve.co.za/week_of_cartns.php'
    stripUrl = None
    imageSearch = compile(r'<IMG BORDER="0" SRC="(cartoons/me\d{6}\.(gif|jpg))">')
    prevSearch = compile(r'<a href="(weekend_cartoon.php)"')


class MagickChicks(_BasicScraper):
    url = 'http://www.magickchicks.com/'
    stripUrl = url + 'strips-mc/%s'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-mc/[^"]+)', before="cn[id]prevt"))
    help = 'Index format: name'


class ManlyGuysDoingManlyThings(_BasicScraper):
    url = 'http://thepunchlineismachismo.com/'
    stripUrl = url + 'archives/comic/%s'
    imageSearch = compile(tagre("img", "src", r'(http://thepunchlineismachismo\.com/wp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://thepunchlineismachismo\.com/archives/comic/[^"]+)', after="previous"))
    help = 'Index format: ddmmyyyy'


class Marilith(_BasicScraper):
    url = 'http://www.marilith.com/'
    stripUrl = url + 'archive.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)" border')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class MarryMe(_BasicScraper):
    url = 'http://marryme.keenspot.com/'
    stripUrl = url + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("link", "href", r'(/d/[^"]+)', before="prev"))
    help = 'Index format: yyyymmdd'


class Meek(_BasicScraper):
    url = 'http://www.meekcomic.com/'
    stripUrl = url + '%s'
    imageSearch = compile(r'meekcomic.com(/comics/.+?)"')
    prevSearch = compile(r'\s.+?(http://www.meekcomic.com/.+?)".+?Previous<')
    help = 'Index format: yyyy/mm/dd/ch-p/'


class MegaTokyo(_BasicScraper):
    url = 'http://megatokyo.com/'
    stripUrl = url + 'strip/%s'
    imageSearch = compile(r'"(strips/.+?)"', IGNORECASE)
    prevSearch = compile(r'"(./strip/\d+?)">Prev')
    help = 'Index format: nnnn'


class Meiosis(_BasicScraper):
    url = 'http://meiosiswebcomic.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://meiosiswebcomic\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://meiosiswebcomic\.com/[^"]+)', after="navi-prev"))
    help = 'Index format: yyyy/mm/ddmmyyyy'


class MacHall(_BasicScraper):
    url = 'http://www.machall.com/'
    stripUrl = url + 'view.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img[^>]+?src=\'drop_shadow/previous.gif\'>')
    help = 'Index format: yyyy-mm-dd'


class MenageA3(_BasicScraper):
    adult = True
    url = 'http://www.ma3comic.com/'
    stripUrl = url + 'strips-ma3/%s'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-ma3/[^"]+)', before="cn[id]prev"))
    help = 'Index format: name'


class Melonpool(_BasicScraper):
    url = 'http://www.melonpool.com/'
    stripUrl = url + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.melonpool\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.melonpool\.com/\?p=\d+)', after="prev"))
    help = 'Index format: n'


class Misfile(_BasicScraper):
    url = 'http://www.misfile.com/'
    stripUrl = url + '?date=%s'
    imageSearch = compile(tagre("img", "src", r"(comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("link", "href", r"([^']+)", quote="'", before="Previous"))
    help = 'Index format: yyyy-mm-dd'


class MysteriesOfTheArcana(_BasicScraper):
    url = 'http://mysteriesofthearcana.com/'
    stripUrl = url + 'index.php?action=comics&cid=%s'
    imageSearch = compile(tagre("img", "src", r'(image\.php\?type=com&i=[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php[^"]+)', after="navprevious"))
    help = 'Index format: n (unpadded)'


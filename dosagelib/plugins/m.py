# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre


# broken links - disable for now
class _MadamAndEve(_BasicScraper):
    latestUrl = 'http://www.madamandeve.co.za/week_of_cartns.php'
    stripUrl = None
    imageSearch = compile(r'<IMG BORDER="0" SRC="(cartoons/me\d{6}\.(gif|jpg))">')
    prevSearch = compile(r'<a href="(weekend_cartoon.php)"')


class Marilith(_BasicScraper):
    latestUrl = 'http://www.marilith.com/'
    stripUrl = latestUrl + 'archive.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)" border')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class MarryMe(_BasicScraper):
    latestUrl = 'http://marryme.keenspot.com/'
    stripUrl = latestUrl + 'd/%s.html'
    imageSearch = compile(tagre("img", "src", r'(/comics/[^"]+)'))
    prevSearch = compile(tagre("link", "href", r'(/d/[^"]+)', before="prev"))
    help = 'Index format: yyyymmdd'


class Meek(_BasicScraper):
    latestUrl = 'http://www.meekcomic.com/'
    stripUrl = latestUrl + '%s'
    imageSearch = compile(r'meekcomic.com(/comics/.+?)"')
    prevSearch = compile(r'\s.+?(http://www.meekcomic.com/.+?)".+?Previous<')
    help = 'Index format: yyyy/mm/dd/ch-p/'


class MegaTokyo(_BasicScraper):
    latestUrl = 'http://megatokyo.com/'
    stripUrl = latestUrl + 'strip/%s'
    imageSearch = compile(r'"(strips/.+?)"', IGNORECASE)
    prevSearch = compile(r'"(./strip/\d+?)">Prev')
    help = 'Index format: nnnn'


class Meiosis(_BasicScraper):
    latestUrl = 'http://meiosiswebcomic.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://meiosiswebcomic\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://meiosiswebcomic\.com/[^"]+)', after="navi-prev"))
    help = 'Index format: yyyy/mm/ddmmyyyy'


class MacHall(_BasicScraper):
    latestUrl = 'http://www.machall.com/'
    stripUrl = latestUrl + 'view.php?date=%s'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img[^>]+?src=\'drop_shadow/previous.gif\'>')
    help = 'Index format: yyyy-mm-dd'


class Melonpool(_BasicScraper):
    latestUrl = 'http://www.melonpool.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.melonpool\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.melonpool\.com/\?p=\d+)', after="prev"))
    help = 'Index format: n'


class Misfile(_BasicScraper):
    latestUrl = 'http://www.misfile.com/'
    stripUrl = latestUrl + '?date=%s'
    imageSearch = compile(tagre("img", "src", r"(comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("link", "href", r"([^']+)", quote="'", before="Previous"))
    help = 'Index format: yyyy-mm-dd'


class MysteriesOfTheArcana(_BasicScraper):
    latestUrl = 'http://mysteriesofthearcana.com/'
    stripUrl = latestUrl + 'index.php?action=comics&cid=%s'
    imageSearch = compile(tagre("img", "src", r'(image\.php\?type=com&i=[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php[^"]+)', after="navprevious"))
    help = 'Index format: n (unpadded)'


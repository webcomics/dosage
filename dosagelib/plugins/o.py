# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper, _ParserScraper
from ..helpers import indirectStarter
from ..util import tagre


class OctopusPie(_ParserScraper):
    url = 'http://www.octopuspie.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2007-05-14/001-pea-wiggle'
    imageSearch = '//img[@title]'
    prevSearch = '//a[@rel="prev"]'
    help = 'Index format: yyyy-mm-dd/nnn-strip-name'


class OddFish(_BasicScraper):
    url = 'http://www.odd-fish.net/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'tv-tentacles'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: stripname'


class Oglaf(_BasicScraper):
    url = 'http://oglaf.com/'
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(http://media\.oglaf\.com/comic/[^"]+)', before="strip"))
    prevSearch = (
      # first search for "next page" URLs
      compile(tagre("a", "href", r'(/[^"]+/\d+/)') + tagre("div", "id", "nx")),
      # then for "prev story"
      compile(tagre("a", "href", r'(/[^"]+)') + tagre("div", "id", "pvs?")),
    )
    help = 'Index format: stripname'
    adult = True


class OhJoySexToy(_BasicScraper):
    url = 'http://www.ohjoysextoy.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % 'introduction'
    imageSearch =  compile(tagre("div", "class", r'comicpane') + "\s*.*\s*" + tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after='navi navi-prev'))
    textSearch = compile(tagre("div", "class", r'comicpane') + "\s*.*\s*" + tagre("img", "alt", r'([^"]+)'))
    help = 'Index Format: name'
    adult = True


class OkCancel(_BasicScraper):
    url = 'http://okcancel.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s.html'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(%sstrips/okcancel\d{8}\.gif)' % rurl))
    prevSearch = compile(tagre("div", "class", "previous") + tagre("a", "href", r'(%scomic/\d{1,4}\.html)' % rurl))
    starter = indirectStarter(url, prevSearch)
    help = 'Index format: yyyymmdd'


class OmakeTheater(_ParserScraper):
    url = 'http://omaketheater.com/comics/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1'
    css = True
    imageSearch = ".comicImage img"
    prevSearch = ".previous a"
    help = 'Index format: number (unpadded)'


class OnTheFastrack(_BasicScraper):
    url = 'http://onthefastrack.com/'
    stripUrl = url + 'comics/%s'
    firstStripUrl = stripUrl % 'november-13-2000'
    imageSearch = compile(r'(http://safr\.kingfeatures\.com/idn/cnfeed/zone/js/content\.php\?file=.+)"')
    prevSearch = compile(r'id="previouscomic" class="button white"><a href="(%scomics/[a-z0-9-]+/)"' % url)
    help = 'Index format: monthname-dd-yyyy'
    
    @classmethod
    def namer(cls, imageUrl, pageUrl):
        name = pageUrl.rsplit('/', 3)[2]
        if name == "onthefastrack.com":
                import datetime
                name = datetime.date.today().strftime("%B-%d-%Y")
        # name.title ensures that the comics are named the same
        # as in the previous scraper
        return "%s.gif" % name.title()


class OneQuestion(_BasicScraper):
    url = 'http://onequestioncomic.com/'
    stripUrl = url + 'comic.php?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'((?:\.\./)?istrip_files/strips/\d+\.\w{3,4})'))
    prevSearch = compile(tagre("a", "href", r'(comic\.php\?strip_id=\d+)') + tagre("img", "src", r'img/arrow_prev\.jpg'))
    help = 'Index format: n (unpadded)'


class Optipess(_BasicScraper):
    url = 'http://www.optipess.com/'
    stripUrl = url + '%s'
    firstStripUrl =  url + '2008/12/01/jason-friend-of-the-butterflies/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[x|\d]+[^"]+\.[^"]+)' % url))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="navi navi-prev"))
    textSearch = compile(tagre("img", "alt", r'([^"]+)', before=url))
    help = 'Index format: yyyy/mm/dd/stripname'


class OrnerBoy(_BasicScraper):
    url = 'http://www.orneryboy.com/'
    rurl = escape(url)
    stripUrl = url + 'index.php?comicID=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(comics/\d+\.[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%sindex\.php\?comicID=\d+)' % rurl) +
        tagre("img", "src", r'images/prev_a\.gif'))
    help = 'Index format: number'


class OurHomePlanet(_BasicScraper):
    url = 'http://gdk.gd-kun.net/'
    stripUrl = url + '%s.html'
    firstStripUrl = stripUrl % '01'
    imageSearch = compile(r'<img src="(pages/comic.+?)"')
    prevSearch = compile(r'coords="50,18,95,65".+?href="(.+?\.html)".+?alt=')
    help = 'Index format: n (unpadded)'


class OverCompensating(_BasicScraper):
    url = 'http://www.overcompensating.com/'
    stripUrl = url + 'oc/index.php?comic=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(tagre("img", "src", r'(/oc/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href",
      r'(/oc/index\.php\?comic=\d+)', after="go back"))
    help = 'Index format: number'

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class LasLindas(_BasicScraper):
    url = 'http://laslindas.katbox.net/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/[^"]+)' % rurl, after="attachment-full"))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'


class LeastICouldDo(_BasicScraper):
    description = u'A daily webcomic series about the life of Rayne Summers. Created by Ryan Sohmer and Lar deSouza.'
    url = 'http://www.leasticoulddo.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '20130109'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.leasticoulddo\.com/wp-content/uploads/\d+/\d+/\d{8,9}\.\w{1,4})'))
    prevSearch = compile(tagre("a", "href", r'(%scomic/\d+/)' % rurl, after="Previous"))
    starter = indirectStarter(url,
      compile(tagre("a", "href", r'(%scomic/\d+/)' % rurl, after="feature-comic")))
    help = 'Index format: yyyymmdd'


class Lint(_BasicScraper):
    url = 'http://www.purnicellin.com/lint/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2004/01/10/01102004'
    imageSearch = compile(r'<img src="(%scomics/.+?)"' % rurl)
    prevSearch = compile(r'\| <a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/num-name'


class LittleGamers(_BasicScraper):
    description = u'The comic everyone knows, but no one reads'
    url = 'http://www.little-gamers.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2000/12/01/99'
    imageSearch = compile(tagre("img", "src", r'(http://little-gamers\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.little-gamers\.com/[^"]+)', before="comic-nav-prev-link"))
    help = 'Index format: yyyy/mm/dd/name'


class LoadingArtist(_BasicScraper):
    description = u'A webcomic by Gregor Czaykowski'
    url = 'http://www.loadingartist.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2011/01/04/born'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+/)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class LookingForGroup(_BasicScraper):
    url = 'http://www.lfgcomic.com/'
    rurl = escape(url)
    stripUrl = url + 'page/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://cdn\.lfgcomic\.com/wp-content/uploads/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(%spage/[-0-9]+/)' % rurl, after="navtop-prev"))
    starter = indirectStarter(url,
        compile(tagre("a", "href", r'(%spage/[-0-9]+/)' % rurl, after="feature-previous")))
    nameSearch = compile(r'/page/([-0-9]+)/')
    help = 'Index format: nnn'

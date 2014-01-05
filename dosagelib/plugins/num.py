# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape

from ..util import tagre
from ..scraper import _BasicScraper


class NineteenNinetySeven(_BasicScraper):
    description = u'1977 the Comic - Sex, Drugs and Rock and Roll Just Not in That Order'
    name = '1997'
    url = 'http://1977thecomic.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1977-comics/from-the-beginning-part-1'
    imageSearch = compile(tagre("img", "src", r'(%scomics-1977/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"Previous")
    help = 'Index format: yyyy/mm/dd/strip-name'

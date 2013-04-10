# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile

from ..util import tagre
from ..scraper import _BasicScraper


class NineteenNinetySeven(_BasicScraper):
    name = '1997'
    url = 'http://www.1977thecomic.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '1977-comics/from-the-beginning-part-1'
    imageSearch = compile(tagre("img", "src", r'(http://www\.1977thecomic\.com/comics-1977/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)')+"Previous")
    help = 'Index format: yyyy/mm/dd/strip-name'

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import re

from ..scraper import _ParserScraper
from ..helpers import bounceStarter


class _WLPComics(_ParserScraper):
    imageSearch = '//center/*/img[contains(@alt, " Comic")]'
    prevSearch = '//a[contains(text(), "Previous ")]'
    nextSearch = '//a[contains(text(), "Next ")]'
    starter = bounceStarter
    help = 'Index format: nnn'

    def __init__(self, name):
        super(_WLPComics, self).__init__('WLP/' + name)

    def namer(self, image_url, page_url):
        return (page_url.rsplit('/', 1)[-1].split('.')[0] + '_' +
                image_url.rsplit('/', 1)[-1])

    def getIndexStripUrl(self, index):
        return self.url + '%s.html' % index


class ChichiChan(_WLPComics):
    url = 'http://www.wlpcomics.com/adult/chichi/'
    adult = True


class ChocolateMilkMaid(_WLPComics):
    # Newer pages seem to be broken
    baseurl = 'http://www.wlpcomics.com/adult/cm/'
    url = baseurl + '264.html'
    adult = True

    def getIndexStripUrl(self, index):
        return self.baseurl + '%s.html' % index

    def link_modifier(self, fromurl, tourl):
        """Bugfix for self-referencing pages..."""
        if tourl == fromurl:
            return re.sub(r'/(\d+)\.ht',
                          lambda m: '/%03i.ht' % (int(m.group(1)) - 1), tourl)
        if '263.html' in fromurl and '265.html' in tourl:
            return self.baseurl + '264.html'
        return tourl


class MaidAttack(_WLPComics):
    url = 'http://www.wlpcomics.com/general/maidattack/'


class PeterIsTheWolfAdult(_WLPComics):
    url = 'http://www.peteristhewolf.com/adult/home.html'
    adult = True


class PeterIsTheWolfGeneral(_WLPComics):
    url = 'http://www.peteristhewolf.com/general/'


class Stellar(_WLPComics):
    url = 'http://www.wlpcomics.com/adult/stellar/'
    adult = True

    def link_modifier(self, fromurl, tourl):
        """Bugfix for empty page..."""
        if tourl == self.url + '075.html':
            return self.url + '074.html'
        return tourl

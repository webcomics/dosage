# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
import re

from ..scraper import ParserScraper
from ..helpers import bounceStarter


class WLPComics(ParserScraper):
    imageSearch = '//img[contains(@alt, " Comic")]'
    prevSearch = '//a[contains(text(), "Previous ")]'
    nextSearch = '//a[contains(text(), "Next ")]'
    starter = bounceStarter
    help = 'Index format: nnn'

    def __init__(self, name):
        super().__init__('WLP/' + name)

    def namer(self, image_url, page_url):
        return (page_url.rsplit('/', 1)[-1].split('.')[0] + '_' +
                image_url.rsplit('/', 1)[-1])


class ChichiChan(WLPComics):
    url = 'http://www.wlpcomics.com/adult/chichi/'
    stripUrl = url + '%s.html'
    adult = True


class ChocolateMilkMaid(WLPComics):
    # Newer pages seem to be broken
    stripUrl = 'http://www.wlpcomics.com/adult/cm/%s.html'
    url = stripUrl % '264'
    adult = True

    def link_modifier(self, fromurl, tourl):
        """Bugfix for self-referencing pages..."""
        if tourl == fromurl:
            return re.sub(r'/(\d+)\.ht',
                          lambda m: '/%03i.ht' % (int(m.group(1)) - 1), tourl)
        if '263.html' in fromurl and '265.html' in tourl:
            return self.stripUrl % '264'
        return tourl


class MaidAttack(WLPComics):
    url = 'http://www.wlpcomics.com/general/maidattack/'
    stripUrl = url + '%s.html'


class PeterIsTheWolfAdult(WLPComics):
    stripUrl = 'http://www.peteristhewolf.com/adult/%s.html'
    # navigation to newest page is broken
    url = stripUrl % '427'
    firstStripUrl = stripUrl % '001'
    multipleImagesPerStrip = True
    adult = True
    endOfLife = True

    def namer(self, imageUrl, pageUrl):
        name = pageUrl.rsplit('/', 1)[-1].split('.')[0] + '_' + imageUrl.rsplit('/', 1)[-1]
        if 'adult' in imageUrl:
            name = name.split('.')
            return name[0] + '_adult.' + name[1]
        return name

    def getPrevUrl(self, url, data):
        # Fix loop in site navigation
        if url == self.stripUrl % '194':
            return self.stripUrl % '193'
        return super(PeterIsTheWolfAdult, self).getPrevUrl(url, data)


class PeterIsTheWolfGeneral(WLPComics):
    stripUrl = 'http://www.peteristhewolf.com/general/%s.html'
    # navigation to newest page is broken
    url = stripUrl % '427'
    firstStripUrl = stripUrl % '001'
    endOfLife = True

    def getPrevUrl(self, url, data):
        # Fix loops in site navigation
        if url == self.stripUrl % '406':
            return self.stripUrl % '405'
        if url == self.stripUrl % '230':
            return self.stripUrl % '229'
        if url == self.stripUrl % '229':
            return self.stripUrl % '228'
        if url == self.stripUrl % '153':
            return self.stripUrl % '152'
        return super(PeterIsTheWolfGeneral, self).getPrevUrl(url, data)


class Stellar(WLPComics):
    url = 'http://www.wlpcomics.com/adult/stellar/'
    stripUrl = url + '%s.html'
    adult = True

    def link_modifier(self, fromurl, tourl):
        """Bugfix for empty page..."""
        if tourl == self.url + '075.html':
            return self.url + '074.html'
        return tourl

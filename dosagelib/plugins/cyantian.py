# -*- coding: utf-8 -*-
# Copyright (C) 2019-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from .common import _WordPressScraper


class TheCyantianChronicles(_WordPressScraper):
    baseUrl = 'https://cyantian.net/'
    stripUrl = baseUrl + 'comic/%s/'

    def __init__(self, name, story, first, last=None, nav=None):
        super(TheCyantianChronicles, self).__init__('TheCyantianChronicles/' + name)

        self.url = self.baseUrl + 'story/' + story + '/'
        self.firstStripUrl = self.stripUrl % first

        self.nav = nav

        if last:
            self.url = self.stripUrl % last
            self.endOfLife = True

    def getPrevUrl(self, url, data):
        # Missing/broken navigation links
        url = url.rstrip('/').rsplit('/', 1)[-1]
        if self.nav and url in self.nav:
            return self.stripUrl % self.nav[url]
        return super(TheCyantianChronicles, self).getPrevUrl(url, data)

    @classmethod
    def getmodules(cls):
        return (
            cls('Akaelae', 'akaelae', '05182003', last='01202010'),
            cls('Artwork', 'artwork', '07162003', nav={'d-71': 'a-17'}),
            cls('CampusSafari', 'ocs', '10012000', last='03282008'),
            cls('CampusSafariReboot', 'campus-safari', 'campus-safari-chapter-0'),
            cls('CesileesDiary', 'cdiary', '12062001-2', last='05312006'),
            cls('CookieCaper', 'cookie-caper', 'cookie-war', last='2014-04-17'),
            cls('Darius', 'dbook-01', '03102010', last='darius-end'),
            cls('DracoVulpes', 'draco-vulpes', 'draco-vulpes'),
            cls('GenoworksSaga', 'genoworks-saga', '07012004'),
            cls('GralenCraggHall', 'gchall', '07152002', last='chapter-6-05', nav={'chapter-5': '02152005'}),
            cls('Kiet', 'kiet', 'kiet-c01'),
            cls('NoAngel', 'no-angel', '08112001', last='12142006'),
            cls('Pawprints', 'pawprints', 'airboard-page-1', last='pawprints-sheana-10'),
            cls('RandomRamblings', 'random-ramblings', 'darrik'),
            cls('SinkOrSwim', 'sos', 'sink-or-swim', last='ricochete-and-seraphim')
        )


class Shivae(_WordPressScraper):
    url = 'https://shivae.com/'
    stripUrl = url + 'gnip/%s/'
    firstStripUrl = stripUrl % 'cler/09202001'


class ShivaeComics(_WordPressScraper):
    baseUrl = 'https://shivae.net/'

    def __init__(self, name, story, first, last=None, nav=None):
        super(ShivaeComics, self).__init__('Shivae/' + name)

        self.url = self.baseUrl + story + '/'
        self.stripUrl = self.url + 'comic/%s/'
        self.firstStripUrl = self.stripUrl % first

        self.nav = nav

        if last:
            self.url = self.stripUrl % last
            self.endOfLife = True

    def getPrevUrl(self, url, data):
        # Missing/broken navigation links
        url = url.rstrip('/').rsplit('/', 1)[-1]
        if self.nav and url in self.nav:
            return self.stripUrl % self.nav[url]
        return super(ShivaeComics, self).getPrevUrl(url, data)

    @classmethod
    def getmodules(cls):
        return (
            cls('BlackRose', 'blackrose', '11012004'),
            cls('CafeAnime', 'cafeanime', '08172004', last='09192009'),
            cls('Extras', 'extras', '01012012', nav={'12302012': '08152013'}),
            cls('Pure', 'pure', '04082002', last='chapter-6-page-1'),
            cls('SerinFairyHunter', 'serin', 'character-serin'),
            cls('SivineBlades', 'sivine', '06302002', last='10242008')
        )

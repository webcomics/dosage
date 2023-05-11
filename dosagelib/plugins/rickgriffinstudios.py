# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2022 Daniel Ring
from ..helpers import indirectStarter
from .common import WordPressScraper, WordPressNaviIn


class Housepets(WordPressScraper):
    url = 'http://www.housepetscomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = '2008/06/02/when-boredom-strikes'


class RickGriffinStudios(WordPressNaviIn):
    baseUrl = 'http://rickgriffinstudios.com/'
    stripUrl = baseUrl + 'comic-post/%s/'
    latestSearch = '//a[contains(@title, "Permanent Link")]'
    starter = indirectStarter
    nav = None

    def __init__(self, name, sub, first, last=None, adult=False, nav=None):
        super().__init__('RickGriffinStudios/' + name)
        self.url = self.baseUrl + sub + '/'
        self.firstStripUrl = self.stripUrl % first

        if last:
            self.url = self.stripUrl % last
            self.starter = super(RickGriffinStudios, self).starter
            self.endOfLife = True

        if adult:
            self.latestSearch = '//a[contains(@title, "NSFW")]'
            self.adult = True

        if nav:
            self.nav = nav

    def getPrevUrl(self, url, data):
        # Links between chapters
        url = url.rstrip('/').rsplit('/', 1)[-1]
        if self.nav and url in self.nav:
            return self.stripUrl % self.nav[url]
        return super(RickGriffinStudios, self).getPrevUrl(url, data)

    @classmethod
    def getmodules(cls):
        return (
            cls('AHClub', 'ah-club', 'cover', nav={
                'ah-club-2-cover': 'ah-club-1-page-24',
                'ah-club-3-cover': 'ah-club-2-page-28',
                'ah-club-4-cover': 'ah-club-3-page-22',
                'ah-club-5-cover': 'ah-club-4-page-24',
            }),
            cls('HayvenCelestia', 'hayven-celestia', 'skinchange-p1'),
            cls('TheStoryboard', 'the-storyboard', 'the-storyboard-001'),
            cls('TracesOfThePast', 'in-the-new-age', 'totp-page-1'),
            cls('TracesOfThePastNSFW', 'in-the-new-age', 'totp-page-1-nsfw', adult=True),
            cls('ZootopiaNightTerrors', 'zootopia-night-terrors',
                'zootopia-night-terrors-p1', 'zootopia-night-terrors-p7'),
        )

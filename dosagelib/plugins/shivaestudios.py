# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from .common import WordPressSpliced


class _CommonMulti(WordPressSpliced):
    def __init__(self, name, path, first, eol=False):
        super().__init__(name)
        self.url = self.baseUrl + 'series/' + path + '/'
        self.firstStripUrl = self.stripUrl % first
        self.endOfLife = eol


class AlienDice(WordPressSpliced):
    url = 'https://aliendice.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '05162001'

    def shouldSkipUrl(self, url, data):
        """Skip pages without images."""
        return not data.xpath(self.imageSearch)

    def getPrevUrl(self, url, data):
        # Fix broken navigation
        if url == self.stripUrl % 'day-29-part-2-page-3-4':
            return self.stripUrl % 'day-29-part-2-page-3-2'
        return super().getPrevUrl(url, data)

    def namer(self, imageUrl, pageUrl):
        # Fix inconsistent filename
        return imageUrl.rsplit('/', 1)[-1].replace('20010831', '2001-08-31')


class AlienDiceLegacy(WordPressSpliced):
    name = 'AlienDice/Legacy'
    baseUrl = 'https://aliendice.com/'
    url = baseUrl + 'series/legacy/'
    stripUrl = baseUrl + 'comic/%s/'
    firstStripUrl = stripUrl % 'legacy-1'
    endOfLife = True

    def isfirststrip(self, url):
        # Strip series identifier
        return super().isfirststrip(url.rsplit('?', 1)[0])


class TheCyantianChronicles(_CommonMulti):
    baseUrl = 'https://cyantian.net/'

    def __init__(self, name, path, first, sid, eol=False):
        self.stripUrl = self.baseUrl + f'%s/?sid={sid}'
        super().__init__('TheCyantianChronicles/' + name, path, first, eol)

    @classmethod
    def getmodules(cls):
        return (
            cls('Akaelae', 'akaelae', '05182003', 15043, eol=True),
            cls('Artwork', 'art-gallery', '07162003', 15102),
            cls('CampusSafari', 'original-campus-safari', '10012000', 13804, eol=True),
            cls('CampusSafariReboot', 'campus-safari', 'campus-safari-chapter-0', 13790),
            cls('CesileesDiary', 'cesilees-diary', '12062001-2', 16726, eol=True),
            cls('Darius', 'darius', '03102010', 14353, eol=True),
            cls('DracoVulpes', 'draco-vulpes', 'draco-vulpes', 13788),
            cls('GenoworksSaga', 'genoworks-saga', '07012004', 13794),
            cls('GralenCraggHall', 'kiet', '07152002', 13798, eol=True),
            cls('Kiet', 'kiet-2', 'kiet-c01', 14351),
            cls('NoAngel', 'no-angel', '08112001', 16644, eol=True),
            cls('RandomRamblings', 'gallery', 'cookie-war', 13801),
            cls('SinkOrSwim', 'sink-or-swim', '05112001', 13796, eol=True),
            cls('VincentAndFilaire', 'vincent-and-filaire', 'vincent-and-filaire', 13792),
        )


class Shivae(WordPressSpliced):
    url = 'https://shivae.net/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '2002-02-27'


class ShivaeComics(_CommonMulti):
    baseUrl = 'https://shivae.net/'

    def __init__(self, name, path, first, sid, eol=False):
        self.stripUrl = self.baseUrl + f'comic/%s/?sid={sid}'
        super().__init__('Shivae/' + name, path, first, eol)

    @classmethod
    def getmodules(cls):
        return (
            cls('Pure', 'pure-2', '2002-02-27', 1328, eol=True),
            cls('SerinFairyHunter', 'pure', 'character-serin', 1289),
            cls('SivineBlades', 'sivine-blades', '2002-06-30', 1326, eol=True),
        )

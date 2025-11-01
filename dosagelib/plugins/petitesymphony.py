# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from .. import util
from .common import WordPressNavi, WordPressScraper


class PetiteSymphony(WordPressNavi):
    multipleImagesPerStrip = True
    help = 'Index format: named number'

    def __init__(self, name):
        super(PetiteSymphony, self).__init__('PetiteSymphony/' +
                                             name.capitalize())
        self.url = 'http://%s.petitesymphony.com/' % name
        self.stripUrl = self.url + 'comic/%s'

    @classmethod
    def getmodules(cls):
        return (
            cls('knuckleup'),
            cls('sangria'),
        )


class ComicsBreak(WordPressScraper):
    def __init__(self, name, archive=None, adult=False):
        super(ComicsBreak, self).__init__('ComicsBreak/' + name)
        self.url = 'http://%s.comicsbreak.com/' % name.lower()
        if archive:
            self.url = 'https://web.archive.org/web/{}/{}'.format(
                archive, self.url)
            self.endOfLife = True
        if adult:
            self.adult = adult

    def namer(self, image_url, page_url):
        if self.name == 'ComicsBreak/Djandora':
            # Fix inconsistent filenames
            filename = util.urlpathsplit(image_url)[-1]
            filename = filename.replace('2014-10-31-Page70', 'Page70')
            filename = filename.replace('a3p69eng', 'Page69')
            if '2015/08/a4p57eng' in image_url:
                filename = filename.replace('p57', 'p56')
            return filename
        else:
            return super().namer(image_url, page_url)

    @classmethod
    def getmodules(cls):
        return (
            cls('Djandora', archive='20170923062433'),
            cls('Generation17', adult=True),
        )

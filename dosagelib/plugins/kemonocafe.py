# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from .. import scraper, util


class KemonoCafe(scraper.ParserScraper):
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[contains(@class, "comic-nav-previous")]'

    def __init__(self, name, sub, first, last=None, adult=False):
        super(KemonoCafe, self).__init__('KemonoCafe/' + name)

        self.url = 'https://%s.kemono.cafe/' % sub
        self.stripUrl = self.url + 'comic/%s/'
        self.firstStripUrl = self.stripUrl % first

        if last:
            self.url = self.stripUrl % last
            self.endOfLife = True

        if adult:
            self.adult = True

    def namer(self, image_url, page_url):
        # Strip date from filenames
        filename = util.urlpathsplit(image_url)[-1]
        if 'ultrarosa' not in page_url:
            if filename[4] == '-' and filename[7] == '-':
                filename = filename[10:]
            if filename[0] == '-' or filename[0] == '_':
                filename = filename[1:]
        # Fix duplicate filenames
        if 'paprika' in page_url and '69-2' in page_url:
            filename = filename.replace('69', '69-2')
        elif 'rascals' in page_url and '89-2' in page_url:
            filename = filename.replace('89', '90')
        elif 'rascals' in page_url and '133-2' in page_url:
            filename = filename.replace('133', '134')
        elif 'caughtinorbit' in page_url and '26gs' in filename:
            filename = filename.replace('026gs', '021')
        elif 'caughtinorbit' in page_url and '27gs' in filename:
            filename = filename.replace('027gs', '022')
        # Fix unordered filenames
        if 'addictivescience' in page_url:
            page = self.getPage(page_url)
            num = int(self.match(page, '//div[@id="comic-wrap"]/@class')[0].replace('comic-id-', ''))
            filename = '%04d_%s' % (num, filename)
        elif 'CaughtInOrbit' in filename:
            filename = filename.replace('CaughtInOrbit', 'CIO')
        return filename

    @classmethod
    def getmodules(cls):
        return (
            cls('AddictiveScience', 'addictivescience', 'page0001'),
            cls('Bethellium', 'bethellium', 'c01p00'),
            cls('CaribbeanBlue', 'cb', 'page000', last='page325'),
            cls('CaughtInOrbit', 'caughtinorbit', 'comic-cover'),
            cls('IMew', 'imew', 'imew00', last='imew50'),
            cls('Knighthood', 'knighthood', 'kh0001'),
            cls('KnuckleUp', 'knuckle-up', 'page001', adult=True),
            cls('LasLindas', 'laslindas', 'll0001', adult=True),
            cls('Paprika', 'paprika', 'page000'),
            cls('PracticeMakesPerfect', 'pmp', 'title-001'),
            cls('Rascals', 'rascals', 'rascals-pg-0', adult=True),
            cls('TheEyeOfRamalach', 'theeye', 'theeye-page01'),
            cls('TinaOfTheSouth', 'tots', 'tos-01-01'),
            cls('UltraRosa', 'ultrarosa', 'pg001'),
        )

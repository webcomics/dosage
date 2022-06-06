# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Tobias Gruetzmacher
from .common import WordPressScraper


class KrisStraub(WordPressScraper):
    prevSearch = '//a[text()="Previous"]'
    endOfLife = True
    help = 'Index format: yyyymmdd'

    def __init__(self, name, firstDate):
        super().__init__(name)
        self.url = 'https://{}.krisstraub.com/'.format(name.lower())
        self.stripUrl = self.url + '%s.shtml'
        self.firstStripUrl = self.stripUrl % firstDate

    @classmethod
    def getmodules(cls):
        return (
            cls('BroodHollow', '20121006'),
            cls('ChainsawSuit', '20080810'),
            cls('Starslip', '20050523'),
        )

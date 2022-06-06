# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from ..helpers import bounceStarter
from ..scraper import ParserScraper


class DMFA(ParserScraper):
    url = 'http://www.missmab.com/'
    stripUrl = url + 'Comics/%s.php'
    imageSearch = '//center//img'
    prevSearch = '//a[./img[contains(@src, "comicprev")]]'
    nextSearch = '//a[./img[contains(@src, "comicnext")]]'
    starter = bounceStarter

    def __init__(self, name, first, last=None):
        if name == 'DMFA':
            super(DMFA, self).__init__(name)
        else:
            super(DMFA, self).__init__('DMFA/' + name)

        self.firstStripUrl = self.stripUrl % first

        if last:
            self.url = self.stripUrl % last
            self.starter = super(DMFA, self).starter
            self.endOfLife = True

    @classmethod
    def getmodules(cls):
        return (
            cls('AbelsStory', 'Abel_01', last='Ab_106'),
            cls('AprilFools', 'Vol_Fools001', last='Vol_Foolslast'),
            cls('Bonus', 'Vol_Bonus001', last='Vol_Bonuslast'),
            cls('Christmas', 'HJ_01', last='HJ_06'),
            cls('DMFA', 'Vol_001'),
            cls('Guest', 'Vol_Guest001', last='Vol_Guestlast'),
            cls('Matilda', 'Ma_001', last='Ma_060'),
            cls('PerfectDate', 'PD_01', last='PD_18'),
            cls('TakePride', 'P_01', last='P_08'),
            cls('Valentines', 'Vol_VDay001', last='Vol_VDaylast'),
        )

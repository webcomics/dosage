# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from .common import WordPressScraper, WordPressWebcomic


class YAFGC(WordPressScraper):
    baseUrl = 'https://www.yafgc.net/'
    url = baseUrl + '?latest'
    stripUrl = baseUrl + 'comic/%s'
    firstStripUrl = stripUrl % 'bob-meets-gren'

    def __init__(self, name):
        super().__init__(name)
        self.session.add_throttle('www.yafgc.net', 3.0, 15.5)


class YoshSaga(WordPressWebcomic):
    url = 'https://www.yoshsaga.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'introduction'

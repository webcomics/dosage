# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from .common import _WordPressScraper, _WPWebcomic


class YAFGC(_WordPressScraper):
    url = 'http://yafgc.net/'


class YoshSaga(_WPWebcomic):
    url = 'https://www.yoshsaga.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % 'introduction'

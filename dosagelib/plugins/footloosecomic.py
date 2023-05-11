# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
from ..scraper import ParserScraper


class Footloose(ParserScraper):
    url = 'http://footloosecomic.com/footloose.php'
    imageSearch = '//body/p[1]//img'
    prevSearch = '//body/a[2]'


class Cherry(Footloose):
    url = 'http://footloosecomic.com/cherry/index.php'


class Desigaspring(Footloose):
    url = 'http://footloosecomic.com/dspring/index.php'

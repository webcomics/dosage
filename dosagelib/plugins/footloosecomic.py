# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..scraper import _ParserScraper

class Footloose(_ParserScraper):
    url = 'http://footloosecomic.com/footloose.php'
    imageSearch='//body/p[1]//img'
    prevSearch='//body/a[2]'

class Cherry(Footloose):
    url = 'http://footloosecomic.com/cherry/index.php'

class Desigaspring(Footloose):
    url = 'http://footloosecomic.com/dspring/index.php'


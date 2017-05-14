# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import re

from dosagelib import scraper


class TestComicNames(object):

    def test_names(self):
        for scraperobj in scraper.get_scrapers():
            name = scraperobj.name
            assert name.count('/') <= 1
            if '/' in name:
                comicname = name.split('/')[1]
            else:
                comicname = name
            assert re.sub("[^0-9a-zA-Z_]", "", comicname) == comicname

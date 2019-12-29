# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import re

from dosagelib import scraper
from dosagelib.plugins import old


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

    def test_renamed(self):
        for scraperobj in scraper.get_scrapers(include_removed=True):
            if not isinstance(scraperobj, old.Renamed):
                continue
            assert len(scraperobj.getDisabledReasons()) > 0
            # Renamed scraper should only point to an non-disabled scraper
            newscraper = scraper.find_scrapers(scraperobj.newname)[0]
            assert len(newscraper.getDisabledReasons()) == 0

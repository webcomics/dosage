# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import pytest
from dosagelib import scraper


class TestScraper(object):
    """Test scraper module functions."""

    def test_get_scrapers(self):
        for scraperobj in scraper.get_scrapers():
            scraperobj.indexes = ["bla"]
            assert scraperobj.url, "missing url in %s" % scraperobj.name

    def test_find_scrapers_single(self):
        result = scraper.find_scrapers("xkcd")
        assert len(result) == 1

    def test_find_scrapers_multi(self):
        result = scraper.find_scrapers("a", multiple_allowed=True)
        assert len(result) > 1

    def test_find_scrapers_error(self):
        with pytest.raises(ValueError):
            scraper.find_scrapers("")

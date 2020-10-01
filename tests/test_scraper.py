# SPDX-License-Identifier: MIT
# Copyright (C) 2013-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
import pytest
from dosagelib.scraper import scrapers


class TestScraper(object):
    """Test scraper module functions."""

    def test_get_scrapers(self):
        for scraperobj in scrapers.get():
            scraperobj.indexes = ["bla"]
            assert scraperobj.url, "missing url in %s" % scraperobj.name

    def test_find_scrapers_single(self):
        result = scrapers.find("xkcd")
        assert len(result) == 1

    def test_find_scrapers_multi(self):
        result = scrapers.find("a", multiple_allowed=True)
        assert len(result) > 1

    def test_find_scrapers_error(self):
        with pytest.raises(ValueError, match='empty comic name'):
            scrapers.find('')

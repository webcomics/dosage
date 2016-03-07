# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

import pytest
from dosagelib import scraper


class TestScraper(object):
    """Test scraper module functions."""

    def test_get_scraperclasses(self):
        for scraperclass in scraper.get_scraperclasses():
            scraperobj = scraperclass()
            scraperobj = scraperclass(indexes=["bla"])
            assert scraperobj.url, "missing url in %s" % scraperobj.getName()

    def test_find_scraperclasses_single(self):
        result = scraper.find_scraperclasses("xkcd")
        assert len(result) == 1

    def test_find_scraperclasses_multi(self):
        result = scraper.find_scraperclasses("a", multiple_allowed=True)
        assert len(result) > 1

    def test_find_scraperclasses_error(self):
        with pytest.raises(ValueError):
            scraper.find_scraperclasses("")

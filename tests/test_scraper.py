# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2013 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
from pathlib import Path

import pytest

from dosagelib.scraper import scrapers


class TestScraper:
    """Test scraper module functions."""

    def test_get_scrapers(self):
        for scraperobj in scrapers.all():
            scraperobj.indexes = ["bla"]
            assert scraperobj.url, f"missing url in {scraperobj.name}"

    def test_find_scrapers_single(self):
        assert scrapers.find("xkcd")

    def test_find_scrapers_multi(self):
        with pytest.raises(ValueError, match='multiple comics found'):
            scrapers.find("a")

    def test_find_scrapers_error(self):
        with pytest.raises(ValueError, match='empty comic name'):
            scrapers.find('')

    def test_user_dir(self):
        oldlen = len(scrapers.all())
        scrapers.adddir(Path(__file__).parent / 'mocks' / 'extra')
        assert len(scrapers.all()) == oldlen + 1
        assert scrapers.find('AnotherDummyTestScraper')

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2013 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
from pathlib import Path

import pytest

from dosagelib.scraper import scrapers


def test_get_scrapers():
    for scraperobj in scrapers.all():
        scraperobj.indexes = ["bla"]
        assert scraperobj.url, "missing url in %s" % scraperobj.name


def test_find_scrapers_single():
    assert scrapers.find("xkcd")


def test_find_scrapers_multi():
    with pytest.raises(ValueError, match='multiple comics found'):
        scrapers.find("a")


def test_find_scrapers_error():
    with pytest.raises(ValueError, match='empty comic name'):
        scrapers.find('')


def test_user_dir():
    oldlen = len(scrapers.all())
    scrapers.adddir(Path(__file__).parent / 'mocks' / 'extra')
    assert len(scrapers.all()) == oldlen + 1
    assert scrapers.find('AnotherDummyTestScraper')

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import re
from operator import attrgetter

import pytest

from dosagelib.plugins import old
from dosagelib.scraper import scrapers


def test_names():
    for scraperobj in scrapers.all():
        name = scraperobj.name
        assert name.count('/') <= 1
        if '/' in name:
            comicname = name.split('/')[1]
        else:
            comicname = name
        assert re.sub("[^0-9a-zA-Z_]", "", comicname) == comicname


@pytest.mark.parametrize(('scraperobj'),
    [obj for obj in scrapers.all(include_removed=True)
        if isinstance(obj, old.Renamed)], ids=attrgetter('name'))
def test_renamed(scraperobj):
    assert len(scraperobj.getDisabledReasons()) > 0
    # Renamed scraper should only point to an non-disabled scraper
    newscraper = scrapers.find(scraperobj.newname)
    assert len(newscraper.getDisabledReasons()) == 0

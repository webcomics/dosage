# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
import re
from operator import attrgetter

import pytest

from dosagelib.scraper import scrapers
from dosagelib.plugins import old


class TestComicNames:

    def test_names(self):
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
    def test_renamed(self, scraperobj):
        assert len(scraperobj.getDisabledReasons()) > 0
        # Renamed scraper should only point to an non-disabled scraper
        newscraper = scrapers.find(scraperobj.newname)
        assert len(newscraper.getDisabledReasons()) == 0

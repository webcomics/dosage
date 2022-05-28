# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
import re
import os

import pytest
from xdist.dsession import LoadScopeScheduling

from dosagelib.scraper import scrapers


def get_test_scrapers():
    """Return scrapers that should be tested."""
    if 'TESTALL' in os.environ:
        # test all comics (this will take some time)
        return scrapers.get()
    elif 'TESTCOMICS' in os.environ:
        scraper_pattern = os.environ['TESTCOMICS']
    else:
        # Get limited number of scraper tests as default
        testscrapernames = [
            # "classic" _BasicScraper
            'AbstruseGoose',
            # complex _ParserScraper
            'GoComics/CalvinAndHobbes',
            # _WordPressScraper
            'GrrlPower',
        ]
        scraper_pattern = '^(' + '|'.join(testscrapernames) + ')$'

    matcher = re.compile(scraper_pattern)
    return [
        scraperobj for scraperobj in scrapers.get()
        if matcher.match(scraperobj.name)
    ]


def pytest_generate_tests(metafunc):
    if 'scraperobj' in metafunc.fixturenames:
        scrapers = get_test_scrapers()
        scraperids = [x.name for x in scrapers]
        metafunc.parametrize('scraperobj', scrapers, ids=scraperids)


class LoadModScheduling(LoadScopeScheduling):
    """Implement load scheduling for comic modules. See xdist for details."""

    def _split_scope(self, nodeid):
        mod, test = nodeid.split("::", 1)
        return mod + "::" + test.split("/", 1)[0]


@pytest.mark.trylast()
def pytest_xdist_make_scheduler(config, log):
    return LoadModScheduling(config, log)

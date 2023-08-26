# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import re
import os
from operator import attrgetter

import pytest
from xdist.dsession import LoadScopeScheduling

from dosagelib.scraper import scrapers


def get_test_scrapers():
    """Return scrapers that should be tested."""
    if 'TESTALL' in os.environ:
        # test all comics (this will take some time)
        # Ignore known-broken (and never-to-be-fixed) modules
        scraper_pattern = '^(?!Schuelert)'
    elif 'TESTCOMICS' in os.environ:
        scraper_pattern = os.environ['TESTCOMICS']
    else:
        # Get limited number of scraper tests as default
        testscrapernames = [
            # "classic" BasicScraper
            'AbstruseGoose',
            # complex ParserScraper
            'GoComics/CalvinAndHobbes',
            # WordPressScraper
            'GrrlPower',
        ]
        scraper_pattern = '^(' + '|'.join(testscrapernames) + ')$'

    matcher = re.compile(scraper_pattern)
    return [
        scraperobj for scraperobj in scrapers.all()
        if matcher.match(scraperobj.name)
    ]


def pytest_generate_tests(metafunc):
    if 'scraperobj' in metafunc.fixturenames:
        scrapers = sorted(get_test_scrapers(), key=attrgetter('name'))
        metafunc.parametrize('scraperobj', scrapers, ids=attrgetter('name'))


class LoadModScheduling(LoadScopeScheduling):
    """Implement load scheduling for comic modules. See xdist for details."""

    def _split_scope(self, nodeid):
        mod, test = nodeid.split("::", 1)
        return mod + "::" + test.split("/", 1)[0]


@pytest.hookimpl(trylast=True)
def pytest_xdist_make_scheduler(config, log):
    return LoadModScheduling(config, log)

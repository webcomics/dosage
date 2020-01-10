# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import re
import operator
import os

import pytest
from xdist.dsession import LoadScopeScheduling

from dosagelib import scraper


def get_test_scrapers():
    """Return scrapers that should be tested."""
    if "TESTALL" in os.environ:
        # test all comics (this will take some time)
        scrapers = scraper.get_scrapers()
    else:
        if 'TESTCOMICS' in os.environ:
            scraper_pattern = re.compile(os.environ['TESTCOMICS'])
        else:
            # Get limited number of scraper tests on Travis builds to make it
            # faster
            testscrapernames = [
                # "classic" _BasicScraper
                'AbstruseGoose',
                # complex _ParserScraper
                'GoComics/CalvinAndHobbes',
                # _WordPressScraper
                'GrrlPower'
            ]
            scraper_pattern = re.compile('^(' + '|'.join(testscrapernames) +
                                         ')$')

        scrapers = [
            scraperobj for scraperobj in scraper.get_scrapers()
            if scraper_pattern.match(scraperobj.name)
        ]
    return scrapers


def pytest_generate_tests(metafunc):
    if 'scraperobj' in metafunc.fixturenames:
        scrapers = get_test_scrapers()
        scraperids = list(x.name for x in scrapers)
        metafunc.parametrize('scraperobj', scrapers, ids=scraperids)


class LoadModScheduling(LoadScopeScheduling):
    """Implement load scheduling for comic modules. See xdist for details."""

    def _split_scope(self, nodeid):
        mod, test = nodeid.split("::", 1)
        return mod + "::" + test.split("/", 1)[0]


@pytest.mark.trylast
def pytest_xdist_make_scheduler(config, log):
    return LoadModScheduling(config, log)

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2014-2016 Tobias Gruetzmacher

import re
import operator
import os

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
                    'AbstruseGoose',
                    'GoComics/CalvinAndHobbes',
                    'xkcd'
            ]
            scraper_pattern = re.compile('|'.join(testscrapernames))

        scrapers = [
            scraperobj for scraperobj in scraper.get_scrapers()
            if scraper_pattern.match(scraperobj.name)
        ]
    return scrapers


def pytest_generate_tests(metafunc):
    if 'scraperobj' in metafunc.fixturenames:
        metafunc.parametrize('scraperobj', get_test_scrapers(),
                             ids=operator.attrgetter('name'))

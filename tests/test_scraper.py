# -*- coding: iso-8859-1 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
# Copyright (C) 2015 Tobias Gruetzmacher
from unittest import TestCase
from dosagelib import scraper


class ScraperTester(TestCase):
    """Test scraper module functions."""

    def test_get_scraperclasses(self):
        for scraperclass in scraper.get_scraperclasses():
            scraperobj = scraperclass()
            scraperobj = scraperclass(indexes=["bla"])
            self.assertTrue(scraperobj.url,
                "missing url in %s" % scraperobj.getName())

    def test_find_scraperclasses_single(self):
        result = scraper.find_scraperclasses("xkcd")
        self.assertEqual(len(result), 1)

    def test_find_scraperclasses_multi(self):
        result = scraper.find_scraperclasses("a", multiple_allowed=True)
        self.assertTrue(len(result) > 1)

    def test_find_scraperclasses_error(self):
        self.assertRaises(ValueError, scraper.find_scraperclasses, "")

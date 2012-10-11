# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import tempfile
import shutil
from itertools import islice
from unittest import TestCase
from dosagelib import scraper


class _ComicTester(TestCase):
    """Basic comic test class."""
    scraperclass=None

    def setUp(self):
        self.name = self.scraperclass.get_name()

    def test_comic(self):
        # Test a scraper. It must be able to traverse backward for
        # at least 5 pages from the start, and find strip images
        # on at least 4 pages.
        scraperobj = self.scraperclass()
        num = empty = 0
        for strip in islice(scraperobj.getAllStrips(), 0, 5):
            images = 0
            for image in strip.getImages():
                images += 1
                self.save(image)
            if not images:
                empty += 1
            num += 1
        self.check(num >= 4, 'traversal failed after %d strips.' % num)
        self.check(empty <= 1, 'failed to find images on %d pages.' % empty)

    def save(self, image):
        # create a temporary directory
        tmpdir = tempfile.mkdtemp()
        try:
            image.save(tmpdir)
        except Exception, msg:
            self.check(False, 'could not save to %s: %s' % (tmpdir, msg))
        finally:
            shutil.rmtree(tmpdir)

    def check(self, condition, msg):
        self.assertTrue(condition, "%s: %s" % (self.name, msg))


def generate_comic_testers():
    """For each comic scraper, create a test class."""
    # Limit number of scraper tests for now
    max_scrapers = 10
    for scraperclass in islice(scraper.get_scrapers(), 0, max_scrapers):
        name = 'Test'+scraperclass.__name__
        globals()[name] = type(name,
            (_ComicTester,),
            dict(scraperclass=scraperclass)
        )

generate_comic_testers()

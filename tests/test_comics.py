# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import tempfile
import shutil
import re
from itertools import islice
from unittest import TestCase
from dosagelib import scraper


class _ComicTester(TestCase):
    """Basic comic test class."""
    scraperclass=None

    def setUp(self):
        self.name = self.scraperclass.get_name()
        self.url = self.scraperclass.starter()

    def test_comic(self):
        # Test a scraper. It must be able to traverse backward for
        # at least 5 strips from the start, and find strip images
        # on at least 4 pages.
        scraperobj = self.scraperclass()
        num = empty = 0
        for strip in islice(scraperobj.getAllStrips(), 0, 5):
            images = 0
            for image in strip.getImages():
                images += 1
                self.save(image)
            if num > 0:
                self.check_stripurl(strip)
            else:
                empty += 1
            num += 1
        if self.scraperclass.prevSearch:
            self.check(num >= 4, 'traversal failed after %d strips, check the prevSearch pattern.' % num)
        self.check(empty <= 1, 'failed to find images on %d pages, check the imageSearch pattern.' % empty)

    def check_stripurl(self, strip):
        if not self.scraperclass.stripUrl:
            # no indexing support
            return
        # test that the stripUrl regex matches the retrieved strip URL
        urlmatch = re.escape(self.scraperclass.stripUrl)
        urlmatch = urlmatch.replace(r"\%s", r".+")
        urlmatch = "^%s$" % urlmatch
        ro = re.compile(urlmatch)
        mo = ro.search(strip.stripUrl)
        self.check(mo is not None, 'strip URL %r does not match stripUrl pattern %s' % (strip.stripUrl, urlmatch))

    def save(self, image):
        # create a temporary directory
        tmpdir = tempfile.mkdtemp()
        try:
            image.save(tmpdir)
        except Exception as msg:
            self.check(False, 'could not save %s to %s: %s' % (image.url, tmpdir, msg))
        finally:
            shutil.rmtree(tmpdir)

    def check(self, condition, msg):
        self.assertTrue(condition, "%s %s %s" % (self.name, self.url, msg))


def generate_comic_testers():
    """For each comic scraper, create a test class."""
    # Limit number of scraper tests for now
    max_scrapers = 100
    for scraperclass in islice(scraper.get_scrapers(), 0, max_scrapers):
        name = 'Test'+scraperclass.__name__
        globals()[name] = type(name,
            (_ComicTester,),
            dict(scraperclass=scraperclass)
        )

generate_comic_testers()

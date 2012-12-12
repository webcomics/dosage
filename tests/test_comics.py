# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import tempfile
import shutil
import re
import os
from itertools import islice
from unittest import TestCase
from dosagelib import scraper


class _ComicTester(TestCase):
    """Basic comic test class."""
    scraperclass=None

    def setUp(self):
        self.name = self.scraperclass.get_name()
        self.url = self.scraperclass.starter()
        # create a temporary directory for images
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def get_saved_images(self):
        """Get saved images."""
        dirs = tuple(self.name.split('/'))
        return os.listdir(os.path.join(self.tmpdir, *dirs))

    def test_comic(self):
        # Test a scraper. It must be able to traverse backward for
        # at least 5 strips from the start, and find strip images
        # on at least 4 pages.
        scraperobj = self.scraperclass()
        num = 0
        max_strips = 5
        for strip in islice(scraperobj.getAllStrips(), 0, max_strips):
            images = []
            for image in strip.getImages():
                images.append(image.url)
                self.save(image)
            self.check(images, 'failed to find images at %s' % strip.stripUrl)
            if not self.scraperclass.multipleImagesPerStrip:
                self.check(len(images) == 1, 'found more than 1 image at %s: %s' % (strip.stripUrl, images))
            if num > 0 and self.scraperclass.prevUrlMatchesStripUrl:
                self.check_stripurl(strip)
            num += 1
        if self.scraperclass.prevSearch:
            self.check(num >= 4, 'traversal failed after %d strips, check the prevSearch pattern at %s.' % (num, strip.stripUrl))
            # Check that exactly or for multiple pages at least 5 images are saved.
            # This is different than the image number check above since it checks saved files,
            # ie. it detects duplicate filenames.
            saved_images = self.get_saved_images()
            num_images = len(saved_images)
            attrs = (num_images, saved_images, max_strips, self.tmpdir)
            if self.scraperclass.multipleImagesPerStrip:
                self.check(num_images >= max_strips, 'saved %d %s instead of at least %d images in %s' % attrs)
            else:
                self.check(num_images == max_strips, 'saved %d %s instead of %d images in %s' % attrs)

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
        try:
            image.save(self.tmpdir)
        except Exception as msg:
            self.check(False, 'could not save %s to %s: %s' % (image.url, self.tmpdir, msg))

    def check(self, condition, msg):
        self.assertTrue(condition, "%s %s %s" % (self.name, self.url, msg))


def make_comic_tester(name, **kwargs):
    """Create and return a _ComicTester class with given name and attributes."""
    return type(name, (_ComicTester,), kwargs)


def generate_comic_testers():
    """For each comic scraper, create a test class."""
    g = globals()
    # optional: limit number of scraper tests
    max_scrapers = 0
    if max_scrapers:
        scrapers = islice(scraper.get_scrapers(), 0, max_scrapers)
    else:
        scrapers = scraper.get_scrapers()
    for scraperclass in scrapers:
        name = 'Test'+scraperclass.__name__
        g[name] = make_comic_tester(name, scraperclass=scraperclass)


generate_comic_testers()

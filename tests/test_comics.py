# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
import tempfile
import shutil
import re
import os
import multiprocessing
try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit
from unittest import TestCase
from dosagelib import scraper


def get_host(url):
    """Get host part of URL."""
    return urlsplit(url)[1].lower()


# Dictionary with per-host locks.
_locks = {}
# Allowed number of connections per host
MaxConnections = 4

def get_lock(host):
    """Get bounded semphore for given host."""
    if host not in _locks:
        _locks[host] = multiprocessing.BoundedSemaphore(MaxConnections)
    return _locks[host]


class _ComicTester(TestCase):
    """Basic comic test class."""
    scraperclass=None

    def setUp(self):
        if self.scraperclass is not None:
            self.name = self.scraperclass.getName()
            self.url = self.scraperclass.starter()
            # create a temporary directory for images
            self.tmpdir = tempfile.mkdtemp()
        else:
            self.tmpdir = None

    def tearDown(self):
        if self.tmpdir is not None:
            shutil.rmtree(self.tmpdir)

    def get_saved_images(self, filtertxt=False):
        """Get saved images."""
        dirs = tuple(self.name.split('/'))
        files = os.listdir(os.path.join(self.tmpdir, *dirs))
        if filtertxt:
            files = [x for x in files if not x.endswith(".txt")]
        return files

    def test_comic(self):
        if self.scraperclass is None:
            # only run subclasses
            import pytest
            pytest.skip("base class")
        # Test a scraper. It must be able to traverse backward for
        # at least 5 strips from the start, and find strip images
        # on at least 4 pages.
        scraperobj = self.scraperclass()
        # Limit number of connections to one host.
        host = get_host(scraperobj.url)
        try:
            with get_lock(host):
                self._test_comic(scraperobj)
        except OSError:
            # interprocess lock not supported
            self._test_comic(scraperobj)

    def _test_comic(self, scraperobj):
        num_strips = 0
        max_strips = 5
        strip = None
        for strip in scraperobj.getStrips(max_strips):
            images = []
            for image in strip.getImages():
                images.append(image.url)
                self.save(image)
            self.check(images, 'failed to find images at %s' % strip.stripUrl)
            if not self.scraperclass.multipleImagesPerStrip:
                self.check(len(images) == 1, 'found more than 1 image at %s: %s' % (strip.stripUrl, images))
            if num_strips > 0 and self.scraperclass.prevUrlMatchesStripUrl:
                self.check_stripurl(strip)
            num_strips += 1
        if self.scraperclass.prevSearch and not scraperobj.hitFirstStripUrl:
            # check strips
            num_strips_expected = max_strips - len(scraperobj.skippedUrls)
            msg = 'Traversed %d strips instead of %d.' % (num_strips, num_strips_expected)
            if strip:
                msg += " Check the prevSearch pattern at %s" % strip.stripUrl
            self.check(num_strips == num_strips_expected, msg)
            # check images
            if strip:
                self.check_scraperesult(num_strips_expected, strip, scraperobj)

    def check_scraperesult(self, num_images_expected, strip, scraperobj):
        # Check that exactly or for multiple pages at least num_strips images are saved.
        # This checks saved files, ie. it detects duplicate filenames.
        saved_images = self.get_saved_images(filtertxt=bool(scraperobj.textSearch))
        num_images = len(saved_images)
        # subtract the number of skipped URLs with no image from the expected image number
        attrs = (num_images, saved_images, num_images_expected, self.tmpdir)
        if self.scraperclass.multipleImagesPerStrip:
            self.check(num_images >= num_images_expected, 'saved %d %s instead of at least %d images in %s' % attrs)
        else:
            self.check(num_images == num_images_expected, 'saved %d %s instead of %d images in %s' % attrs)

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
            self.check(False, 'could not save %s at %s to %s: %s' % (image.url, image.referrer, self.tmpdir, msg))

    def check(self, condition, msg):
        self.assertTrue(condition, "%s %s %s" % (self.name, self.url, msg))


def make_comic_tester(name, **kwargs):
    """Create and return a _ComicTester class with given name and attributes."""
    return type(name, (_ComicTester,), kwargs)


def generate_comic_testers():
    """For each comic scraper, create a test class."""
    g = globals()
    if "TESTALL" in os.environ:
        # test all comics (this will take some time)
        scraperclasses = scraper.get_scraperclasses()
    else:
        # Get limited number of scraper tests on Travis builds to make
        # it faster
        testscrapernames = ['GoComics/CalvinandHobbes']
        scraperclasses = [
            scraperclass for scraperclass in scraper.get_scraperclasses()
            if scraperclass.getName() in testscrapernames
        ]
    for scraperclass in scraperclasses:
        name = 'Test'+scraperclass.__name__
        g[name] = make_comic_tester(name, scraperclass=scraperclass)


generate_comic_testers()

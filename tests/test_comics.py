# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam
import tempfile
import shutil
import re
import os
import multiprocessing
import urlparse
from itertools import islice
from unittest import TestCase
from dosagelib import scraper


def get_host(url):
    """Get host part of URL."""
    return urlparse.urlsplit(url)[1].lower()


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
        self.name = self.scraperclass.getName()
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
        # Limit number of connections to one host.
        host = get_host(scraperobj.url)
        try:
            with get_lock(host):
                self._test_comic(scraperobj)
        except OSError:
            # interprocess lock not supported
            self._test_comic(scraperobj)

    def _test_comic(self, scraperobj):
        num = 0
        max_strips = 5
        for strip in scraperobj.getStrips(max_strips):
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
        if self.scraperclass.prevSearch and not scraperobj.hitFirstStripUrl:
            self.check(num >= 4, 'traversal failed after %d strips, check the prevSearch pattern at %s.' % (num, strip.stripUrl))
            # Check that exactly or for multiple pages at least 5 images are saved.
            # This is different than the image number check above since it checks saved files,
            # ie. it detects duplicate filenames.
            saved_images = self.get_saved_images()
            num_images = len(saved_images)
            # subtract the number of skipped URLs with no image from the expected image number
            num_images_expected = max_strips - len(scraperobj.skippedUrls)
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
    if "TRAVIS" in os.environ:
        # Get limited number of scraper tests on Travis builds.
        max_scrapers = 10
        scraperclasses = islice(scraper.get_scraperclasses(), 0, max_scrapers)
    else:
        scraperclasses = scraper.get_scraperclasses()
    for scraperclass in scraperclasses:
        name = 'Test'+scraperclass.__name__
        g[name] = make_comic_tester(name, scraperclass=scraperclass)


generate_comic_testers()

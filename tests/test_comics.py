# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015 Tobias Gruetzmacher
import tempfile
import shutil
import re
import os
import multiprocessing
import pytest
try:
    from urllib.parse import urlsplit
except ImportError:
    from urlparse import urlsplit
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

@pytest.yield_fixture
def tmpdir():
    tmpdir = tempfile.mkdtemp()
    yield tmpdir
    shutil.rmtree(tmpdir)

def get_saved_images(tmpdir, scraper, filtertxt=False):
    """Get saved images."""
    dirs = tuple(scraper.getName().split('/'))
    files = os.listdir(os.path.join(tmpdir, *dirs))
    if filtertxt:
        files = [x for x in files if not x.endswith(".txt")]
    return files

def test_comicmodule(tmpdir, scraperclass):
    # Test a scraper. It must be able to traverse backward for
    # at least 5 strips from the start, and find strip images
    # on at least 4 pages.
    scraperobj = scraperclass()
    # Limit number of connections to one host.
    host = get_host(scraperobj.url)
    try:
        with get_lock(host):
            _test_comic(tmpdir, scraperobj)
    except OSError:
        # interprocess lock not supported
        _test_comic(tmpdir, scraperobj)

def _test_comic(tmpdir, scraperobj):
    num_strips = 0
    max_strips = 5
    strip = None
    for strip in scraperobj.getStrips(max_strips):
        images = []
        for image in strip.getImages():
            images.append(image.url)
            image.save(tmpdir)
        assert images, 'failed to find images at %s' % strip.stripUrl
        if not scraperobj.multipleImagesPerStrip:
            assert len(images) == 1, 'found more than 1 image at %s: %s' % (strip.stripUrl, images)
        if num_strips > 0 and scraperobj.prevUrlMatchesStripUrl:
            check_stripurl(strip, scraperobj)
        num_strips += 1
    if scraperobj.prevSearch and not scraperobj.hitFirstStripUrl:
        # check strips
        num_strips_expected = max_strips - len(scraperobj.skippedUrls)
        msg = 'Traversed %d strips instead of %d.' % (num_strips, num_strips_expected)
        if strip:
            msg += " Check the prevSearch pattern at %s" % strip.stripUrl
        assert num_strips == num_strips_expected, msg
        # check images
        if strip:
            check_scraperesult(tmpdir, num_strips_expected, strip, scraperobj)

def check_scraperesult(tmpdir, num_images_expected, strip, scraperobj):
    # Check that exactly or for multiple pages at least num_strips images are saved.
    # This checks saved files, ie. it detects duplicate filenames.
    saved_images = get_saved_images(tmpdir, scraperobj, filtertxt=bool(scraperobj.textSearch))
    num_images = len(saved_images)
    # subtract the number of skipped URLs with no image from the expected image number
    attrs = (num_images, saved_images, num_images_expected, tmpdir)
    if scraperobj.multipleImagesPerStrip:
        assert num_images >= num_images_expected, 'saved %d %s instead of at least %d images in %s' % attrs
    else:
        assert num_images == num_images_expected, 'saved %d %s instead of %d images in %s' % attrs

def check_stripurl(strip, scraperobj):
    if not scraperobj.stripUrl:
        # no indexing support
        return
    # test that the stripUrl regex matches the retrieved strip URL
    urlmatch = re.escape(scraperobj.stripUrl)
    urlmatch = urlmatch.replace(r"\%s", r".+")
    urlmatch = "^%s$" % urlmatch
    ro = re.compile(urlmatch)
    mo = ro.search(strip.stripUrl)
    assert mo is not None, 'strip URL %r does not match stripUrl pattern %s' % (strip.stripUrl, urlmatch)

def get_test_scraperclasses():
    """Return scrapers that should be tested."""
    if "TESTALL" in os.environ:
        # test all comics (this will take some time)
        scraperclasses = scraper.get_scraperclasses()
    else:
        # Get limited number of scraper tests on Travis builds to make
        # it faster
        testscrapernames = ['AbstruseGoose', 'GoComics/CalvinandHobbes', 'xkcd']
        scraperclasses = [
            scraperclass for scraperclass in scraper.get_scraperclasses()
            if scraperclass.getName() in testscrapernames
        ]
    return scraperclasses

def pytest_generate_tests(metafunc):
    if 'scraperclass' in metafunc.fixturenames:
        metafunc.parametrize('scraperclass', get_test_scraperclasses())


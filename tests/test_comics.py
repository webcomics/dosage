# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

import re
import os
import operator
import multiprocessing
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
# Maximum number of strips to get to test a comic
MaxStrips = 5


def get_lock(host):
    """Get bounded semphore for given host."""
    if host not in _locks:
        _locks[host] = multiprocessing.BoundedSemaphore(MaxConnections)
    return _locks[host]


def _get_saved_images(outdir, scraperobj):
    """Get saved images."""
    dirs = tuple(scraperobj.name.split('/'))
    files = os.listdir(os.path.join(outdir, *dirs))
    files = [x for x in files if not x.endswith(".txt")]
    return files


def test_comicmodule(tmpdir, scraperobj):
    '''Test a scraper. It must be able to traverse backward for at least 5
    strips from the start, and find strip images on at least 4 pages.'''
    # Limit number of connections to one host.
    host = get_host(scraperobj.url)
    try:
        with get_lock(host):
            _test_comic(str(tmpdir), scraperobj)
    except OSError:
        # interprocess lock not supported
        _test_comic(str(tmpdir), scraperobj)


def _test_comic(outdir, scraperobj):
    num_strips = 0
    strip = None
    for strip in scraperobj.getStrips(MaxStrips):
        _check_strip(outdir, strip, scraperobj.multipleImagesPerStrip)

        if num_strips > 0:
            _check_stripurl(strip, scraperobj)
        num_strips += 1

    if scraperobj.prevSearch and not scraperobj.hitFirstStripUrl:
        # subtract the number of skipped URLs with no image from the expected
        # image number
        num_strips_expected = MaxStrips - len(scraperobj.skippedUrls)
        msg = 'Traversed %d strips instead of %d.' % (num_strips,
                                                      num_strips_expected)
        if strip:
            msg += " Check the prevSearch pattern at %s" % strip.stripUrl
        assert num_strips == num_strips_expected, msg
        if strip:
            _check_scraperesult(outdir, num_strips_expected, strip, scraperobj)


def _check_strip(outdir, strip, multipleImagesPerStrip):
    '''Check that a specific page yields images and the comic module correctly
    declares if there are multiple images per page.'''
    images = []
    for image in strip.getImages():
        images.append(image.url)
        image.save(outdir)
    assert images, 'failed to find images at %s' % strip.stripUrl
    if not multipleImagesPerStrip:
        assert len(images) == 1, 'found more than 1 image at %s: %s' % (
                strip.stripUrl, images)


def _check_scraperesult(outdir, num_images_expected, strip, scraperobj):
    '''Check that exactly or for multiple pages at least num_strips images are
    saved. This checks saved files, ie. it detects duplicate filenames.'''
    saved_images = _get_saved_images(outdir, scraperobj)
    num_images = len(saved_images)

    attrs = (num_images, saved_images, num_images_expected, outdir)
    if scraperobj.multipleImagesPerStrip:
        err = 'saved %d %s instead of at least %d images in %s' % attrs
        assert num_images >= num_images_expected, err
    else:
        err = 'saved %d %s instead of %d images in %s' % attrs
        assert num_images == num_images_expected, err


def _check_stripurl(strip, scraperobj):
    if not scraperobj.stripUrl:
        # no indexing support
        return
    # test that the stripUrl regex matches the retrieved strip URL
    urlmatch = re.escape(scraperobj.stripUrl)
    urlmatch = urlmatch.replace(r"\%s", r".+")
    urlmatch = "^%s$" % urlmatch
    ro = re.compile(urlmatch)
    mo = ro.search(strip.stripUrl)
    err = 'strip URL %r does not match stripUrl pattern %s' % (
            strip.stripUrl, urlmatch)
    assert mo is not None, err


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

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import re
import multiprocessing
from six.moves.urllib.parse import urlsplit


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
    files = []
    for strip in scraperobj.getStrips(MaxStrips):
        files.append(_check_strip(outdir, strip,
                                  scraperobj.multipleImagesPerStrip))

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
            msg += " Check the prevSearch pattern at %s" % strip.strip_url
        assert num_strips == num_strips_expected, msg
        if strip:
            _check_scraperesult(files, num_strips_expected, strip, scraperobj)


def _check_strip(outdir, strip, multipleImagesPerStrip):
    '''Check that a specific page yields images and the comic module correctly
    declares if there are multiple images per page.'''
    images = []
    files = []
    for image in strip.getImages():
        images.append(image.url)

        # write a fake image (to download less)
        fakeimg = image._fnbase(outdir) + '.fake'
        with open(fakeimg, 'w') as f:
            f.write("fake image for testing")

        fn, _ = image.save(outdir)
        files.append(fn)
    assert images, 'failed to find images at %s' % strip.strip_url
    if not multipleImagesPerStrip:
        assert len(images) == 1, 'found more than 1 image at %s: %s' % (
                strip.strip_url, images)
    return files


def _check_scraperesult(saved_images, num_images_expected, strip, scraperobj):
    '''Check that exactly or for multiple pages at least num_strips images are
    saved. This checks saved files, ie. it detects duplicate filenames.'''
    num_images = len(saved_images)

    attrs = (num_images, saved_images, num_images_expected)
    if scraperobj.multipleImagesPerStrip:
        err = 'saved %d %s instead of at least %d images' % attrs
        assert num_images >= num_images_expected, err
    else:
        err = 'saved %d %s instead of %d images' % attrs
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
    mo = ro.search(strip.strip_url)
    err = 'strip URL %r does not match stripUrl pattern %s' % (
            strip.strip_url, urlmatch)
    assert mo is not None, err

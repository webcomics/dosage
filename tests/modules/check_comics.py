# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2021 Tobias Gruetzmacher
import json
import multiprocessing
import os
import re
import warnings
from urllib.parse import urlsplit


# Dictionary with per-host locks.
_locks = {}
# Allowed number of connections per host
MaxConnections = 2
# Maximum number of strips to get to test a comic
MaxStrips = 5
# Match (already-escaped) archive.org URL
ARCHIVE_ORG_MATCH = re.compile(r'(?<=web\\.archive\\.org/web)/\d+/')
# Matches some (maybe-escaped - because Python 2) printf-style format specifiers
PRINTF_MATCH = re.compile(r'\\?%[0-9]*[sd]')
# Classes where the modules are very similar, so that testing the history of
# each modules doesn't make much sense
standarized_modules = {
    'ComicSherpa',
    'ComicsKingdom',
    'GoComics',
    'MangaDex',
    'WebToons',
}
# Already seen classes
seen_modules = set()


def get_lock(host):
    """Get bounded semphore for given host."""
    if host not in _locks:
        _locks[host] = multiprocessing.BoundedSemaphore(MaxConnections)
    return _locks[host]


def test_comicmodule(tmpdir, scraperobj, worker_id):
    '''Test a scraper. It must be able to traverse backward for at least 5
    strips from the start, and find strip images on at least 4 pages.'''
    # Limit number of connections to one host.
    host = urlsplit(scraperobj.url).hostname
    with get_lock(host):
        maxstrips = MaxStrips
        parts = scraperobj.name.split('/', maxsplit=1)
        if len(parts) > 1 and parts[0] in standarized_modules:
            if parts[0] in seen_modules:
                maxstrips = 1
            else:
                seen_modules.add(parts[0])

        _test_comic(str(tmpdir), scraperobj, maxstrips)


def _test_comic(outdir, scraperobj, maxstrips):
    num_strips = 0
    strip = None
    files = []
    PROXYMAP.apply(scraperobj.name)
    for strip in scraperobj.getStrips(maxstrips):
        files.append(_check_strip(outdir, strip,
                                  scraperobj.multipleImagesPerStrip))

        if num_strips > 0:
            _check_stripurl(strip, scraperobj)
        num_strips += 1

    if scraperobj.prevSearch and not scraperobj.hitFirstStripUrl:
        # subtract the number of skipped URLs with no image from the expected
        # image number
        num_strips_expected = maxstrips - len(scraperobj.skippedUrls)
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
        assert len(images) == 1, 'found more than 1 image at {}: {}'.format(
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
    urlmatch = PRINTF_MATCH.sub('.+', urlmatch)
    urlmatch = ARCHIVE_ORG_MATCH.sub(r'/\\d+/', urlmatch)
    ro = re.compile(urlmatch)
    mo = ro.match(strip.strip_url)
    if not mo:
        warnings.warn('strip URL {!r} does not match stripUrl pattern {}'.format(
            strip.strip_url, urlmatch))


class ProxyConfig:
    """Loads proxy config from an environment variable and applies it for each test."""
    def __init__(self):
        self.config = {}
        if 'PROXYMAP' in os.environ:
            for regex, server in json.loads(os.environ['PROXYMAP']).items():
                self.config[re.compile(regex)] = server

    def apply(self, name):
        useserver = ''
        for regex, server in self.config.items():
            if regex.match(name):
                useserver = server
                break
        os.environ['http_proxy'] = useserver
        os.environ['https_proxy'] = useserver


# External proxy config to fetch some modules via proxies
PROXYMAP = ProxyConfig()

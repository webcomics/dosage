# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
from __future__ import annotations

import codecs
import contextlib
import glob
import logging
import os
from collections.abc import Iterator
from datetime import datetime

from rich import filesize

from .events import getHandler
from .util import getFilename, unquote, urlopen

logger = logging.getLogger(__name__)

# Maximum content size for images
MAX_IMAGE_BYTES = 1024 * 1024 * 20  # 20 MB
# RFC 1123 format, as preferred by RFC 2616
RFC_1123_DT_STR = "%a, %d %b %Y %H:%M:%S GMT"


class ComicStrip:
    """A list of comic image URLs."""

    def __init__(self, scraper, strip_url: str, image_urls: str, text=None) -> None:
        """Store the image URL list."""
        self.scraper = scraper
        self.strip_url = strip_url
        self.image_urls = image_urls
        self.text = text

    def getImages(self) -> Iterator[ComicImage]:
        """Get a list of image downloaders."""
        for image_url in self.image_urls:
            yield self.getDownloader(image_url)

    def getDownloader(self, url: str) -> ComicImage:
        """Get an image downloader."""
        filename = self.scraper.namer(url, self.strip_url)
        return ComicImage(self.scraper, url, self.strip_url, filename,
                          text=self.text)


class ComicImage:
    """A comic image downloader."""

    ChunkBytes = 1024 * 100  # 100KB

    def __init__(self, scraper, url, referrer, filename, text=None) -> None:
        """Set URL and filename."""
        self.scraper = scraper
        self.referrer = referrer
        self.url = url
        filename = getFilename(filename)
        self.filename, self.ext = os.path.splitext(filename)
        self.text = text

    def connect(self, lastchange=None):
        """Connect to host and get meta information."""
        headers = {}
        if lastchange:
            headers['If-Modified-Since'] = lastchange.strftime(RFC_1123_DT_STR)
        self.urlobj = urlopen(self.url, self.scraper.session,
                              referrer=self.referrer,
                              max_content_bytes=MAX_IMAGE_BYTES, stream=True,
                              headers=headers)
        if self.urlobj.status_code == 304:  # Not modified
            return
        content_type = unquote(self.urlobj.headers.get(
            'content-type', 'application/octet-stream'))
        content_type = content_type.split(';', 1)[0]
        if '/' in content_type:
            maintype, subtype = content_type.split('/', 1)
        else:
            maintype = content_type
            subtype = None
        if maintype != 'image' and content_type not in (
                'application/octet-stream', 'application/x-shockwave-flash'):
            raise OSError('content type {!r} is not an image at {}'.format(
                content_type, self.url))
        # Always use mime type for file extension if it is sane.
        if maintype == 'image':
            self.ext = '.' + subtype.replace('jpeg', 'jpg')
        self.contentLength = int(self.urlobj.headers.get('content-length', 0))
        logger.debug('... filename = %r, ext = %r, contentLength = %d', self.filename, self.ext, self.contentLength)

    def save(self, basepath):
        """Save comic URL to filename on disk."""
        fnbase = self._fnbase(basepath)
        exist = [x for x in glob.glob(fnbase + ".*") if not x.endswith(".txt")]
        logger.moreinfo("Get image URL %r", self.url)
        if len(exist) == 1:
            lastchange = os.path.getmtime(exist[0])
            self.connect(datetime.utcfromtimestamp(lastchange))
            if self.urlobj.status_code == 304:  # Not modified
                self._exist_err(exist[0])
                return exist[0], False
        else:
            self.connect()
        fn = fnbase + self.ext
        # compare with >= since content length could be the compressed size
        if os.path.isfile(fn) and os.path.getsize(fn) >= self.contentLength:
            self._exist_err(fn)
            return fn, False
        logger.debug('Writing comic to file %r...', fn)
        with self.fileout(fn) as f:
            for chunk in self.urlobj.iter_content(self.ChunkBytes):
                f.write(chunk)
        if self.text:
            fntext = fnbase + ".txt"
            logger.debug('Writing comic text to file %s...', fntext)
            with self.fileout(fntext, encoding='utf-8') as f:
                f.write(self.text)
        getHandler().comicDownloaded(self, fn)
        return fn, True

    @contextlib.contextmanager
    def fileout(self, filename, encoding=None):
        """Write content to given filename. Checks for zero-sized files.
        If encoding is given writes to a codec.open() file."""
        def getfp(filename, encoding):
            """Get open file object."""
            if encoding:
                return codecs.open(filename, 'w', encoding)
            return open(filename, 'wb')

        try:
            with getfp(filename, encoding) as fp:
                yield fp
                size = fp.tell()
        except Exception:
            if os.path.isfile(filename):
                os.remove(filename)
            raise
        else:
            logger.info("Saved %r (%s).", filename, filesize.decimal(size))

    def _exist_err(self, fn):
        logger.info('Skipping existing file %r.', fn)

    def _fnbase(self, basepath):
        '''Determine the target base name of this comic file and make sure the
        directory exists.'''
        comicdir = self.scraper.get_download_dir(basepath)
        if not os.path.isdir(comicdir):
            os.makedirs(comicdir)
        return os.path.join(comicdir, self.filename)

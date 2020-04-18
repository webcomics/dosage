# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
import os
import glob
import codecs
import contextlib
from datetime import datetime

from .output import out
from .util import unquote, getFilename, urlopen, strsize
from .events import getHandler


# Maximum content size for images
MaxImageBytes = 1024 * 1024 * 20  # 20 MB
# RFC 1123 format, as preferred by RFC 2616
RFC_1123_DT_STR = "%a, %d %b %Y %H:%M:%S GMT"


class ComicStrip(object):
    """A list of comic image URLs."""

    def __init__(self, scraper, strip_url, image_urls, text=None):
        """Store the image URL list."""
        self.scraper = scraper
        self.strip_url = strip_url
        self.image_urls = image_urls
        self.text = text

    def getImages(self):
        """Get a list of image downloaders."""
        for image_url in self.image_urls:
            yield self.getDownloader(image_url)

    def getDownloader(self, url):
        """Get an image downloader."""
        filename = self.scraper.namer(url, self.strip_url)
        if filename is None:
            filename = url.rsplit('/', 1)[1]
        return ComicImage(self.scraper, url, self.strip_url, filename,
                          text=self.text)


class ComicImage(object):
    """A comic image downloader."""

    ChunkBytes = 1024 * 100  # 100KB

    def __init__(self, scraper, url, referrer, filename, text=None):
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
                              max_content_bytes=MaxImageBytes, stream=True,
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
            raise IOError('content type %r is not an image at %s' % (
                content_type, self.url))
        # Always use mime type for file extension if it is sane.
        if maintype == 'image':
            self.ext = '.' + subtype.replace('jpeg', 'jpg')
        self.contentLength = int(self.urlobj.headers.get('content-length', 0))
        out.debug(u'... filename = %r, ext = %r, contentLength = %d' % (
            self.filename, self.ext, self.contentLength))

    def save(self, basepath):
        """Save comic URL to filename on disk."""
        fnbase = self._fnbase(basepath)
        exist = [x for x in glob.glob(fnbase + ".*") if not x.endswith(".txt")]
        out.info(u"Get image URL %s" % self.url, level=1)
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
        out.debug(u'Writing comic to file %s...' % fn)
        with self.fileout(fn) as f:
            for chunk in self.urlobj.iter_content(self.ChunkBytes):
                f.write(chunk)
        if self.text:
            fntext = fnbase + ".txt"
            out.debug(u'Writing comic text to file %s...' % fntext)
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
            out.info(u"Saved %s (%s)." % (filename, strsize(size)))

    def _exist_err(self, fn):
        out.info(u'Skipping existing file "%s".' % fn)

    def _fnbase(self, basepath):
        '''Determine the target base name of this comic file and make sure the
        directory exists.'''
        comicdir = self.scraper.get_download_dir(basepath)
        if not os.path.isdir(comicdir):
            os.makedirs(comicdir)
        return os.path.join(comicdir, self.filename)

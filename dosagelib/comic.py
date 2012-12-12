# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

import os
import rfc822
import time

from .output import out
from .util import getImageObject, normaliseURL, unquote, strsize, getDirname, getFilename
from .events import getHandler

class FetchComicError(IOError):
    """Exception for comic fetching errors."""
    pass

class ComicStrip(object):
    """A list of comic image URLs."""

    def __init__(self, name, stripUrl, imageUrls, namer):
        """Store the image URL list."""
        self.name = name
        self.stripUrl = stripUrl
        self.imageUrls = imageUrls
        self.namer = namer

    def getImages(self):
        """Get a list of image downloaders."""
        for imageUrl in self.imageUrls:
            yield self.getDownloader(normaliseURL(imageUrl))

    def getDownloader(self, url):
        """Get an image downloader."""
        filename = self.namer(url, self.stripUrl)
        if filename is None:
            filename = url.rsplit('/', 1)[1]
        dirname = getDirname(self.name)
        return ComicImage(self.name, url, self.stripUrl, dirname, filename)


class ComicImage(object):
    """A comic image downloader."""

    def __init__(self, name, url, referrer, dirname, filename):
        """Set URL and filename."""
        self.name = name
        self.referrer = referrer
        self.url = url
        self.dirname = dirname
        filename = getFilename(filename)
        self.filename, self.ext = os.path.splitext(filename)

    def connect(self):
        """Connect to host and get meta information."""
        try:
            self.urlobj = getImageObject(self.url, self.referrer)
        except IOError as msg:
            raise FetchComicError('Unable to retrieve URL.', self.url, msg)

        content_type = unquote(self.urlobj.headers.get('content-type'))
        content_type = content_type.split(';', 1)[0]
        if '/' in content_type:
            maintype, subtype = content_type.split('/', 1)
        else:
            maintype = content_type
            subtype = None
        if maintype != 'image' and content_type not in ('application/octet-stream', 'application/x-shockwave-flash'):
            raise FetchComicError('Content type %r is not an image.' % content_type, self.url)

        # Always use mime type for file extension if it is sane.
        if maintype == 'image':
            self.ext = '.' + subtype.replace('jpeg', 'jpg')
        self.contentLength = int(self.urlobj.headers.get('content-length', 0))
        self.lastModified = self.urlobj.headers.get('last-modified')
        out.debug('... filename = %r, ext = %r, contentLength = %d' % (self.filename, self.ext, self.contentLength))

    def touch(self, filename):
        """Set last modified date on filename."""
        if self.lastModified:
            tt = rfc822.parsedate(self.lastModified)
            if tt:
                mtime = time.mktime(tt)
                os.utime(filename, (mtime, mtime))

    def save(self, basepath):
        """Save comic URL to filename on disk."""
        self.connect()
        filename = "%s%s" % (self.filename, self.ext)
        comicSize = self.contentLength
        comicDir = os.path.join(basepath, self.dirname)
        if not os.path.isdir(comicDir):
            os.makedirs(comicDir)

        fn = os.path.join(comicDir, filename)
        if os.path.isfile(fn) and os.path.getsize(fn) >= comicSize:
            self.touch(fn)
            out.info('Skipping existing file "%s".' % fn)
            return fn, False

        try:
            out.debug('Writing comic to file %s...' % fn)
            with open(fn, 'wb') as comicOut:
                comicOut.write(self.urlobj.content)
            self.touch(fn)
        except Exception:
            if os.path.isfile(fn):
                os.remove(fn)
            raise
        else:
            size = strsize(os.path.getsize(fn))
            out.info("Saved %s (%s)." % (fn, size))
            getHandler().comicDownloaded(self.name, fn)

        return fn, True

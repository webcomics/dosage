# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

import os
import rfc822
import time

from .output import out
from .util import urlopen, normaliseURL, unquote, strsize
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
        return ComicImage(self.name, url, self.stripUrl, filename)


class ComicImage(object):
    """A comic image downloader."""

    def __init__(self, name, url, referrer, filename):
        """Set URL and filename."""
        self.name = name
        self.referrer = referrer
        self.url = url
        self.filename, self.ext = os.path.splitext(filename)
        self.filename = self.filename.replace(os.sep, '_')
        self.ext = self.ext.replace(os.sep, '_')

    def connect(self):
        """Connect to host and get meta information."""
        try:
            self.urlobj = urlopen(self.url, referrer=self.referrer)
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
        out.write('... filename = %r, ext = %r, contentLength = %d' % (self.filename, self.ext, self.contentLength), 2)

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
        comicDir = os.path.join(basepath, self.name.replace('/', os.sep))
        if not os.path.isdir(comicDir):
            os.makedirs(comicDir)

        fn = os.path.join(comicDir, filename)
        if os.path.isfile(fn) and os.path.getsize(fn) >= comicSize:
            self.touch(fn)
            out.write('Skipping existing file "%s".' % fn, 1)
            return fn, False

        try:
            out.write('Writing comic to file %s...' % fn, 3)
            with open(fn, 'wb') as comicOut:
                comicOut.write(self.urlobj.content)
            self.touch(fn)
        except Exception:
            if os.path.isfile(fn):
                os.remove(fn)
            raise
        else:
            size = strsize(os.path.getsize(fn))
            out.write("Saved %s (%s)." % (fn, size), 1)
            getHandler().comicDownloaded(self.name, fn)

        return fn, True

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam
import os

from .output import out
from .util import getImageObject, normaliseURL, unquote, strsize, getDirname, getFilename
from .events import getHandler

class ComicStrip(object):
    """A list of comic image URLs."""

    def __init__(self, name, stripUrl, imageUrls, namer, session):
        """Store the image URL list."""
        self.name = name
        self.stripUrl = stripUrl
        self.imageUrls = imageUrls
        self.namer = namer
        self.session = session

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
        return ComicImage(self.name, url, self.stripUrl, dirname, filename, self.session)


class ComicImage(object):
    """A comic image downloader."""

    ChunkBytes = 1024 * 100 # 100KB

    def __init__(self, name, url, referrer, dirname, filename, session):
        """Set URL and filename."""
        self.name = name
        self.referrer = referrer
        self.url = url
        self.dirname = dirname
        filename = getFilename(filename)
        self.filename, self.ext = os.path.splitext(filename)
        self.session = session

    def connect(self):
        """Connect to host and get meta information."""
        try:
            self.urlobj = getImageObject(self.url, self.referrer, self.session)
        except IOError as msg:
            raise IOError('error retrieving URL %s: %s' % (self.url, msg))
        content_type = unquote(self.urlobj.headers.get('content-type', 'application/octet-stream'))
        content_type = content_type.split(';', 1)[0]
        if '/' in content_type:
            maintype, subtype = content_type.split('/', 1)
        else:
            maintype = content_type
            subtype = None
        if maintype != 'image' and content_type not in ('application/octet-stream', 'application/x-shockwave-flash'):
            raise IOError('content type %r is not an image at %s' % (content_type, self.url))
        # Always use mime type for file extension if it is sane.
        if maintype == 'image':
            self.ext = '.' + subtype.replace('jpeg', 'jpg')
        self.contentLength = int(self.urlobj.headers.get('content-length', 0))
        out.debug('... filename = %r, ext = %r, contentLength = %d' % (self.filename, self.ext, self.contentLength))

    def save(self, basepath):
        """Save comic URL to filename on disk."""
        out.info("Get image URL %s" % self.url, level=1)
        self.connect()
        filename = "%s%s" % (self.filename, self.ext)
        comicDir = os.path.join(basepath, self.dirname)
        if not os.path.isdir(comicDir):
            os.makedirs(comicDir)
        fn = os.path.join(comicDir, filename)
        # compare with >= since content length could be the compressed size
        if os.path.isfile(fn) and os.path.getsize(fn) >= self.contentLength:
            out.info('Skipping existing file "%s".' % fn)
            return fn, False
        content = self.urlobj.content
        if not content:
            out.warn("Empty content from %s, try again..." % self.url)
            self.connect()
            content = self.urlobj.content
        try:
            out.debug('Writing comic to file %s...' % fn)
            with open(fn, 'wb') as comicOut:
                comicOut.write(content)
                comicOut.flush()
                os.fsync(comicOut.fileno())
            size = os.path.getsize(fn)
            if size == 0:
                raise OSError("empty file %s" % fn)
        except Exception:
            if os.path.isfile(fn):
                os.remove(fn)
            raise
        else:
            out.info("Saved %s (%s)." % (fn, strsize(size)))
            getHandler().comicDownloaded(self.name, fn)
        return fn, True

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
import os

from .output import out
from .util import getImageObject, normaliseURL, unquote, getDirname, getFilename, writeFile
from .events import getHandler

class ComicStrip(object):
    """A list of comic image URLs."""

    def __init__(self, name, stripUrl, imageUrls, namer, session, text=None):
        """Store the image URL list."""
        self.name = name
        self.stripUrl = stripUrl
        self.imageUrls = imageUrls
        self.namer = namer
        self.session = session
        self.text = text

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
        return ComicImage(self.name, url, self.stripUrl, dirname, filename, self.session, text=self.text)


class ComicImage(object):
    """A comic image downloader."""

    ChunkBytes = 1024 * 100 # 100KB

    def __init__(self, name, url, referrer, dirname, filename, session, text=None):
        """Set URL and filename."""
        self.name = name
        self.referrer = referrer
        self.url = url
        self.dirname = dirname
        filename = getFilename(filename)
        self.filename, self.ext = os.path.splitext(filename)
        self.session = session
        self.text = text

    def connect(self):
        """Connect to host and get meta information."""
        self.urlobj = getImageObject(self.url, self.referrer, self.session)
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
        out.debug(u'... filename = %r, ext = %r, contentLength = %d' % (self.filename, self.ext, self.contentLength))

    def save(self, basepath):
        """Save comic URL to filename on disk."""
        out.info(u"Get image URL %s" % self.url, level=1)
        self.connect()
        filename = "%s%s" % (self.filename, self.ext)
        comicDir = os.path.join(basepath, self.dirname)
        if not os.path.isdir(comicDir):
            os.makedirs(comicDir)
        fn = os.path.join(comicDir, filename)
        # compare with >= since content length could be the compressed size
        if os.path.isfile(fn) and os.path.getsize(fn) >= self.contentLength:
            out.info(u'Skipping existing file "%s".' % fn)
            return fn, False
        content = self.urlobj.content
        if not content:
            out.warn(u"Empty content from %s, try again..." % self.url)
            self.connect()
            content = self.urlobj.content
        out.debug(u'Writing comic to file %s...' % fn)
        writeFile(fn, content)
        if self.text:
            fntext = os.path.join(comicDir, "%s.txt" % self.filename)
            out.debug(u'Writing comic text to file %s...' % fntext)
            writeFile(fntext, self.text, encoding='utf-8')
        getHandler().comicDownloaded(self, fn, text=self.text)
        return fn, True

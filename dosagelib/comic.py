# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
import urllib2
import os
import locale
import rfc822
import time
import shutil
# XXX why is this done??
locale.setlocale(locale.LC_ALL, '')

from .output import out
from .util import urlopen, saneDataSize, normaliseURL
from .progress import progressBar, OperationComplete
from .events import handler

class FetchComicError(IOError): pass

class Comic(object):
    def __init__(self, moduleName, url, referrer=None, filename=None):
        self.moduleName = moduleName
        url = normaliseURL(url)
        out.write('Getting headers for %s...' % (url,), 2)
        try:
            self.urlobj = urlopen(url, referrer=referrer)
        except urllib2.HTTPError, he:
            raise FetchComicError, ('Unable to retrieve URL.', url, he.code)

        if self.urlobj.info().getmaintype() != 'image' and \
           self.urlobj.info().gettype() not in ('application/octet-stream', 'application/x-shockwave-flash'):
            raise FetchComicError, ('No suitable image found to retrieve.', url)

        self.filename, self.ext = os.path.splitext(url.split('/')[-1])
        self.filename = filename or self.filename
        self.filename = self.filename.replace(os.sep, '_')
        # Always use mime type for file extension if it is sane.
        if self.urlobj.info().getmaintype() == 'image':
            self.ext = '.' + self.urlobj.info().getsubtype()
        self.contentLength = int(self.urlobj.info().get('content-length', 0))
        self.lastModified = self.urlobj.info().get('last-modified')
        out.write('... filename = "%s", ext = "%s", contentLength = %d' % (self.filename, self.ext, self.contentLength), 2)

    def touch(self, filename):
        if self.lastModified:
            tt = rfc822.parsedate(self.lastModified)
            if tt:
                mtime = time.mktime(tt)
                os.utime(filename, (mtime, mtime))

    def save(self, basepath, showProgress=False):
        comicName, comicExt = self.filename, self.ext
        comicSize = self.contentLength
        comicDir = os.path.join(basepath, self.moduleName.replace('/', os.sep))
        if not os.path.isdir(comicDir):
            os.makedirs(comicDir)

        fn = os.path.join(comicDir, '%s%s' % (self.filename, self.ext))
        if os.path.isfile(fn) and os.path.getsize(fn) >= comicSize:
            self.urlobj.close()
            self.touch(fn)
            out.write('Skipping existing file "%s".' % (fn,), 1)
            return fn, False

        try:
            tmpFn = os.path.join(comicDir, '__%s%s' % (self.filename, self.ext))
            out.write('Writing comic to temporary file %s...' % (tmpFn,), 3)
            comicOut = file(tmpFn, 'wb')
            try:
                startTime = time.time()
                if showProgress:
                    def pollData():
                        data = self.urlobj.read(8192)
                        if not data:
                            raise OperationComplete
                        comicOut.write(data)
                        return len(data), self.contentLength
                    progressBar(pollData)
                else:
                    comicOut.write(self.urlobj.read())
                endTime = time.time()
            finally:
                comicOut.close()
            out.write('Copying temporary file (%s) to %s...' % (tmpFn, fn), 3)
            shutil.copy2(tmpFn, fn)
            self.touch(fn)

            size = os.path.getsize(fn)
            bytes = locale.format('%d', size, True)
            if endTime != startTime:
                speed = saneDataSize(size / (endTime - startTime))
            else:
                speed = '???'
            attrs = dict(fn=fn, bytes=bytes, speed=speed)
            out.write('Saved "%(fn)s" (%(bytes)s bytes, %(speed)s/sec).' % attrs, 1)
            handler.comicDownloaded(self.moduleName, fn)
            self.urlobj.close()
        finally:
            try:
                out.write('Removing temporary file %s...' % (tmpFn,), 3)
                os.remove(tmpFn)
            except:
                pass

        return fn, True

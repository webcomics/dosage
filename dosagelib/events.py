# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
import os
import time
import urllib
from . import rss, util, configuration

class EventHandler(object):
    """Base class for writing events to files. The currently defined events are
    start(), comicDownloaded() and end()."""

    def __init__(self, basepath, baseurl):
        """Initialize base path and url."""
        self.basepath = basepath
        self.baseurl = baseurl or self.getBaseUrl()

    def getBaseUrl(self):
        '''Return a file: URL that probably points to the basedir.

        This is used as a halfway sane default when the base URL is not
        provided; not perfect, but should work in most cases.'''
        components = util.splitpath(os.path.abspath(self.basepath))
        url = '/'.join([urllib.quote(component, '') for component in components])
        return 'file:///' + url + '/'

    def getUrlFromFilename(self, filename):
        """Construct URL from filename."""
        components = util.splitpath(util.getRelativePath(self.basepath, filename))
        url = '/'.join([urllib.quote(component, '') for component in components])
        return self.baseurl + url

    def start(self):
        """Emit a start event. Should be overridden in subclass."""
        pass

    def comicDownloaded(self, comic, filename):
        """Emit a comic downloaded event. Should be overridden in subclass."""
        pass

    def end(self):
        """Emit an end event. Should be overridden in subclass."""
        pass


class RSSEventHandler(EventHandler):
    """Output in RSS format."""

    def getFilename(self):
        """Return RSS filename."""
        return os.path.abspath(os.path.join(self.basepath, 'dailydose.rss'))

    def start(self):
        """Log start event."""
        today = time.time()
        yesterday = today - 86400
        today = time.localtime(today)
        yesterday = time.localtime(yesterday)

        link = configuration.Url

        self.rssfn = self.getFilename()

        if os.path.exists(self.rssfn):
            self.newfile = False
            self.rss = rss.parseFeed(self.rssfn, yesterday)
        else:
            self.newfile = True
            self.rss = rss.Feed('Daily Dosage', link, 'Comics for %s' % time.strftime('%Y/%m/%d', today))

    def comicDownloaded(self, comic, filename):
        """Write RSS entry for downloaded comic."""
        url = self.getUrlFromFilename(filename)
        args = (
            '%s - %s' % (comic, os.path.basename(filename)),
            url,
            '<a href="%s">View Comic</a>' % url,
            util.rfc822date(time.time())
        )

        if self.newfile:
            self.newfile = False
            self.rss.addItem(*args)
        else:
            self.rss.insertHead(*args)

    def end(self):
        """Write RSS data to file."""
        self.rss.write(self.rssfn)


class HtmlEventHandler(EventHandler):
    """Output in HTML format."""

    def fnFromDate(self, date):
        """Get filename from date."""
        fn = time.strftime('comics-%Y%m%d.html', date)
        fn = os.path.join(self.basepath, 'html', fn)
        fn = os.path.abspath(fn)
        return fn

    def start(self):
        """Start HTML output."""
        today = time.time()
        yesterday = today - 86400
        tomorrow = today + 86400
        today = time.localtime(today)
        yesterday = time.localtime(yesterday)
        tomorrow = time.localtime(tomorrow)

        fn = self.fnFromDate(today)
        assert not os.path.exists(fn), 'Comic page for today already exists!'

        d = os.path.dirname(fn)
        if not os.path.isdir(d):
            os.makedirs(d)

        yesterdayUrl = self.getUrlFromFilename(self.fnFromDate(yesterday))
        tomorrowUrl = self.getUrlFromFilename(self.fnFromDate(tomorrow))

        self.html = file(fn, 'w')
        self.html.write('''<html>
<head>
<title>Comics for %s</title>
</head>
<body>
<a href="%s">Previous Day</a> | <a href="%s">Next Day</a>
<ul>
''' % (time.strftime('%Y/%m/%d', today), yesterdayUrl, tomorrowUrl))

        self.lastComic = None

    def comicDownloaded(self, comic, filename):
        """Write HTML entry for downloaded comic."""
        if self.lastComic != comic:
            self.newComic(comic)
        url = self.getUrlFromFilename(filename)
        self.html.write('        <li><a href="%s">%s</a></li>\n' % (url, os.path.basename(filename)))

    def newComic(self, comic):
        """Start new comic list in HTML."""
        if self.lastComic is not None:
            self.html.write('    </ul>\n')
        self.lastComic = comic
        self.html.write('''    <li>%s</li>
    <ul>
''' % (comic,))

    def end(self):
        """End HTML output."""
        if self.lastComic is not None:
            self.html.write('    </ul>\n')
        self.html.write('''</ul>
</body>
</html>''')
        self.html.close()


handlers = {
    'html': HtmlEventHandler,
    'rss': RSSEventHandler,
}

def getHandlers():
    """Get sorted handler names."""
    return sorted(handlers.keys())

_handler = EventHandler(".", None)

def installHandler(name, basepath=None, baseurl=None):
    """Install a global handler with given name."""
    global _handler
    if basepath is None:
        basepath = '.'
    _handler = handlers[name](basepath, baseurl)

def getHandler():
    """Get installed event handler."""
    return _handler

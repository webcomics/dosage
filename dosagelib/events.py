# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
import os.path
import time
import rss
import urllib
import util

class EventHandler(object):
    def __init__(self, basepath, baseurl):
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
        components = util.splitpath(util.getRelativePath(self.basepath, filename))
        url = '/'.join([urllib.quote(component, '') for component in components])
        return self.baseurl + url

    def start(self):
        pass

    def comicDownloaded(self, comic, filename):
        pass

    def end(self):
        pass

class TextEventHandler(EventHandler):
    pass

class RSSEventHandler(EventHandler):
    def RFC822Date(self, indate):
        return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(indate))

    def getFilename(self):
        return os.path.abspath(os.path.join(self.basepath, 'dailydose.rss'))

    def start(self):
        today = time.time()
        yesterday = today - 86400
        today = time.localtime(today)
        yesterday = time.localtime(yesterday)

        link = 'https://github.com/wummel/dosage'

        self.rssfn = self.getFilename()

        if os.path.exists(self.rssfn):
            self.newfile = False
            self.rss = rss.parseFeed(self.rssfn, yesterday)
        else:
            self.newfile = True
            self.rss = rss.Feed('Daily Dosage', link, 'Comics for %s' % time.strftime('%Y/%m/%d', today))

    def comicDownloaded(self, comic, filename):
        url = self.getUrlFromFilename(filename)
        args = (
            '%s - %s' % (comic, os.path.basename(filename)),
            url,
            '<a href="%s">View Comic</a>' % (url,),
            self.RFC822Date(time.time())
        )

        if self.newfile:
            self.newfile = False
            self.rss.addItem(*args)
        else:
            self.rss.insertHead(*args)

    def end(self):
        self.rss.write(self.rssfn)

class HtmlEventHandler(EventHandler):
    def fnFromDate(self, date):
        fn = time.strftime('comics-%Y%m%d.html', date)
        fn = os.path.join(self.basepath, 'html', fn)
        fn = os.path.abspath(fn)
        return fn

    def start(self):
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
        if self.lastComic != comic:
            self.newComic(comic)
        url = self.getUrlFromFilename(filename)
        self.html.write('        <li><a href="%s">%s</a></li>\n' % (url, os.path.basename(filename)))

    def newComic(self, comic):
        if self.lastComic is not None:
            self.html.write('    </ul>\n')
        self.lastComic = comic
        self.html.write('''    <li>%s</li>
    <ul>
''' % (comic,))

    def end(self):
        if self.lastComic is not None:
            self.html.write('    </ul>\n')
        self.html.write('''</ul>
</body>
</html>''')
        self.html.close()


handlers = {
    'text': TextEventHandler,
    'html': HtmlEventHandler,
    'rss': RSSEventHandler,
}

def getHandlers():
    l = handlers.keys()
    l.sort()
    return l

def installHandler(name=None, basepath=None, baseurl=None):
    global handler
    if name is None:
        name = 'text'
    if basepath is None:
        basepath = '.'
    handler = handlers[name](basepath, baseurl)

installHandler()

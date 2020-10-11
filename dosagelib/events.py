# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
import os
import time
from urllib.parse import quote as url_quote
import codecs
import json

import imagesize

from . import rss, util, configuration
from .output import out

# Maximum width or height to display an image in exported pages.
# Note that only the displayed size is adjusted, not the image itself.
MaxImageSize = (800, 800)


class EventHandler(object):
    """Base class for writing events to files. The currently defined events are
    start(), comicDownloaded() and end()."""

    def __init__(self, basepath, baseurl, allowdownscale):
        """Initialize base path and url."""
        self.basepath = basepath
        self.baseurl = baseurl or self.getBaseUrl()
        self.allowdownscale = allowdownscale

    def getBaseUrl(self):
        '''Return a file: URL that probably points to the basedir.

        This is used as a halfway sane default when the base URL is not
        provided; not perfect, but should work in most cases.'''
        components = util.splitpath(os.path.abspath(self.basepath))
        url = '/'.join([url_quote(component, '') for component in components])
        return 'file:///' + url + '/'

    def getUrlFromFilename(self, filename):
        """Construct URL from filename."""
        components = util.splitpath(util.getRelativePath(self.basepath, filename))
        url = '/'.join([url_quote(component, '') for component in components])
        return self.baseurl + url

    def start(self):
        """Emit a start event. Should be overridden in subclass."""
        pass

    def comicDownloaded(self, comic, filename):
        """Emit a comic downloaded event. Should be overridden in subclass.
        Parameters are:

        comic: The ComicImage class calling this event
        filename: The target filename
        """
        pass

    def comicPageLink(self, scraper, url, prevUrl):
        """Emit an event to inform the handler about links between comic pages.
        Should be overridden in subclass. Parameters are:

        scraper: The Scraper class calling this event
        url: The current page url
        prevUrl: The previous page url
        """
        pass

    def end(self):
        """Emit an end event. Should be overridden in subclass."""
        pass


class RSSEventHandler(EventHandler):
    """Output in RSS format."""

    name = 'rss'

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
            self.rss = rss.Feed('Daily Dosage', link,
                'Comics for %s' % time.strftime('%Y/%m/%d', today))

    def comicDownloaded(self, comic, filename):
        """Write RSS entry for downloaded comic."""
        imageUrl = self.getUrlFromFilename(filename)
        size = None
        if self.allowdownscale:
            size = getDimensionForImage(filename, MaxImageSize)
        title = '%s - %s' % (comic.scraper.name, os.path.basename(filename))
        pageUrl = comic.referrer
        description = '<img src="%s"' % imageUrl
        if size:
            description += ' width="%d" height="%d"' % size
        description += '/>'
        if comic.text:
            description += '<br/>%s' % comic.text
        description += '<br/><a href="%s">View Comic Online</a>' % pageUrl
        args = (
            title,
            imageUrl,
            description,
            util.rfc822date(time.time()),
        )

        if self.newfile:
            self.newfile = False
            self.rss.addItem(*args)
        else:
            self.rss.addItem(*args, append=False)

    def end(self):
        """Write RSS data to file."""
        self.rss.write(self.rssfn)


def getDimensionForImage(filename, maxsize):
    """Return scaled image size in (width, height) format.
    The scaling preserves the aspect ratio."""
    try:
        origsize = imagesize.get(filename)
    except Exception as e:
        out.warn("Could not get image size of {}: {}".format(os.path.basename(filename), e))
        return None

    width, height = origsize
    if width > maxsize[0]:
        height = max(round(height * maxsize[0] / width), 1)
        width = round(maxsize[0])
    if height > maxsize[1]:
        width = max(round(width * maxsize[1] / height), 1)
        height = round(maxsize[1])

    if width < origsize[0] or height < origsize[1]:
        out.info("Downscaled display size from %s to %s" % (origsize, (width, height)))
    return (width, height)


class HtmlEventHandler(EventHandler):
    """Output in HTML format."""

    name = 'html'
    encoding = 'utf-8'

    def fnFromDate(self, date):
        """Get filename from date."""
        fn = time.strftime('comics-%Y%m%d', date)
        fn = os.path.join(self.basepath, 'html', fn + ".html")
        return os.path.abspath(fn)

    def addNavLinks(self):
        if self.yesterdayUrl:
            self.html.write(u'<a href="%s">Previous Day</a> | ' % self.yesterdayUrl)
        self.html.write(u'<a href="%s">Next Day</a>\n' % self.tomorrowUrl)

    def start(self):
        """Start HTML output."""
        today = time.time()
        yesterday = today - 86400
        tomorrow = today + 86400
        today = time.localtime(today)
        yesterday = time.localtime(yesterday)
        tomorrow = time.localtime(tomorrow)

        fn = self.fnFromDate(today)
        if os.path.exists(fn):
            out.warn('HTML output file %r already exists' % fn)
            out.warn('the page link of previous run will skip this file')
            out.warn('try to generate HTML output only once per day')
            fn = util.getNonexistingFile(fn)

        d = os.path.dirname(fn)
        if not os.path.isdir(d):
            os.makedirs(d)

        try:
            fn_yesterday = self.fnFromDate(yesterday)
            fn_yesterday = util.getExistingFile(fn_yesterday)
            self.yesterdayUrl = self.getUrlFromFilename(fn_yesterday)
        except ValueError:
            self.yesterdayUrl = None
        self.tomorrowUrl = self.getUrlFromFilename(self.fnFromDate(tomorrow))

        self.html = codecs.open(fn, 'w', self.encoding)
        self.html.write(u'''<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=%s"/>
<meta name="generator" content="%s"/>
<title>Comics for %s</title>
</head>
<body>
''' % (self.encoding, configuration.App, time.strftime('%Y/%m/%d', today)))
        self.addNavLinks()
        self.html.write(u'<ul>\n')
        # last comic name (eg. CalvinAndHobbes)
        self.lastComic = None
        # last comic strip URL (eg. http://example.com/page42)
        self.lastUrl = None

    def comicDownloaded(self, comic, filename, text=None):
        """Write HTML entry for downloaded comic."""
        if self.lastComic != comic.scraper.name:
            self.newComic(comic)
        size = None
        if self.allowdownscale:
            size = getDimensionForImage(filename, MaxImageSize)
        imageUrl = self.getUrlFromFilename(filename)
        pageUrl = comic.referrer
        if pageUrl != self.lastUrl:
            self.html.write(u'<li><a href="%s">%s</a>\n' % (pageUrl, pageUrl))
        self.html.write(u'<br/><img src="%s"' % imageUrl)
        if size:
            self.html.write(' width="%d" height="%d"' % size)
        self.html.write('/>\n')
        if text:
            self.html.write(u'<br/>%s\n' % text)
        self.lastComic = comic.scraper.name
        self.lastUrl = pageUrl

    def newComic(self, comic):
        """Start new comic list in HTML."""
        if self.lastUrl is not None:
            self.html.write(u'</li>\n')
        if self.lastComic is not None:
            self.html.write(u'</ul>\n')
        self.html.write(u'<li>%s</li>\n' % comic.scraper.name)
        self.html.write(u'<ul>\n')

    def end(self):
        """End HTML output."""
        if self.lastUrl is not None:
            self.html.write(u'</li>\n')
        if self.lastComic is not None:
            self.html.write(u'</ul>\n')
        self.html.write(u'</ul>\n')
        self.addNavLinks()
        self.html.close()


class JSONEventHandler(EventHandler):
    """Output metadata for comics in JSON format."""

    name = 'json'
    encoding = 'utf-8'

    def start(self):
        """Start with empty data."""
        self.data = {}

    def jsonFn(self, scraper):
        """Get filename for the JSON file for a comic."""
        fn = os.path.join(scraper.get_download_dir(self.basepath), 'dosage.json')
        return os.path.abspath(fn)

    def getComicData(self, scraper):
        """Return dictionary with comic info."""
        if scraper not in self.data:
            if os.path.exists(self.jsonFn(scraper)):
                with codecs.open(self.jsonFn(scraper), 'r', self.encoding) as f:
                    self.data[scraper] = json.load(f)
            else:
                self.data[scraper] = {'pages': {}}
        return self.data[scraper]

    def getPageInfo(self, scraper, url):
        """Return dictionary with comic page info."""
        comicData = self.getComicData(scraper)
        if url not in comicData['pages']:
            comicData['pages'][url] = {'images': {}}
        return comicData['pages'][url]

    def comicDownloaded(self, comic, filename):
        """Add URL-to-filename mapping into JSON."""
        pageInfo = self.getPageInfo(comic.scraper, comic.referrer)

        # If there's already an image for this page start keeping track of their order
        if len(pageInfo['images'].keys()) == 1:
            pageInfo['imagesOrder'] = list(pageInfo['images'].keys())
        if 'imagesOrder' in pageInfo.keys():
            pageInfo['imagesOrder'].append(comic.url)

        pageInfo['images'][comic.url] = os.path.basename(filename)

    def comicPageLink(self, scraper, url, prevUrl):
        """Write previous link into JSON."""
        pageInfo = self.getPageInfo(scraper, url)
        pageInfo['prev'] = prevUrl

    def end(self):
        """Write all JSON data to files."""
        for scraper in self.data:
            with codecs.open(self.jsonFn(scraper), 'w', self.encoding) as f:
                json.dump(self.data[scraper], f, indent=2, separators=(',', ': '), sort_keys=True)


_handler_classes = {}


def addHandlerClass(clazz):
    """Register handler class."""
    if not issubclass(clazz, EventHandler):
        raise ValueError("%s must be subclassed from %s" % (clazz, EventHandler))
    _handler_classes[clazz.name] = clazz


addHandlerClass(HtmlEventHandler)
addHandlerClass(RSSEventHandler)
addHandlerClass(JSONEventHandler)


def getHandlerNames():
    """Get sorted handler names."""
    return sorted(_handler_classes.keys())


# FIXME: Hidden singleton :(
_handlers = []


def addHandler(name, basepath=None, baseurl=None, allowDownscale=False):
    """Add an event handler with given name."""
    if basepath is None:
        basepath = '.'
    _handlers.append(_handler_classes[name](basepath, baseurl, allowDownscale))


def clear_handlers():
    del _handlers[:]


class MultiHandler(object):
    """Encapsulate a list of handlers."""

    def start(self):
        """Emit start events for handlers."""
        for handler in _handlers:
            handler.start()

    def comicDownloaded(self, comic, filename):
        """Emit comic downloaded events for handlers."""
        for handler in _handlers:
            handler.comicDownloaded(comic, filename)

    def comicPageLink(self, scraper, url, prevUrl):
        """Emit an event to inform the handler about links between comic pages.
        Should be overridden in subclass."""
        for handler in _handlers:
            handler.comicPageLink(scraper, url, prevUrl)

    def end(self):
        """Emit end events for handlers."""
        for handler in _handlers:
            handler.end()


multihandler = MultiHandler()


def getHandler():
    """Get installed event handler."""
    return multihandler

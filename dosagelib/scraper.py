# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam
import requests
from . import loader
from .util import fetchUrl, fetchUrls, getPageContent
from .comic import ComicStrip
from .output import out


class _BasicScraper(object):
    '''Base class with scrape functions for comics.

    @type url: C{string}
    @cvar url: The URL for the comic strip.
    @type stripUrl: C{string}
    @cvar stripUrl: A string that is interpolated with the strip index
        to yield the URL for a particular strip.
    @type firstStripUrl: C{string} optional
    @cvar firstStripUrl: Stop searching for previous URLs at this URL.
        If not set and no previous URL is found a warning is printed.
    @type imageSearch: C{regex}
    @cvar imageSearch: A compiled regex that will locate the strip image URL
        when applied to the strip page.
    @type prevSearch: C{regex}
    @cvar prevSearch: A compiled regex that will locate the URL for the
        previous strip when applied to a strip page.
    '''

    # stop at this URL
    firstStripUrl = None

    # if more than one image per URL is expected
    multipleImagesPerStrip = False

    # set to False if previous URLs do not match the strip URL (ie. because of redirects)
    prevUrlMatchesStripUrl = True

    # set to True if this comic contains adult content
    adult = False

    # a description of the comic contents
    description = ''

    # usually the index format help
    help = ''

    # HTTP session storing cookies
    session = requests.session()

    def __init__(self, indexes=None):
        """Initialize internal variables."""
        self.urls = set()
        if indexes:
            self.indexes = tuple(indexes)
        else:
            self.indexes = tuple()

    def __cmp__(self, other):
        if not isinstance(other, _BasicScraper):
            return 1
        # first, order by name
        d = cmp(self.get_name(), other.get_name())
        if d != 0:
            return d
        # then by indexes
        return cmp(self.indexes, other.indexes)

    def __hash__(self):
        return hash((self.get_name(), self.indexes))

    def getCurrentStrips(self):
        """Get current comic strip."""
        msg = 'Retrieving the current strip'
        if self.indexes:
            msg += " for indexes %s" % self.indexes
        out.info(msg+"...")
        if self.indexes:
            for index in self.indexes:
                url = self.stripUrl % index
                yield self.getStrip(url)
        else:
            yield self.getStrip(self.getLatestUrl())

    def getStrip(self, url):
        """Get comic strip for given URL."""
        data, baseUrl = getPageContent(url, self.session)
        imageUrls = set(fetchUrls(url, data, baseUrl, self.imageSearch))
        if len(imageUrls) > 1 and not self.multipleImagesPerStrip:
            out.warn("found %d images instead of 1 with %s" % (len(imageUrls), self.imageSearch.pattern))
        return self.getComicStrip(url, imageUrls)

    def getComicStrip(self, url, imageUrls):
        """Get comic strip downloader for given URL and images."""
        return ComicStrip(self.get_name(), url, imageUrls, self.namer, self.session)

    def getAllStrips(self, maxstrips=None):
        """Get all comic strips."""
        if maxstrips:
            msg = 'Retrieving %d strips' % maxstrips
        else:
            msg = 'Retrieving all strips'
        if self.indexes:
            msg += " for indexes %s" % self.indexes
        if self.adult:
            msg += " (including adult content)"
        out.info(msg)
        if self.indexes:
            for index in self.indexes:
                url = self.stripUrl % index
                for strip in self.getStripsFor(url, maxstrips):
                    yield strip
        else:
            url = self.getLatestUrl()
            for strip in self.getStripsFor(url, maxstrips):
                yield strip

    def getStripsFor(self, url, maxstrips):
        """Get comic strips for an URL. If maxstrips is a positive number, stop after
        retrieving the given number of strips."""
        seen_urls = set()
        while url:
            data, baseUrl = getPageContent(url, self.session)
            imageUrls = set(fetchUrls(url, data, baseUrl, self.imageSearch))
            yield self.getComicStrip(url, imageUrls)
            if self.firstStripUrl == url:
                out.debug("Stop at first URL %s" % url)
                break
            prevUrl = None
            if self.prevSearch:
                try:
                    prevUrl = fetchUrl(url, data, baseUrl, self.prevSearch)
                except ValueError as msg:
                    # assume there is no previous URL, but print a warning
                    out.warn("%s Assuming no previous comic strips exist." % msg)
                else:
                    prevUrl = self.prevUrlModifier(prevUrl)
                    out.debug("Matched previous URL %s" % prevUrl)
            seen_urls.add(url)
            if prevUrl in seen_urls:
                # avoid recursive URL loops
                out.warn("Already seen previous URL %r" % prevUrl)
                break
            url = prevUrl
            if maxstrips is not None:
                maxstrips -= 1
                if maxstrips <= 0:
                    break

    def setStrip(self, index):
        """Set current comic strip URL."""
        self.currentUrl = self.stripUrl % index

    @classmethod
    def get_name(cls):
        """Get scraper name."""
        if hasattr(cls, 'name'):
            return cls.name
        return cls.__name__

    @classmethod
    def starter(cls):
        """Get starter URL from where to scrape comic strips."""
        return cls.url

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Return filename for given image and page URL."""
        return None

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        """Optional modification of parsed previous URLs. Useful if
        there are domain redirects. The default implementation does
        not modify the URL.
        """
        return prevUrl

    def getFilename(self, imageUrl, pageUrl):
        """Return filename for given image and page URL."""
        return self.namer(imageUrl, pageUrl)

    def getLatestUrl(self):
        """Get starter URL from where to scrape comic strips."""
        return self.starter()


def find_scraperclasses(comic, multiple_allowed=False):
    """Get a list comic scraper classes. Can return more than one entries if
    multiple_allowed is True, else it raises a ValueError if multiple
    modules match. The match is a case insensitive substring search."""
    if not comic:
        raise ValueError("empty comic name")
    candidates = []
    cname = comic.lower()
    for scraperclass in get_scraperclasses():
        lname = scraperclass.get_name().lower()
        if lname == cname:
            # perfect match
            if not multiple_allowed:
                return [scraperclass]
            else:
                candidates.append(scraperclass)
        elif cname in lname:
            candidates.append(scraperclass)
    if len(candidates) > 1 and not multiple_allowed:
        comics = ", ".join(x.get_name() for x in candidates)
        raise ValueError('multiple comics found: %s' % comics)
    elif not candidates:
        raise ValueError('comic %r not found' % comic)
    return candidates


_scraperclasses = None
def get_scraperclasses():
    """Find all comic scraper classes in the plugins directory.
    The result is cached.
    @return: list of _BasicScraper classes
    @rtype: list of _BasicScraper
    """
    global _scraperclasses
    if _scraperclasses is None:
        out.debug("Loading comic modules...")
        modules = loader.get_modules()
        plugins = loader.get_plugins(modules, _BasicScraper)
        _scraperclasses = list(plugins)
        _scraperclasses.sort(key=lambda s: s.get_name())
        check_scrapers()
        out.debug("... %d modules loaded." % len(_scraperclasses))
    return _scraperclasses


def check_scrapers():
    """Check for duplicate scraper class names."""
    d = {}
    for scraperclass in _scraperclasses:
        name = scraperclass.get_name().lower()
        if name in d:
            name1 = scraperclass.get_name()
            name2 = d[name].get_name()
            raise ValueError('duplicate scrapers %s and %s found' % (name1, name2))
        d[name] = scraperclass


def make_scraper(classname, **attributes):
    """Make a new scraper class with given name and attributes."""
    return type(classname, (_BasicScraper,), attributes)

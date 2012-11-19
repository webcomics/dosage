# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import os
from . import loader
from .util import fetchUrls
from .comic import ComicStrip
from .output import out

disabled = []
def init_disabled():
    filename = os.path.expanduser('~/.dosage/disabled')
    if os.path.isfile(filename):
        with open(filename) as f:
            for line in f:
                if line and not line.startswith('#'):
                    disabled.append(line.rstrip())
init_disabled()

class DisabledComicError(ValueError):
    pass


class _BasicScraper(object):
    '''Base class with scrape functions for comics.

    @type latestUrl: C{string}
    @cvar latestUrl: The URL for the latest comic strip.
    @type stripUrl: C{string}
    @cvar stripUrl: A string that is interpolated with the strip index
        to yield the URL for a particular strip.
    @type imageSearch: C{regex}
    @cvar imageSearch: A compiled regex that will locate the strip image URL
        when applied to the strip page.
    @type prevSearch: C{regex}
    @cvar prevSearch: A compiled regex that will locate the URL for the
        previous strip when applied to a strip page.
    '''
    help = 'Sorry, no help for this comic yet.'

    def __init__(self, indexes=None):
        """Initialize internal variables."""
        self.urls = set()
        self.indexes = indexes

    def getCurrentStrips(self):
        """Get current comic strip."""
        msg = 'Retrieving the current strip'
        if self.indexes:
            msg += " for indexes %s" % self.indexes
        out.write(msg+"...")
        if self.indexes:
            for index in self.indexes:
                url = self.stripUrl % index
                yield self.getStrip(url)
        else:
            yield self.getStrip(self.getLatestUrl())

    def getStrip(self, url):
        """Get comic strip for given URL."""
        imageUrls = fetchUrls(url, self.imageSearch)
        return self.getComicStrip(url, imageUrls)

    def getComicStrip(self, url, imageUrls):
        """Get comic strip downloader for given URL and images."""
        return ComicStrip(self.get_name(), url, imageUrls, self.namer)

    def getAllStrips(self):
        """Get all comic strips."""
        msg = 'Retrieving all strips'
        if self.indexes:
            msg += " for indexes %s" % self.indexes
        out.write(msg+"...")
        if self.indexes:
            for index in self.indexes:
                url = self.stripUrl % index
                for strip in self.getAllStripsFor(url):
                    yield strip
        else:
            url = self.getLatestUrl()
            for strip in self.getAllStripsFor(url):
                yield strip

    def getAllStripsFor(self, url):
        """Get all comic strips for an URL."""
        seen_urls = set()
        while url:
            imageUrls, prevUrl = fetchUrls(url, self.imageSearch, self.prevSearch)
            seen_urls.add(url)
            yield self.getComicStrip(url, imageUrls)
            # avoid recursive URL loops
            url = prevUrl if prevUrl not in seen_urls else None

    def setStrip(self, index):
        """Set current comic strip URL."""
        self.currentUrl = self.stripUrl % index

    def getHelp(self):
        """Return help text for this scraper."""
        return self.help

    @classmethod
    def get_name(cls):
        """Get scraper name."""
        if hasattr(cls, 'name'):
            return cls.name
        return cls.__name__

    @classmethod
    def starter(cls):
        """Get starter URL from where to scrape comic strips."""
        return cls.latestUrl

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Return filename for given image and page URL."""
        return None

    def getFilename(self, imageUrl, pageUrl):
        """Return filename for given image and page URL."""
        return self.namer(imageUrl, pageUrl)

    def getLatestUrl(self):
        """Get starter URL from where to scrape comic strips."""
        return self.starter()


def get_scraper(comic):
    """Returns a comic module object."""
    candidates = []
    cname = comic.lower()
    for scraperclass in get_scrapers():
        lname = scraperclass.get_name().lower()
        if lname == cname:
            # perfect match
            return scraperclass
        if cname in lname:
            candidates.append(scraperclass)
    if len(candidates) == 1:
        return candidates[0]
    elif candidates:
        comics = ", ".join(x.get_name() for x in candidates)
        raise ValueError('Multiple comics found: %s' % comics)
    else:
        raise ValueError('Comic %r not found' % comic)


_scrapers = None
def get_scrapers():
    """Find all comic scraper classes in the plugins directory.
    The result is cached.
    @return: list of _BasicScraper classes
    @rtype: list of _BasicScraper
    """
    global _scrapers
    if _scrapers is None:
        modules = loader.get_modules()
        plugins = loader.get_plugins(modules, _BasicScraper)
        _scrapers = list(plugins)
        _scrapers.sort(key=lambda s: s.get_name())
        check_scrapers()
    return _scrapers


def check_scrapers():
    """Check for duplicate scraper class names."""
    d = {}
    for scraperclass in _scrapers:
        name = scraperclass.get_name().lower()
        if name in d:
            name1 = scraperclass.get_name()
            name2 = d[name].get_name()
            raise ValueError('Duplicate scrapers %s and %s found' % (name1, name2))
        d[name] = scraperclass

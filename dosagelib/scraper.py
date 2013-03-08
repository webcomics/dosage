# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam
import requests
import time
from . import loader
from .util import fetchUrl, fetchUrls, getPageContent
from .comic import ComicStrip
from .output import out


class _BasicScraper(object):
    '''Base class with scrape functions for comics.'''

    # The URL for the comic strip
    url = None

    # A string that is interpolated with the strip index to yield the URL for a particular strip.
    stripUrl = None

    # Stop search for previous URLs at this URL
    firstStripUrl = None

    # if more than one image per URL is expected
    multipleImagesPerStrip = False

    # set to False if previous URLs do not match the strip URL (ie. because of redirects)
    prevUrlMatchesStripUrl = True

    # set to True if this comic contains adult content
    adult = False

    # a description of the comic contents
    description = ''

    # langauge of the comic (two-letter ISO 639-1 code)
    lang = 'en'

    # compiled regular expression that will locate the URL for the previous strip in a page
    prevSearch = None

    # compiled regular expression that will locate the strip image URLs strip in a page
    imageSearch = None

    # usually the index format help
    help = ''

    # wait time between downloading comic strips
    waitSeconds = 0

    # HTTP session storing cookies
    session = requests.session()

    def __init__(self, indexes=None):
        """Initialize internal variables."""
        self.urls = set()
        if indexes:
            self.indexes = tuple(sorted(indexes))
        else:
            self.indexes = tuple()
        self.skippedUrls = set()
        self.hitFirstStripUrl = False

    def __cmp__(self, other):
        """Compare scraper by name and index list."""
        if not isinstance(other, _BasicScraper):
            return 1
        # first, order by name
        d = cmp(self.getName(), other.getName())
        if d != 0:
            return d
        # then by indexes
        return cmp(self.indexes, other.indexes)

    def __hash__(self):
        """Get hash value from name and index list."""
        return hash((self.getName(), self.indexes))

    def shouldSkipUrl(self, url):
        """Determine if search for images in given URL should be skipped."""
        return False

    def getComicStrip(self, url, data, baseUrl):
        """Get comic strip downloader for given URL and data."""
        imageUrls = fetchUrls(url, data, baseUrl, self.imageSearch)
        imageUrls = set(map(self.imageUrlModifier, imageUrls))
        if len(imageUrls) > 1 and not self.multipleImagesPerStrip:
            out.warn("found %d images instead of 1 at %s with %s" % (len(imageUrls), url, self.imageSearch.pattern))
        elif not imageUrls:
            out.warn("found no images at %s with %s" % (url, self.imageSearch.pattern))
        return ComicStrip(self.getName(), url, imageUrls, self.namer, self.session)

    def getStrips(self, maxstrips=None):
        """Get comic strips."""
        if maxstrips:
            word = "strip" if maxstrips == 1 else "strips"
            msg = 'Retrieving %d %s' % (maxstrips, word)
        else:
            msg = 'Retrieving all strips'
        if self.indexes:
            if len(self.indexes) == 1:
                msg += " for index %s" % self.indexes[0]
            else:
                msg += " for indexes %s" % self.indexes
            urls = [self.getIndexStripUrl(index) for index in self.indexes]
        else:
            urls = [self.getLatestUrl()]
        if self.adult:
            msg += " (including adult content)"
        out.info(msg)
        for url in urls:
            for strip in self.getStripsFor(url, maxstrips):
                yield strip

    def getStripsFor(self, url, maxstrips):
        """Get comic strips for an URL. If maxstrips is a positive number, stop after
        retrieving the given number of strips."""
        self.hitFirstStripUrl = False
        seen_urls = set()
        while url:
            out.info('Get strip URL %s' % url, level=1)
            data, baseUrl = getPageContent(url, self.session)
            if self.shouldSkipUrl(url):
                out.info('Skipping URL %s' % url)
                self.skippedUrls.add(url)
            else:
                yield self.getComicStrip(url, data, baseUrl)
            if self.firstStripUrl == url:
                out.debug("Stop at first URL %s" % url)
                self.hitFirstStripUrl = True
                break
            if maxstrips is not None:
                maxstrips -= 1
                if maxstrips <= 0:
                    break
            prevUrl = self.getPrevUrl(url, data, baseUrl)
            seen_urls.add(url)
            if prevUrl in seen_urls:
                # avoid recursive URL loops
                out.warn("Already seen previous URL %r" % prevUrl)
                break
            url = prevUrl
            if url and self.waitSeconds:
                time.sleep(self.waitSeconds)

    def getPrevUrl(self, url, data, baseUrl):
        """Find previous URL."""
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
        return prevUrl

    def getIndexStripUrl(self, index):
        """Get comic strip URL from index."""
        return self.stripUrl % index

    @classmethod
    def getName(cls):
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

    @classmethod
    def imageUrlModifier(cls, imageUrl):
        """Optional modification of parsed image URLs. Useful if the URL
        needs to be fixed before usage. The default implementation does
        not modify the URL.
        """
        return imageUrl

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
        lname = scraperclass.getName().lower()
        if lname == cname:
            # perfect match
            if not multiple_allowed:
                return [scraperclass]
            else:
                candidates.append(scraperclass)
        elif cname in lname:
            candidates.append(scraperclass)
    if len(candidates) > 1 and not multiple_allowed:
        comics = ", ".join(x.getName() for x in candidates)
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
        check_scrapers()
        out.debug("... %d modules loaded." % len(_scraperclasses))
    return _scraperclasses


def check_scrapers():
    """Check for duplicate scraper class names."""
    d = {}
    for scraperclass in _scraperclasses:
        name = scraperclass.getName().lower()
        if name in d:
            name1 = scraperclass.getName()
            name2 = d[name].getName()
            raise ValueError('duplicate scrapers %s and %s found' % (name1, name2))
        d[name] = scraperclass


def make_scraper(classname, **attributes):
    """Make a new scraper class with given name and attributes."""
    return type(classname, (_BasicScraper,), attributes)

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import re
import urlparse

from .util import fetchUrl, getQueryParams
from .scraper import _BasicScraper

def queryNamer(paramName, usePageUrl=False):
    """Get name from URL query part."""
    @staticmethod
    def _namer(imageUrl, pageUrl):
        url = (imageUrl, pageUrl)[usePageUrl]
        return getQueryParams(url)[paramName][0]
    return _namer


def regexNamer(regex):
    """Get name from regular expression."""
    @staticmethod
    def _namer(imageUrl, pageUrl):
        return regex.search(imageUrl).group(1)
    return _namer


def constStarter(latestUrl):
    """Start from constant URL."""
    @staticmethod
    def _starter():
        return latestUrl
    return _starter


def bounceStarter(latestUrl, nextSearch):
    """Get start URL by "bouncing" back and forth one time."""
    @classmethod
    def _starter(cls):
        url = fetchUrl(latestUrl, cls.prevSearch)
        if url:
            url = fetchUrl(url, nextSearch)
        return url
    return _starter


def indirectStarter(baseUrl, latestSearch):
    """Get start URL by indirection."""
    @staticmethod
    def _starter():
        return fetchUrl(baseUrl, latestSearch)
    return _starter


class IndirectLatestMixin(object):
    '''
    Mixin for comics that link to the latest comic from a base page of
    some kind. This also supports comics which don't link to the last comic
    from the base page, but the beginning of the latest chapter or similiar
    schemes. It simulates going forward until it can't find a 'next' link as
    specified by the 'nextSearch' regex.

    @type baseUrl: C{string}
    @cvar baseUrl: the URL where the link to the latest comic is found.
    @type latestSearch C{regex}
    @cvar latestSearch: a compiled regex for finding the 'latest' URL.
    @type nextSearch C{regex}
    @cvar nextSearch: a compiled regex for finding the 'next' URL.
    '''

    __latestUrl = None

    def getLatestUrl(self):
        """Get latest comic URL."""
        if not self.__latestUrl:
            self.__latestUrl = fetchUrl(self.baseUrl, self.latestSearch)
            if hasattr(self, "nextSearch"):
                nextUrl = fetchUrl(self.__latestUrl, self.nextSearch)
                while nextUrl:
                    self.__latestUrl = nextUrl
                    nextUrl = fetchUrl(self.__latestUrl, self.nextSearch)
        return self.__latestUrl

    latestUrl = property(getLatestUrl)


class _PHPScraper(_BasicScraper):
    """
    Scraper for comics using phpComic/CUSP.

    This provides an easy way to define scrapers for webcomics using phpComic.
    """
    imageUrl = property(lambda self: self.basePath + 'daily.php?date=%s')
    imageSearch = property(lambda self: re.compile(r'<img alt=[^>]+ src="(%scomics/\d{6}\..+?)">' % (self.basePath,)))

    help = 'Index format: yymmdd'

    @classmethod
    def starter(cls):
        """Get starter URL."""
        return cls.basePath + cls.latestUrl

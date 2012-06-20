# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import re

from .util import fetchUrl, fetchManyUrls, getQueryParams
from .comic import Comic

class _BasicScraper(object):
    '''Base class with scrape functions for comics.

    @type latestUrl: C{string}
    @cvar latestUrl: The URL for the latest comic strip.
    @type imageUrl: C{string}
    @cvar imageUrl: A string that is interpolated with the strip index
        to yield the URL for a particular strip.
    @type imageSearch: C{regex}
    @cvar imageSearch: A compiled regex that will locate the strip image URL
        when applied to the strip page.
    @type prevSearch: C{regex}
    @cvar prevSearch: A compiled regex that will locate the URL for the
        previous strip when applied to a strip page.
    '''
    referrer = None
    help = 'Sorry, no help for this comic yet.'

    def __init__(self):
        self.currentUrl = None
        self.urls = set()

    def getReferrer(self, imageUrl, pageUrl):
        return self.referrer or pageUrl or self.getLatestUrl()

    def getComic(self, url, pageUrl):
        if not url:
            return None
        return Comic(self.get_name(), url, filename=self.getFilename(url, pageUrl), referrer=self.getReferrer(url, pageUrl))

    def getCurrentComics(self):
        self.currentUrl = self.getLatestUrl()
        comics = self.getNextComics()
        if not comics:
            raise ValueError("Could not find current comic.")
        return comics

    def getNextComics(self):
        comics = []
        while not comics and self.currentUrl and self.currentUrl not in self.urls:
            comicUrlGroups, prevUrl = fetchManyUrls(self.currentUrl, [self.imageSearch, self.prevSearch])

            if prevUrl:
                prevUrl = prevUrl[0]
            else:
                prevUrl = None

            for comicUrl in comicUrlGroups:
                comics.append(self.getComic(comicUrl, self.currentUrl))

            self.urls.update([self.currentUrl])
            self.currentUrl = (prevUrl, None)[prevUrl in self.urls]
        return comics

    def setStrip(self, index):
        self.currentUrl = self.imageUrl % index

    def getHelp(self):
        return self.help

    def __iter__(self):
        """Iterate through the strips, starting from the current one and going backward."""
        if not self.currentUrl:
            self.currentUrl = self.getLatestUrl()

        comics = True
        while comics:
            comics = self.getNextComics()
            if comics:
                yield comics

    @classmethod
    def get_name(cls):
        if hasattr(cls, 'name'):
            return cls.name
        return cls.__name__

    @classmethod
    def starter(cls):
        return cls.latestUrl

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return None

    def getFilename(self, imageUrl, pageUrl):
        return self.namer(imageUrl, pageUrl)

    def getLatestUrl(self):
        return self.starter()


def queryNamer(paramName, usePageUrl=False):
    @staticmethod
    def _namer(imageUrl, pageUrl):
        url = (imageUrl, pageUrl)[usePageUrl]
        return getQueryParams(url)[paramName][0]
    return _namer


def regexNamer(regex):
    @staticmethod
    def _namer(imageUrl, pageUrl):
        return regex.search(imageUrl).group(1)
    return _namer


def constStarter(latestUrl):
    @staticmethod
    def _starter():
        return latestUrl
    return _starter


def bounceStarter(latestUrl, nextSearch):
    @classmethod
    def _starter(cls):
        url = fetchUrl(latestUrl, cls.prevSearch)
        if url:
            url = fetchUrl(url, nextSearch)
        return url
    return _starter


def indirectStarter(baseUrl, latestSearch):
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
    I implement IScraper for comics using phpComic/CUSP.

    This provides an easy way to define scrapers for webcomics using phpComic.
    """
    imageUrl = property(lambda self: self.basePath + 'daily.php?date=%s')
    imageSearch = property(lambda self: re.compile(r'<img alt=[^>]+ src="(%scomics/\d{6}\..+?)">' % (self.basePath,)))

    help = 'Index format: yymmdd'

    @classmethod
    def starter(cls):
        return cls.basePath + cls.latestUrl

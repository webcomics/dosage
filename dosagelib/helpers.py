# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from .util import fetchUrl, getQueryParams

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
        mo = regex.search(imageUrl)
        if mo:
            return mo.group(1)
    return _namer


def bounceStarter(latestUrl, nextSearch):
    """Get start URL by "bouncing" back and forth one time."""
    @classmethod
    def _starter(cls):
        url = fetchUrl(latestUrl, cls.prevSearch)
        if not url:
            raise ValueError("could not find prevSearch pattern %r in %s" % (cls.prevSearch.pattern, latestUrl))
        url = fetchUrl(url, nextSearch)
        if not url:
            raise ValueError("could not find nextSearch pattern %r in %s" % (nextSearch.pattern, latestUrl))
        return url
    return _starter


def indirectStarter(baseUrl, latestSearch):
    """Get start URL by indirection."""
    @staticmethod
    def _starter():
        url = fetchUrl(baseUrl, latestSearch)
        if not url:
            raise ValueError("could not find latestSearch pattern %r in %s" % (latestSearch.pattern, baseUrl))
        return url
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


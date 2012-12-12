# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from .util import fetchUrl, getQueryParams

def queryNamer(paramName, usePageUrl=False):
    """Get name from URL query part."""
    @classmethod
    def _namer(cls, imageUrl, pageUrl):
        """Get URL query part."""
        url = (imageUrl, pageUrl)[usePageUrl]
        return getQueryParams(url)[paramName][0]
    return _namer


def regexNamer(regex):
    """Get name from regular expression."""
    @classmethod
    def _namer(cls, imageUrl, pageUrl):
        """Get first regular expression group."""
        mo = regex.search(imageUrl)
        if mo:
            return mo.group(1)
    return _namer


def bounceStarter(latestUrl, nextSearch):
    """Get start URL by "bouncing" back and forth one time."""
    @classmethod
    def _starter(cls):
        """Get bounced start URL."""
        url = fetchUrl(latestUrl, cls.prevSearch, session=cls.session)
        if not url:
            raise ValueError("could not find prevSearch pattern %r in %s" % (cls.prevSearch.pattern, latestUrl))
        url2 = fetchUrl(url, nextSearch, session=cls.session)
        if not url2:
            raise ValueError("could not find nextSearch pattern %r in %s" % (nextSearch.pattern, url))
        return url2
    return _starter


def indirectStarter(baseUrl, latestSearch):
    """Get start URL by indirection."""
    @classmethod
    def _starter(cls):
        """Get indirect start URL."""
        url = fetchUrl(baseUrl, latestSearch, session=cls.session)
        if not url:
            raise ValueError("could not find latestSearch pattern %r in %s" % (latestSearch.pattern, baseUrl))
        return url
    return _starter


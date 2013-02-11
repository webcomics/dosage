# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam
from .util import fetchUrl, getPageContent, getQueryParams

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


def bounceStarter(url, nextSearch):
    """Get start URL by "bouncing" back and forth one time."""
    @classmethod
    def _starter(cls):
        """Get bounced start URL."""
        data, baseUrl = getPageContent(url, session=cls.session)
        url1 = fetchUrl(url, data, baseUrl, cls.prevSearch)
        data, baseUrl = getPageContent(url1, session=cls.session)
        return fetchUrl(url1, data, baseUrl, nextSearch)
    return _starter


def indirectStarter(url, latestSearch):
    """Get start URL by indirection."""
    @classmethod
    def _starter(cls):
        """Get indirect start URL."""
        data, baseUrl = getPageContent(url, session=cls.session)
        return fetchUrl(url, data, baseUrl, latestSearch)
    return _starter

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
from .util import getQueryParams

def queryNamer(paramName, usePageUrl=False):
    """Get name from URL query part."""
    @classmethod
    def _namer(cls, imageUrl, pageUrl):
        """Get URL query part."""
        url = pageUrl if usePageUrl else imageUrl
        return getQueryParams(url)[paramName][0]
    return _namer


def regexNamer(regex, usePageUrl=False):
    """Get name from regular expression."""
    @classmethod
    def _namer(cls, imageUrl, pageUrl):
        """Get first regular expression group."""
        url = pageUrl if usePageUrl else imageUrl
        mo = regex.search(url)
        if mo:
            return mo.group(1)
    return _namer


def bounceStarter(url, nextSearch):
    """Get start URL by "bouncing" back and forth one time."""
    @classmethod
    def _starter(cls):
        """Get bounced start URL."""
        data = cls.getPage(url)
        url1 = cls.fetchUrl(url, data, cls.prevSearch)
        data = cls.getPage(url1)
        return cls.fetchUrl(url1, data, nextSearch)
    return _starter


def indirectStarter(url, latestSearch):
    """Get start URL by indirection."""
    @classmethod
    def _starter(cls):
        """Get indirect start URL."""
        data = cls.getPage(url)
        return cls.fetchUrl(url, data, latestSearch)
    return _starter

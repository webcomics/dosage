# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

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


def bounceStarter():
    """Get start URL by "bouncing" back and forth one time.

    This needs the url and nextSearch properties be defined on the class.
    """
    @classmethod
    def _starter(cls):
        """Get bounced start URL."""
        data = cls.getPage(cls.url)
        url1 = cls.fetchUrl(cls.url, data, cls.prevSearch)
        data = cls.getPage(url1)
        return cls.fetchUrl(url1, data, cls.nextSearch)
    return _starter


def indirectStarter():
    """Get start URL by indirection.

    This is useful for comics where the latest comic can't be reached at a
    stable URL. If the class has an attribute 'startUrl', this page is fetched
    first, otherwise the page at 'url' is fetched. After that, the attribute
    'latestSearch' is used on the page content to find the latest strip."""
    @classmethod
    def _starter(cls):
        """Get indirect start URL."""
        url = cls.startUrl if hasattr(cls, "startUrl") else cls.url
        data = cls.getPage(url)
        return cls.fetchUrl(url, data, cls.latestSearch)
    return _starter

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from .util import getQueryParams


def queryNamer(param, use_page_url=False):
    """Get name from URL query part."""
    def _namer(self, image_url, page_url):
        """Get URL query part."""
        url = page_url if use_page_url else image_url
        return getQueryParams(url)[param][0]
    return _namer


def regexNamer(regex, use_page_url=False):
    """Get name from regular expression."""
    def _namer(self, image_url, page_url):
        """Get first regular expression group."""
        url = page_url if use_page_url else image_url
        mo = regex.search(url)
        if mo:
            return mo.group(1)
    return _namer


def bounceStarter(self):
    """Get start URL by "bouncing" back and forth one time.

    This needs the url and nextSearch properties be defined on the class.
    """
    data = self.getPage(self.url)
    url1 = self.fetchUrl(self.url, data, self.prevSearch)
    data = self.getPage(url1)
    return self.fetchUrl(url1, data, self.nextSearch)


def indirectStarter(self):
    """Get start URL by indirection.

    This is useful for comics where the latest comic can't be reached at a
    stable URL. If the class has an attribute 'startUrl', this page is fetched
    first, otherwise the page at 'url' is fetched. After that, the attribute
    'latestSearch' is used on the page content to find the latest strip."""
    url = self.startUrl if hasattr(self, "startUrl") else self.url
    data = self.getPage(url)
    return self.fetchUrl(url, data, self.latestSearch)

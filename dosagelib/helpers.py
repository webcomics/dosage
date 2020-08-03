# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
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


def joinPathPartsNamer(pageurlparts, imageurlparts=(-1,), joinchar='_'):
    """Get name by mashing path parts together with underscores."""
    def _namer(self, imageurl, pageurl):
        # Split and drop host name
        pageurlsplit = pageurl.split('/')[3:]
        imageurlsplit = imageurl.split('/')[3:]
        joinparts = ([pageurlsplit[i] for i in pageurlparts] +
            [imageurlsplit[i] for i in imageurlparts])
        return joinchar.join(joinparts)
    return _namer


def bounceStarter(self):
    """Get start URL by "bouncing" back and forth one time.

    This needs the url and nextSearch properties be defined on the class.
    """
    data = self.getPage(self.url)
    prevurl = self.fetchUrl(self.url, data, self.prevSearch)
    prevurl = self.link_modifier(self.url, prevurl)
    data = self.getPage(prevurl)
    nexturl = self.fetchUrl(prevurl, data, self.nextSearch)
    return self.link_modifier(prevurl, nexturl)


def indirectStarter(self):
    """Get start URL by indirection.

    This is useful for comics where the latest comic can't be reached at a
    stable URL. If the class has an attribute 'startUrl', this page is fetched
    first, otherwise the page at 'url' is fetched. After that, the attribute
    'latestSearch' is used on the page content to find the latest strip."""
    url = self.startUrl if hasattr(self, "startUrl") else self.url
    data = self.getPage(url)
    newurl = self.fetchUrl(url, data, self.latestSearch)
    return self.link_modifier(url, newurl)

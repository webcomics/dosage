# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from __future__ import annotations

from typing import Protocol

from .util import getQueryParams
from .scraper import Scraper


class Namer(Protocol):
    """A protocol for generic callbacks to name web comic images."""
    def __call__(_, self: Scraper, image_url: str, page_url: str) -> str | None:
        ...


def queryNamer(param, use_page_url=False) -> Namer:
    """Get name from URL query part."""
    def _namer(self, image_url: str, page_url: str) -> str | None:
        """Get URL query part."""
        url = page_url if use_page_url else image_url
        return getQueryParams(url)[param][0]
    return _namer


def regexNamer(regex, use_page_url=False) -> Namer:
    """Get name from regular expression."""
    def _namer(self, image_url: str, page_url: str) -> str | None:
        """Get first regular expression group."""
        url = page_url if use_page_url else image_url
        mo = regex.search(url)
        return mo.group(1) if mo else None
    return _namer


def joinPathPartsNamer(pageparts=(), imageparts=(), joinchar='_') -> Namer:
    """Get name by mashing path parts together with underscores."""
    def _namer(self: Scraper, image_url: str, page_url: str) -> str | None:
        # Split and drop host name
        pagesplit = page_url.split('/')[3:]
        imagesplit = image_url.split('/')[3:]
        joinparts = ([pagesplit[i] for i in pageparts] +
            [imagesplit[i] for i in imageparts])
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

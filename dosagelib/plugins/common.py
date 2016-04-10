# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper

# Common base classes for comics with the same structure (same hosting
# software, for example) go here. Since those are shared by many modules,
# please don't use lists of expression, as that makes it hard to track which
# expression is for which comics.


def xpath_class(name):
    """Returns an XPath expressions which finds a tag which has a specified
    class."""
    return 'contains(concat(" ", @class, " "), " %s ")' % name


WP_LATEST_SEARCH = '//a[%s]' % xpath_class('comic-nav-last')
WP_PREV_SEARCH = '//a[%s]' % xpath_class('comic-nav-previous')


class _WordPressScraper(_ParserScraper):
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = WP_PREV_SEARCH


class _ComicControlScraper(_ParserScraper):
    imageSearch = '//img[@id="cc-comic"]'
    prevSearch = '//a[@rel="prev"]'

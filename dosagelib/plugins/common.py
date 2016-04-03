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


WP_LATEST_SEARCH = '//a[contains(concat(" ", @class, " "), " comic-nav-last ")]'


class _WordPressScraper(_ParserScraper):
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = "//a[contains(concat(' ', @class, ' '), ' comic-nav-previous ')]"


class _ComicPressScraper(_WordPressScraper):
    prevSearch = "//a[contains(concat(' ', @class, ' '), ' navi-prev-in ')]"

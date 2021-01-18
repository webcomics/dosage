# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from ..scraper import _ParserScraper

# Common base classes for comics with the same structure (same hosting
# software, for example) go here. Since those are shared by many modules,
# please don't use lists of expression, as that makes it hard to track which
# expression is for which comics.


class _WordPressScraper(_ParserScraper):
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[d:class("comic-nav-previous")]'
    nextSearch = '//a[d:class("comic-nav-next")]'
    latestSearch = '//a[d:class("comic-nav-last")]'


class _WordPressSpliced(_ParserScraper):
    imageSearch = '//div[@id="spliced-comic"]//img'
    prevSearch = '//a[d:class("previous-comic")]'


class _WPNavi(_WordPressScraper):
    prevSearch = '//a[d:class("navi-prev")]'


class _WPNaviIn(_WordPressScraper):
    prevSearch = '//a[d:class("navi-prev-in")]'


class _WPWebcomic(_ParserScraper):
    imageSearch = '//div[d:class("webcomic-image")]//img'
    prevSearch = '//a[d:class("previous-webcomic-link")]'
    nextSearch = '///a[d:class("next-webcomic-link")]'
    latestSearch = '//a[d:class("last-webcomic-link")]'


class _ComicControlScraper(_ParserScraper):
    imageSearch = '//img[@id="cc-comic"]'
    prevSearch = '//a[@rel="prev"]'
    nextSearch = '//a[@rel="next"]'
    latestSearch = '//a[@rel="last"]'

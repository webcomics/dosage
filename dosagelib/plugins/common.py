# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
from typing import Sequence, Union

from ..scraper import ParserScraper

# Common base classes for comics with the same structure (same hosting
# software, for example) go here. Since those are shared by many modules,
# please don't use lists of expression, as that makes it hard to track which
# expression is for which comics.
__all__ = (
    'ComicControlScraper',
    'WordPressNavi',
    'WordPressNaviIn',
    'WordPressScraper',
    'WordPressSpliced',
    'WordPressWebcomic',
)


class ComicControlScraper(ParserScraper):
    imageSearch: Union[Sequence[str], str] = '//img[@id="cc-comic"]'
    prevSearch = '//a[@rel="prev"]'
    nextSearch = '//a[@rel="next"]'
    latestSearch = '//a[@rel="last"]'


class WordPressScraper(ParserScraper):
    imageSearch = '//div[@id="comic"]//img'
    prevSearch = '//a[d:class("comic-nav-previous")]'
    nextSearch = '//a[d:class("comic-nav-next")]'
    latestSearch = '//a[d:class("comic-nav-last")]'


class WordPressSpliced(ParserScraper):
    imageSearch = '//div[@id="one-comic-option"]//img'
    prevSearch = '//a[d:class("previous-comic")]'


class WordPressNavi(WordPressScraper):
    prevSearch = '//a[d:class("navi-prev")]'


class WordPressNaviIn(WordPressScraper):
    prevSearch = '//a[d:class("navi-prev-in")]'


class WordPressWebcomic(ParserScraper):
    imageSearch = '//div[d:class("webcomic-image")]//img'
    prevSearch = '//a[d:class("previous-webcomic-link")]'
    nextSearch = '///a[d:class("next-webcomic-link")]'
    latestSearch = '//a[d:class("last-webcomic-link")]'

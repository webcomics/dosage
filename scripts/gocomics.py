#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get a list of gocomics and save the info in a JSON file for further
processing.
"""
from __future__ import absolute_import, division, print_function

from scriptutil import ComicListUpdater


class GoComicsUpdater(ComicListUpdater):
    # names of comics to exclude
    excluded_comics = [
            # "coming soon"
            "AngryProgrammer",
            "Guinness",
            "Jabberwoncky",
            "Pi",
            "RandysRationale",
            "SignsOfOurTimes",
            "TheGagwriter",
            "Yaoyao",

            # duplicate
            "Dilbert",
            "SaturdayMorningBreakfastCereal",

            # not available
            "BillyAndCo",
            "BuffaloChips",
            "Crawdiddy",
    ]

    def handle_url(self, url):
        """Parse one search result page."""
        data = self.get_url(url, expand=False)

        for comiclink in data.cssselect('a.alpha_list'):
            link = comiclink.attrib['href']
            name = comiclink.text
            self.add_comic(name, link)

    def collect_results(self):
        """Parse all listing pages."""
        self.handle_url('http://www.gocomics.com/features')
        self.handle_url('http://www.gocomics.com/explore/espanol')
        self.handle_url('http://www.gocomics.com/explore/editorial_list')
        self.handle_url('http://www.gocomics.com/explore/sherpa_list')

    def get_entry(self, name, url):
        return u"class GC%s(_GoComics%s):\n    path = %r" % (
            name, 'Es' if 'espanol/' in url else '', url[1:])


if __name__ == '__main__':
    GoComicsUpdater(__file__).run()

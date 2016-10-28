#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get arcamax comics and save the info in a JSON file for further
processing.
"""
from __future__ import absolute_import, division, print_function

from scriptutil import ComicListUpdater


class ArcamaxUpdater(ComicListUpdater):
    dup_templates = ("Creators/%s", "DrunkDuck/%s", "GoComics/%s",
                     "KeenSpot/%s", "ComicGenesis/%s", "SmackJeeves/%s")

    # names of comics to exclude
    excluded_comics = (
        # better source available
        "Dilbert",
        "HagarTheHorrible",
    )

    def handle_url(self, url):
        """Parse one search result page."""
        data = self.get_url(url)

        for comiclink in data.cssselect('a.comic-icon'):
            path = comiclink.attrib['href']
            name = comiclink.attrib['title']

            self.add_comic(name, path.rsplit('/', 2)[1])

    def collect_results(self):
        """Parse all search result pages."""
        self.handle_url('http://www.arcamax.com/comics')

    def get_entry(self, name, entry):
        return u"cls('%s', '%s')," % (name, entry)


if __name__ == '__main__':
    ArcamaxUpdater(__file__).run()

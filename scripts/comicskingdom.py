#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2019 Tobias Gruetzmacher
# Copyright (C) 2019 Thomas W. Littauer
"""
Script to get a list of comicskingdom.com comics and save the info in a JSON
file for further processing.
"""
from __future__ import absolute_import, division, print_function

from scriptutil import ComicListUpdater


class ComicsKingdomUpdater(ComicListUpdater):
    dup_templates = ("Creators/%s", "DrunkDuck/%s", "GoComics/%s",
                    "KeenSpot/%s", "ComicGenesis/%s", "SmackJeeves/%s")

    # names of comics to exclude
    excluded_comics = (
    )

    def handle_url(self, url):
        """Parse one listing page."""
        data = self.get_url(url)

        for comicdiv in data.cssselect('ul.comic-link-group li'):
            comiclink = comicdiv.cssselect('a')[0]
            comicurl = comiclink.attrib['href']
            name = comicdiv.cssselect('a')[0].text

            self.add_comic(name, comicurl.rsplit('/', 1)[1])

    def collect_results(self):
        """Parse all search result pages."""
        self.handle_url('https://www.comicskingdom.com/')

    def get_entry(self, name, path):
        return u"cls('%s', '%s')," % (name, path)


if __name__ == '__main__':
    ComicsKingdomUpdater(__file__).run()

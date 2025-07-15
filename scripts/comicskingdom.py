#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Thomas W. Littauer
"""
Script to get a list of comicskingdom.com comics and save the info in a JSON
file for further processing.
"""

from dosagelib import util
from scriptutil import ComicListUpdater


class ComicsKingdomUpdater(ComicListUpdater):
    dup_templates = (
        "Creators/%s",
        "GoComics/%s",
        "KeenSpot/%s",
        "ComicGenesis/%s",
    )

    def handle_listing(self, page):
        for link in self.xpath(page, '//ul[d:class("index")]//a'):
            name = link.text_content().removeprefix('The ')
            url = link.attrib['href']
            lang = 'es' if ' (Spanish)' in name else None

            self.add_comic(name, (url, lang))

    def collect_results(self):
        """Parse all search result pages."""
        self.handle_listing(self.get_url('https://comicskingdom.com/features'))

    def get_entry(self, name: str, data: tuple[str, str]):
        opt = f", lang='{data[1]}'" if data[1] else ''
        pathparts = util.urlpathsplit(data[0])
        path = pathparts[1] if pathparts[0] == 'vintage' else pathparts[0]
        return f"cls('{name}', '{path}'{opt}),"


if __name__ == '__main__':
    ComicsKingdomUpdater(__file__).run()

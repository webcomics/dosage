#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
"""
Script to get arcamax comics and save the info in a JSON file for further
processing.
"""

import scriptutil


class ArcamaxUpdater(scriptutil.ComicListUpdater):
    dup_templates = ("Creators/%s", "DrunkDuck/%s", "GoComics/%s",
                     "KeenSpot/%s", "ComicGenesis/%s")

    # names of comics to exclude
    excluded_comics = (
        # better source available
        "Dilbert",
        "HagarTheHorrible",
    )

    def handle_url(self, url):
        """Parse one search result page."""
        data = self.get_url(url)

        for comiclink in self.xpath(data, '//a[d:class("comic-icon")]'):
            path = comiclink.attrib['href']
            name = comiclink.attrib['title']

            self.add_comic(name, path.rsplit('/', 2)[1])

    def collect_results(self):
        """Parse all search result pages."""
        self.handle_url('http://www.arcamax.com/comics')

    def get_entry(self, name, entry):
        return f"cls('{name}', '{entry}'),"


if __name__ == '__main__':
    ArcamaxUpdater(__file__).run()

#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
"""
Script to get a list of creators.com comics and save the info in a JSON file
for further processing.
"""

import scriptutil


class CreatorsUpdater(scriptutil.ComicListUpdater):
    dup_templates = ('GoComics/%s',)

    # names of comics to exclude
    excluded_comics = (
        # no images
        'Doodles',
    )

    def handle_url(self, url):
        """Parse one listing page."""
        data = self.get_url(url)

        for comicdiv in self.xpath(data, '//ul[d:class("all-test")]/li'):
            comiclink = self.xpath(comicdiv, './a')[0]
            comicurl = comiclink.attrib['href']
            name = self.xpath(comicdiv, './/p/strong')[0].text

            self.add_comic(name, comicurl.rsplit('/', 1)[1])

    def collect_results(self):
        """Parse all search result pages."""
        self.handle_url('https://www.creators.com/categories/comics/all')
        self.handle_url('https://www.creators.com/categories/cartoons/all')

    def get_entry(self, name, path):
        langopt = ", 'es'" if name.lower().endswith('spanish') else ''
        return f"cls('{name}', '{path}'{langopt}),"


if __name__ == '__main__':
    CreatorsUpdater(__file__).run()

#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get a list of creators.com comics and save the info in a JSON file
for further processing.
"""

from scriptutil import ComicListUpdater


class CreatorsUpdater(ComicListUpdater):
    dup_templates = ('GoComics/%s',)

    # names of comics to exclude
    excluded_comics = (
        # no images
        'Doodles',
    )

    def handle_url(self, url):
        """Parse one listing page."""
        data = self.get_url(url)

        for comicdiv in data.cssselect('ul.all-test li'):
            comiclink = comicdiv.cssselect('a')[0]
            comicurl = comiclink.attrib['href']
            name = comicdiv.cssselect('p strong')[0].text

            self.add_comic(name, comicurl.rsplit('/', 1)[1])

    def collect_results(self):
        """Parse all search result pages."""
        self.handle_url('https://www.creators.com/categories/comics/all')
        self.handle_url('https://www.creators.com/categories/cartoons/all')

    def get_entry(self, name, path):
        langopt = ", 'es'" if name.lower().endswith('spanish') else ''
        return u"cls('%s', '%s'%s)," % (name, path, langopt)


if __name__ == '__main__':
    CreatorsUpdater(__file__).run()

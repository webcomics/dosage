#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher
"""
Script to get a list of gocomics and save the info in a JSON file for further
processing.
"""
from __future__ import absolute_import, division, print_function

from scriptutil import ComicListUpdater


class GoComicsUpdater(ComicListUpdater):
    # names of comics to exclude
    excluded_comics = (
        # too short
        'LukeyMcGarrysTLDR',
    )

    def handle_gocomics(self, url, outercss='a.amu-media-item-link', lang=None):
        """Parse one GoComics alphabetic page."""
        data = self.get_url(url, expand=False)

        for comiclink in data.cssselect(outercss):
            link = comiclink.attrib['href']
            name = comiclink.cssselect('h4')[0].text
            self.add_comic(name, (link, lang))

    def collect_results(self):
        """Parse all listing pages."""
        for part in ('a-b', 'c-e', 'f-i', 'j-n', 'o-r', 's-t', 'u-%23'):
            self.handle_gocomics('http://www.gocomics.com/comics/a-to-z?page=' + part)
        self.handle_gocomics('http://www.gocomics.com/comics/espanol', 'a.gc-card-item', 'es')

    def get_entry(self, name, data):
        url, lang = data
        langopt = ", '%s'" % lang if lang else ''
        return u"cls('%s', '%s'%s)," % (name, url[1:], langopt)


if __name__ == '__main__':
    GoComicsUpdater(__file__).run()

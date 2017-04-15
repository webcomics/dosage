#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher
"""
Script to get a list of ComicSherpa and save the info in a JSON file for
further processing.
"""
from __future__ import absolute_import, division, print_function

from scriptutil import ComicListUpdater


class ComicSherpaUpdater(ComicListUpdater):
    # names of comics to exclude
    excluded_comics = (
        # missing images
        'Pi',
        'Rufus',

        # too short
        'BeneathTheFerns',
        'BillyAndCo',
        'BuffaloChips',
        'Crawdiddy',
        'Gravy',
        'NewFeature',
    )

    def collect_results(self):
        """Parse all listing pages."""
        data = self.get_url('http://www.comicssherpa.com/site/home.html', expand=False)

        for comiclink in data.xpath('//a[contains(@href, "site/feature")]'):
            link = comiclink.attrib['href'].split('=')[1]
            name = comiclink.text
            self.add_comic(name, link)

    def get_entry(self, name, url):
        return u"cls('%s', '%s')," % (name, url)


if __name__ == '__main__':
    ComicSherpaUpdater(__file__).run()

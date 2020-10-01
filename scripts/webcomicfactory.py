#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Script to get WebComicFactory comics and save the info in a JSON file for
further processing.
"""
from scriptutil import ComicListUpdater


class WebComicFactoryUpdater(ComicListUpdater):

    def find_first(self, url):
        data = self.get_url(url)

        firstlinks = data.cssselect('a.comic-nav-first')
        if not firstlinks:
            print("INFO:", "No first link on »%s«, already first page?" %
                  (url))
            return url
        return firstlinks[0].attrib['href']

    def collect_results(self):
        """Parse start page for supported comics."""
        url = 'http://www.thewebcomicfactory.com/'
        data = self.get_url(url)

        for comicdiv in data.cssselect('div.ceo_thumbnail_widget'):
            comicname = comicdiv.cssselect('h2')[0]
            comiclink = comicdiv.cssselect('a')[0]
            comicurl = comiclink.attrib['href']
            name = comicname.text
            if 'comic-color-key' in comicurl:
                continue
            comicurl = self.find_first(comicurl)
            self.add_comic(name, comicurl)

    def get_entry(self, name, url):
        return (u"cls('%s',\n    '%s')," % (name, url))


if __name__ == '__main__':
    WebComicFactoryUpdater(__file__).run()

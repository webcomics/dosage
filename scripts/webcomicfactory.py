#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: 2015 Tobias Gruetzmacher
"""
Script to get WebComicFactory comics and save the info in a JSON file for
further processing.
"""
import scriptutil


class WebComicFactoryUpdater(scriptutil.ComicListUpdater):

    def find_first(self, url):
        data = self.get_url(url)

        firstlinks = self.xpath(data, '//a[d:class("comic-nav-first")]')
        if not firstlinks:
            print("INFO:", "No first link on »%s«, already first page?" %
                  (url))
            return url
        return firstlinks[0].attrib['href']

    def collect_results(self):
        """Parse start page for supported comics."""
        url = 'http://www.thewebcomicfactory.com/'
        data = self.get_url(url)

        for comicdiv in self.xpath(data, '//div[d:class("ceo_thumbnail_widget")]'):
            comicname = self.xpath(comicdiv, './/h2')[0]
            comiclink = self.xpath(comicdiv, './/a')[0]
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

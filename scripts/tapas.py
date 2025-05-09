#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
"""
Script to get a list of Tapastic comics and save the info in a
JSON file for further processing.
"""
from urllib import parse

from scriptutil import ComicListUpdater


class TapasUpdater(ComicListUpdater):
    def collect_results(self):
        # Retrieve the first 10 top comics list pages
        url = 'https://tapas.io/comics?browse=ALL&sort_type=LIKE&pageNumber='
        count = 10

        data = [self.get_url(url + str(i), robot=False) for i in range(0, count)]
        for page in data:
            for comiclink in page.xpath('//a[@class="preferred title"]'):
                comicurl = comiclink.attrib['href']
                name = comiclink.text
                self.add_comic(name, comicurl)

    def get_entry(self, name, url):
        shortName = name.replace(' ', '').replace('\'', '')
        titleNum = int(parse.parse_qs(parse.urlsplit(url).query)['title_no'][0])
        url = url.rsplit('/', 1)[0].replace('/series/', '')
        return u"cls('%s', '%s', %d)," % (shortName, url, titleNum)


if __name__ == '__main__':
    TapasUpdater(__file__).run()

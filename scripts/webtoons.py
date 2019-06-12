#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2019-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
"""
Script to get a list of WebToons comics and save the info in a
JSON file for further processing.
"""
from __future__ import absolute_import, division, print_function

from six.moves.urllib.parse import urlsplit, parse_qs

from scriptutil import ComicListUpdater
from dosagelib.util import check_robotstxt


class WebToonsUpdater(ComicListUpdater):
    def collect_results(self):
        # Parse the comic list page
        data = self.get_url('https://www.webtoons.com/en/dailySchedule')

        for comiclink in data.xpath('//a[contains(@class, "daily_card_item")]'):
            comicurl = comiclink.attrib['href']
            name = comiclink.xpath('.//div[@class="info"]/p[@class="subj"]')[0].text
            try:
                check_robotstxt(comicurl, self.session)
            except IOError as e:
                print('[%s] INFO: robots.txt denied: %s' % (name, e))
                continue

            self.add_comic(name, comicurl)

    def get_entry(self, name, url):
        shortName = name.replace(' ', '')
        titleNum = int(parse_qs(urlsplit(url).query)['title_no'][0])
        url = url.rsplit('/', 1)[0].replace('https://www.webtoons.com/en/', '')
        return u"cls('%s', '%s', %d)," % (shortName, url, titleNum)


if __name__ == '__main__':
    WebToonsUpdater(__file__).run()

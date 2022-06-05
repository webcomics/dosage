#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019 Thomas W. Littauer
"""
Script to get a list of comicskingdom.com comics and save the info in a JSON
file for further processing.
"""

from scriptutil import ComicListUpdater
from dosagelib.xml import NS


class ComicsKingdomUpdater(ComicListUpdater):
    dup_templates = (
        "Creators/%s",
        "GoComics/%s",
        "KeenSpot/%s",
        "ComicGenesis/%s",
    )

    def handle_startpage(self, page):
        """Parse list of comics from the bottom of the start page."""
        for li in page.xpath('//div[d:class("comics-list")]//li', namespaces=NS):
            link = li.xpath('./a')[0]
            url = link.attrib['href']
            name = link.text.removeprefix('The ')

            self.add_comic(name, (url, None))

    def handle_listing(self, page, lang: str = None, add: str = ''):

        hasnew = True
        while hasnew:
            hasnew = False
            for comicdiv in page.xpath('//div[d:class("tile")]', namespaces=NS):
                nametag = comicdiv.xpath('./a/comic-name')
                if len(nametag) == 0:
                    continue
                name = nametag[0].text.removeprefix('The ') + add
                url = comicdiv.xpath('./a')[0].attrib['href']

                if self.add_comic(name, (url, lang)):
                    hasnew = True

            nextlink = page.xpath('//a[./img[contains(@src, "page-right")]]')
            page = self.get_url(nextlink[0].attrib['href'])

    def collect_results(self):
        """Parse all search result pages."""
        page = self.get_url('https://www.comicskingdom.com/')
        self.handle_startpage(page)
        self.handle_listing(page)
        self.handle_listing(self.get_url('https://www.comicskingdom.com/spanish'), 'es', 'Spanish')

    def get_entry(self, name: str, data: tuple[str, str]):
        opt = f", lang='{data[1]}'" if data[1] else ''
        return f"cls('{name}', '{data[0].split('/')[3]}'{opt}),"


if __name__ == '__main__':
    ComicsKingdomUpdater(__file__).run()

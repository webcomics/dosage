#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
"""
Script to get a list of gocomics and save the info in a JSON file for further
processing.
"""

from scriptutil import ComicListUpdater

from dosagelib import xml


class GoComicsUpdater(ComicListUpdater):
    dup_templates = (
        "ComicsKingdom/%s",
    )

    # names of comics to exclude
    excluded_comics = (
        # too short
        'LukeyMcGarrysTLDR',
        # Has its own module
        'Widdershins',
        # Moved to webtoons
        "FalseKnees",
    )

    def handle_gocomics(self, url):
        """Parse one GoComics alphabetic page."""
        data = self.get_url(url, expand=False)

        for comiclink in data.xpath('//a[d:class_start("ComicsAtoZ_comics__link_")]', namespaces=xml.NS):
            link = comiclink.attrib['href'].split('/')[1].strip()
            name = comiclink.xpath('.//h3')[0].text
            # Language heuristics
            lang = "es" if "espanol" in link else None
            self.add_comic(name, (link, lang))

    def collect_results(self):
        """Parse all listing pages."""
        self.handle_gocomics('https://www.gocomics.com/comics/a-to-z')

    def get_entry(self, name: str, data: tuple[str, str]):
        url, lang = data
        langopt = ", '%s'" % lang if lang else ''
        return u"cls('%s', '%s'%s)," % (name, url, langopt)


if __name__ == '__main__':
    GoComicsUpdater(__file__).run()

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


class GoComicsUpdater(ComicListUpdater):
    dup_templates = (
        "ComicsKingdom/%s",
    )

    # names of comics to exclude
    excluded_comics = (
        # Has its own module
        'Widdershins',
        # Moved to webtoons
        "FalseKnees",
    )
    spanish: set[str] = set()

    def handle_atozlist(self, url: str) -> None:
        """Parse one GoComics alphabetic page."""
        data = self.get_url(url, expand=False)

        for comiclink in self.xpath(data, '//a[d:class_start("ComicsAtoZ_comics__link_")]'):
            link = comiclink.attrib['href'].split('/')[1].strip()
            name = comiclink.xpath('.//h3')[0].text
            self.add_comic(name, (link, self.detect_lang(name, link)))

    def detect_lang(self, name: str, link: str) -> str | None:
        '''Language heuristics'''
        if ("en Español" in name or
                "spanish" in link or "espanol" in link or
                link in self.spanish):
            return "es"
        return None

    def find_spanish(self) -> None:
        data = self.get_url('https://www.gocomics.com/comics', expand=False)
        for comiclink in self.xpath(data, '//section[.//h2[contains(text(), "en Español")]]//a'):
            self.spanish.add(comiclink.attrib['href'].split('/')[1].strip())

    def collect_results(self) -> None:
        """Parse all listing pages."""
        self.find_spanish()
        self.handle_atozlist('https://www.gocomics.com/comics/a-to-z')
        self.handle_atozlist('https://www.gocomics.com/political-cartoons/political-a-to-z')

    def get_entry(self, name: str, data: tuple[str, str]) -> str:
        url, lang = data
        langopt = f", '{lang}'" if lang else ''
        return f"cls('{name}', '{url}'{langopt}),"


if __name__ == '__main__':
    GoComicsUpdater(__file__).run()

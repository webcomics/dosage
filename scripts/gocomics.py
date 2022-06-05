#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
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
        # too short
        'LukeyMcGarrysTLDR',
    )

    def handle_gocomics(self, url, outercss='a.gc-blended-link', lang=None):
        """Parse one GoComics alphabetic page."""
        data = self.get_url(url, expand=False)

        for comiclink in data.cssselect(outercss):
            link = comiclink.attrib['href'].split('/')[1].strip()
            name = comiclink.cssselect('h4')[0].text
            self.add_comic(name, (link, lang))

    def collect_results(self):
        """Parse all listing pages."""
        # We add the spanish comics first since they are now also listed on the list of all
        # comics... (Expect duplicate warnings for all spanish comics)
        self.handle_gocomics('https://www.gocomics.com/comics/espanol', lang='es')
        self.handle_gocomics('https://www.gocomics.com/comics/espanol?page=2', lang='es')
        self.handle_gocomics('https://www.gocomics.com/comics/a-to-z')

    def get_entry(self, name: str, data: tuple[str, str]):
        url, lang = data
        langopt = ", '%s'" % lang if lang else ''
        return u"cls('%s', '%s'%s)," % (name, url, langopt)


if __name__ == '__main__':
    GoComicsUpdater(__file__).run()

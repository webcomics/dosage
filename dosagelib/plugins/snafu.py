# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from ..scraper import _BasicScraper

def snafuComics():
    class _SnafuComics(_BasicScraper):
        imageSearch = compile(r'<img src=http://\w+\.snafu-comics\.com/(comics/\d{6}_\w*\.\w{3,4})')
        prevSearch = compile(r'<a href="(\?comic_id=\d+)">Previous</a>')
        help = 'Index format: n (unpadded)'

        @property
        def stripUrl(self):
            return self.latestUrl + 'index.php?strip_id=%s'

    comics = {
        'Grim': 'grim',
        'KOF': 'kof',
        'PowerPuffGirls': 'ppg',
        'Snafu': 'www',
        'Tin': 'tin',
        'TW': 'tw',
        'Sugar': 'sugar',
        'SF': 'sf',
        'Titan': 'titan',
        'EA': 'ea',
        'Zim': 'zim',
        'Soul': 'soul',
        'FT': 'ft',
        'Bunnywith': 'bunnywith',
        'Braindead': 'braindead',
        }

    url = 'http://%s.snafu-comics.com/'
    return dict((name, type('SnafuComics_%s' % name,
                            (_SnafuComics,),
                             dict(name='SnafuComics/' + name,
                             latestUrl=url % host)))
                for name, host in comics.items())

globals().update(snafuComics())

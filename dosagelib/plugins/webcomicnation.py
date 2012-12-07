# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, IGNORECASE, DOTALL
from ..scraper import make_scraper

_imageSearch = compile(r'<a name="strip\d*?">.*?<img[^>]+?src="([^"]*?memberimages/.+?)"', IGNORECASE + DOTALL)
_prevSearch = compile(r'href="([^"]*?whichbutton=prev[^"]*?)"', IGNORECASE)


def add(name, subpath):
    baseUrl = 'http://www.webcomicsnation.com/'
    classname = 'WebcomicsNation_%s' % name
    globals()[classname] = make_scraper(classname,
        name = 'WebcomicsNation/' + name,
        latestUrl = baseUrl + subpath,
        stripUrl = baseUrl + '?view=archive&amp;chapter=%s',
        imageSearch = _imageSearch,
        multipleImagesPerStrip = True,
        prevSearch = _prevSearch,
        # the prevSearch is a redirect
        prevUrlMatchesStripUrl = False,
        help = 'Index format: nnnn (non-contiguous)',
    )


add('AgnesQuill', 'daveroman/agnes/')
add('MyMuse', 'gc/muse/')
add('NekkoAndJoruba', 'nekkoandjoruba/nekkoandjoruba/')
add('ClownSamurai', 'qsamurai/clownsamurai/')

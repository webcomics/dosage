# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from re import compile
from ..scraper import _BasicScraper
from ..helpers import bounceStarter
from ..util import tagre


def smackJeeves(names):
    # XXX mature content can be viewed directly with:
    # http://www.smackjeeves.com/mature.php?ref=<percent-encoded-url>
    class _SJScraper(_BasicScraper):
        stripUrl = property(lambda self: self.baseUrl + self.shortName)
        imageSearch = compile(tagre("img", "src", r'(http://www\.smackjeeves\.com/images/uploaded/comics/[^"]*)'))
        prevSearch = compile(tagre("a", "href", r'(/comics/\d+/[^"]*)') + '<img[^>]*alt="< Previous"')
        help = 'Index format: nnnn (some increasing number)'

        @classmethod
        def namer(cls, imageUrl, pageUrl):
            return pageUrl.split('/')[-2]


    def makeScraper(shortName):
        baseUrl = 'http://%s.smackjeeves.com/comics/' % shortName
        return type('SmackJeeves_%s' % shortName,
            (_SJScraper,),
            dict(
              name='SmackJeeves/' + shortName,
              baseUrl=baseUrl,
              starter=bounceStarter(baseUrl, compile(tagre("a", "href", r'(/comics/\d+/[^"]*)') + '<img[^>]*alt="Next >"'))
            )
        )
    return dict((name, makeScraper(name)) for name in names)


globals().update(smackJeeves([
    '20galaxies',
    'axe13',
    'beartholomew',
    'bliss',
    'durian',
    'heard',
    'mpmcomic',
    'nlmo-project',
    'paranoidloyd',
    'thatdreamagain',
    'wowcomics',
    ]))

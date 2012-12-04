# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from re import compile
from ..scraper import make_scraper
from ..util import tagre, getQueryParams, fetchUrl


_linkTag = tagre("a", "href", r'([^"]+)')
_prevSearch = compile(_linkTag + tagre("img", "src", r"previous\.gif"))
_nextSearch = compile(_linkTag + tagre("img", "src", r"next\.gif"))
_lastSearch = compile(_linkTag + tagre("img", "src", r"last\.gif"))

def add(name, shortName, imageFolder=None, lastStrip=None):
    classname = 'CloneManga_%s' % name
    _url = 'http://manga.clone-army.org'
    baseUrl = '%s/%s.php' % (_url, shortName)
    if imageFolder is None:
        imageFolder = shortName

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        return '%03d' % int(getQueryParams(pageUrl)['page'][0])

    @classmethod
    def _starter(cls):
        # first, try hopping to previous and next comic
        url = fetchUrl(baseUrl, _prevSearch)
        if not url:
            # no previous link found, try hopping to last comic
            url = fetchUrl(baseUrl, _lastSearch)
            if not url:
                raise ValueError("could not find lastSearch pattern %r in %s" % (_lastSearch.pattern, baseUrl))
            return url
        url = fetchUrl(url, _nextSearch)
        if not url:
            raise ValueError("could not find nextSearch pattern %r in %s" % (_nextSearch.pattern, url))
        return url

    attrs = dict(
        name='CloneManga/' + name,
        stripUrl = baseUrl + '?page=%s',
        imageSearch=compile(tagre("img", "src", r'((?:%s/)?%s/[^"]+)' % (_url, imageFolder), after="center")),
        prevSearch=_prevSearch,
        help='Index format: n',
        namer=namer,
    )
    if lastStrip is None:
        attrs['starter'] = _starter
    else:
        attrs['latestUrl'] = attrs['stripUrl'] % lastStrip
    globals()[classname] = make_scraper(classname, **attrs)


add('AprilAndMay', 'anm', imageFolder='AAM')
add('Kanami', 'kanami')
add('MomokaCorner', 'momoka')
add('NanasEverydayLife', 'nana', lastStrip='78')
add('PaperEleven', 'pxi', imageFolder='papereleven', lastStrip='311')
add('Tomoyo42sRoom', 't42r')
add('PennyTribute', 'penny')

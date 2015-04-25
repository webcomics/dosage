# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
from re import compile
from ..scraper import make_scraper
from ..util import tagre, getQueryParams


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
        data = cls.getPage(baseUrl)
        try:
            url = cls.fetchUrl(baseUrl, data, _prevSearch)
        except ValueError:
            # no previous link found, try hopping to last comic
            return cls.fetchUrl(baseUrl, data, _lastSearch)
        else:
            data = cls.getPage(url)
            return cls.fetchUrl(url, data, _nextSearch)

    attrs = dict(
        name='CloneManga/' + name,
        stripUrl = baseUrl + '?page=%s',
        imageSearch=compile(tagre("img", "src", r'((?:%s/)?%s/[^"]+)' % (_url, imageFolder), after="center")),
        prevSearch=_prevSearch,
        help='Index format: n',
        namer=namer,
        url=baseUrl,
    )
    if lastStrip is None:
        attrs['starter'] = _starter
    else:
        attrs['url'] = attrs['stripUrl'] % lastStrip
    globals()[classname] = make_scraper(classname, **attrs)


add('AprilAndMay', 'anm', imageFolder='AAM')
add('Kanami', 'kanami')
add('MomokaCorner', 'momoka')
add('NanasEverydayLife', 'nana', lastStrip='78')
add('PaperEleven', 'pxi', imageFolder='papereleven', lastStrip='311')
add('Tomoyo42sRoom', 't42r')
add('PennyTribute', 'penny')

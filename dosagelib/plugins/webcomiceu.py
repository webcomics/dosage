# -*- coding: iso-8859-1 -*-
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre

_prevSearch = compile(tagre("a", "href", r'(\?id=\d+)') + tagre("img", "src", r'images/navi-zurueck\.gif'))
_imageSearch = compile(tagre("img", "src", r'([^"]+/img/comic/[^"]+)', after="comicimg"))

def add(name, shortname):
    latestUrl = 'http://%s.webcomic.eu/' % shortname
    classname = 'WebcomicEu_%s' % name
    globals()[classname] = make_scraper(classname,
        name = 'WebcomicEu/' + name,
        latestUrl = latestUrl,
        stripUrl = latestUrl + '?id=%s',
        imageSearch = _imageSearch,
        prevSearch = _prevSearch,
        help = 'Index format: number',
    )


add('TheBessEffect', 'thebesseffect')
add('TheBessEffectEnglish', 'tbe-english')
add('Talandor', 'talandor')

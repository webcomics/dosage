# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
from re import compile

from ..scraper import _BasicScraper
from ..helpers import bounceStarter


class xkcd(_BasicScraper):
    starter = bounceStarter('http://xkcd.com/', compile(r'<a rel="next" href="(/?\d+/?)"[^>]*>Next'))
    stripUrl = 'http://xkcd.com/c%s.html'
    imageSearch = compile(r'<img[^<]+src="(http://imgs.xkcd.com/comics/[^<>"]+)"')
    prevSearch = compile(r'<a rel="prev" href="(/?\d+/?)"[^>]*>&lt; Prev')
    help = 'Index format: n (unpadded)'

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        index = int(pageUrl.rstrip('/').split('/')[-1])
        name = imageUrl.split('/')[-1].split('.')[0]
        return 'c%03d-%s' % (index, name)



class xkcdSpanish(_BasicScraper):
    latestUrl = 'http://es.xkcd.com/xkcd-es/'
    stripUrl = latestUrl + 'strips/%s/'
    imageSearch = compile(r'src="(/site_media/strips/.+?)"')
    prevSearch = compile(r'<a rel="prev" href="(http://es.xkcd.com/xkcd-es/strips/.+?)">Anterior</a>')
    help = 'Index format: stripname'

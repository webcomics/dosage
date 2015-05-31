# -*- coding: utf-8 -*-
from ..scraper import make_scraper, _ParserScraper


def add(name, url):
    attrs = dict(
        name=name,
        url='http://footloosecomic.com/' + url,
        imageSearch='//body/p[1]//img',
        prevSearch='//body/a[2]'
    )
    globals()[name] = make_scraper(name, _ParserScraper, **attrs)


add('Cherry', 'cherry/index.php')
add('Desigaspring', 'dspring/index.php')
add('Footloose', 'footloose.php')

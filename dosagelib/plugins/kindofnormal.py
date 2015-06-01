# -*- coding: utf-8 -*-
from dosagelib.helpers import indirectStarter
from ..scraper import make_scraper, _ParserScraper


def add(name, url):
    attrs = dict(
        name=name,
        url='http://kindofnormal.com/' + url,
        imageSearch='//article[1]//div[@class="box-content"]//img',
        prevSearch='//a[@class="prev"]'
    )
    globals()[name] = make_scraper(name, _ParserScraper, **attrs)


add('MeAndDanielle', 'meanddanielle')
add('TruthFacts', 'truthfacts')
add('Wumo', 'wumo')
add('Wulffmorgenthaler', 'wumo') # name in previous versions

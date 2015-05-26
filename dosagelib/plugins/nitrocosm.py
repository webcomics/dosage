# -*- coding: utf-8 -*-
from ..scraper import make_scraper, _ParserScraper


def add(name, relativeUrl):
    attrs = dict(
        name=name,
        url='http://www.nitrocosm.com/go/' + relativeUrl,
        imageSearch='//img[@class="gallery_display"]',
        prevSearch='//a[@class="nav_btn_previous"]'
    )
    globals()[name] = make_scraper(name, _ParserScraper, **attrs)


add('2214', '2214_classic/')
add('OTE', 'ote/')
add('ProperBarn', 'gag/')

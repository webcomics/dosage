# -*- coding: utf-8 -*-
from dosagelib.helpers import indirectStarter
from ..scraper import make_scraper, _ParserScraper


def add(name, url, firstUrl=None, starter=None, textSearch=None, lang=None):
    attrs = dict(
        name=name,
        url=url,
        imageSearch=['//div[@id="cc-comicbody"]//img'],
        prevSearch=['//a[@rel="prev"]']
    )
    if lang:
        attrs['lang'] = lang
    if firstUrl:
        attrs['firstUrl'] = url + firstUrl
    if starter:
        attrs['starter'] = starter
    if textSearch:
        attrs['textSearch'] = textSearch
    globals()[name] = make_scraper(name, _ParserScraper, **attrs)


add('GoGetARoomie', 'http://www.gogetaroomie.com')
add('KiwiBlitz', 'http://www.kiwiblitz.com')
add('LetsSpeakEnglish', 'http://www.marycagle.com')
add('Metacarpolis', 'http://www.metacarpolis.com')
add('Spinnerette', 'http://www.spinnyverse.com')
add('StreetFighter', 'http://www.streetfightercomics.com')

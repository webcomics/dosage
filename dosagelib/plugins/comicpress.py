# -*- coding: utf-8 -*-
from ..scraper import make_scraper, _ParserScraper

def add(name, url, firstUrl=None, lang=None):

	attrs = dict(
		name = name,
		url = url,
		imageSearch = '//div[@id="comic"]//img',
		prevSearch = u'//a[text()="‹ Prev"]',
	)
	if lang:
		attrs['lang'] = lang
	if firstUrl:
		attrs['firstUrl'] = url + firstUrl
	globals()[name] = make_scraper(name, _ParserScraper, **attrs)

add('Hipsters', 'http://www.hipsters-comic.com/', 'comic/hip01/')

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
from re import compile, escape
from ..scraper import make_scraper
from ..util import tagre


def add(name, urlName, firstUrl, lang=None):
    baseUrl = 'http://www.sandraandwoo.com/' + urlName
    rurl = escape(baseUrl)

    attrs = dict(
        name = name,
        url = baseUrl,
        stripUrl = baseUrl + '%s/',
        firstStripUrl = '%s/%s/' % (baseUrl, firstUrl),
        imageSearch = compile(tagre("img", "src", r'(/%scomics/\d+-\d+-\d+-[^"]+)' % urlName)),
        prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+/)' % rurl, after="prev")),
        help='Index format: yyyy/mm/dd/(number-)stripname',
    )
    if lang:
        attrs['lang'] = lang
    globals()[name] = make_scraper(name, **attrs)

add('Gaia', 'gaia/', '2000/01/01/welcome-to-gaia/')
add('GaiaGerman', 'gaiade/', '2000/01/01/welcome-to-gaia', lang='de')
add('SandraAndWoo', '', '2000/01/01/welcome-to-sandra-and-woo')
add('SandraAndWooGerman', 'woode/', '2008/10/19/ein-ausgefuchster-waschbar', lang='de')


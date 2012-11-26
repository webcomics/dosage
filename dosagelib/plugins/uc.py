# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
"""
The Universal comics only have some samples, but those samples are always the newest ones.
"""
import datetime
from re import compile, escape
from ..scraper import make_scraper
from ..util import tagre, asciify, getPageContent


def parse_strdate(strdate):
    """Parse date string. XXX this is locale dependant but it should not be."""
    return datetime.datetime.strptime(strdate, "%A, %B %d, %Y")


def add(name, category):
    shortname = name.replace(' ', '').lower()
    latestUrl = 'http://www.universaluclick.com/comics/%s/%s' % (category, shortname)
    classname = 'UClick_%s' % asciify(name)

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Parse publish date from page content which looks like:
         <img alt="Marmaduke" src="http://assets.amuniversal.com/07e7f270fa08012ff506001dd8b71c47" />
         <h4>published: Sunday, November 11, 2012</h4>
        """
        data = getPageContent(pageUrl)[0]
        ro = compile(tagre("img", "src", escape(imageUrl)) + r'\s+<h4>published: ([^<]+)')
        mo = ro.search(data)
        if mo:
             strdate = mo.group(1)
             return parse_strdate(strdate).strftime("%Y%m%d")

    globals()[classname] = make_scraper(classname,
        name='UClick/' + name,
        latestUrl = latestUrl,
        stripUrl = latestUrl + '%s/',
        imageSearch = compile(tagre("img", "src", r'(http://assets\.amuniversal\.com/[^"]+)') + r'\s+<h4>published'),
        multipleImagesPerStrip = True,
        prevSearch = None,
        help = 'Index format: none',
        namer = namer,
    )


# http://www.universaluclick.com/comics/list
comics = {
    '9 Chickweed Lane': 'strip',
}

for name, category in comics.items():
    add(name, category)

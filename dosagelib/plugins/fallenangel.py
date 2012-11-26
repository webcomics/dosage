# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import asciify


def add(name, shortname):
    latestUrl = 'http://www.thefallenangel.co.uk/cgi-bin/%sautokeen/autokeenlite.cgi' % shortname
    classname = asciify(name)
    globals()[classname] = make_scraper(classname,
        latestUrl = latestUrl,
        stripUrl = latestUrl + '?date=%s',
        name='FallenAngel/' + name,
        imageSearch = compile(r'SRC="(http://www.thefallenangel.co.uk/\w+comics/.+?)"'),
        prevSearch = compile(r' <a href="(http://www.thefallenangel.co.uk/.+?)"><img[^>]+?src="http://www.thefallenangel.co.uk/images/previousday.jpg"'),
        help = 'Index format: yyyymmdd',
    )


add('HighMaintenance', 'hm')
add('FAWK', 'fawk')
add('MalloryChan', 'mallorychan')


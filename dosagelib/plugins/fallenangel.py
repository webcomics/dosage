# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from ..scraper import _BasicScraper


def fallenangel(name, shortname):
    pass # XXX

class _TheFallenAngel(_BasicScraper):
    imageSearch = compile(r'SRC="(http://www.thefallenangel.co.uk/\w+comics/.+?)"')
    prevSearch = compile(r' <a href="(http://www.thefallenangel.co.uk/.+?)"><img[^>]+?src="http://www.thefallenangel.co.uk/images/previousday.jpg"')
    help = 'Index format: yyyymmdd'

    @property
    def baseUrl(self):
        return 'http://www.thefallenangel.co.uk/cgi-bin/%sautokeen/autokeenlite.cgi' % (self.shortName,)


    @property
    def stripUrl(self):
        return self.baseUrl + '?date=%s'


    def starter(self):
        return self.baseUrl



class HighMaintenance(_TheFallenAngel):
    name = 'TheFallenAngel/HighMaintenance'
    shortName = 'hm'



class FAWK(_TheFallenAngel):
    name = 'TheFallenAngel/FAWK'
    shortName = 'fawk'



class MalloryChan(_TheFallenAngel):
    name = 'TheFallenAngel/MalloryChan'
    shortName = 'mallorychan'




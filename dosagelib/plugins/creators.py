# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015 Tobias Gruetzmacher

from re import compile
from ..scraper import _ParserScraper
from ..util import tagre

class _Creators(_ParserScraper):
    url = 'http://www.creators.com/comics/'
    imageSearch = '//td/a[@class="z"]'
    prevSearch = '//a[contains(@class,"time_l")]'
    help = 'Index format: n'

    @classmethod
    def getName(cls):
        return 'Creators/' + cls.__name__

    @classmethod
    def starter(cls):
        return cls.url + cls.path + '.html'

    def getIndexStripUrl(self, index):
        return self.url + self.path + '/%s.html' % index

class _CreatorsEs(_Creators):
    lang = 'es'

    def shouldSkipUrl(self, url, data):
        """Images are 404..."""
        return url in (
            self.url + 'heathcliff-spanish/139736.html'
        )

# Some comics are not listed on the "all" page (too old?)
class WinnieThePooh(_Creators):
    path = u'winnie-the-pooh'

class Recess(_Creators):
    path = u'recess'

class NaturalSelection(_Creators):
    path = u'natural-selection'

class FlightDeck(_Creators):
    path = u'flight-deck'

# do not edit anything below since these entries are generated from scripts/update_plugins.sh
# DO NOT REMOVE
# Agnes has a duplicate in gocomics
# AndyCapp has a duplicate in gocomics
class Archie(_Creators):
    path = u'archie'

class ArchieinSpanish(_CreatorsEs):
    path = u'archie-spanish'

# AskShagg has a duplicate in gocomics
# BC has a duplicate in gocomics
class BCinSpanish(_CreatorsEs):
    path = u'bc-spanish'

# BallardStreet has a duplicate in gocomics
class CafeconLeche(_Creators):
    path = u'cafe-con-leche'

# ChuckleBros has a duplicate in gocomics
# DaddysHome has a duplicate in gocomics
# DiamondLil has a duplicate in gocomics
# DogEatDoug has a duplicate in gocomics
# DogsofCKennel has a duplicate in gocomics
class DonaldDuck(_Creators):
    path = u'donald-duck'

class Doodles(_Creators):
    path = u'doodles'

class Flare(_Creators):
    path = u'flare'

class FlightDeck(_Creators):
    path = u'flight-deck'

# FloandFriends has a duplicate in gocomics
# ForHeavensSake has a duplicate in gocomics
# FreeRange has a duplicate in gocomics
class GirlsAndSports(_Creators):
    path = u'girls-and-sports'

class GirlsandSportsinSpanish(_CreatorsEs):
    path = u'girls-and-sports-spanish'

# Heathcliff has a duplicate in gocomics
class HeathcliffinSpanish(_CreatorsEs):
    path = u'heathcliff-spanish'

# HerbandJamaal has a duplicate in gocomics
class HomeOffice(_Creators):
    path = u'stay-at-home-dad'

class HopeAndDeath(_Creators):
    path = u'hope-and-death'

# LibertyMeadows has a duplicate in gocomics
class LongStoryShort(_Creators):
    path = u'long-story-short'

class MickeyMouse(_Creators):
    path = u'mickey-mouse'

# Momma has a duplicate in gocomics
# NestHeads has a duplicate in gocomics
class OffCenter(_Creators):
    path = u'off-center'

# OnaClaireDay has a duplicate in gocomics
# OneBigHappy has a duplicate in gocomics
# Rubes has a duplicate in gocomics
class Rugrats(_Creators):
    path = u'rugrats'

class RugratsinSpanish(_CreatorsEs):
    path = u'rugrats-spanish'

# ScaryGary has a duplicate in gocomics
# SpeedBump has a duplicate in gocomics
# StrangeBrew has a duplicate in gocomics
# TheBarn has a duplicate in gocomics
# TheDinetteSet has a duplicate in gocomics
# TheMeaningofLila has a duplicate in gocomics
# TheOtherCoast has a duplicate in gocomics
class TheQuigmans(_Creators):
    path = u'the-quigmans'

class TheWizardofIdinSpanish(_CreatorsEs):
    path = u'wizard-of-id-spanish'

# ThinLines has a duplicate in gocomics
# WeePals has a duplicate in gocomics
# WizardofId has a duplicate in gocomics
# WorkingitOut has a duplicate in gocomics
# ZackHill has a duplicate in gocomics

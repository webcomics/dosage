# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class _Creators(_ParserScraper):
    url = 'https://www.creators.com/features/'
    imageSearch = '//a[contains(@class,"fancybox")]/img'
    prevSearch = '//a[@id="nav_prev"]'
    latestSearch = '//div[contains(@class,"caption")]/a'

    @property
    def name(self):
        return 'Creators/' + super(_Creators, self).name

    def starter(self):
        start = self.url + self.path
        data = self.getPage(start)
        return self.fetchUrl(start, data, self.latestSearch)


class _CreatorsEs(_Creators):
    lang = 'es'


# Some comics are not listed on the "all" page (too old?)
class CafeconLeche(_Creators):
    path = 'cafe-con-leche'


class DonaldDuck(_Creators):
    path = 'donald-duck'


class Flare(_Creators):
    path = 'flare'


class FlightDeck(_Creators):
    path = 'flight-deck'


class GirlsAndSports(_Creators):
    path = 'girls-and-sports'


class GirlsandSportsSpanish(_CreatorsEs):
    path = 'girls-and-sports-spanish'


class HomeOffice(_Creators):
    path = 'stay-at-home-dad'


class HopeAndDeath(_Creators):
    path = 'hope-and-death'


class MickeyMouse(_Creators):
    path = 'mickey-mouse'


class NaturalSelection(_Creators):
    path = 'natural-selection'


class OffCenter(_Creators):
    path = 'off-center'


class Recess(_Creators):
    path = 'recess'


class Rugrats(_Creators):
    path = 'rugrats'


class RugratsSpanish(_CreatorsEs):
    path = 'rugrats-spanish'


class TheQuigmans(_Creators):
    path = 'the-quigmans'


class WinnieThePooh(_Creators):
    path = 'winnie-the-pooh'


# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# DO NOT REMOVE
# Agnes has a duplicate in gocomics
# AndyCapp has a duplicate in gocomics
class AndyMarlette(_Creators):
    path = 'andy-marlette'


class Archie(_Creators):
    path = 'archie'


class ArchieSpanish(_CreatorsEs):
    path = 'archie-spanish'


# AskShagg has a duplicate in gocomics
# BC has a duplicate in gocomics
# BallardStreet has a duplicate in gocomics
# BobGorrell has a duplicate in gocomics
# ChipBok has a duplicate in gocomics
# ChrisBritt has a duplicate in gocomics
# ChuckleBros has a duplicate in gocomics
# DaddysHome has a duplicate in gocomics
# DiamondLil has a duplicate in gocomics
# DogEatDoug has a duplicate in gocomics
# DogsOfCKennel has a duplicate in gocomics
# FloAndFriends has a duplicate in gocomics
# ForHeavensSake has a duplicate in gocomics
# FreeRange has a duplicate in gocomics
# GaryMarkstein has a duplicate in gocomics
# GaryVarvel has a duplicate in gocomics
# Heathcliff has a duplicate in gocomics
class HeathcliffSpanish(_CreatorsEs):
    path = 'heathcliff-spanish'


# HerbAndJamaal has a duplicate in gocomics
# JohnDeering has a duplicate in gocomics
# KenCatalino has a duplicate in gocomics
# LibertyMeadows has a duplicate in gocomics
class LongStoryShort(_Creators):
    path = 'long-story-short'


# MarshallRamsey has a duplicate in gocomics
# MichaelRamirez has a duplicate in gocomics
# MikeLuckovich has a duplicate in gocomics
# Momma has a duplicate in gocomics
class Mossprints(_Creators):
    path = 'mossprints'


# NestHeads has a duplicate in gocomics
# OneBigHappy has a duplicate in gocomics
# PaulSzep has a duplicate in gocomics
# Rubes has a duplicate in gocomics
# ScaryGary has a duplicate in gocomics
# SpeedBump has a duplicate in gocomics
# SteveBenson has a duplicate in gocomics
# SteveBreen has a duplicate in gocomics
# SteveKelley has a duplicate in gocomics
# StrangeBrew has a duplicate in gocomics
# TheBarn has a duplicate in gocomics
# TheMeaningOfLila has a duplicate in gocomics
# TheOtherCoast has a duplicate in gocomics
class TomStiglich(_Creators):
    path = 'tom-stiglich'


# WeePals has a duplicate in gocomics
# WizardOfId has a duplicate in gocomics
class WizardOfIdSpanish(_CreatorsEs):
    path = 'wizard-of-id-spanish'


# WorkingItOut has a duplicate in gocomics
# ZackHill has a duplicate in gocomics

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from ..scraper import _ParserScraper


class _Arcamax(_ParserScraper):
    imageSearch = '//img[@id="comic-zoom"]'
    prevSearch = '//a[@class="prev"]'

    def __init__(self, name):
        super(_Arcamax, self).__init__('Arcamax/' + name)

    @property
    def url(self):
        return 'http://www.arcamax.com/thefunnies/' + self.path + '/'


# do not edit anything below since these entries are generated from
# scripts/update_plugins.sh
# DO NOT REMOVE
# 9ChickweedLane has a duplicate in GoComics/9ChickweedLane
# Agnes has a duplicate in GoComics/Agnes
# AndyCapp has a duplicate in GoComics/AndyCapp
# Archie has a duplicate in Creators/Archie


class ArcticCircle(_Arcamax):
    path = 'arcticcircle'
# AskShagg has a duplicate in GoComics/AskShagg


class BabyBlues(_Arcamax):
    path = 'babyblues'
# BallardStreet has a duplicate in GoComics/BallardStreet
# BarneyAndClyde has a duplicate in GoComics/BarneyAndClyde


class BarneyGoogleAndSnuffySmith(_Arcamax):
    path = 'barneygoogle'
# BC has a duplicate in GoComics/BC


class BeetleBailey(_Arcamax):
    path = 'beetlebailey'


class Bizarro(_Arcamax):
    path = 'bizarro'
# BleekerTheRechargeableDog has a duplicate in GoComics/BleekerTheRechargeableDog


class Blondie(_Arcamax):
    path = 'blondie'


class Boondocks(_Arcamax):
    path = 'boondocks'


class BrilliantMindOfEdisonLee(_Arcamax):
    path = 'brilliantmindofedisonlee'
# Candorville has a duplicate in GoComics/Candorville


class CarpeDiem(_Arcamax):
    path = 'carpediem'
# Cathy has a duplicate in GoComics/Cathy
# ChipBok has a duplicate in GoComics/ChipBok
# ChuckleBros has a duplicate in GoComics/ChuckleBros
# ClayBennett has a duplicate in GoComics/ClayBennett


class Crankshaft(_Arcamax):
    path = 'crankshaft'
# CulDeSac has a duplicate in GoComics/CulDeSac


class Curtis(_Arcamax):
    path = 'curtis'
# DaddysHome has a duplicate in GoComics/DaddysHome
# DarrinBell has a duplicate in GoComics/DarrinBell


class DeFlocked(_Arcamax):
    path = 'deflocked'


class DennisTheMenace(_Arcamax):
    path = 'dennisthemenace'
# DiamondLil has a duplicate in GoComics/DiamondLil
# Dilbert has a duplicate in Dilbert


class DinetteSet(_Arcamax):
    path = 'thedinetteset'
# DogEatDoug has a duplicate in GoComics/DogEatDoug
# DogsOfCKennel has a duplicate in GoComics/DogsOfCKennel
# Doonesbury has a duplicate in GoComics/Doonesbury


class Dustin(_Arcamax):
    path = 'dustin'


class FamilyCircus(_Arcamax):
    path = 'familycircus'
# FloAndFriends has a duplicate in GoComics/FloAndFriends
# ForBetterOrForWorse has a duplicate in GoComics/ForBetterOrForWorse
# ForHeavensSake has a duplicate in GoComics/ForHeavensSake
# FortKnox has a duplicate in GoComics/FortKnox
# FreeRange has a duplicate in GoComics/FreeRange
# Garfield has a duplicate in GoComics/Garfield
# GetFuzzy has a duplicate in GoComics/GetFuzzy
# HagarTheHorrible has a duplicate in HagarTheHorrible
# Heathcliff has a duplicate in GoComics/Heathcliff
# HerbAndJamaal has a duplicate in GoComics/HerbAndJamaal


class HiAndLois(_Arcamax):
    path = 'hiandlois'


class IntelligentLife(_Arcamax):
    path = 'intelligentlife'


class JerryKingCartoons(_Arcamax):
    path = 'humorcartoon'
# LisaBenson has a duplicate in GoComics/LisaBenson
# LittleDogLost has a duplicate in GoComics/LittleDogLost
# LongStoryShort has a duplicate in Creators/LongStoryShort
# LooseParts has a duplicate in GoComics/LooseParts
# Luann has a duplicate in GoComics/Luann


class MallardFillmore(_Arcamax):
    path = 'mallardfillmore'


class Marvin(_Arcamax):
    path = 'marvin'


class MasterStrokesGolfTips(_Arcamax):
    path = 'masterstrokes'


class MeaningOfLila(_Arcamax):
    path = 'meaningoflila'
# MichaelRamirez has a duplicate in GoComics/MichaelRamirez
# MikeDuJour has a duplicate in GoComics/MikeDuJour
# MikeLester has a duplicate in GoComics/MikeLester
# MikeLuckovich has a duplicate in GoComics/MikeLuckovich
# Momma has a duplicate in GoComics/Momma


class MotherGooseAndGrimm(_Arcamax):
    path = 'mothergooseandgrimm'


class Mutts(_Arcamax):
    path = 'mutts'
# NestHeads has a duplicate in GoComics/NestHeads
# NickAnderson has a duplicate in GoComics/NickAnderson
# NonSequitur has a duplicate in GoComics/NonSequitur
# OneBigHappy has a duplicate in GoComics/OneBigHappy
# Peanuts has a duplicate in GoComics/Peanuts
# PearlsBeforeSwine has a duplicate in GoComics/PearlsBeforeSwine
# Pickles has a duplicate in GoComics/Pickles
# RedAndRover has a duplicate in GoComics/RedAndRover
# ReplyAll has a duplicate in GoComics/ReplyAll


class RhymesWithOrange(_Arcamax):
    path = 'rhymeswithorange'
# Rubes has a duplicate in GoComics/Rubes
# RudyPark has a duplicate in GoComics/RudyPark
# Rugrats has a duplicate in Creators/Rugrats
# ScaryGary has a duplicate in GoComics/ScaryGary
# Shoe has a duplicate in GoComics/Shoe
# SigneWilkinson has a duplicate in GoComics/SigneWilkinson
# SpeedBump has a duplicate in GoComics/SpeedBump
# SteveBenson has a duplicate in GoComics/SteveBenson
# SteveBreen has a duplicate in GoComics/SteveBreen
# StrangeBrew has a duplicate in GoComics/StrangeBrew


class TakeItFromTheTinkersons(_Arcamax):
    path = 'takeitfromthetinkersons'
# TheBarn has a duplicate in GoComics/TheBarn


class TheLockhorns(_Arcamax):
    path = 'thelockhorns'
# TheOtherCoast has a duplicate in GoComics/TheOtherCoast


class TinasGroove(_Arcamax):
    path = 'tinasgroove'
# WeePals has a duplicate in GoComics/WeePals
# WizardOfId has a duplicate in GoComics/WizardOfId
# WorkingItOut has a duplicate in GoComics/WorkingItOut
# Wumo has a duplicate in GoComics/WuMo
# ZackHill has a duplicate in GoComics/ZackHill


class Zits(_Arcamax):
    path = 'zits'

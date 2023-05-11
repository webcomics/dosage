# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
from ..scraper import ParserScraper


class Arcamax(ParserScraper):
    imageSearch = '//img[@id="comic-zoom"]'
    prevSearch = '//a[@class="prev"]'

    def __init__(self, name, path):
        super().__init__('Arcamax/' + name)
        self.url = 'http://www.arcamax.com/thefunnies/' + path + '/'

    @classmethod
    def getmodules(cls):
        return (
            # do not edit anything below since these entries are generated from
            # scripts/arcamax.py
            # START AUTOUPDATE
            # 9ChickweedLane has a duplicate in GoComics/9ChickweedLane
            # Agnes has a duplicate in GoComics/Agnes
            # AndyCapp has a duplicate in GoComics/AndyCapp
            # Archie has a duplicate in Creators/Archie
            cls('ArcticCircle', 'arcticcircle'),
            # AskShagg has a duplicate in GoComics/AskShagg
            cls('BabyBlues', 'babyblues'),
            # BallardStreet has a duplicate in GoComics/BallardStreet
            # BarneyAndClyde has a duplicate in GoComics/BarneyAndClyde
            cls('BarneyGoogleAndSnuffySmith', 'barneygoogle'),
            # BC has a duplicate in GoComics/BC
            cls('BeetleBailey', 'beetlebailey'),
            cls('Bizarro', 'bizarro'),
            # BleekerTheRechargeableDog has a duplicate in GoComics/BleekerTheRechargeableDog
            cls('Blondie', 'blondie'),
            cls('Boondocks', 'boondocks'),
            cls('BrilliantMindOfEdisonLee', 'brilliantmindofedisonlee'),
            # Candorville has a duplicate in GoComics/Candorville
            cls('CarpeDiem', 'carpediem'),
            # Cathy has a duplicate in GoComics/Cathy
            # ChipBok has a duplicate in GoComics/ChipBok
            # ChuckleBros has a duplicate in GoComics/ChuckleBros
            # ClayBennett has a duplicate in GoComics/ClayBennett
            cls('Crankshaft', 'crankshaft'),
            # CulDeSac has a duplicate in GoComics/CulDeSac
            cls('Curtis', 'curtis'),
            # DaddysHome has a duplicate in GoComics/DaddysHome
            # DarrinBell has a duplicate in GoComics/DarrinBell
            cls('DennisTheMenace', 'dennisthemenace'),
            # DiamondLil has a duplicate in GoComics/DiamondLil
            cls('DinetteSet', 'thedinetteset'),
            # DogEatDoug has a duplicate in GoComics/DogEatDoug
            # DogsOfCKennel has a duplicate in GoComics/DogsOfCKennel
            # Doonesbury has a duplicate in GoComics/Doonesbury
            cls('Dustin', 'dustin'),
            cls('FamilyCircus', 'familycircus'),
            # FloAndFriends has a duplicate in GoComics/FloAndFriends
            # ForBetterOrForWorse has a duplicate in GoComics/ForBetterOrForWorse
            # ForHeavensSake has a duplicate in GoComics/ForHeavensSake
            # FortKnox has a duplicate in GoComics/FortKnox
            # FreeRange has a duplicate in GoComics/FreeRange
            # Garfield has a duplicate in GoComics/Garfield
            # GetFuzzy has a duplicate in GoComics/GetFuzzy
            # Heathcliff has a duplicate in GoComics/Heathcliff
            # HerbAndJamaal has a duplicate in GoComics/HerbAndJamaal
            cls('HiAndLois', 'hiandlois'),
            cls('JerryKingCartoons', 'humorcartoon'),
            # LisaBenson has a duplicate in GoComics/LisaBenson
            # LittleDogLost has a duplicate in GoComics/LittleDogLost
            # LongStoryShort has a duplicate in Creators/LongStoryShort
            # LooseParts has a duplicate in GoComics/LooseParts
            # Luann has a duplicate in GoComics/Luann
            cls('MallardFillmore', 'mallardfillmore'),
            cls('Marvin', 'marvin'),
            cls('MasterStrokesGolfTips', 'masterstrokes'),
            cls('MeaningOfLila', 'meaningoflila'),
            # MichaelRamirez has a duplicate in GoComics/MichaelRamirez
            # MikeDuJour has a duplicate in GoComics/MikeDuJour
            # MikeLester has a duplicate in GoComics/MikeLester
            # MikeLuckovich has a duplicate in GoComics/MikeLuckovich
            # Momma has a duplicate in GoComics/Momma
            cls('MotherGooseAndGrimm', 'mothergooseandgrimm'),
            cls('Mutts', 'mutts'),
            # NestHeads has a duplicate in GoComics/NestHeads
            # NickAnderson has a duplicate in GoComics/NickAnderson
            # NonSequitur has a duplicate in GoComics/NonSequitur
            # OneBigHappy has a duplicate in GoComics/OneBigHappy
            # Peanuts has a duplicate in GoComics/Peanuts
            # PearlsBeforeSwine has a duplicate in GoComics/PearlsBeforeSwine
            # Pickles has a duplicate in GoComics/Pickles
            # RedAndRover has a duplicate in GoComics/RedAndRover
            # ReplyAll has a duplicate in GoComics/ReplyAll
            cls('RhymesWithOrange', 'rhymeswithorange'),
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
            cls('TakeItFromTheTinkersons', 'takeitfromthetinkersons'),
            # TheBarn has a duplicate in GoComics/TheBarn
            cls('TheLockhorns', 'thelockhorns'),
            # TheOtherCoast has a duplicate in GoComics/TheOtherCoast
            # WeePals has a duplicate in GoComics/WeePals
            # WizardOfId has a duplicate in GoComics/WizardOfId
            # WorkingItOut has a duplicate in GoComics/WorkingItOut
            # Wumo has a duplicate in GoComics/WuMo
            # ZackHill has a duplicate in GoComics/ZackHill
            cls('Zits', 'zits'),
            # END AUTOUPDATE
        )

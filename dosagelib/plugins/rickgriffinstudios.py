# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
from ..helpers import indirectStarter
from ..scraper import ParserScraper
from .common import WordPressScraper


class Housepets(WordPressScraper):
    url = 'https://www.housepetscomic.com/'
    stripUrl = url + 'comic/%s/'
    firstStripUrl = '2008/06/02/when-boredom-strikes'


class RickGriffinStudios(ParserScraper):
    imageSearch = '//img[@id="comic-image"]'
    prevSearch = '//a[@id="previous-button"]'
    latestSearch = '//a[@id="last-button"]'
    starter = indirectStarter
    nav = None

    def __init__(self, name, sub):
        super().__init__('RickGriffinStudios/' + name)
        self.stripUrl = 'https://rickgriffinstudios.com/' + sub + '/comic/%s/'
        self.url = self.firstStripUrl = self.stripUrl % '001'

    @classmethod
    def getmodules(cls):
        return (
            cls('AHClub', 'ah-club'),
            cls('HayvenCelestia', 'skinchange'),
            cls('TheStoryboard', 'the-storyboard'),
            cls('TheWitchOfKurikuto', 'the-witch-of-kurikuto'),
            cls('TracesOfThePast', 'traces-of-the-past'),
            cls('ZootopiaNightTerrors', 'zootopia-night-terrors'),
        )

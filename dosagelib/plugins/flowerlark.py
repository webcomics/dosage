# SPDX-License-Identifier: MIT
# Copyright (C) 2021 Tobias Gruetzmacher
from ..helpers import indirectStarter
from .common import WordPressScraper


class FlowerlarkStudios(WordPressScraper):
    starter = indirectStarter

    def __init__(self, name, sub):
        super().__init__(name)

        self.url = 'https://www.flowerlarkstudios.com/comic/%s/' % sub
        self.firstStripUrl = self.url

    @classmethod
    def getmodules(cls):
        return (
            cls('Ashes', 'prologue/vol-1-ashes'),
            cls('EasilyAmused', 'adulting-is-hard/making-a-splash'),
            cls('Eryl', 'opening/intro-to-dark-wings'),
            cls('NoMoreSavePoints', 'no-more-save-points/mushroom-hopping'),
        )

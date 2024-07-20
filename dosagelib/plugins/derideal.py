# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
# SPDX-FileCopyrightText: © 2019 Daniel Ring
import itertools

from ..scraper import ParserScraper
from ..helpers import indirectStarter, joinPathPartsNamer


class Derideal(ParserScraper):
    baseUrl = 'https://derideal.com/'
    imageSearch = '//img[d:class("comic-page") or d:class("comic-pag")]'
    prevSearch = '//a[text()="<"]'
    starter = indirectStarter
    namer = joinPathPartsNamer(imageparts=range(-3, 0))

    def __init__(self, name, lang, sub, first, eol=False, multi=False):
        if lang == 'en':
            base = 'Derideal'
            lateststr = 'Read latest update'
        else:
            base = 'DeridealSpanish'
            sub = f'{lang}/{sub}'
            lateststr = 'Leer última actualización'

        if not name:
            super().__init__(base)
        else:
            super().__init__(f'{base}/{name}')

        self.url = f'{self.baseUrl}{sub}'
        self.firstStripUrl = f'{self.url}/{first}/'
        self.latestSearch = f'//a[contains(text(), "{lateststr}")]'
        self.lang = lang
        self.endOfLife = eol
        self.multipleImagesPerStrip = multi

    @classmethod
    def getmodules(cls):
        return itertools.chain.from_iterable((
            cls('', lang, 'derideal', 'chimeras-cover'),
            cls('Legacy', lang, 'derideal-legacy', 'the-dream-cover', eol=True),
            cls('LostMemories', lang, 'lost-memories', 'lost-memories-pixi', multi=True),
            cls('Nova', lang, 'nova', 'xen-prelude-cover'),
            cls('ProjectPrime', lang, 'project-prime', 'custus-part-i-cover'),
            cls('PurpurinaEffect', lang, 'purpurina-effect', 'purpurina-effect-cover'),
            cls('RLE', lang, 'RLE', 'the-leyend-of-the-rose-cover'),
            cls('TheVoid', lang, 'the-void', 'the-void-cover'),
        ) for lang in ('en', 'es'))

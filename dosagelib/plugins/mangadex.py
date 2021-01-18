# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2021 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
import json

from ..scraper import _ParserScraper


class MangaDex(_ParserScraper):
    imageSearch = '//img[contains(@class, "_images")]/@data-url'
    prevSearch = '//a[contains(@class, "_prevEpisode")]'
    multipleImagesPerStrip = True

    def __init__(self, name, mangaid):
        super(MangaDex, self).__init__('MangaDex/' + name)

        baseUrl = 'https://mangadex.org/api/'
        self.url = baseUrl + '?id=%s&type=manga' % str(mangaid)
        self.stripUrl = baseUrl + '?id=%s&type=chapter'

    def starter(self):
        # Retrieve manga metadata from API
        manga = self.session.get(self.url)
        manga.raise_for_status()
        mangaData = manga.json()
        # Determine if manga is complete and/or adult
        if mangaData['manga']['last_chapter'] != '0':
            self.endOfLife = True
        if mangaData['manga']['hentai'] != '0':
            self.adult = True
        # Prepare chapter list
        self.chapters = []
        for ch in mangaData['chapter']:
            if mangaData['chapter'][ch]['lang_code'] != 'gb':
                continue
            if len(self.chapters) < 1:
                self.chapters.append(ch)
                continue
            if mangaData['chapter'][ch]['chapter'] == mangaData['chapter'][self.chapters[-1]]['chapter']:
                continue
            if mangaData['chapter'][ch]['chapter'] == '':
                continue
            self.chapters.append(ch)
        self.chapters.reverse()
        # Find first and last chapter
        self.firstStripUrl = self.stripUrl % self.chapters[0]
        return self.stripUrl % self.chapters[-1]

    def getPrevUrl(self, url, data):
        chapter = url.replace('&type=chapter', '').rsplit('=', 1)[-1]
        return self.stripUrl % self.chapters[self.chapters.index(chapter) - 1]

    def fetchUrls(self, url, data, urlSearch):
        # Retrieve chapter metadata from API
        chapterData = json.loads(data.text_content())
        self.chapter = chapterData['chapter']
        # Save link order for position-based filenames
        imageUrl = chapterData['server'] + chapterData['hash'] + '/%s'
        self.imageUrls = [imageUrl % page for page in chapterData['page_array']]
        return self.imageUrls

    def namer(self, imageUrl, pageUrl):
        # Construct filename from episode number and page index in array
        chapterNum = self.chapter
        pageNum = self.imageUrls.index(imageUrl)
        pageExt = imageUrl.rsplit('.')[-1]
        return '%s-%02d.%s' % (chapterNum, pageNum, pageExt)

    @classmethod
    def getmodules(cls):
        return (
            cls('AttackonTitan', 429),
            cls('Beastars', 20523),
            cls('BokuNoKokoroNoYabaiYatsu', 23811),
            cls('DeliciousinDungeon', 13871),
            cls('DragonDrive', 5165),
            cls('FuguushokuKajishiDakedoSaikyouDesu', 56319),
            cls('HangingOutWithAGamerGirl', 42490),
            cls('HoriMiya', 6770),
            cls('HowToOpenATriangularRiceball', 19305),
            cls('InterspeciesReviewers', 20796),
            cls('JahySamaWaKujikenai', 22369),
            cls('JingaiNoYomeToIchaIchaSuru', 22651),
            cls('KawaiiJoushiWoKomarasetai', 17910),
            cls('KanojoOkarishimasu', 22151),
            cls('Lv2KaraCheatDattaMotoYuushaKouhoNoMattariIsekaiLife', 33797),
            cls('MaouNoOreGaDoreiElfWoYomeNiShitandaGaDouMederebaIi', 25495),
            cls('ModernMoGal', 30308),
            cls('MyTinySenpaiFromWork', 43610),
            cls('OMaidensinYourSavageSeason', 22030),
            cls('OokamiShounenWaKyouMoUsoOKasaneru', 14569),
            cls('OokamiToKoshinryou', 1168),
            cls('OtomeYoukaiZakuro', 4533),
            cls('OversimplifiedSCP', 32834),
            cls('PashiriNaBokuToKoisuruBanchouSan', 25862),
            cls('PleaseDontBullyMeNagatoro', 22631),
            cls('PleaseDontBullyMeNagatoroComicAnthology', 31004),
            cls('PleaseTellMeGalkochan', 12702),
            cls('SaekiSanWaNemutteru', 28834),
            cls('SenpaiGaUzaiKouhaiNoHanashi', 23825),
            cls('SewayakiKitsuneNoSenkoSan', 22723),
            cls('SousouNoFrieren', 48045),
            cls('SwordArtOnline', 1360),
            cls('SwordArtOnlineProgressive', 9604),
            cls('TamenDeGushi', 13939),
            cls('TheWolfAndRedRidingHood', 31079),
            cls('TomoChanWaOnnanoko', 15722),
            cls('TonikakuKawaii', 23439),
            cls('YotsubaAnd', 311),
            cls('YuYuHakusho', 1738),
        )

# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
import json

from ..scraper import ParserScraper


class MangaDex(ParserScraper):
    multipleImagesPerStrip = True

    def __init__(self, name, mangaId):
        super().__init__('MangaDex/' + name)

        baseUrl = 'https://api.mangadex.org/'
        self.url = baseUrl + 'manga/%s' % mangaId
        self.chaptersUrl = baseUrl + 'manga/%s/feed?translatedLanguage[]=en&order[chapter]=desc&limit=500' % mangaId
        self.stripUrl = baseUrl + 'chapter/%s'
        self.cdnUrl = baseUrl + 'at-home/server/%s'
        self.imageUrl = 'https://uploads.mangadex.org/data/%s/%%s'

    def starter(self):
        # Retrieve manga metadata from API
        mangaData = self.session.get(self.url)
        mangaData.raise_for_status()
        manga = mangaData.json()['data']

        # Retrieve chapter list from API
        chapterList = []
        chapterTotal = 1
        chapterOffset = 0
        while len(chapterList) < chapterTotal:
            chapterData = self.session.get(self.chaptersUrl + '&offset=%d' % chapterOffset)
            chapterData.raise_for_status()
            chapterBlock = chapterData.json()
            chapterTotal = chapterBlock['total']
            chapterOffset = chapterBlock['offset'] + chapterBlock['limit']
            chapterList.extend(chapterBlock['data'])

        # Determine if manga is complete and/or adult
        if manga['attributes']['lastChapter'] != '0':
            for chapter in chapterList:
                if chapter['attributes']['chapter'] == manga['attributes']['lastChapter']:
                    self.endOfLife = True
                    break

        if manga['attributes']['contentRating'] != 'safe':
            self.adult = True

        # Prepare chapter list
        self.chapters = []
        for chapter in chapterList:
            if chapter['attributes']['chapter'] == '':
                continue
            if chapter['attributes']['pages'] == 0:
                continue
            if len(self.chapters) >= 1 and chapter['attributes']['chapter'] == self.chapters[-1]['attributes']['chapter']:
                continue
            self.chapters.append(chapter)
        self.chapters.reverse()

        # Find first and last chapter
        self.firstStripUrl = self.stripUrl % self.chapters[0]['id']
        return self.stripUrl % self.chapters[-1]['id']

    def getPrevUrl(self, url, data):
        # Determine previous chapter ID from cached list
        chapterId = url.rsplit('/', 1)[-1]
        chapter = list(filter(lambda c: c['id'] == chapterId, self.chapters))
        if len(chapter) == 0:
            return None
        return self.stripUrl % self.chapters[self.chapters.index(chapter[0]) - 1]['id']

    def fetchUrls(self, url, data, urlSearch):
        # Retrieve chapter metadata from API
        chapterData = json.loads(data.text_content())
        self.chapter = chapterData['data']
        cdnData = self.session.get(self.cdnUrl % self.chapter['id'])
        cdnData.raise_for_status()
        cdnBlock = cdnData.json()

        # Save link order for position-based filenames
        imageUrl = self.imageUrl % cdnBlock['chapter']['hash']
        self.imageUrls = [imageUrl % page for page in cdnBlock['chapter']['data']]
        return self.imageUrls

    def namer(self, imageUrl, pageUrl):
        # Construct filename from episode number and page index in array
        chapter = self.chapter['attributes']['chapter']
        chapterNum = chapter if chapter is not None else 0
        pageNum = self.imageUrls.index(imageUrl)
        pageExt = imageUrl.rsplit('.')[-1]
        return '%s-%02d.%s' % (chapterNum, pageNum, pageExt)

    @classmethod
    def getmodules(cls):
        return (
            cls('AttackOnTitan', '304ceac3-8cdb-4fe7-acf7-2b6ff7a60613'),
            cls('Beastars', 'f5e3baad-3cd4-427c-a2ec-ad7d776b370d'),
            cls('BokuNoKokoroNoYabaiYatsu', '3df1a9a3-a1be-47a3-9e90-9b3e55b1d0ac'),
            cls('CheerfulAmnesia', 'f9448f90-c068-4b6a-8c85-03d739aef255'),
            cls('DoChokkyuuKareshiXKanojo', 'efb62763-c940-4495-aba5-69c192a999a4'),
            cls('DeliciousinDungeon', 'd90ea6cb-7bc3-4d80-8af0-28557e6c4e17'),
            cls('DragonDrive', '5c06ae70-b5cf-431a-bcd5-262a411de527'),
            cls('FuguushokuKajishiDakedoSaikyouDesu', '17b3b648-fd89-4a69-9a42-6068ffbfa7a7'),
            cls('GanbareDoukiChan', '190616bc-7da6-45fd-abd4-dd2ca656c183'),
            cls('HangingOutWithAGamerGirl', 'de9e3b62-eac5-4c0a-917d-ffccad694381'),
            cls('HoriMiya', 'a25e46ec-30f7-4db6-89df-cacbc1d9a900'),
            cls('HowToOpenATriangularRiceball', '6ebd90ce-d5e8-49c0-a4bc-e02e0f8ecb93'),
            cls('HunterXHunter', 'db692d58-4b13-4174-ae8c-30c515c0689c'),
            cls('IchaichasuruToOkaneGaWaichauFutariNoHanashi', '8eaaec7d-7aa7-490e-8d52-5a3d0a28e78b'),
            cls('InterspeciesReviewers', '1b2fddf9-1385-4f3c-b37a-cf86a9428b1a'),
            cls('JahySamaWaKujikenai', '2f4e5f5b-d930-4266-8c8a-c4cf9a81e51f'),
            cls('JingaiNoYomeToIchaIchaSuru', '809d2493-df3c-4e72-a57e-3e0026cae9fb'),
            cls('KaetteKudasaiAkutsuSan', '737a846b-2e67-4d63-9f7e-f54b3beebac4'),
            cls('KawaiiJoushiWoKomarasetai', '23b7cc7a-df89-4049-af28-1fa78f88713e'),
            cls('KanojoOkarishimasu', '32fdfe9b-6e11-4a13-9e36-dcd8ea77b4e4'),
            cls('KoiToUtatane', 'f7d40a27-e289-45b3-9c68-d1cb251897e6'),
            cls('Lv2KaraCheatDattaMotoYuushaKouhoNoMattariIsekaiLife', '58bc83a0-1808-484e-88b9-17e167469e23'),
            cls('MaouNoOreGaDoreiElfWoYomeNiShitandaGaDouMederebaIi', '55ace2fb-e157-4d76-9e72-67c6bd762a39'),
            cls('ModernMoGal', 'b1953f80-36f7-492c-b0f8-e9dd0ad01752'),
            cls('MyTinySenpaiFromWork', '28ed63af-61f8-43af-bac3-762030c72963'),
            cls('OMaidensinYourSavageSeason', 'c4613b7d-7a6e-48f9-82f0-bce3dd33383a'),
            cls('OokamiShounenWaKyouMoUsoOKasaneru', '5e77d9e2-2e44-431a-a995-5fefd411e55e'),
            cls('OokamiToKoshinryou', 'de900fd3-c94c-4148-bbcb-ca56eaeb57a4'),
            cls('OtomeYoukaiZakuro', 'c1fa97be-0f1f-4686-84bc-806881c97d53'),
            cls('OversimplifiedSCP', 'e911fe33-a9b3-43dc-9eb7-f5ee081a6dc8'),
            cls('PashiriNaBokuToKoisuruBanchouSan', '838e5b3a-51c8-44cf-b6e2-68193416f6fe'),
            cls('PleaseDontBullyMeNagatoro', 'd86cf65b-5f6c-437d-a0af-19a31f94ec55'),
            cls('PleaseDontBullyMeNagatoroComicAnthology', '2a4bc9ec-2d70-428a-8b46-27f6218ed267'),
            cls('PleaseTellMeGalkochan', '7a2f2f6b-a6a6-4149-879b-3fc2f6916549'),
            cls('RebuildWorld', '99182618-ae92-4aec-a5df-518659b7b613'),
            cls('SaekiSanWaNemutteru', 'd9aecdab-8aef-4b90-98d5-32e86faffb28'),
            cls('SeijoSamaIieToorisugariNoMamonotsukaiDesu', 'd4c40e73-251a-4bcb-a5a6-1edeec1e00e7'),
            cls('SenpaiGaUzaiKouhaiNoHanashi', 'af38f328-8df1-4b4c-a272-e737625c3ddc'),
            cls('SewayakiKitsuneNoSenkoSan', 'c26269c7-0f5d-4966-8cd5-b79acb86fb7a'),
            cls('ShinNoJitsuryokuWaGirigiriMadeKakushiteIyouToOmou', '22fda941-e603-4601-a536-c3ad6d004ba8'),
            cls('SoloLeveling', '32d76d19-8a05-4db0-9fc2-e0b0648fe9d0'),
            cls('SousouNoFrieren', 'b0b721ff-c388-4486-aa0f-c2b0bb321512'),
            cls('SwordArtOnline', '3dd0b814-23f4-4342-b75b-f206598534f6'),
            cls('SwordArtOnlineProgressive', '22ea3f54-11e4-4932-a527-89d63d3a62d9'),
            cls('TadokoroSan', '8ffbfa2f-23fa-4490-848e-942581a4d873'),
            cls('TamenDeGushi', '3f1453fb-9dac-4aca-a2ea-69613856c952'),
            cls('TenseiShitaraSlimeDattaKen', 'e78a489b-6632-4d61-b00b-5206f5b8b22b'),
            cls('TheNewGate', 'b41bef1e-7df9-4255-bd82-ecf570fec566'),
            cls('TheWolfAndRedRidingHood', 'a7d1283b-ed38-4659-b8bc-47bfca5ccb8a'),
            cls('TomoChanWaOnnanoko', '76ee7069-23b4-493c-bc44-34ccbf3051a8'),
            cls('TonikakuKawaii', '30f3ac69-21b6-45ad-a110-d011b7aaadaa'),
            cls('UramikoiKoiUramikoi', '009b6788-48f3-4e78-975c-097f54def7ab'),
            cls('YotsubaAnd', '58be6aa6-06cb-4ca5-bd20-f1392ce451fb'),
            cls('YuYuHakusho', '44a5cbe1-0204-4cc7-a1ff-0fda2ac004b6'),
        )

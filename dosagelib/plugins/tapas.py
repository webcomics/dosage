# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2022 Tobias Gruetzmacher
# Copyright (C) 2019-2022 Daniel Ring
from ..output import out
from ..scraper import ParserScraper
from ..xml import NS


class Tapas(ParserScraper):
    baseUrl = 'https://tapas.io/'
    imageSearch = '//article[contains(@class, "js-episode-article")]//img/@data-src'
    prevSearch = '//a[contains(@class, "js-prev-ep-btn")]'
    latestSearch = '//ul[contains(@class, "js-episode-list")]//a'
    multipleImagesPerStrip = True

    def __init__(self, name, url):
        super().__init__('Tapas/' + name)
        self.url = self.baseUrl + 'series/' + url + '/info'
        self.stripUrl = self.baseUrl + 'episode/%s'

    def starter(self):
        # Retrieve comic metadata from info page
        info = self.getPage(self.url)
        series = info.xpath('//@data-series-id')[0]
        # Retrieve comic metadata from API
        data = self.session.get(self.baseUrl + 'series/' + series + '/episodes?sort=NEWEST')
        data.raise_for_status()
        episodes = data.json()['data']['body']
        return self.stripUrl % episodes.split('data-id="')[1].split('"')[0]

    def getPrevUrl(self, url, data):
        # Retrieve comic metadata from API
        data = self.session.get(url + '/info')
        data.raise_for_status()
        apiData = data.json()['data']
        if apiData['scene'] == 2:
            self.firstStripUrl = self.stripUrl % apiData['prev_ep_id']
        return self.stripUrl % apiData['prev_ep_id']

    def fetchUrls(self, url, data, urlSearch):
        # Save link order for position-based filenames
        self.imageUrls = super().fetchUrls(url, data, urlSearch)
        return self.imageUrls

    def shouldSkipUrl(self, url, data):
        if data.xpath('//button[d:class("js-have-to-sign")]', namespaces=NS):
            out.warn(f'Nothing to download on "{url}", because a login is required.')
            return True
        return False

    def namer(self, imageUrl, pageUrl):
        # Construct filename from episode number and image position on page
        episodeNum = pageUrl.rsplit('/', 1)[-1]
        imageNum = self.imageUrls.index(imageUrl)
        imageExt = pageUrl.rsplit('.', 1)[-1]
        if len(self.imageUrls) > 1:
            filename = "%s-%d.%s" % (episodeNum, imageNum, imageExt)
        else:
            filename = "%s.%s" % (episodeNum, imageExt)
        return filename

    @classmethod
    def getmodules(cls):
        return (
            # Manually-added comics
            cls('AmpleTime', 'Ample-Time'),
            cls('FANGS', 'fangscomic'),
            cls('FishNuggets', 'Fish-Nuggets'),
            cls('HoneyAndTheMoon', 'Honey-and-the-Moon'),
            cls('InsignificantOtters', 'IOtters'),
            cls('MagicalBoy', 'magicalboy'),
            cls('NoFuture', 'NoFuture'),
            cls('OrensForge', 'OrensForge'),
            cls('RadioactivePanda', 'Radioactive-Panda'),
            cls('RavenWolf', 'RavenWolf'),
            cls('SyntheticInstinct', 'Synthetic-Instinct'),
            cls('TheCatTheVineAndTheVictory', 'The-Cat-The-Vine-and-The-Victory'),
            cls('TheInkApprentice', 'The-Ink-Apprentice'),
            cls('TheSeaInYou', 'theseainyou'),
            cls('TheSelkiesSkin', 'theselkiesskincomic'),
            cls('TheWitchsThrone', 'thewitchsthrone'),
            cls('VenturaCityDrifters', 'Ventura-City-Drifters'),

            # START AUTOUPDATE
            # END AUTOUPDATE
        )

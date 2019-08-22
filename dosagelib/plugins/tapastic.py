# SPDX-License-Identifier: MIT
# Copyright (C) 2019-2020 Tobias Gruetzmacher
# Copyright (C) 2019-2020 Daniel Ring
import json
import re

from ..scraper import _ParserScraper


class Tapastic(_ParserScraper):
    baseUrl = 'https://tapas.io/'
    imageSearch = '//article[@class="ep-contents"]//img'
    episodeIdSearch = re.compile(r'episodeId : (\d+),')
    episodeListSearch = re.compile(r'episodeList : (.*),')
    multipleImagesPerStrip = True

    def __init__(self, name, url):
        super(Tapastic, self).__init__('Tapastic/' + name)
        self.url = self.baseUrl + 'series/' + url
        self.stripUrl = self.baseUrl + 'episode/%s'

    def starter(self):
        # Retrieve series data object
        seriesPage = self.getPage(self.url)
        dataScript = seriesPage.xpath('//script[contains(text(), "var _data")]')[0].text
        # Extract episode list
        currentEpisode = self.episodeIdSearch.findall(dataScript)[0]
        self.episodeList = json.loads(self.episodeListSearch.findall(dataScript)[0])
        return self.stripUrl % currentEpisode

    def fetchUrls(self, url, data, urlSearch):
        # Save link order for position-based filenames
        self.imageUrls = super().fetchUrls(url, data, urlSearch)
        # Update firstStripUrl with the correct episode title
        if int(url.rsplit('/', 1)[-1]) == self.episodeList[0]['id']:
            self.firstStripUrl = url
        return self.imageUrls

    def getPrevUrl(self, url, data):
        episodeId = int(url.rsplit('/', 1)[-1])
        index = [i for i, ep in enumerate(self.episodeList) if ep['id'] == episodeId][0]
        if index == 0:
            return None
        return self.stripUrl % str(self.episodeList[index - 1]['id'])

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
            cls('NoFuture', 'NoFuture'),
            cls('OrensForge', 'OrensForge'),
            cls('RavenWolf', 'RavenWolf'),
            cls('TheCatTheVineAndTheVictory', 'The-Cat-The-Vine-and-The-Victory'),
            cls('TheGodsPack', 'The-Gods-Pack'),

            # START AUTOUPDATE
            # END AUTOUPDATE
        )

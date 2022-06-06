# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2022 Tobias Gruetzmacher
import responses

from dosagelib import scraper


class ATestScraper(scraper.BasicScraper):
    pass


class TestVote(object):
    @responses.activate
    def test_vote(self):
        responses.add(responses.POST, 'https://buildbox.23.gs/count/', '')

        ATestScraper('Test_Test').vote()

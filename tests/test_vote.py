# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import pytest
import requests
import responses

from dosagelib import cmd, scraper


class ATestScraper(scraper.BasicScraper):
    pass


class TestVote:
    @responses.activate
    def test_vote(self):
        responses.add(responses.POST, 'https://buildbox.23.gs/count/')

        ATestScraper('Test_Test').vote()

    @responses.activate
    def test_vote_err(self):
        responses.add(responses.POST, 'https://buildbox.23.gs/count/', status=500)

        with pytest.raises(requests.exceptions.HTTPError):
            ATestScraper('Test_Test').vote()

    @responses.activate
    def test_run_vote(self):
        responses.add(responses.POST, 'https://buildbox.23.gs/count/')

        assert cmd.main(('-v', '--vote', 'xkcd')) == 0

    @responses.activate
    def test_run_vote_err(self):
        responses.add(responses.POST, 'https://buildbox.23.gs/count/', status=500)

        assert cmd.main(('-v', '--allow-multiple', '--vote', 'xkcd')) == 1

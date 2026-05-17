# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import pytest
import requests
import responses

from dosagelib import scraper


class ATestScraper(scraper.BasicScraper):
    pass


@responses.activate
def test_vote():
    responses.add(responses.POST, 'https://buildbox.23.gs/count/')

    ATestScraper('Test_Test').vote()


@responses.activate
def test_vote_err():
    responses.add(responses.POST, 'https://buildbox.23.gs/count/', status=500)

    with pytest.raises(requests.exceptions.HTTPError):
        ATestScraper('Test_Test').vote()


@responses.activate
def test_run_vote(run):
    responses.add(responses.POST, 'https://buildbox.23.gs/count/')

    run('--vote', 'xkcd')


@responses.activate
def test_run_vote_err(run):
    responses.add(responses.POST, 'https://buildbox.23.gs/count/', status=500)

    run('--vote', 'xkcd', expected=1)

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import responses

from dosagelib import scraper
import httpmocks


class ATestScraper(scraper._BasicScraper):
    pass


class TestVote(object):

    @responses.activate
    def test_vote(self):
        httpmocks.vote()
        ATestScraper('Test_Test').vote()

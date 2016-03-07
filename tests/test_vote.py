# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
# Copyright (C) 2016 Tobias Gruetzmacher

from dosagelib import scraper


class ATestScraper(scraper._BasicScraper):
    name = 'Test_Test'


class TestVote(object):

    def test_vote(self):
        answer = ATestScraper.vote()
        assert answer in ('counted', 'no'), 'invalid answer %r' % answer

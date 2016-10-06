# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

from dosagelib import scraper


class ATestScraper(scraper._BasicScraper):
    pass


class TestVote(object):

    def test_vote(self):
        answer = ATestScraper('Test_Test').vote()
        assert answer in ('counted', 'no'), 'invalid answer %r' % answer

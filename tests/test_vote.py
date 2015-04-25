# -*- coding: iso-8859-1 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
from unittest import TestCase
from dosagelib import scraper


class ATestScraper(scraper._BasicScraper):
    name = 'Test_Test'

class TestVote(TestCase):

    def test_vote(self):
        answer = ATestScraper.vote()
        self.assertTrue(answer in ('counted', 'no'), 'invalid answer %r' % answer)

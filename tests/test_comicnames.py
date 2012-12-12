# -*- coding: iso-8859-1 -*-
# Copyright (C) 2012 Bastian Kleineidam
from unittest import TestCase
from dosagelib import scraper, util


class TestComicNames(TestCase):

    def test_names(self):
        for scraperclass in scraper.get_scrapers():
            name = scraperclass.get_name()
            self.assertTrue(name.count('/') <= 1, name)
            if '/' in name:
                comicname = name.split('/')[1]
            else:
                comicname = name
            self.assertEqual(util.asciify(comicname), comicname)

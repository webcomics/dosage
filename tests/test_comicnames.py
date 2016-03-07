# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2016 Tobias Gruetzmacher

from dosagelib import scraper, util


class TestComicNames(object):

    def test_names(self):
        for scraperclass in scraper.get_scraperclasses():
            name = scraperclass.getName()
            assert name.count('/') <= 1
            if '/' in name:
                comicname = name.split('/')[1]
            else:
                comicname = name
            assert util.asciify(comicname) == comicname

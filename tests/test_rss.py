# SPDX-License-Identifier: MIT
# Copyright (C) 2019 Tobias Gruetzmacher
import time
from dosagelib.rss import parseFeed


class TestFeed(object):
    """
    Tests for rss.py
    """

    def test_parseFeed(self):
        testTime = time.localtime(1560000000.0)
        feed = parseFeed('./tests/mocks/dailydose.rss', testTime)

        xmlBlob = feed.getXML()

        assert u'PlumedDotage - 4034.png'.encode() in xmlBlob
        assert u'PachinkoParlor - 20190626.jpg'.encode() not in xmlBlob

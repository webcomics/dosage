# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
import time

from dosagelib.rss import parseFeed


class TestFeed:
    """
    Tests for rss.py
    """

    def test_parseFeed(self):
        testTime = time.localtime(1560000000.0)
        feed = parseFeed('./tests/mocks/dailydose.rss', testTime)

        xmlBlob = feed.getXML()

        assert b'PlumedDotage - 4034.png' in xmlBlob
        assert b'PachinkoParlor - 20190626.jpg' not in xmlBlob

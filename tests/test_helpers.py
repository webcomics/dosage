# SPDX-License-Identifier: MIT
# Copyright (C) 2019 Tobias Gruetzmacher
from dosagelib.helpers import joinPathPartsNamer, queryNamer


class TestNamer(object):
    """
    Tests for comic namer.
    """

    def test_queryNamer(self):
        testurl = 'http://FOO?page=result&page2=result2'
        assert queryNamer('page')(self, testurl, "") == 'result'
        assert queryNamer('page2', True)(self, "", testurl) == 'result2'

    def test_joinPathPartsNamer(self):
        imgurl = 'https://HOST/wp-content/uploads/2019/02/tennis5wp-1.png'
        pageurl = 'https://HOST/2019/03/11/12450/'
        assert joinPathPartsNamer((0, 1, 2))(self, imgurl, pageurl) == '2019_03_11_tennis5wp-1.png'
        assert joinPathPartsNamer((0, 1, 2), (-1,), '-')(self, imgurl, pageurl) == '2019-03-11-tennis5wp-1.png'
        assert joinPathPartsNamer((0, -2), ())(self, imgurl, pageurl) == '2019_12450'

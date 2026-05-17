# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2019 Tobias Gruetzmacher
from dosagelib.helpers import joinPathPartsNamer, queryNamer


def test_queryNamer():
    testurl = 'http://FOO?page=result&page2=result2'
    assert queryNamer('page')(None, testurl, "") == 'result'
    assert queryNamer('page2', True)(None, "", testurl) == 'result2'


def test_joinPathPartsNamer():
    imgurl = 'https://HOST/wp-content/uploads/2019/02/tennis5wp-1.png'
    pageurl = 'https://HOST/2019/03/11/12450/'
    assert joinPathPartsNamer(pageparts=(0, 1, 2), imageparts=(-1,))(None,
        imgurl, pageurl) == '2019_03_11_tennis5wp-1.png'
    assert joinPathPartsNamer(pageparts=(0, 1, 2), imageparts=(-1,), joinchar='-')(None,
        imgurl, pageurl) == '2019-03-11-tennis5wp-1.png'
    assert joinPathPartsNamer(pageparts=(0, -1))(None, imgurl, pageurl) == '2019_12450'

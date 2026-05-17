# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2020 Tobias Gruetzmacher

from lxml import html

import httpmocks
from dosagelib.xml import NS

tree = html.document_fromstring(httpmocks.content('zp-222'))


def xpath(path):
    return tree.xpath(path, namespaces=NS)


def test_class_ext():
    assert len(xpath('//li[d:class("menu-item-3773")]')) == 1
    assert len(xpath('//ul[d:class("menu")]')) == 1
    assert len(xpath('//li[d:class("menu-item-object-custom")]')) == 2
    assert len(xpath('//li[d:class("menu-item")]')) == 25


def test_re_ext():
    assert len(xpath(r'//img[re:test(@src, "posters.*jpg")]')) == 1

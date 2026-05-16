# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2020 Tobias Gruetzmacher

from lxml import html

import httpmocks
from dosagelib.xml import NS

tree = html.document_fromstring(httpmocks.content('zp-222'))


class TestXML:
    def xpath(self, path):
        return tree.xpath(path, namespaces=NS)

    def test_class_ext(self):
        assert len(self.xpath('//li[d:class("menu-item-3773")]')) == 1
        assert len(self.xpath('//ul[d:class("menu")]')) == 1
        assert len(self.xpath('//li[d:class("menu-item-object-custom")]')) == 2
        assert len(self.xpath('//li[d:class("menu-item")]')) == 25

    def test_re_ext(self):
        assert len(self.xpath(r'//img[re:test(@src, "posters.*jpg")]')) == 1

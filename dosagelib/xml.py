# SPDX-License-Identifier: MIT
# Copyright (C) 2020 Tobias Gruetzmacher
from lxml import etree


NS = {
    'd': 'https://dosage.rocks/xpath',
    're': 'http://exslt.org/regular-expressions',
}


def find_by_class(context, cls):
    attributes = context.context_node.attrib
    if 'class' in attributes:
        return cls in attributes['class'].split(' ')
    return False


dosagens = etree.FunctionNamespace(NS['d'])
dosagens['class'] = find_by_class

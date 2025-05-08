# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2020 Tobias Gruetzmacher
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


def find_by_class_start(context, cls):
    """Matches elements where any class name starts with the specified string.
    This is a "workaround" for frameworks which append random stuff to class
    names when delivering static files.
    """
    attributes = context.context_node.attrib
    if 'class' in attributes:
        return any(clsname.startswith(cls) for clsname in attributes['class'].split(' '))
    return False


dosagens = etree.FunctionNamespace(NS['d'])
dosagens['class'] = find_by_class
dosagens['class_start'] = find_by_class_start

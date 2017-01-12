# -*- coding: iso-8859-1 -*-
# Copyright (C) 2016 Peter Janes
# TODO: Might be nice to categorise Comics under one Item

import xml.dom.minidom
from datetime import datetime
from time import mktime
import dateutil.parser
import email.utils
from .configuration import App

class Feed(object):
    """Write an Atom feed with comic strip images."""

    def __init__(self, title, link, description, lang='en', encoding="utf-8"):
        """Initialize Atom writer with given title, link and description."""
        self.encoding = encoding
        self.atom = xml.dom.minidom.Document()
        self.feed = self.atom.appendChild(self.atom.createElement('feed'))
        self.feed.setAttribute('xmlns', 'http://www.w3.org/2005/Atom')
        self.addElement(self.feed, 'title', title)
        altLink = self.atom.createElement('link')
        altLink.setAttribute('href', link)
        altLink.setAttribute('rel', 'self')
        self.feed.appendChild(altLink)
        self.addElement(self.feed, 'subtitle', description)
        self.addElement(self.feed, 'updated', '{0}Z'.format(datetime.now().isoformat()))
        self.addElement(self.feed, 'generator', App)
        author = self.atom.createElement('author')
        self.addElement(author, 'name', App)
        self.feed.appendChild(author)
        self.addElement(self.feed, 'id', link)

    def addElement(self, parent, tag, value):
        """Add an Atom entry."""
        elem = self.atom.createElement(tag)
        node = self.atom.createTextNode(value)
        return parent.appendChild(elem).appendChild(node)

    def addItem(self, title, link, description, date, append=True):
        """Insert an entry."""
        entry = self.atom.createElement('entry')

        self.addElement(entry, 'title', title)
        altLink = self.atom.createElement('link')
        altLink.setAttribute('rel', 'alternate')
        altLink.setAttribute('href', link)
        entry.appendChild(altLink)
        content = self.atom.createElement('content')
        content.setAttribute('type', 'xhtml')
        contentEl = xml.dom.minidom.parseString('<div>%s</div>' % description).childNodes[0]
        content.appendChild(self.atom.importNode(contentEl, True))
        entry.appendChild(content)
        self.addElement(entry, 'id', link)
        self.addElement(entry, 'updated', date)

        if append:
            self.feed.appendChild(entry)
        else:
            elems = self.feed.getElementsByTagName('entry')
            if elems:
                self.feed.insertBefore(entry, elems[0])
            else:
                self.feed.appendChild(entry)

    def write(self, path):
        """Write Atom content to file."""
        with open(path, 'wb') as f:
            f.write(self.getXML())

    def getXML(self):
        """Get Atom content in XML format."""
        return self.atom.toxml(self.encoding)


def parseFeed(filename, yesterday):
    """Parse an Atom feed and filter only entries that are newer than yesterday."""
    dom = xml.dom.minidom.parse(filename)

    getText = lambda node, tag: node.getElementsByTagName(tag)[0].childNodes[0].data
    getNode = lambda tag: dom.getElementsByTagName(tag)

    content = getNode('feed')[0] # Only one feed node

    feedTitle = getText(content, 'title')
    feedLink = getNode('link')[0].getAttribute('href')
    feedDesc = getText(content, 'subtitle')

    feed = Feed(feedTitle, feedLink, feedDesc)

    for entry in getNode('entry'):
        entryDate = dateutil.parser.parse(getText(entry, 'updated'))
        if (entryDate > datetime.fromtimestamp(mktime(yesterday))): # If newer than yesterday
            feed.addItem(getText(entry, 'title'),
                         getNode('link')[0].getAttribute('href'),
                         entry.getElementsByTagName('content')[0].toxml(),
                         getText(entry, 'updated'))
    return feed

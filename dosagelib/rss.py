# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2015-2017 Tobias Gruetzmacher
import xml.dom.minidom
import time
from .configuration import App

# TODO: Not sure if this RSS output is "valid", should be though.
#       Might also be nice categorise Comics under one Item


class Feed(object):
    """Write an RSS feed with comic strip images."""

    def __init__(self, title, link, description, lang='en-us', encoding="utf-8"):
        """Initialize RSS writer with given title, link and description."""
        self.encoding = encoding
        self.rss = xml.dom.minidom.Document()
        root = self.rss.appendChild(self.rss.createElement('rss'))
        root.setAttribute('version', '2.0')
        self.channel = root.appendChild(self.rss.createElement('channel'))
        self.addElement(self.channel, 'title', title)
        self.addElement(self.channel, 'link', link)
        self.addElement(self.channel, 'language', lang)
        self.addElement(self.channel, 'description', description)
        self.addElement(self.channel, 'generator', App)

    def addElement(self, parent, tag, value):
        """Add an RSS item."""
        elem = self.rss.createElement(tag)
        node = self.rss.createTextNode(value)
        return parent.appendChild(elem).appendChild(node)

    def addItem(self, title, link, description, date, append=True):
        """Insert an item."""
        item = self.rss.createElement('item')

        self.addElement(item, 'title', title)
        self.addElement(item, 'link', link)
        self.addElement(item, 'description', description)
        self.addElement(item, 'guid', link)
        self.addElement(item, 'pubDate', date)

        if append:
            self.channel.appendChild(item)
        else:
            elems = self.rss.getElementsByTagName('item')
            if elems:
                self.channel.insertBefore(item, elems[0])
            else:
                self.channel.appendChild(item)

    def write(self, path):
        """Write RSS content to file."""
        with open(path, 'wb') as f:
            f.write(self.getXML())

    def getXML(self):
        """Get RSS content in XML format."""
        return self.rss.toxml(self.encoding)


def parseFeed(filename, yesterday):
    """Parse an RSS feed and filter only entries that are newer than yesterday."""
    dom = xml.dom.minidom.parse(filename)

    def getText(node, tag):
        return node.getElementsByTagName(tag)[0].childNodes[0].data

    def getNode(tag):
        return dom.getElementsByTagName(tag)

    content = getNode('channel')[0]  # Only one channel node

    feedTitle = getText(content, 'title')
    feedLink = getText(content, 'link')
    feedDesc = getText(content, 'description')

    feed = Feed(feedTitle, feedLink, feedDesc)

    for item in getNode('item'):
        itemDate = time.strptime(getText(item, 'pubDate'), '%a, %d %b %Y %H:%M:%S GMT')
        if (itemDate > yesterday):  # If newer than yesterday
            feed.addItem(getText(item, 'title'),
                         getText(item, 'link'),
                         getText(item, 'description'),
                         getText(item, 'pubDate'))
    return feed

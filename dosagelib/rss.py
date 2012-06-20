# TODO: Not sure if this RSS output is "valid", should be though.
#       Might also be nice categorise Comics under one Item

import xml.dom.minidom
import time

class Feed(object):
    def __init__(self, title, link, description, lang='en-us'):
        self.rss = xml.dom.minidom.Document()

        rss_root = self.rss.appendChild(self.rss.createElement('rss'))
        rss_root.setAttribute('version', '2.0')

        self.channel = rss_root.appendChild(self.rss.createElement('channel'))

        self.addElement(self.channel, 'title', title)
        self.addElement(self.channel, 'link', link)
        self.addElement(self.channel, 'language', lang)
        self.addElement(self.channel, 'description', description)

    def RFC822Date(data):
        return time.strftime('%a, %d %b %Y %H:%M:%S GMT', data)

    def addElement(self, parent, tag, value):
        return parent.appendChild(self.rss.createElement(tag)).appendChild(self.rss.createTextNode(value))

    def insertHead(self, title, link, description, date):
        item = self.rss.createElement('item')

        self.addElement(item, 'title', title)
        self.addElement(item, 'link', link)
        self.addElement(item, 'description', description)
        self.addElement(item, 'pubDate', date)

        elems = self.rss.getElementsByTagName('item')
        if elems:
            self.channel.insertBefore(item, elems[0])
        else:
            self.channel.appendChild(item)

    def addItem(self, title, link, description, date):
        item = self.rss.createElement('item')

        self.addElement(item, 'title', title)
        self.addElement(item, 'link', link)
        self.addElement(item, 'description', description)
        self.addElement(item, 'pubDate', date)

        self.channel.appendChild(item)

    def write(self, path):
        file = open(path, 'w')
        file.write(self.getXML())
        file.close()

    def getXML(self):
        return self.rss.toxml()

def parseFeed(filename, yesterday):
    dom = xml.dom.minidom.parse(filename)

    getText = lambda node, tag: node.getElementsByTagName(tag)[0].childNodes[0].data
    getNode = lambda tag: dom.getElementsByTagName(tag)

    content = getNode('channel')[0] # Only one channel node

    feedTitle = getText(content, 'title')
    feedLink = getText(content, 'link')
    feedDesc = getText(content, 'description')

    feed = Feed(feedTitle, feedLink, feedDesc)

    for item in getNode('item'):
        itemDate = time.strptime(getText(item, 'pubDate'), '%a, %d %b %Y %H:%M:%S GMT')
        if (itemDate > yesterday): # If newer than yesterday
            feed.addItem(getText(item, 'title'),
                         getText(item, 'link'),
                         getText(item, 'description'),
                         getText(item, 'pubDate'))
    return feed

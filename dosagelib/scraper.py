# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
import requests
import time
import random
import os
import re
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

try:
    from lxml import html
    from lxml.html.defs import link_attrs as html_link_attrs
except ImportError:
    html = None

try:
    import cssselect
except ImportError:
    cssselect = None

try:
    import pycountry
except ImportError:
    pycountry = None

from . import loader, configuration, util, languages
from .util import (getPageContent, makeSequence, get_system_uid, urlopen,
        getDirname, unescape, tagre, normaliseURL, prettyMatcherList)
from .comic import ComicStrip
from .output import out
from .events import getHandler


class Scraper(object):
    '''Base class for all comic scraper, but without a specific scrape implementation.'''

    # The URL for the comic strip
    url = None

    # A string that is interpolated with the strip index to yield the URL for a particular strip.
    stripUrl = None

    # Stop search for previous URLs at this URL
    firstStripUrl = None

    # if more than one image per URL is expected
    multipleImagesPerStrip = False

    # set to False if previous URLs do not match the strip URL (ie. because of redirects)
    prevUrlMatchesStripUrl = True

    # set to True if this comic contains adult content
    adult = False

    # set to True if this comic will not get updated anymore
    endOfLife = False

    # langauge of the comic (two-letter ISO 639-1 code)
    lang = 'en'

    # an expression that will locate the URL for the previous strip in a page
    # this can also be a list or tuple
    prevSearch = None

    # an expression that will locate the strip image URLs strip in a page
    # this can also be a list or tuple
    imageSearch = None

    # an expression to store a text together with the image
    # sometimes comic strips have additional text info for each comic
    textSearch = None

    # Is the additional text required or optional?  When it is required (the
    # default), you see an error message whenever a comic page is encountered
    # that does not have the text
    textOptional = False

    # usually the index format help
    help = ''

    # HTTP session storing cookies
    session = requests.session()

    def __init__(self, indexes=None):
        """Initialize internal variables."""
        self.urls = set()
        if indexes:
            self.indexes = tuple(sorted(indexes))
        else:
            self.indexes = tuple()
        self.skippedUrls = set()
        self.hitFirstStripUrl = False

    def __cmp__(self, other):
        """Compare scraper by name and index list."""
        if not isinstance(other, Scraper):
            return 1
        # first, order by name
        d = cmp(self.getName(), other.getName())
        if d != 0:
            return d
        # then by indexes
        return cmp(self.indexes, other.indexes)

    def __hash__(self):
        """Get hash value from name and index list."""
        return hash((self.getName(), self.indexes))

    def shouldSkipUrl(self, url, data):
        """Determine if search for images in given URL should be skipped."""
        return False

    def getComicStrip(self, url, data):
        """Get comic strip downloader for given URL and data."""
        imageUrls = self.fetchUrls(url, data, self.imageSearch)
        # map modifier function on image URLs
        imageUrls = [self.imageUrlModifier(x, data) for x in imageUrls]
        # remove duplicate URLs
        imageUrls = set(imageUrls)
        if len(imageUrls) > 1 and not self.multipleImagesPerStrip:
            out.warn(u"Found %d images instead of 1 at %s with expressions %s" % (len(imageUrls), url, prettyMatcherList(self.imageSearch)))
            image = sorted(imageUrls)[0]
            out.warn(u"Choosing image %s" % image)
            imageUrls = (image,)
        elif not imageUrls:
            out.warn(u"Found no images at %s with expressions %s" % (url, prettyMatcherList(self.imageSearch)))
        if self.textSearch:
            text = self.fetchText(url, data, self.textSearch, optional=self.textOptional)
        else:
            text = None
        return ComicStrip(self.getName(), url, imageUrls, self.namer, self.session, text=text)

    def getStrips(self, maxstrips=None):
        """Get comic strips."""
        if maxstrips:
            word = u"strip" if maxstrips == 1 else "strips"
            msg = u'Retrieving %d %s' % (maxstrips, word)
        else:
            msg = u'Retrieving all strips'
        if self.indexes:
            if len(self.indexes) == 1:
                msg += u" for index %s" % self.indexes[0]
            else:
                msg += u" for indexes %s" % self.indexes
            # Always call starter() since it might initialize cookies.
            # See for example Oglaf comic.
            self.starter()
            urls = [self.getIndexStripUrl(index) for index in self.indexes]
        else:
            urls = [self.getLatestUrl()]
        if self.adult:
            msg += u" (including adult content)"
        out.info(msg)
        for url in urls:
            for strip in self.getStripsFor(url, maxstrips):
                yield strip

    def getStripsFor(self, url, maxstrips):
        """Get comic strips for an URL. If maxstrips is a positive number, stop after
        retrieving the given number of strips."""
        self.hitFirstStripUrl = False
        seen_urls = set()
        while url:
            out.info(u'Get strip URL %s' % url, level=1)
            data = self.getPage(url)
            if self.shouldSkipUrl(url, data):
                out.info(u'Skipping URL %s' % url)
                self.skippedUrls.add(url)
            else:
                try:
                    yield self.getComicStrip(url, data)
                except ValueError as msg:
                    # image not found
                    out.exception(msg)
            if self.firstStripUrl == url:
                out.debug(u"Stop at first URL %s" % url)
                self.hitFirstStripUrl = True
                break
            if maxstrips is not None:
                maxstrips -= 1
                if maxstrips <= 0:
                    break
            prevUrl = self.getPrevUrl(url, data)
            seen_urls.add(url)
            if prevUrl in seen_urls:
                # avoid recursive URL loops
                out.warn(u"Already seen previous URL %r" % prevUrl)
                break
            url = prevUrl
            if url:
                # wait up to 2 seconds for next URL
                time.sleep(1.0 + random.random())

    def getPrevUrl(self, url, data):
        """Find previous URL."""
        prevUrl = None
        if self.prevSearch:
            try:
                prevUrl = self.fetchUrl(url, data, self.prevSearch)
            except ValueError as msg:
                # assume there is no previous URL, but print a warning
                out.warn(u"%s Assuming no previous comic strips exist." % msg)
            else:
                prevUrl = self.prevUrlModifier(prevUrl)
                out.debug(u"Found previous URL %s" % prevUrl)
                getHandler().comicPageLink(self.getName(), url, prevUrl)
        return prevUrl

    def getIndexStripUrl(self, index):
        """Get comic strip URL from index."""
        return self.stripUrl % index

    @classmethod
    def getName(cls):
        """Get scraper name."""
        if hasattr(cls, 'name'):
            return cls.name
        return cls.__name__

    @classmethod
    def starter(cls):
        """Get starter URL from where to scrape comic strips."""
        return cls.url

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Return filename for given image and page URL."""
        return None

    @classmethod
    def prevUrlModifier(cls, prevUrl):
        """Optional modification of parsed previous URLs. Useful if
        there are domain redirects. The default implementation does
        not modify the URL.
        """
        return prevUrl

    @classmethod
    def imageUrlModifier(cls, imageUrl, data):
        """Optional modification of parsed image URLs. Useful if the URL
        needs to be fixed before usage. The default implementation does
        not modify the URL. The given data is the URL page data.
        """
        return imageUrl

    def getLatestUrl(self):
        """Get starter URL from where to scrape comic strips."""
        return self.starter()

    @classmethod
    def vote(cls):
        """Cast a public vote for this comic."""
        url = configuration.VoteUrl + 'count/'
        uid = get_system_uid()
        data = {"name": cls.getName().replace('/', '_'), "uid": uid}
        page = urlopen(url, cls.session, data=data)
        return page.text

    def getCompleteFile(self, basepath):
        """Get filename indicating all comics are downloaded."""
        dirname = getDirname(self.getName())
        return os.path.join(basepath, dirname, "complete.txt")

    def isComplete(self, basepath):
        """Check if all comics are downloaded."""
        return os.path.isfile(self.getCompleteFile(basepath))

    def setComplete(self, basepath):
        """Set complete flag for this comic, ie. all comics are downloaded."""
        if self.endOfLife:
            filename = self.getCompleteFile(basepath)
            if not os.path.exists(filename):
                with open(filename, 'w') as f:
                    f.write('All comics should be downloaded here.')

    @classmethod
    def getPage(cls, url):
        """
        Fetch a page and return the opaque repesentation for the data parameter
        of fetchUrls and fetchText.

        Implementation notes: While this base class does not restrict how the
        returned data is structured, subclasses (specific scrapers) should specify
        how this data works, since the stracture is passed into different methods
        which can be defined by comic modules and these methods should be able to
        use the data if they so desire... (Affected methods: shouldSkipUrl,
        imageUrlModifier)
        """
        raise ValueError("No implementation for getPage!")

    @classmethod
    def fetchUrls(cls, url, data, urlSearch):
        raise ValueError("No implementation for fetchUrls!")

    @classmethod
    def fetchUrl(cls, url, data, urlSearch):
        return cls.fetchUrls(url, data, urlSearch)[0]

    @classmethod
    def fetchText(cls, url, data, textSearch, optional):
        raise ValueError("No implementation for fetchText!")

    @classmethod
    def getDisabledReasons(cls):
        """
        Get a dict of reasons why this comic module is disabled. The key is a
        short (unique) identifier, the value is a string explaining why the
        module is deactivated. If the module is not disabled, just return an
        empty dict.
        """
        return {}

    @classmethod
    def language(cls):
        """
        Return language of the comic as a human-readable language name instead
        of a 2-character ISO639-1 code.
        """
        lang = 'Unknown (%s)' % cls.lang
        if pycountry is None:
            if cls.lang in languages.Languages:
                lang = languages.Languages[cls.lang]
        else:
            try:
                lang = pycountry.languages.get(alpha2 = cls.lang).name
            except KeyError:
                try:
                    lang = pycountry.languages.get(iso639_1_code = cls.lang).name
                except KeyError:
                    pass
        return lang

class _BasicScraper(Scraper):
    """
    Scraper base class that matches regular expressions against HTML pages.

    Subclasses of this scraper should use compiled regular expressions as
    values for prevSearch, imageSearch and textSearch.

    Implementation note: The return value of getPage is a tuple: the first
    element is the raw HTML page text, the second element is the base URL (if
    any).
    """

    BASE_SEARCH = re.compile(tagre("base", "href", '([^"]*)'))

    @classmethod
    def getPage(cls, url):
        content = getPageContent(url, cls.session)
        # determine base URL
        baseUrl = None
        match = cls.BASE_SEARCH.search(content)
        if match:
            baseUrl = match.group(1)
        else:
            baseUrl = url
        return (content, baseUrl)

    @classmethod
    def fetchUrls(cls, url, data, urlSearch):
        """Search all entries for given URL pattern(s) in a HTML page."""
        searchUrls = []
        searches = makeSequence(urlSearch)
        for search in searches:
            for match in search.finditer(data[0]):
                searchUrl = match.group(1)
                if not searchUrl:
                    raise ValueError("Pattern %s matched empty URL at %s." % (search.pattern, url))
                out.debug(u'matched URL %r with pattern %s' % (searchUrl, search.pattern))
                searchUrls.append(normaliseURL(urljoin(data[1], searchUrl)))
            if searchUrls:
                # do not search other links if one pattern matched
                break
        if not searchUrls:
            patterns = [x.pattern for x in searches]
            raise ValueError("Patterns %s not found at URL %s." % (patterns, url))
        return searchUrls

    @classmethod
    def fetchText(cls, url, data, textSearch, optional):
        """Search text entry for given text pattern in a HTML page."""
        if textSearch:
            match = textSearch.search(data[0])
            if match:
                text = match.group(1)
                out.debug(u'matched text %r with pattern %s' % (text, textSearch.pattern))
                return unescape(text).strip()
            if optional:
                return None
            else:
                raise ValueError("Pattern %s not found at URL %s." % (textSearch.pattern, url))
        else:
            return None


class _ParserScraper(Scraper):
    """
    Scraper base class that uses a HTML parser and XPath expressions.

    All links are resolved before XPath searches are applied, so all URLs are
    absolute!

    Subclasses of this class should use XPath expressions as values for
    prevSearch, imageSearch and textSearch. When the XPath directly selects an
    attribute, it is used as the output.

    All those searches try to do something intelligent when they match a
    complete HTML Element: prevSearch and imageSearch try to find a "link
    attribute" and use that as URL. textSearch strips all tags from the content
    of the HTML element and returns that.
    """

    # Switch between CSS and XPath selectors for this class. Since CSS needs
    # another Python module, XPath is the default for now.
    css = False

    @classmethod
    def getPage(cls, url):
        tree = html.document_fromstring(getPageContent(url, cls.session))
        tree.make_links_absolute(url)
        return tree

    @classmethod
    def fetchUrls(cls, url, data, urlSearch):
        """Search all entries for given XPath in a HTML page."""
        searchUrls = []
        if cls.css:
            searchFun = data.cssselect
        else:
            searchFun = data.xpath
        searches = makeSequence(urlSearch)
        for search in searches:
            for match in searchFun(search):
                try:
                    for attrib in html_link_attrs:
                        if attrib in match.attrib:
                            searchUrls.append(match.get(attrib))
                except AttributeError:
                    searchUrls.append(str(match))
            if not cls.multipleImagesPerStrip and searchUrls:
                # do not search other links if one pattern matched
                break
        if not searchUrls:
            raise ValueError("XPath %s not found at URL %s." % (searches, url))
        return searchUrls

    @classmethod
    def fetchText(cls, url, data, textSearch, optional):
        """Search text entry for given text XPath in a HTML page."""
        if cls.css:
            searchFun = data.cssselect
        else:
            searchFun = data.xpath
        if textSearch:
            text = ''
            for match in searchFun(textSearch):
                try:
                    text += ' ' + match.text_content()
                except AttributeError:
                    text += ' ' + unicode(match)
            if text.strip() == '':
                if optional:
                    return None
                else:
                    raise ValueError("XPath %s did not match anything at URL %s." % (textSearch, url))
            out.debug(u'Matched text %r with XPath %s' % (text, textSearch))
            return unescape(text).strip()
        else:
            return None

    @classmethod
    def getDisabledReasons(cls):
        res = {}
        if cls.css and cssselect is None:
            res['css'] = u"This module needs the cssselect (python-cssselect) python module which is not installed."
        if html is None:
            res['lxml'] = u"This module needs the lxml (python-lxml) python module which is not installed."
        return res

def find_scraperclasses(comic, multiple_allowed=False):
    """Get a list comic scraper classes. Can return more than one entries if
    multiple_allowed is True, else it raises a ValueError if multiple
    modules match. The match is a case insensitive substring search."""
    if not comic:
        raise ValueError("empty comic name")
    candidates = []
    cname = comic.lower()
    for scraperclass in get_scraperclasses():
        lname = scraperclass.getName().lower()
        if lname == cname:
            # perfect match
            if not multiple_allowed:
                return [scraperclass]
            else:
                candidates.append(scraperclass)
        elif cname in lname:
            candidates.append(scraperclass)
    if len(candidates) > 1 and not multiple_allowed:
        comics = ", ".join(x.getName() for x in candidates)
        raise ValueError('multiple comics found: %s' % comics)
    elif not candidates:
        raise ValueError('comic %r not found' % comic)
    return candidates


_scraperclasses = None
def get_scraperclasses():
    """Find all comic scraper classes in the plugins directory.
    The result is cached.
    @return: list of Scraper classes
    @rtype: list of Scraper
    """
    global _scraperclasses
    if _scraperclasses is None:
        out.debug(u"Loading comic modules...")
        modules = loader.get_modules('plugins')
        plugins = loader.get_plugins(modules, Scraper)
        _scraperclasses = list(plugins)
        check_scrapers()
        out.debug(u"... %d modules loaded." % len(_scraperclasses))
    return _scraperclasses


def check_scrapers():
    """Check for duplicate scraper class names."""
    d = {}
    for scraperclass in _scraperclasses:
        name = scraperclass.getName().lower()
        if name in d:
            name1 = scraperclass.getName()
            name2 = d[name].getName()
            raise ValueError('duplicate scrapers %s and %s found' % (name1, name2))
        d[name] = scraperclass


def make_scraper(classname, scraperType = _BasicScraper, **attributes):
    """Make a new scraper class with given name and attributes."""
    return type(classname, (scraperType,), attributes)

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import os
import re
from six.moves.urllib.parse import urljoin

from lxml import html, etree
from lxml.html.defs import link_attrs as html_link_attrs

try:
    import cssselect
except ImportError:
    cssselect = None

try:
    import pycountry
except ImportError:
    pycountry = None

from . import configuration, http, languages, loader
from .util import (get_page, makeSequence, get_system_uid, unescape, tagre,
    normaliseURL, prettyMatcherList, uniq)
from .comic import ComicStrip
from .output import out
from .events import getHandler


ARCHIVE_ORG_URL = re.compile(r'https?://web\.archive\.org/web/[^/]*/')


class Scraper(object):
    '''Base class for all comic scraper, but without a specific scrape
    implementation.'''

    # The URL for the comic strip
    url = None

    # A string that is interpolated with the strip index to yield the URL for a
    # particular strip.
    stripUrl = None

    # Stop search for previous URLs at this URL
    firstStripUrl = None

    # if more than one image per URL is expected
    multipleImagesPerStrip = False

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

    # Specifing a list of HTTP error codes which should be handled as a
    # successful request.  This is a workaround for some comics which return
    # regular pages with strange HTTP codes. By default, all HTTP errors raise
    # exceptions.
    allow_errors = ()

    # HTTP session for configuration & cookies
    session = http.default_session

    @classmethod
    def getmodules(cls):
        name = cls.__name__
        if hasattr(cls, 'name'):
            name = cls.name
        return [cls(name)]

    @property
    def indexes(self):
        return self._indexes

    @indexes.setter
    def indexes(self, val):
        if val:
            self._indexes = tuple(sorted(val))

    def __init__(self, name):
        """Initialize internal variables."""
        self.name = name
        self.urls = set()
        self._indexes = tuple()
        self.skippedUrls = set()
        self.hitFirstStripUrl = False

    def __hash__(self):
        """Get hash value from name and index list."""
        return hash((self.name, self.indexes))

    def shouldSkipUrl(self, url, data):
        """Determine if search for images in given URL should be skipped."""
        return False

    def getComicStrip(self, url, data):
        """Get comic strip downloader for given URL and data."""
        imageUrls = self.fetchUrls(url, data, self.imageSearch)
        # map modifier function on image URLs
        imageUrls = [self.imageUrlModifier(x, data) for x in imageUrls]
        # remove duplicate URLs
        imageUrls = uniq(imageUrls)
        if len(imageUrls) > 1 and not self.multipleImagesPerStrip:
            out.warn(
                u"Found %d images instead of 1 at %s with expressions %s" %
                (len(imageUrls), url, prettyMatcherList(self.imageSearch)))
            image = imageUrls[0]
            out.warn(u"Choosing image %s" % image)
            imageUrls = (image,)
        elif not imageUrls:
            out.warn(u"Found no images at %s with expressions %s" % (url,
                     prettyMatcherList(self.imageSearch)))
        if self.textSearch:
            text = self.fetchText(url, data, self.textSearch,
                                  optional=self.textOptional)
        else:
            text = None
        return ComicStrip(self, url, imageUrls, text=text)

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
            urls = [self.starter()]
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
            if self.isfirststrip(url):
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

    def isfirststrip(self, url):
        """Check if the specified URL is the first strip of a comic. This is
        specially for comics taken from archive.org, since the base URL of
        archive.org changes whenever pages are taken from a different
        snapshot."""
        if not self.firstStripUrl:
            return False
        firsturl = ARCHIVE_ORG_URL.sub('', self.firstStripUrl)
        currenturl = ARCHIVE_ORG_URL.sub('', url)
        return firsturl == currenturl

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
                prevUrl = self.link_modifier(url, prevUrl)
                out.debug(u"Found previous URL %s" % prevUrl)
                getHandler().comicPageLink(self, url, prevUrl)
        return prevUrl

    def getIndexStripUrl(self, index):
        """Get comic strip URL from index."""
        return self.stripUrl % index

    def starter(self):
        """Get starter URL from where to scrape comic strips."""
        return self.url

    def namer(self, image_url, page_url):
        """Return filename for given image and page URL."""
        return None

    def link_modifier(self, fromurl, tourl):
        """Optional modification of parsed link (previous/back/latest) URLs.
        Useful if there are domain redirects. The default implementation does
        not modify the URL.
        """
        return tourl

    def imageUrlModifier(self, image_url, data):
        """Optional modification of parsed image URLs. Useful if the URL
        needs to be fixed before usage. The default implementation does
        not modify the URL. The given data is the URL page data.
        """
        return image_url

    def vote(self):
        """Cast a public vote for this comic."""
        uid = get_system_uid()
        data = {"name": self.name.replace('/', '_'), "uid": uid}
        response = self.session.post(configuration.VoteUrl, data=data)
        response.raise_for_status()

    def get_download_dir(self, basepath):
        """Try to find the corect download directory, ignoring case
        differences."""
        path = basepath
        for part in self.name.split('/'):
            done = False
            if (os.path.isdir(path) and
               not os.path.isdir(os.path.join(path, part))):
                for entry in os.listdir(path):
                    if (entry.lower() == part.lower() and
                       os.path.isdir(os.path.join(path, entry))):
                        path = os.path.join(path, entry)
                        done = True
                        break
            if not done:
                path = os.path.join(path, part)
        return path

    def getCompleteFile(self, basepath):
        """Get filename indicating all comics are downloaded."""
        dirname = self.get_download_dir(basepath)
        return os.path.join(dirname, "complete.txt")

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

    def getPage(self, url):
        """
        Fetch a page and return the opaque repesentation for the data parameter
        of fetchUrls and fetchText.

        Implementation notes: While this base class does not restrict how the
        returned data is structured, subclasses (specific scrapers) should
        specify how this data works, since the stracture is passed into
        different methods which can be defined by comic modules and these
        methods should be able to use the data if they so desire... (Affected
        methods: shouldSkipUrl, imageUrlModifier)
        """
        return get_page(url, self.session, allow_errors=self.allow_errors)

    def fetchUrls(self, url, data, urlsearch):
        raise ValueError("No implementation for fetchUrls!")

    def fetchUrl(self, url, data, urlsearch):
        return self.fetchUrls(url, data, urlsearch)[0]

    def fetchText(self, url, data, textsearch, optional):
        raise ValueError("No implementation for fetchText!")

    def getDisabledReasons(self):
        """
        Get a dict of reasons why this comic module is disabled. The key is a
        short (unique) identifier, the value is a string explaining why the
        module is deactivated. If the module is not disabled, just return an
        empty dict.
        """
        return {}

    def language(self):
        """
        Return language of the comic as a human-readable language name instead
        of a 2-character ISO639-1 code.
        """
        lang = 'Unknown (%s)' % self.lang
        if pycountry is None:
            if self.lang in languages.Languages:
                lang = languages.Languages[self.lang]
        else:
            try:
                lang = pycountry.languages.get(alpha_2=self.lang).name
            except KeyError:
                try:
                    lang = pycountry.languages.get(alpha2=self.lang).name
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

    def getPage(self, url):
        content = super(_BasicScraper, self).getPage(url).text
        # determine base URL
        baseUrl = None
        match = self.BASE_SEARCH.search(content)
        if match:
            baseUrl = match.group(1)
        else:
            baseUrl = url
        return (content, baseUrl)

    def fetchUrls(self, url, data, urlSearch):
        """Search all entries for given URL pattern(s) in a HTML page."""
        searchUrls = []
        searches = makeSequence(urlSearch)
        for search in searches:
            for match in search.finditer(data[0]):
                searchUrl = match.group(1)
                if not searchUrl:
                    raise ValueError("Pattern %s matched empty URL at %s." %
                                     (search.pattern, url))
                out.debug(u'matched URL %r with pattern %s' %
                          (searchUrl, search.pattern))
                searchUrls.append(normaliseURL(urljoin(data[1], searchUrl)))
            if searchUrls:
                # do not search other links if one pattern matched
                break
        if not searchUrls:
            patterns = [x.pattern for x in searches]
            raise ValueError("Patterns %s not found at URL %s." %
                             (patterns, url))
        return searchUrls

    def fetchText(self, url, data, textSearch, optional):
        """Search text entry for given text pattern in a HTML page."""
        if textSearch:
            match = textSearch.search(data[0])
            if match:
                text = match.group(1)
                out.debug(u'matched text %r with pattern %s' %
                          (text, textSearch.pattern))
                return unescape(text).strip()
            if optional:
                return None
            else:
                raise ValueError("Pattern %s not found at URL %s." %
                                 (textSearch.pattern, url))
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

    BROKEN_NOT_OPEN_TAGS = re.compile(r'(<+)([ =0-9])')

    # Taken directly from LXML
    XML_DECL = re.compile(
        r'^(<\?xml[^>]+)\s+encoding\s*=\s*["\'][^"\']*["\'](\s*\?>|)', re.U)

    NS = {
        "re": "http://exslt.org/regular-expressions"
    }

    # Switch between CSS and XPath selectors for this class. Since CSS needs
    # another Python module, XPath is the default for now.
    css = False

    # Activate a workaround for unescaped < characters on libxml version older
    # then 2.9.3. This is disabled by default since most sites are not THAT
    # broken ;)
    broken_html_bugfix = False

    def getPage(self, url):
        page = super(_ParserScraper, self).getPage(url)
        if page.encoding:
            # Requests figured out the encoding, so we can deliver Unicode to
            # LXML. Unfortunatly, LXML feels betrayed if there is still an XML
            # declaration with (probably wrong!) encoding at the top of the
            # document. Web browsers ignore such if the encoding was specified
            # in the HTTP header and so do we.
            text = self.XML_DECL.sub('\1\2', page.text, count=1)
            tree = self._parse_page(text)
        else:
            tree = self._parse_page(page.content)
        tree.make_links_absolute(url)
        return tree

    def _parse_page(self, data):
        if self.broken_html_bugfix and etree.LIBXML_VERSION < (2, 9, 3):
            def fix_not_open_tags(match):
                fix = (len(match.group(1)) * '&lt;') + match.group(2)
                out.warn("Found possibly broken HTML '%s', fixing as '%s'" % (
                         match.group(0), fix), level=2)
                return fix
            data = self.BROKEN_NOT_OPEN_TAGS.sub(fix_not_open_tags, data)

        tree = html.document_fromstring(data)
        return tree

    def fetchUrls(self, url, data, urlSearch):
        """Search all entries for given XPath in a HTML page."""
        searchUrls = []
        for match, search in self._matchPattern(data, urlSearch):
            searchUrl = None
            try:
                for attrib in html_link_attrs:
                    if attrib in match.attrib:
                        searchUrl = match.get(attrib)
            except AttributeError:
                searchUrl = str(match)
            out.debug(u'Matched URL %r with pattern %s' % (searchUrl, search))
            if searchUrl is not None:
                searchUrls.append(searchUrl)

        if not searchUrls:
            raise ValueError("XPath %s not found at URL %s." %
                             (urlSearch, url))
        return searchUrls

    def fetchText(self, url, data, textSearch, optional):
        """Search text entry for given text XPath in a HTML page."""
        if not textSearch:
            return None
        text = []
        for match, search in self._matchPattern(data, textSearch):
            try:
                text.append(match.text_content())
            except AttributeError:
                text.append(match)
            out.debug(u'Matched text %r with XPath %s' % (text, search))
        text = u' '.join(text)
        if text.strip() == '':
            if optional:
                return None
            else:
                raise ValueError("XPath %s did not match anything at URL %s." %
                                 (textSearch, url))
        return text.strip()

    def _matchPattern(self, data, patterns):
        if self.css:
            searchFun = data.cssselect
        else:
            def searchFun(s):
                return data.xpath(s, namespaces=self.NS)
        patterns = makeSequence(patterns)
        for search in patterns:
            matched = False
            for match in searchFun(search):
                matched = True
                yield match, search

            if matched and not self.multipleImagesPerStrip:
                # do not search other links if one pattern matched
                break

    def getDisabledReasons(self):
        res = {}
        if self.css and cssselect is None:
            res['css'] = (u"This module needs the cssselect " +
                          u"(python-cssselect) python module which is " +
                          u"not installed.")
        return res


def find_scrapers(comic, multiple_allowed=False):
    """Get a list comic scraper objects.

    Can return more than one entry if multiple_allowed is True, else it raises
    a ValueError if multiple modules match. The match is a case insensitive
    substring search.
    """
    if not comic:
        raise ValueError("empty comic name")
    candidates = []
    cname = comic.lower()
    for scrapers in get_scrapers(include_removed=True):
        lname = scrapers.name.lower()
        if lname == cname:
            # perfect match
            if not multiple_allowed:
                return [scrapers]
            else:
                candidates.append(scrapers)
        elif cname in lname and scrapers.url:
            candidates.append(scrapers)
    if len(candidates) > 1 and not multiple_allowed:
        comics = ", ".join(x.name for x in candidates)
        raise ValueError('multiple comics found: %s' % comics)
    elif not candidates:
        raise ValueError('comic %r not found' % comic)
    return candidates


_scrapers = None


def get_scrapers(include_removed=False):
    """Find all comic scraper classes in the plugins directory.
    The result is cached.
    @return: list of Scraper classes
    @rtype: list of Scraper
    """
    global _scrapers
    if _scrapers is None:
        out.debug(u"Loading comic modules...")
        modules = loader.get_modules('plugins')
        plugins = list(loader.get_plugins(modules, Scraper))
        _scrapers = sorted([m for x in plugins for m in x.getmodules()],
                           key=lambda p: p.name)
        check_scrapers()
        out.debug(u"... %d modules loaded from %d classes." % (
            len(_scrapers), len(plugins)))
    if include_removed:
        return _scrapers
    else:
        return [x for x in _scrapers if x.url]


def check_scrapers():
    """Check for duplicate scraper names."""
    d = {}
    for scraper in _scrapers:
        name = scraper.name.lower()
        if name in d:
            name1 = scraper.name
            name2 = d[name].name
            raise ValueError('duplicate scrapers %s and %s found' %
                             (name1, name2))
        d[name] = scraper

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
from __future__ import annotations

import html
import logging
import os
import pathlib
import re
import warnings
from typing import Collection, Dict, List, Optional, Pattern, Sequence, Union
from urllib.parse import urljoin

import lxml
from lxml.html.defs import link_attrs as lxml_link_attrs

try:
    import pycountry
except ImportError:
    pycountry = None

from . import configuration, http, languages, loader
from .comic import ComicStrip
from .events import getHandler
from .util import (
    get_page,
    get_system_uid,
    makeSequence,
    normaliseURL,
    prettyMatcherList,
    tagre,
    uniq,
)
from .xml import NS

logger = logging.getLogger(__name__)
ARCHIVE_ORG_URL = re.compile(r'https?://web\.archive\.org/web/[^/]*/')
html_link_attrs = lxml_link_attrs - {'usemap'}


if lxml.etree.LIBXML_VERSION < (2, 9, 3):
    warnings.warn(  # noqa: B028 - false positive
        'Your libxml2 is very old (< 2.9.3), some dosage modules might missbehave')


class GeoblockedException(IOError):
    def __init__(self):
        super().__init__('It seems your current location is geo-blocked.')


class Scraper:
    '''Base class for all comic scraper, but without a specific scrape
    implementation.'''

    # The URL for the comic strip
    url: Optional[str] = None

    # A string that is interpolated with the strip index to yield the URL for a
    # particular strip.
    stripUrl: Optional[str] = None

    # Stop search for previous URLs at this URL
    firstStripUrl: Optional[str] = None

    # if more than one image per URL is expected
    multipleImagesPerStrip: bool = False

    # set to True if this comic contains adult content
    adult: bool = False

    # set to True if this comic will not get updated anymore
    endOfLife: bool = False

    # langauge of the comic (two-letter ISO 639-1 code)
    lang: str = 'en'

    # an expression that will locate the URL for the previous strip in a page
    # this can also be a list or tuple
    prevSearch: Optional[Union[Sequence[Union[str, Pattern]], str, Pattern]] = None

    # an expression that will locate the strip image URLs strip in a page
    # this can also be a list or tuple
    imageSearch: Optional[Union[Sequence[Union[str, Pattern]], str, Pattern]] = None

    # an expression to store a text together with the image
    # sometimes comic strips have additional text info for each comic
    textSearch: Optional[Union[Sequence[Union[str, Pattern]], str, Pattern]] = None

    # Is the additional text required or optional?  When it is required (the
    # default), you see an error message whenever a comic page is encountered
    # that does not have the text
    textOptional: bool = False

    # usually the index format help
    help: str = ''

    # Specifing a list of HTTP error codes which should be handled as a
    # successful request.  This is a workaround for some comics which return
    # regular pages with strange HTTP codes. By default, all HTTP errors raise
    # exceptions.
    allow_errors: Sequence[int] = ()

    # HTTP session for configuration & cookies
    session: http.Session = http.default_session

    @classmethod
    def getmodules(cls) -> Collection[Scraper]:
        if cls.url is None:
            return ()
        name = cls.__name__
        if hasattr(cls, 'name'):
            name = cls.name
        return (cls(name),)

    @property
    def indexes(self):
        return self._indexes

    @indexes.setter
    def indexes(self, val):
        if val:
            self._indexes = tuple(sorted(val))

    def __init__(self, name: str) -> None:
        """Initialize internal variables."""
        self.name = name
        self.urls: set[str] = set()
        self._indexes = ()
        self.skippedUrls: set[str] = set()
        self.hitFirstStripUrl = False

    def __hash__(self) -> int:
        """Get hash value from name and index list."""
        return hash((self.name, self.indexes))

    def shouldSkipUrl(self, url: str, data) -> bool:
        """Determine if search for images in given URL should be skipped."""
        return False

    def getComicStrip(self, url, data) -> ComicStrip:
        """Get comic strip downloader for given URL and data."""
        urls = self.extract_image_urls(url, data)
        # map modifier function on image URLs
        urls = [self.imageUrlModifier(x, data) for x in urls]
        # remove duplicate URLs
        urls = uniq(urls)
        if len(urls) > 1 and not self.multipleImagesPerStrip:
            logger.warning("Found %d images instead of 1 at %s with expressions %r",
                len(urls), url, prettyMatcherList(self.imageSearch))
            image = urls[0]
            logger.warning("Choosing image %r", image)
            urls = (image,)
        elif not urls:
            logger.warning("Found no images at %r with expressions %r", url,
                prettyMatcherList(self.imageSearch))
        if self.textSearch:
            text = self.fetchText(url, data, self.textSearch,
                optional=self.textOptional)
        else:
            text = None
        return ComicStrip(self, url, urls, text=text)

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
        logger.info(msg)
        for url in urls:
            for strip in self.getStripsFor(url, maxstrips):
                yield strip

    def getStripsFor(self, url, maxstrips):
        """Get comic strips for an URL. If maxstrips is a positive number, stop after
        retrieving the given number of strips."""
        self.hitFirstStripUrl = False
        seen_urls = set()
        while url:
            logger.moreinfo('Get strip URL %r', url)
            data = self.getPage(url)
            if self.shouldSkipUrl(url, data):
                logger.info('Skipping URL %r', url)
                self.skippedUrls.add(url)
            else:
                try:
                    yield self.getComicStrip(url, data)
                except ValueError as msg:
                    logger.exception(msg)  # noqa: G200
            if self.isfirststrip(url):
                logger.debug("Stop at first URL %r", url)
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
                logger.warning("Already seen previous URL %r", prevUrl)
                break
            url = prevUrl

    def isfirststrip(self, url: str) -> bool:
        """Check if the specified URL is the first strip of a comic. This is
        specially for comics taken from archive.org, since the base URL of
        archive.org changes whenever pages are taken from a different
        snapshot."""
        if not self.firstStripUrl:
            return False
        firsturl = ARCHIVE_ORG_URL.sub('', self.firstStripUrl)
        currenturl = ARCHIVE_ORG_URL.sub('', url)
        return firsturl == currenturl

    def getPrevUrl(self, url: str, data) -> str | None:
        """Find previous URL."""
        prevUrl = None
        if self.prevSearch:
            try:
                prevUrl = self.fetchUrl(url, data, self.prevSearch)
            except ValueError as msg:
                # assume there is no previous URL, but print a warning
                logger.warning("%s Assuming no previous comic strips exist.", msg)  # noqa: G200
            else:
                prevUrl = self.link_modifier(url, prevUrl)
                logger.debug("Found previous URL %r", prevUrl)
                getHandler().comicPageLink(self, url, prevUrl)
        return prevUrl

    def getIndexStripUrl(self, index: str) -> str:
        """Get comic strip URL from index."""
        if not self.stripUrl:
            raise ValueError("Getting by index is not supported!")
        return self.stripUrl % index

    def starter(self) -> str | None:
        """Get starter URL from where to scrape comic strips."""
        return self.url

    def namer(self, image_url: str, page_url: str) -> str:
        """Return filename for given image and page URL."""
        return image_url.rsplit('/', 1)[1]

    def link_modifier(self, fromurl: str, tourl: str) -> str:
        """Optional modification of parsed link (previous/back/latest) URLs.
        Useful if there are domain redirects. The default implementation does
        not modify the URL.
        """
        return tourl

    def imageUrlModifier(self, image_url: str, data) -> str:
        """Optional modification of parsed image URLs. Useful if the URL
        needs to be fixed before usage. The default implementation does
        not modify the URL. The given data is the URL page data.
        """
        return image_url

    def vote(self) -> None:
        """Cast a public vote for this comic."""
        uid = get_system_uid()
        data = {"name": self.name.replace('/', '_'), "uid": uid}
        response = self.session.post(configuration.VoteUrl, data=data)
        response.raise_for_status()

    def get_download_dir(self, basepath: str) -> str:
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

    def getCompleteFile(self, basepath: str) -> str:
        """Get filename indicating all comics are downloaded."""
        dirname = self.get_download_dir(basepath)
        return os.path.join(dirname, "complete.txt")

    def isComplete(self, basepath: str) -> bool:
        """Check if all comics are downloaded."""
        return os.path.isfile(self.getCompleteFile(basepath))

    def setComplete(self, basepath: str) -> None:
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

    def extract_image_urls(self, url, data):
        """
        Extract image URLs from page data using the classes imageSearch attribute.
        """
        return self.fetchUrls(url, data, self.imageSearch)

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
        if pycountry is None:
            if self.lang in languages.Languages:
                return languages.Languages[self.lang]
        else:
            try:
                return pycountry.languages.get(alpha_2=self.lang).name
            except KeyError:
                try:
                    return pycountry.languages.get(alpha2=self.lang).name
                except KeyError:
                    pass
        return 'Unknown (%s)' % self.lang

    def geoblocked(self):
        """Helper method to indicate that the user is most probably geo-blocked."""
        raise GeoblockedException()


class BasicScraper(Scraper):
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
        content = super().getPage(url).text
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
                logger.debug('matched URL %r with pattern %r', searchUrl, search.pattern)
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
                logger.debug('matched text %r with pattern %r', text, textSearch.pattern)
                return html.unescape(text).strip()
            if optional:
                return None
            else:
                raise ValueError("Pattern %s not found at URL %s." %
                                 (textSearch.pattern, url))
        else:
            return None


class ParserScraper(Scraper):
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

    # Taken directly from LXML
    XML_DECL = re.compile(
        r'^(<\?xml[^>]+)\s+encoding\s*=\s*["\'][^"\']*["\'](\s*\?>|)', re.U)

    def getPage(self, url):
        page = super().getPage(url)
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
        return lxml.html.document_fromstring(data)

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
            logger.debug('Matched URL %r with pattern %r', searchUrl, search)
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
            logger.debug('Matched text %r with XPath %r', text, search)
        text = u' '.join(text)
        if text.strip() == '':
            if optional:
                return None
            else:
                raise ValueError("XPath %s did not match anything at URL %s." %
                                 (textSearch, url))
        return text.strip()

    def _matchPattern(self, data, patterns):
        patterns = makeSequence(patterns)
        for search in patterns:
            matched = False
            for match in self.match(data, search):
                matched = True
                yield match, search

            if matched and not self.multipleImagesPerStrip:
                # do not search other links if one pattern matched
                break

    def match(self, data, pattern):
        """Match an XPath pattern against a page."""
        return data.xpath(pattern, namespaces=NS)


# Legacy aliases
_BasicScraper = BasicScraper
_ParserScraper = ParserScraper


class Cache:
    """Cache for comic scraper objects. The cache is initialized on first use.
    This is cached, since iterating & loading a complete package might be quite
    slow.
    """
    def __init__(self) -> None:
        self.data: List[Scraper] = []
        self.userdirs: set[pathlib.Path] = set()

    def find(self, comic: str) -> Scraper:
        """Find a comic scraper object based on its name. This prefers a
        perfect match, but falls back to a substring match, if that is unique.
        Otharwise a ValueError is thrown.
        """
        if not comic:
            raise ValueError("empty comic name")
        candidates = []
        cname = comic.lower()
        for scraper in self.all(include_removed=True):
            lname = scraper.name.lower()
            if lname == cname:
                # perfect match
                return scraper
            elif cname in lname and scraper.url:
                candidates.append(scraper)
        if len(candidates) > 1:
            comics = ", ".join(x.name for x in candidates)
            raise ValueError('multiple comics found: %s' % comics)
        elif not candidates:
            raise ValueError('comic %r not found' % comic)
        return candidates[0]

    def load(self) -> None:
        logger.debug("Loading comic modules...")
        modules = 0
        classes = 0
        for module in loader.get_plugin_modules():
            modules += 1
            classes += self.addmodule(module)
        self.validate()
        logger.debug("... %d scrapers loaded from %d classes in %d modules.",
            len(self.data), classes, modules)

    def adddir(self, path: pathlib.Path) -> None:
        """Add an additional directory with python modules to the scraper list.
        These are handled as if the were part of the plugins package.
        """
        if path in self.userdirs:
            return
        if not self.data:
            self.load()
        modules = 0
        classes = 0
        logger.debug("Loading user scrapers from %r...", path)
        for module in loader.get_plugin_modules_from_dir(path):
            modules += 1
            classes += self.addmodule(module)
        self.validate()
        self.userdirs.add(path)
        if classes > 0:
            logger.debug("Added %d user classes from %d modules.",
                classes, modules)

    def addmodule(self, module) -> int:
        """Adds all valid plugin classes from the specified module to the cache.
        @return: number of classes added
        """
        classes = 0
        for plugin in loader.get_module_plugins(module, Scraper):
            classes += 1
            self.data.extend(plugin.getmodules())
        return classes

    def all(self, include_removed=False) -> list[Scraper]:
        """Return all comic scraper classes in the plugins directory.
        @return: list of Scraper classes
        @rtype: list of Scraper
        """
        if not self.data:
            self.load()
        if include_removed:
            return self.data
        else:
            return [x for x in self.data if x.url]

    def validate(self) -> None:
        """Check for duplicate scraper names."""
        d: Dict[str, Scraper] = {}
        for scraper in self.data:
            name = scraper.name.lower()
            if name in d:
                name1 = scraper.name
                name2 = d[name].name
                raise ValueError('duplicate scrapers %s and %s found' %
                                 (name1, name2))
            d[name] = scraper


scrapers = Cache()

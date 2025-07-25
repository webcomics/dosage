# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
from __future__ import annotations

import html
import logging
import os
import re
import subprocess
import sys
import time
import traceback
from urllib import parse

import lxml

from . import AppName, http
from .configuration import App, SupportUrl

logger = logging.getLogger(__name__)

# Maximum content size for HTML pages
MaxContentBytes = 1024 * 1024 * 3  # 3 MB

# The character set to encode non-ASCII characters in a URL. See also
# http://tools.ietf.org/html/rfc2396#section-2.1
# Note that the encoding is not really specified, but most browsers
# encode in UTF-8 when no encoding is specified by the HTTP headers,
# else they use the page encoding for followed link. See als
# http://code.google.com/p/browsersec/wiki/Part1#Unicode_in_URLs
UrlEncoding = "utf-8"


def get_system_uid():
    """Get a (probably) unique ID to identify a system.
    Used to differentiate votes.
    """
    try:
        if os.name == 'nt':
            return get_nt_system_uid()
        if sys.platform == 'darwin':
            return get_osx_system_uid()
    except Exception:
        return get_mac_uid()
    else:
        return get_mac_uid()


def get_nt_system_uid():
    r"""Get the MachineGuid from
    HKEY_LOCAL_MACHINE\Software\Microsoft\Cryptography\MachineGuid
    """
    import winreg
    lm = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    try:
        key = winreg.OpenKey(lm, r"Software\Microsoft\Cryptography")
        try:
            return winreg.QueryValueEx(key, "MachineGuid")[0]
        finally:
            key.Close()
    finally:
        lm.Close()


def get_osx_system_uid():
    """Get the OSX system ID.
    $ system_profiler |grep "r (system)"
    Serial Number (system): C24E1322XYZ
    """
    res = backtick(["system_profile"]).splitlines()
    for line in res:
        if "r (system)" in line:
            return line.split(':', 1)[1].strip()
    raise ValueError("Could not find system number in %r" % res)


def get_mac_uid():
    """Get the MAC address of the system."""
    import uuid
    return "%d" % uuid.getnode()


def backtick(cmd, encoding='utf-8'):
    """Return decoded output from command."""
    data = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
    return data.decode(encoding)


def unicode_safe(text, encoding=UrlEncoding, errors='ignore'):
    """Decode text to Unicode if not already done."""
    if isinstance(text, str):
        return text
    return text.decode(encoding, errors)


def tagre(tag, attribute, value, quote='"', before="", after=""):
    """Return a regular expression matching the given HTML tag, attribute
    and value. It matches the tag and attribute names case insensitive,
    and skips arbitrary whitespace and leading HTML attributes. The "<>" at
    the start and end of the HTML tag is also matched.
    @param tag: the tag name
    @ptype tag: string
    @param attribute: the attribute name
    @ptype attribute: string
    @param value: the attribute value
    @ptype value: string
    @param quote: the attribute quote (default ")
    @ptype quote: string
    @param after: match after attribute value but before end
    @ptype after: string

    @return: the generated regular expression suitable for re.compile()
    @rtype: string
    """
    if before:
        prefix = r"[^>]*%s[^>]*\s+" % before
    else:
        prefix = r"(?:[^>]*\s+)?"
    attrs = {
        'tag': case_insensitive_re(tag),
        'attribute': case_insensitive_re(attribute),
        'value': value,
        'quote': quote,
        'prefix': prefix,
        'after': after,
    }
    return (r'<\s*%(tag)s\s+%(prefix)s' +
            r'%(attribute)s\s*=\s*%(quote)s%(value)s%(quote)' +
            r's[^>]*%(after)s[^>]*>') % attrs


def case_insensitive_re(name):
    """Reformat the given name to a case insensitive regular expression string
    without using re.IGNORECASE. This way selective strings can be made case
    insensitive.
    @param name: the name to make case insensitive
    @ptype name: string
    @return: the case insensitive regex
    @rtype: string
    """
    return "".join("[%s%s]" % (c.lower(), c.upper()) for c in name)


def get_page(url, session, **kwargs):
    """Get text content of given URL."""
    http.check_robotstxt(url, session)
    # read page data
    page = urlopen(url, session, max_content_bytes=MaxContentBytes, **kwargs)
    logger.trace("Got page content %r", page.content)
    return page


def makeSequence(item):
    """If item is already a list or tuple, return it.
    Else return a tuple with item as single element."""
    if isinstance(item, (list, tuple)):
        return item
    return (item,)


def prettyMatcherList(things):
    """Try to construct a nicely-formatted string for a list of matcher
    objects. Those may be compiled regular expressions or strings..."""
    norm = []
    for x in makeSequence(things):
        if hasattr(x, 'pattern'):
            norm.append(x.pattern)
        else:
            norm.append(x)
    return "('%s')" % "', '".join(norm)


def normaliseURL(url):
    """Normalising
    - strips and leading or trailing whitespace,
    - replaces HTML entities and character references,
    - removes any leading empty segments to avoid breaking urllib2.
    """
    url = unicode_safe(url).strip()
    # XXX: brutal hack
    url = html.unescape(url)

    pu = list(parse.urlparse(url))
    segments = pu[2].split('/')
    while segments and segments[0] in ('', '..'):
        del segments[0]
    pu[2] = '/' + '/'.join(segments)
    # remove leading '&' from query
    if pu[4].startswith('&'):
        pu[4] = pu[4][1:]
    # remove anchor
    pu[5] = ""
    return parse.urlunparse(pu)


def urlopen(url, session, referrer=None, max_content_bytes=None,
            allow_errors=(), **kwargs):
    """Open an URL and return the response object."""
    logger.debug('Open URL %r', url)
    if 'headers' not in kwargs:
        kwargs['headers'] = {}
    if referrer:
        kwargs['headers']['Referer'] = referrer
    logger.trace('Sending headers %r', kwargs['headers'])
    logger.debug('Sending cookies %r', session.cookies)
    if 'data' not in kwargs:
        method = 'GET'
    else:
        method = 'POST'
        logger.trace('Sending POST data %r', kwargs['data'])
    req = session.request(method, url, **kwargs)
    logger.debug('Response cookies: %r', req.cookies)
    check_content_size(url, req.headers, max_content_bytes)
    if req.status_code not in allow_errors:
        req.raise_for_status()
    return req


def check_content_size(url, headers, max_content_bytes):
    """Check that content length in URL response headers do not exceed the
    given maximum bytes.
    """
    if not max_content_bytes:
        return
    if 'content-length' in headers:
        size = int(headers['content-length'])
        if size > max_content_bytes:
            raise IOError(
                'URL content of %s with %d bytes exceeds %d bytes.' %
                (url, size, max_content_bytes))


def splitpath(path):
    """Split a path in its components."""
    c = []
    head, tail = os.path.split(path)
    while tail:
        c.insert(0, tail)
        head, tail = os.path.split(head)
    return c


def getRelativePath(basepath, path):
    """Get a path that is relative to the given base path."""
    basepath = splitpath(os.path.abspath(basepath))
    path = splitpath(os.path.abspath(path))
    afterCommon = False
    for c in basepath:
        if afterCommon or path[0] != c:
            path.insert(0, os.path.pardir)
            afterCommon = True
        else:
            del path[0]
    return os.path.join(*path)


def getQueryParams(url):
    """Get URL query parameters."""
    query = parse.urlsplit(url).query
    logger.debug('Extracting query parameters from %r (%r)...', url, query)
    return parse.parse_qs(query)


def internal_error(out=sys.stderr, etype=None, evalue=None, tb=None):
    """Print internal error message (output defaults to stderr)."""
    print(os.linesep, file=out)
    print(f"""********** Oops, I did it again. *************

You have found an internal error in {AppName}. Please write a bug report
at {SupportUrl} and include at least the information below:

Not disclosing some of the information below due to privacy reasons is ok.
I will try to help you nonetheless, but you have to give me something
I can work with ;) .
""", file=out)
    if etype is None:
        etype = sys.exc_info()[0]
    if evalue is None:
        evalue = sys.exc_info()[1]
    print(etype, evalue, file=out)
    if tb is None:
        tb = sys.exc_info()[2]
    traceback.print_exception(etype, evalue, tb, None, out)
    print_app_info(out=out)
    print_proxy_info(out=out)
    print_locale_info(out=out)
    print(os.linesep,
          f"******** {AppName} internal error, over and out ********",
          file=out)


def print_env_info(key, out=sys.stderr):
    """If given environment key is defined, print it out."""
    value = os.getenv(key)
    if value is not None:
        print(key, "=", repr(value), file=out)


def print_proxy_info(out=sys.stderr):
    """Print proxy info."""
    print_env_info("http_proxy", out=out)


def print_locale_info(out=sys.stderr):
    """Print locale info."""
    for key in ("LANGUAGE", "LC_ALL", "LC_CTYPE", "LANG"):
        print_env_info(key, out=out)


def print_app_info(out=sys.stderr):
    """Print system and application info (output defaults to stderr)."""
    print("System info:", file=out)
    print(App, file=out)
    print("Python %(version)s on %(platform)s" %
          {"version": sys.version, "platform": sys.platform}, file=out)
    print("libxml2 version: %i.%i.%i" % lxml.etree.LIBXML_VERSION, file=out)
    stime = strtime(time.time())
    print("Local time:", stime, file=out)
    print("sys.argv", sys.argv, file=out)


def strtime(t):
    """Return ISO 8601 formatted time."""
    return (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t)) +
            strtimezone())


def strtimezone():
    """Return timezone info, %z on some platforms, but not supported on all.
    """
    if time.daylight:
        zone = time.altzone
    else:
        zone = time.timezone
    return "%+04d" % (-zone // 3600)


def rfc822date(indate):
    """Format date in rfc822 format."""
    return time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime(indate))


def unquote(text):
    """Replace all percent-encoded entities in text."""
    while '%' in text:
        newtext = parse.unquote(text)
        if newtext == text:
            break
        text = newtext
    return text


def getFilename(name):
    """Get a filename from given name without dangerous or incompatible
    characters."""
    # first replace all illegal chars
    name = re.sub(r"[^0-9a-zA-Z_\-\.]", "_", name)
    # then remove double dots and underscores
    while ".." in name:
        name = name.replace('..', '.')
    while "__" in name:
        name = name.replace('__', '_')
    # remove a leading dot or minus
    if name.startswith((".", "-")):
        name = name[1:]
    return name


def getExistingFile(name, max_suffix=1000):
    """Add filename suffix until file exists
    @return: filename if file is found
    @raise: ValueError if maximum suffix number is reached while searching
    """
    num = 1
    stem, ext = os.path.splitext(name)
    filename = name
    while not os.path.exists(filename):
        suffix = "-%d" % num
        filename = stem + suffix + ext
        num += 1
        if num >= max_suffix:
            raise ValueError("No file %r found" % name)
    return filename


def getNonexistingFile(name):
    """Add filename suffix until file not exists
    @return: filename
    """
    num = 1
    stem, ext = os.path.splitext(name)
    filename = name
    while os.path.exists(filename):
        suffix = "-%d" % num
        filename = stem + suffix + ext
        num += 1
    return filename


def strlimit(s, length=72):
    """If the length of the string exceeds the given limit, it will be cut
    off and three dots will be appended.

    @param s: the string to limit
    @type s: string
    @param length: maximum length
    @type length: non-negative integer
    @return: limited string, at most length+3 characters long
    """
    assert length >= 0, "length limit must be a non-negative integer"
    if not s or len(s) <= length:
        return s
    if length == 0:
        return ""
    return "%s..." % s[:length]


def uniq(input):
    """Remove duplicates from a list while preserving the list order"""
    output = []
    for item in input:
        if item not in output:
            output.append(item)
    return output


def urlpathsplit(url: str) -> list[str]:
    """Split the path of an URL into components, removing empty leading and
    trailing segments. This makes URL handling more robust against added or
    removed slashes.
    """
    parts = parse.urlsplit(url).path.split('/')
    while parts and not parts[-1]:
        del parts[-1]
    while parts and not parts[0]:
        del parts[0]
    return parts

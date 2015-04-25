# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
import re
from unittest import TestCase

from dosagelib.util import normaliseURL, unescape, tagre, get_system_uid


class URLTest(TestCase):
    """
    Tests for URL utility functions.
    """
    def test_unescape(self):
        # Test HTML replacement.
        self.assertEqual(unescape(u'foo&amp;bar'), u'foo&bar')
        self.assertEqual(unescape(u'foo&#160;bar'), u'foo\xa0bar')
        self.assertEqual(unescape(u'&quot;foo&quot;'), u'"foo"')

    def test_normalisation(self):
        # Test URL normalisation.
        self.assertEqual(normaliseURL('http://example.com//bar/baz&amp;baz'),
                         u'http://example.com/bar/baz&baz')


class RegexTest(TestCase):

    ValuePrefix = '/bla/'
    TagTests = (
        ('<img src="%s">', ValuePrefix+'foo', True),
        ('< img  src = "%s" >', ValuePrefix, True),
        ('<img class="prev" src="%s">', ValuePrefix+'...', True),
        ('<img origsrc="%s">', ValuePrefix, False),
        ('<Img src="%s">', ValuePrefix, True),
        ('<img SrC="%s">', ValuePrefix, True),
        ('<img src="%s">', ValuePrefix[:-1], False),
        ('<img class="prev" src="%s" a="b">', ValuePrefix, True),
    )

    def test_regex(self):
        matcher = re.compile(tagre("img", "src", '(%s[^"]*)' % self.ValuePrefix))
        for tag, value, domatch in self.TagTests:
            self.match_tag(matcher, tag, value, domatch)

    def match_tag(self, matcher, tag, value, domatch=True):
        text = tag % value
        match = matcher.search(text)
        if domatch:
            self.assertTrue(match, "%s should match %s" % (matcher.pattern, text))
            self.assertEqual(match.group(1), value)
        else:
            self.assertFalse(match, "%s should not match %s" % (matcher.pattern, text))


class UidTest(TestCase):
    """
    Tests for unique system IDs.
    """

    def test_system_uid(self):
        self.assertTrue(get_system_uid())

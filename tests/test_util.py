# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
import pytest
import re
from dosagelib.util import normaliseURL, tagre, get_system_uid


class TestURL(object):
    """
    Tests for URL utility functions.
    """

    def test_normalisation(self):
        # Test URL normalisation.
        assert (normaliseURL('http://example.com//bar/baz&amp;baz') ==
            u'http://example.com/bar/baz&baz')


class TestRegex(object):

    ValuePrefix = '/bla/'

    @pytest.mark.parametrize(('tag', 'value', 'domatch'), [
        ('<img src="%s">', ValuePrefix + 'foo', True),
        ('< img  src = "%s" >', ValuePrefix, True),
        ('<img class="prev" src="%s">', ValuePrefix + '...', True),
        ('<img origsrc="%s">', ValuePrefix, False),
        ('<Img src="%s">', ValuePrefix, True),
        ('<img SrC="%s">', ValuePrefix, True),
        ('<img src="%s">', ValuePrefix[:-1], False),
        ('<img class="prev" src="%s" a="b">', ValuePrefix, True),
    ])
    def test_regex(self, tag, value, domatch):
        matcher = re.compile(tagre("img", "src", '(%s[^"]*)' %
                             self.ValuePrefix))
        self.match_tag(matcher, tag, value, domatch)

    def match_tag(self, matcher, tag, value, domatch=True):
        text = tag % value
        match = matcher.search(text)
        if domatch:
            assert match, "%s should match %s" % (matcher.pattern, text)
            assert match.group(1) == value
        else:
            assert not match, "%s should not match %s" % (matcher.pattern,
                                                          text)


class TestUid(object):
    """
    Tests for unique system IDs.
    """

    def test_system_uid(self):
        assert get_system_uid()

# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
import re

import pytest

from dosagelib.util import get_system_uid, normaliseURL, tagre


class TestURL:
    """
    Tests for URL utility functions.
    """

    def test_normalisation(self):
        # Test URL normalisation.
        assert (normaliseURL('http://example.com//bar/baz&amp;baz') ==
            'http://example.com/bar/baz&baz')


class TestRegex:

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
            assert match, f"{matcher.pattern!r} should match {text!r}"
            assert match.group(1) == value
        else:
            assert not match, f"{matcher.pattern!r} should not match {text!r}"


class TestUid:
    """
    Tests for unique system IDs.
    """

    def test_system_uid(self):
        assert get_system_uid()

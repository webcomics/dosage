# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2017 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import pytest
import sys

import dosagelib.cmd

def cmd(*options):
    """'Fake' run dosage with given options."""
    return dosagelib.cmd.main(('--allow-multiple',) + options)

def cmd_ok(*options):
    assert cmd(*options) == 0

def cmd_err(*options):
    assert cmd(*options) == 1

class TestDosage(object):
    """Test the dosage commandline client."""

    def test_list_comics(self):
        for option in ("-l", "--list", "--singlelist"):
            cmd_ok(option)

    def test_display_version(self):
        cmd_ok("--version")

    def test_display_help(self):
        for option in ("-h", "--help"):
            with pytest.raises(SystemExit):
                cmd(option)

    def test_module_help(self):
        cmd_ok("-m", "xkcd")

    def test_no_comics_specified(self):
        cmd_err()

    def test_unknown_option(self):
        with pytest.raises(SystemExit):
            cmd('--imadoofus')

    def test_multiple_comics_match(self):
        cmd_err('Garfield')

    def test_fetch_html_and_rss_json(self, tmpdir):
        cmd_ok("-n", "2", "-v", "-b", str(tmpdir), "-o", "html", "-o", "rss",
                "-o", "json", "xkcd")

    def test_fetch_html_and_rss_2(self, tmpdir):
        cmd_ok("--numstrips", "2", "--baseurl", "bla", "--basepath",
                str(tmpdir), "--output", "rss", "--output", "html", "--adult",
                "BloomingFaeries")

    def test_fetch_indexed(self, tmpdir):
        cmd_ok("-n", "2", "-v", "-b", str(tmpdir), "xkcd:303")

# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import unittest
import sys
import shutil
import tempfile
from . import dosage_cmd, run_checked


def run_with_options(options, cmd=dosage_cmd):
    """Run dosage with given options."""
    run_checked([sys.executable, cmd] + options)


class TestDosage (unittest.TestCase):
    """Test the dosage commandline client."""

    def test_dosage(self):
        # list comics
        for option in ("-l", "--list", "--singlelist"):
            run_with_options([option])
        # display version
        run_with_options(["--version"])
        # display help
        for option in ("-h", "--help"):
            run_with_options([option])
        # module help
        run_with_options(["-m", "xkcd"])
        # no comics specified
        self.assertRaises(OSError, run_with_options, [])
        # unknown option
        self.assertRaises(OSError, run_with_options, ['--imadoofus'])
        # multiple comics match
        self.assertRaises(OSError, run_with_options, ['Garfield'])
        # create a temporary directory for images
        tmpdir = tempfile.mkdtemp()
        try:
            # fetch html and rss
            run_with_options(["-n", "2", "-v", "-b", tmpdir, "-o", "html", "-o", "rss", "xkcd"])
        finally:
            shutil.rmtree(tmpdir)
        # create a temporary directory for images
        tmpdir = tempfile.mkdtemp()
        try:
            # fetch html and rss 2
            run_with_options(["--numstrips", "2", "--baseurl", "bla", "--basepath", tmpdir, "--output", "rss", "--output", "html", "--adult", "sexyloser"])
        finally:
            shutil.rmtree(tmpdir)
        # create a temporary directory for images
        tmpdir = tempfile.mkdtemp()
        try:
            # fetch indexed
            run_with_options(["-n", "2", "-v", "-b", tmpdir, "xkcd:303"])
        finally:
            shutil.rmtree(tmpdir)

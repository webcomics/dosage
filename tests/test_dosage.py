# -*- coding: utf-8 -*-
# Copyright (C) 2013 Bastian Kleineidam
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


def run_with_options(options):
    """Run dosage with given options."""
    run_checked([sys.executable, dosage_cmd] + options)


class TestDosage (unittest.TestCase):
    """Test the dosage commandline client."""

    def setUp(self):
        # create a temporary directory for images
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_list_comics(self):
        for option in ("-l", "--list", "--singlelist"):
            run_with_options([option])

    def test_version(self):
        run_with_options(["--version"])

    def test_help(self):
        for option in ("-h", "--help"):
            run_with_options([option])
        # module help
        run_with_options(["-m", "calvinandhobbes"])

    def test_error(self):
        self.assertRaises(OSError, run_with_options, [])
        self.assertRaises(OSError, run_with_options, ['--imadoofus'])

    def test_fetch(self):
        run_with_options(["-n", "2", "-b", self.tmpdir, "-o", "html", "calvinandhobbes"])
        run_with_options(["--numstrips", "2", "--baseurl", "bla", "--basepath", self.tmpdir, "--output", "rss", "--adult", "sexyloser"])

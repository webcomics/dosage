# -*- coding: iso-8859-1 -*-
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
import os
import subprocess

basedir = os.path.dirname(__file__)
dosage_cmd = os.path.join(os.path.dirname(basedir), "dosage")
mainline_cmd = os.path.join(os.path.dirname(basedir), "mainline")


def run (cmd, verbosity=0, **kwargs):
    """Run command without error checking.
    @return: command return code"""
    if kwargs.get("shell"):
        # for shell calls the command must be a string
        cmd = " ".join(cmd)
    return subprocess.call(cmd, **kwargs)


def run_checked (cmd, ret_ok=(0,), **kwargs):
    """Run command and raise OSError on error."""
    retcode = run(cmd, **kwargs)
    if retcode not in ret_ok:
        msg = "Command `%s' returned non-zero exit status %d" % (cmd, retcode)
        raise OSError(msg)
    return retcode

# -*- coding: utf-8 -*-
# Copyright (C) 2013-2014 Bastian Kleineidam
# Copyright (C) 2016 Tobias Gruetzmacher

import os
import subprocess

basedir = os.path.dirname(__file__)
dosage_cmd = os.path.join(os.path.dirname(basedir), "dosage")


def run(cmd, verbosity=0, **kwargs):
    """Run command without error checking.
    @return: command return code"""
    if kwargs.get("shell"):
        # for shell calls the command must be a string
        cmd = " ".join(cmd)
    return subprocess.call(cmd, **kwargs)


def run_checked(cmd, ret_ok=(0,), **kwargs):
    """Run command and raise OSError on error."""
    retcode = run(cmd, **kwargs)
    if retcode not in ret_ok:
        msg = "Command `%s' returned non-zero exit status %d" % (cmd, retcode)
        raise OSError(msg)
    return retcode

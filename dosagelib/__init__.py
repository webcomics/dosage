# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""
Automated comic downloader. Dosage traverses comic websites in
order to download each strip of the comic. The intended use is for
mirroring the strips locally for ease of viewing; redistribution of the
downloaded strips may violate copyright, and is not advisable unless you
have communicated with all of the relevant copyright holders, described
your intentions, and received permission to distribute.

The primary interface is the 'dosage' commandline script.
Comic modules for each comic are located in L{dosagelib.plugins}.
"""
from __future__ import absolute_import, division, print_function

import sys
import os
from pbr.version import VersionInfo

AppName = u'dosage'

# Workaround for pkg_resources not working inside PyInstaller...
if hasattr(sys, 'frozen'):
    os.environ['PBR_VERSION'] = '2.15.0'

version_info = VersionInfo(AppName)
__version__ = version_info.version_string()  # PEP 396
AppVersion = version_info.release_string()

# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2019 Tobias Gruetzmacher
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

AppName = u'dosage'

from pkg_resources import get_distribution, DistributionNotFound
try:
    version_info = get_distribution(AppName)
    __version__ = version_info.version  # PEP 396
except DistributionNotFound:
    # package is not installed
    pass

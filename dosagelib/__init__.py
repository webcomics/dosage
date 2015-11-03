# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
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

from pkg_resources import get_distribution

AppName = u'dosage'
dist = get_distribution(AppName)
__version__ = dist.version # PEP 396

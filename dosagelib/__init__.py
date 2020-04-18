# SPDX-License-Identifier: MIT
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

try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

from .output import out

AppName = u'dosage'
try:
    __version__ = version(AppName)  # PEP 396
except PackageNotFoundError:
    # package is not installed
    out.warn('{} is not installed, no version available.'
        ' Use at least {!r} or {!r} to fix this.'.format(
            AppName, 'pip install -e .', 'setup.py egg_info'))
    __version__ = 'ERR.NOT.INSTALLED'

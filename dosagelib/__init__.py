# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
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

from importlib import metadata

from .output import out

AppName = 'dosage'
try:
    __version__ = metadata.version(AppName)  # PEP 396
except metadata.PackageNotFoundError:
    # package is not installed
    out.warn('{} is not installed, no version available.'
        ' Use at least {!r} or {!r} to fix this.'.format(
            AppName, 'pip install -e .', 'setup.py egg_info'))
    __version__ = 'ERR.NOT.INSTALLED'

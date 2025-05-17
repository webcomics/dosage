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
import logging
from importlib import metadata

from . import logext  # noqa: F401 - needed here to preload logging extensions

logger = logging.getLogger(__name__)

AppName = 'dosage'
try:
    __version__ = metadata.version(AppName)  # PEP 396
except metadata.PackageNotFoundError:
    # package is not installed
    logger.warning('%s is not installed, no version available.'
        ' Use something like %r to fix this.', AppName, 'pip install -e .')
    __version__ = 'ERR.NOT.INSTALLED'

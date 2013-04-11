# -*- coding: iso-8859-1 -*-
"""
Function to check for updates.
"""
import os
from .configuration import Version as CurrentVersion
from .util import urlopen
from distutils.version import StrictVersion
import requests

# Use the Freecode submit file as source since that file gets updated
# only when releasing a new version.
UPDATE_URL = "https://raw.github.com/wummel/dosage/master/dosage.freecode"
VERSION_TAG = 'Version:'
if os.name == 'nt':
    URL_TAG = 'Windows-installer-URL:'
else:
    URL_TAG = 'Source-Package-URL:'


def check_update ():
    """Return the following values:
       (False, errmsg) - online version could not be determined
       (True, None) - user has newest version
       (True, (version, url string)) - update available
       (True, (version, None)) - current version is newer than online version
    """
    version, value = get_online_version()
    if version is None:
        # value is an error message
        return False, value
    if version == CurrentVersion:
        # user has newest version
        return True, None
    if is_newer_version(version):
        # value is an URL linking to the update package
        return True, (version, value)
    # user is running a local or development version
    return True, (version, None)


def get_online_version ():
    """Download update info and parse it."""
    session = requests.session()
    page = urlopen(UPDATE_URL, session)
    version, url = None, None
    for line in page.text.splitlines():
        if line.startswith(VERSION_TAG):
            version = line.split(':', 1)[1].strip()
        elif line.startswith(URL_TAG):
            url = line.split(':', 1)[1].strip()
            url = url.replace('${version}', version)
    return version, url


def is_newer_version (version):
    """Check if given version is newer than current version."""
    return StrictVersion(version) > StrictVersion(CurrentVersion)

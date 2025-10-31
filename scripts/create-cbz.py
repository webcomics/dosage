#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2004 Tristan Seligmann and Jonathan Jacobs
# SPDX-FileCopyrightText: © 2012 Bastian Kleineidam
# SPDX-FileCopyrightText: © 2015 Tobias Gruetzmacher
"""
Creates a CBZ file in the comic directory.
Uses an ordered symlink directory (see order-symlinks.py) if it exists,
else the plain files are used.
"""

import os
import sys
import zipfile

from dosagelib.configuration import App

# known image file extensions
ImageExts = (
    ".jpg",
    ".jpeg",
    ".gif",
    ".png",
)


def is_image(filename):
    """Determine if given filename is an image."""
    # note: isfile() also accepts symlinks
    return os.path.isfile(filename) and filename.lower().endswith(ImageExts)


def get_cbz_comment():
    """Return a UTF-8 encoded comment no longer than 65535 bytes.
    At the moment this just returns the application name and version,
    since cbz readers do not seem to use the comment string anyway."""
    return (f"Created by {App}").encode()


def create_cbz(directory):
    """Creates or updates a CBZ from files in the given comic directory."""
    if not os.path.isdir(directory):
        print(f"ERROR: Directory {directory} not found.")
        return
    base = os.path.basename(directory.rstrip(os.path.sep))
    zipname = '%s.cbz' % base
    zipname = os.path.join(directory, zipname)
    d = os.path.join(directory, 'inorder')
    if os.path.isdir(d):
        # use directory with ordered symlinks
        directory = d
    if os.path.exists(zipname):
        os.remove(zipname)
    with zipfile.ZipFile(zipname, 'w') as myzip:
        for filename in sorted(os.listdir(d)):
            fullname = os.path.join(d, filename)
            if is_image(fullname):
                myzip.write(fullname)
        myzip.comment = get_cbz_comment()
    print(f"INFO: Created {zipname}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            create_cbz(arg)
    else:
        print(f"Usage: {os.path.basename(sys.argv[0])} <comic-dir>...")

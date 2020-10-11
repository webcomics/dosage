# SPDX-License-Identifier: PSF-2.0
# Copied from: https://github.com/pycontribs/tendo
# Author: Sorin Sbarnea
# Changes: changed logging and formatting
import sys
import os
import errno
import tempfile
from .output import out


class SingleInstance(object):
    """
    To prevent a script from running in parallel instantiate the
    SingleInstance() class. If is there another instance
    already running it will exit the application with the message
    "Another instance is already running, quitting.",
    returning an error code of -1.

    >>> me = SingleInstance()

    This is very useful to execute scripts by crontab that should only run
    one at a time.

    Note that this works by creating a lock file with a filename based
    on the full path to the script file.
    """

    def __init__(self, flavor_id="", exit_code=-1):
        """Create an exclusive lockfile or exit with an error and the given
        exit code."""
        self.initialized = False
        scriptname = os.path.splitext(os.path.realpath(sys.argv[0]))[0]
        lockname = scriptname.replace("/", "-").replace(":", "").replace("\\", "-")
        if flavor_id:
            lockname += "-%s" % flavor_id
        lockname += '.lock'
        tempdir = tempfile.gettempdir()
        self.lockfile = os.path.normpath(os.path.join(tempdir, lockname))
        out.debug("SingleInstance lockfile: " + self.lockfile)
        if sys.platform == 'win32':
            try:
                # file already exists, try to remove it in case the previous
                # execution was interrupted
                if os.path.exists(self.lockfile):
                    os.unlink(self.lockfile)
                self.fd = os.open(self.lockfile, os.O_CREAT | os.O_EXCL | os.O_RDWR)
            except OSError:
                type, e, tb = sys.exc_info()
                if e.errno == errno.EACCES:  # EACCES == 13
                    self.exit(exit_code)
                raise
        else:  # non Windows
            import fcntl
            self.fp = open(self.lockfile, 'w')
            try:
                fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
                # raises IOError on Python << 3.3, else OSError
            except OSError:
                self.exit(exit_code)
        self.initialized = True

    def exit(self, exit_code):
        """Exit with an error message and the given exit code."""
        out.error("Another instance is already running, quitting.")
        sys.exit(exit_code)

    def __del__(self):
        """Remove the lock file."""
        if not self.initialized:
            return
        try:
            if sys.platform == 'win32':
                if hasattr(self, 'fd'):
                    os.close(self.fd)
                    os.unlink(self.lockfile)
            else:
                import fcntl
                fcntl.lockf(self.fp, fcntl.LOCK_UN)
                if os.path.isfile(self.lockfile):
                    os.unlink(self.lockfile)
        except Exception as e:
            out.exception("could not remove lockfile: %s" % e)

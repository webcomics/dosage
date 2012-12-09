# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
from __future__ import print_function
import time
import sys
import threading

lock = threading.Lock()

class Output(object):
    """Print output with context, indentation and optional timestamps."""

    def __init__(self):
        """Initialize context and indentation."""
        self.context = ''
        self.level = 0
        self.timestamps = False

    def info(self, s, level=0):
        self.write(s, level=level)

    def debug(self, s):
        self.write(s, level=2)

    def warn(self, s):
        self.write("WARN: %s" % s, file=sys.stderr)

    def error(self, s):
        self.write("ERROR: %s" % s, file=sys.stderr)

    def write(self, s, level=0, file=sys.stdout):
        """Write message with indentation, context and optional timestamp."""
        if level > self.level:
            return
        if self.level > 1 or self.timestamps:
            timestamp = time.strftime('%H:%M:%S ')
        else:
            timestamp = ''
        with lock:
            print('%s%s> %s' % (timestamp, self.context, s), file=file)
            file.flush()

    def writelines(self, lines, level=0):
        """Write multiple messages."""
        for line in lines:
            for line in line.rstrip('\n').split('\n'):
                self.write(line.rstrip('\n'), level=level)

out = Output()

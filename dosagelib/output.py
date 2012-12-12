# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import time
import sys
import os
import threading
from .ansicolor import Colorizer

lock = threading.Lock()

class Output(object):
    """Print output with context, indentation and optional timestamps."""

    def __init__(self, stream=sys.stdout):
        """Initialize context and indentation."""
        self.context = ''
        self.level = 0
        self.timestamps = False
        self.stream = Colorizer(stream)

    def info(self, s, level=0):
        """Write an informational message."""
        self.write(s, level=level)

    def debug(self, s):
        """Write a debug message."""
        self.write(s, level=2, color='white')

    def warn(self, s):
        """Write a warning message."""
        self.write("WARN: %s" % s, color='bold;yellow')

    def error(self, s):
        """Write an error message."""
        self.write("ERROR: %s" % s, color='light;red')

    def write(self, s, level=0, color=None):
        """Write message with indentation, context and optional timestamp."""
        if level > self.level:
            return
        if self.level > 1 or self.timestamps:
            timestamp = time.strftime('%H:%M:%S ')
        else:
            timestamp = ''
        with lock:
            self.stream.write('%s%s> ' % (timestamp, self.context))
            self.stream.write('%s' % s, color=color)
            self.stream.write(os.linesep)
            self.stream.flush()

    def writelines(self, lines, level=0):
        """Write multiple messages."""
        for line in lines:
            for line in line.rstrip('\n').split('\n'):
                self.write(line.rstrip('\n'), level=level)

out = Output()

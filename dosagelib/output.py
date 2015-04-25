# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
import time
import sys
import os
import threading
import traceback
import codecs
from .ansicolor import Colorizer

lock = threading.Lock()

def get_threadname():
    """Return name of current thread."""
    return threading.current_thread().getName()


class Output(object):
    """Print output with context, indentation and optional timestamps."""

    def __init__(self, stream=None):
        """Initialize context and indentation."""
        self.context = None
        self.level = 0
        self.timestamps = False
        if stream is None:
            if hasattr(sys.stdout, "encoding") and sys.stdout.encoding:
                self.encoding = sys.stdout.encoding
            else:
                self.encoding = 'utf-8'
            if sys.version_info[0] >= 3:
                stream = sys.stdout.buffer
            else:
                stream = sys.stdout
            stream = codecs.getwriter(self.encoding)(stream, 'replace')
        self.setStream(stream)

    def setStream(self, stream):
        """Initialize context and indentation."""
        self.stream = Colorizer(stream)

    def info(self, s, level=0):
        """Write an informational message."""
        self.write(s, level=level)

    def debug(self, s, level=2):
        """Write a debug message."""
        self.write(s, level=level, color='white')

    def warn(self, s):
        """Write a warning message."""
        self.write(u"WARN: %s" % s, color='bold;yellow')

    def error(self, s, tb=None):
        """Write an error message."""
        self.write(u"ERROR: %s" % s, color='light;red')
        #if tb is not None:
        #    self.write('Traceback (most recent call last):', 1)

    def exception(self, s):
        """Write error message with traceback info."""
        self.error(s)
        type, value, tb = sys.exc_info()
        self.writelines(traceback.format_stack(), 1)
        self.writelines(traceback.format_tb(tb)[1:], 1)
        self.writelines(traceback.format_exception_only(type, value), 1)

    def write(self, s, level=0, color=None):
        """Write message with indentation, context and optional timestamp."""
        if level > self.level:
            return
        if self.timestamps:
            timestamp = time.strftime(u'%H:%M:%S ')
        else:
            timestamp = u''
        with lock:
            if self.context:
                self.stream.write(u'%s%s> ' % (timestamp, self.context))
            elif self.context is None:
                self.stream.write(u'%s%s> ' % (timestamp, get_threadname()))
            self.stream.write(u'%s' % s, color=color)
            try:
                text_type = unicode
            except NameError:
                text_type = str
            self.stream.write(text_type(os.linesep))
            self.stream.flush()

    def writelines(self, lines, level=0):
        """Write multiple messages."""
        for line in lines:
            for line in line.rstrip(u'\n').split(u'\n'):
                self.write(line.rstrip(u'\n'), level=level)

out = Output()

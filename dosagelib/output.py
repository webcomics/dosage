# -*- coding: utf-8 -*-
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher

from __future__ import absolute_import, division, print_function

import time
import sys
import os
import threading
import traceback
import codecs
import contextlib
import pydoc
import io
import six

try:
    from shutil import get_terminal_size
except ImportError:
    from backports.shutil_get_terminal_size import get_terminal_size

import colorama
from colorama import Fore, Style


lock = threading.Lock()


def get_threadname():
    """Return name of current thread."""
    return threading.current_thread().name


class Output(object):
    """Print output with context, indentation and optional timestamps."""

    DEFAULT_WIDTH = 80

    def __init__(self, stream=None):
        """Initialize context and indentation."""
        self.context = None
        self.level = 0
        self.timestamps = False
        if stream is None:
            colorama.init(wrap=False)
            if hasattr(sys.stdout, "encoding") and sys.stdout.encoding:
                self.encoding = sys.stdout.encoding
            else:
                self.encoding = 'utf-8'
            if hasattr(sys.stdout, 'buffer'):
                stream = sys.stdout.buffer
            else:
                stream = sys.stdout
            stream = codecs.getwriter(self.encoding)(stream, 'replace')
            if os.name == 'nt':
                stream = colorama.AnsiToWin32(stream).stream
        self.stream = stream

    @property
    def stream(self):
        """The underlaying stream."""
        return self._stream

    @stream.setter
    def stream(self, attr):
        """Change stream and base stream. base_stream is used for terminal
        interaction when _stream is redirected to a pager."""
        self._stream = attr
        self._base_stream = attr

    def info(self, s, level=0):
        """Write an informational message."""
        self.write(s, level=level)

    def debug(self, s, level=2):
        """Write a debug message."""
        # "white" is the default color for most terminals...
        self.write(s, level=level, color=Fore.WHITE)

    def warn(self, s, level=0):
        """Write a warning message."""
        self.write(u"WARN: %s" % s, level=level, color=Style.BRIGHT +
                   Fore.YELLOW)

    def error(self, s, level=0):
        """Write an error message."""
        self.write(u"ERROR: %s" % s, level=level, color=Style.DIM + Fore.RED)

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
            if color and self.is_tty:
                s = u'%s%s%s' % (color, s, Style.RESET_ALL)
            self.stream.write(six.text_type(s))
            self.stream.write(six.text_type(os.linesep))
            self.stream.flush()

    def writelines(self, lines, level=0):
        """Write multiple messages."""
        for line in lines:
            for line in line.rstrip(u'\n').split(u'\n'):
                self.write(line.rstrip(u'\n'), level=level)

    @property
    def width(self):
        """Get width of this output."""
        if not self.is_tty:
            return self.DEFAULT_WIDTH
        try:
            w = get_terminal_size().columns
            if w <= 0:
                return self.DEFAULT_WIDTH
            return w
        except ValueError:
            return self.DEFAULT_WIDTH

    @property
    def is_tty(self):
        """Is this output stream a terminal?"""
        return getattr(self._base_stream, "isatty", lambda: False)()

    @contextlib.contextmanager
    def temporary_context(self, context):
        """Run a block with a temporary output context"""
        orig_context = self.context
        self.context = context
        try:
            yield
        finally:
            self.context = orig_context

    @contextlib.contextmanager
    def pager(self):
        """Run the output of a block through a pager."""
        try:
            if self.is_tty:
                fd = io.StringIO()
                self._stream = fd
            with self.temporary_context(u''):
                yield
            if self.is_tty:
                pydoc.pager(fd.getvalue())
        finally:
            self._stream = self._base_stream


out = Output()

# SPDX-License-Identifier: MIT
# Copyright (C) 2004-2008 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2020 Tobias Gruetzmacher
import codecs
import contextlib
import io
import os
import pydoc
import sys
import threading
import time
import traceback

from shutil import get_terminal_size

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
        self.base_stream = stream

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
            # FIXME: context is some kind of magic tri-state:
            # - non-empty string
            # - explicit None
            # - anything falsy (empty string is used elsewhere)
            if self.context:
                self.stream.write(u'%s%s> ' % (timestamp, self.context))
            elif self.context is None:
                self.stream.write(u'%s%s> ' % (timestamp, get_threadname()))
            if color and self.is_tty:
                s = u'%s%s%s' % (color, s, Style.RESET_ALL)
            self.stream.write(str(s) + os.linesep)
            self.stream.flush()

    def writelines(self, lines, level=0):
        """Write multiple messages."""
        for line in lines:
            for sline in line.rstrip(u'\n').split(u'\n'):
                self.write(sline.rstrip(u'\n'), level=level)

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
        return getattr(self.base_stream, "isatty", lambda: False)()

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
                self.stream = fd
            with self.temporary_context(u''):
                yield
            if self.is_tty:
                pydoc.pager(fd.getvalue())
        finally:
            self.stream = self.base_stream


out = Output()

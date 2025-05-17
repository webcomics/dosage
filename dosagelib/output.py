# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025 Tobias Gruetzmacher
import io
import logging
import threading
import traceback

from rich import console, table, text, theme

from . import logext

logger = logging.getLogger(__name__)


def setup_console() -> console.Console:
    return console.Console(theme=theme.Theme({
        # Simulates old dosage style
        "logging.level.error": "dim red",
        "logging.level.warning": "bold yellow",
        "logging.level.info": "default",
        "logging.level.debug": "white",
        "logging.level.trace": "dim",
    }))


def console_logging(console: console.Console, level: int, timestamps: bool) -> None:
    """
    Configure Python logging for simple Dosage console output. This tries to
    emulate Dosage's legacy output style as much as possible.

    Levels work roughly like this:
      0 - The default, with shortened exception logging
      1 - Enables MOREINFO and verbose exception logging
      2 - Enables DEBUG logging
      3 - Enables TRACE logging
    """
    root = logging.getLogger()
    root.setLevel(translate_level(level))
    handler = RichHandler(console, showtime=timestamps, stacktrace=level > 0)
    handler.setFormatter(logging.Formatter(datefmt="%X"))
    root.addHandler(handler)
    # We don't want to see the low-level requests logging
    logging.getLogger("urllib3").setLevel(logging.INFO)


def translate_level(level: int) -> int:
    return {
        0: logging.INFO,
        1: logext.MOREINFO,
        2: logging.DEBUG,
        3: logext.TRACE,
    }.get(level, logging.NOTSET)


class RichHandler(logging.Handler):
    '''Custom logging handler using rich for nice colors. This emulates the
    legacy dosage style, while taking some inspiration from rich's own
    logging handler.'''

    def __init__(self, console: console.Console, showtime: bool = False,
            stacktrace: bool = True) -> None:
        super().__init__()

        self.console = console
        self.showtime = showtime
        self.stacktrace = stacktrace
        self._lastts = text.Text("")

    def emit(self, record: logging.LogRecord) -> None:
        # "Hide" exception information from formatter
        exc_info = record.exc_info
        record.exc_info = None
        record.exc_text = None  # This is just a cache, so we don't need to restore it later

        message = self.format(record)
        msgstyle = f"logging.level.{record.levelname.lower()}"

        context = getattr(record, "context", '')
        if not context and threading.current_thread() != threading.main_thread():
            context = threading.current_thread().name

        output = table.Table.grid(padding=(0, 1))
        row: list = []
        if self.showtime:
            output.add_column(style="log.time")
            row.append(self.timetext(record))
        if context:
            output.add_column()
            row.append(text.Text(f"{context}>"))
        output.add_column(ratio=1, style="log.message", overflow="fold")

        msgtext = text.Text(style=msgstyle)
        if record.levelno > logging.INFO:
            msgtext.append(f"{record.levelname.upper()}: ")

        if getattr(record, "markup", False):
            msgtext.append_text(text.Text.from_markup(message))
        else:
            msgtext.append_text(text.Text(message))
        row.append(msgtext)

        output.add_row(*row)

        # Add styled exception data
        if self.stacktrace and exc_info:
            extrarow: list[console.RenderableType] = ([""] * (len(row) - 1))
            extrarow.append(text.Text.from_ansi(self.colorexception(exc_info)))
            output.add_row(*extrarow)

            # Restore for next handler
            record.exc_info = exc_info

        try:
            self.console.print(output)
        except Exception:
            self.handleError(record)

    def usesTime(self) -> bool:
        return self.showtime

    def timetext(self, record: logging.LogRecord) -> text.Text:
        '''
        Get formatted time text or an empty placeholder if the time would be
        the same as for the previous log message. This should only be called
        inside the lock taken by "emit".
        '''
        timestamp = text.Text(self.time(record))
        if self._lastts == timestamp:
            return text.Text(" " * len(timestamp))
        else:
            self._lastts = timestamp
            return timestamp

    def time(self, record: logging.LogRecord) -> str:
        if self.formatter:
            return self.formatter.formatTime(record, self.formatter.datefmt)
        else:
            return ""

    def colorexception(self, ei):
        """
        Format and return the specified exception information as a string with ANSI
        colors (on PYthon 3.13+).
        """
        sio = io.StringIO()
        traceback.print_exception(ei[0], ei[1], ei[2], limit=None, file=sio, colorize=True)
        s = sio.getvalue()
        sio.close()
        if s[-1:] == "\n":
            s = s[:-1]
        return s

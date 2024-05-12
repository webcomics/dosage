# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2024 Tobias Gruetzmacher
"""
Helpers for logging.
"""
import logging

from rich.console import ConsoleRenderable
from rich.logging import RichHandler
from rich.text import Text


def setup_console(level: int, timestamps: bool) -> None:
    """
    Configure Python logging for simple Dosage console output. This tries to
    emulate Dosage's legacy output style as much as possible.

    Levels work roughly like this:
      0 - The default, with shortened exception logging
      1 - Enables verbose exception logging
      2 - Enables DEBUG logging
      3 - Enables TRACE logging
    """
    logging.basicConfig(
        level=translate_level(level),
        format="%(threadName)s> %(message)s",
        datefmt="%X",
        handlers=[DosageRichHandler(show_time=timestamps)]
    )

def translate_level(level: int) -> int:
    if level < 2:
        return logging.INFO
    if level == 2:
        return logging.DEBUG
    return logging.NOTSET


class DosageRichHandler(RichHandler):
    def __init__(self,
            show_time: bool = True) -> None:
        super().__init__(show_level=False, show_time=show_time, show_path=False)

    def render_message(self, record: logging.LogRecord, message: str) -> ConsoleRenderable:
        if record.levelno > logging.INFO:
            message = f"{record.levelname.upper()}: {message}"
            style = f"logging.level.{record.levelname.lower()}"
        else:
            style = ''

        use_markup = getattr(record, "markup", self.markup)
        message_text = Text.from_markup(message, style=style) if use_markup else Text(message,
            style=style)

        highlighter = getattr(record, "highlighter", self.highlighter)
        if highlighter:
            message_text = highlighter(message_text)

        if self.keywords is None:
            self.keywords = self.KEYWORDS

        if self.keywords:
            message_text.highlight_words(self.keywords, "logging.keyword")

        return message_text

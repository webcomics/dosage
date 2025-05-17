# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2025 Tobias Gruetzmacher

import logging
from typing import TYPE_CHECKING

MOREINFO = 15
TRACE = 5

if TYPE_CHECKING:
    parentlogger = logging.Logger
else:
    parentlogger = logging.getLoggerClass()

class ExtLogger(parentlogger):
    def moreinfo(self, msg, *args, **kwargs):
        if self.isEnabledFor(MOREINFO):
            self._log(MOREINFO, msg, args, **kwargs)

    def trace(self, msg, *args, **kwargs):
        if self.isEnabledFor(TRACE):
            self._log(TRACE, msg, args, **kwargs)


logging.addLevelName(MOREINFO, "MOREINFO")
logging.addLevelName(TRACE, "TRACE")
logging.setLoggerClass(ExtLogger)

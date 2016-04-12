#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015-2016 Tobias Gruetzmacher
"""Remove all lines after a given marker line."""
from __future__ import absolute_import, division, print_function

import fileinput
import sys


def main(args):
    """Remove lines after marker."""
    filename = args[0]
    marker = args[1]
    for line in fileinput.input(filename, inplace=1):
        print(line.rstrip())
        if line.startswith(marker):
            break


if __name__ == '__main__':
    main(sys.argv[1:])

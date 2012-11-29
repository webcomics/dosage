#!/usr/bin/env python
# Copyright (C) 2012 Bastian Kleineidam
"""Remove all lines after a given marker line.
"""
from __future__ import print_function
import fileinput
import sys

def main(args):
    filename = args[0]
    marker = args[1]
    for line in fileinput.input(filename, inplace=1):
        print(line.rstrip())
        if line.startswith(marker):
            break

if __name__ == '__main__':
    main(sys.argv[1:])

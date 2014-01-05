#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2012-2014 Bastian Kleineidam
from __future__ import print_function
import sys
import os
import requests
from dosagelib.util import urlopen
from dosagelib.configuration import VoteUrl


def write_votes(filename):
    session = requests.session()
    url = VoteUrl + 'counters/'
    req = urlopen(url, session)
    with open(filename, 'wb') as f:
        f.write(req.content)


def main(args):
    """Generate HTML output for test result."""
    filename = os.path.join('data', 'votes.json')
    write_votes(filename)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

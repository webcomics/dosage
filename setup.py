#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2015 Tobias Gruetzmacher

from __future__ import print_function
import os
import codecs
from setuptools import setup, find_packages

def get_authors():
    """Read list of authors from a text file, filtering comments."""
    authors = []
    authorfile = os.path.join('doc', 'authors.txt')
    with codecs.open(authorfile, 'r', 'utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith(u'#'):
                authors.append(line)
    return u", ".join(authors)


config = {}
with codecs.open(os.path.join('dosagelib', 'configuration.py')) as fp:
    exec(fp.read(), config)

setup(
    name = config['AppName'],
    version = config['Version'],
    description = 'a comic strip downloader and archiver',
    keywords = 'comic,webcomic,downloader,archiver',
    author = get_authors(),
    maintainer = config['Maintainer'],
    maintainer_email = config['MaintainerEmail'],
    license = 'MIT',
    url = config['Url'],
    packages = find_packages(exclude=['tests']),
    scripts = (
        'dosage',
    ),
    classifiers = (
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Internet :: WWW/HTTP',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ),
    install_requires = (
        'requests',
    ),
    extras_require = {
        'xpath': ["lxml"],
        'css': ['cssselect'],
    },
    setup_requires = [
        "setuptools_git >= 1.0",
    ]
)

# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam
import os
import sys

from .helpers import _BasicScraper

disabled = []
def init_disabled():
    filename = os.path.expanduser('~/.dosage/disabled')
    if not os.path.isfile(filename):
        return
    with open(filename) as f:
        for line in f:
            if line and not line.startswith('#'):
                disabled.append(line.rstrip())
init_disabled()

class DisabledComicError(ValueError):
    pass


def get(comicName):
    """Returns a comic module object."""
    candidates = []
    for scraper in get_scrapers():
        lname = scraper.get_name().lower()
        cname = comicName.lower()
        if lname == cname:
            # perfect match
            return scraper
        if cname in lname:
            candidates.append(scraper)
    if len(candidates) == 1:
        return candidates[0]
    elif candidates:
        comics = ", ".join(x.get_name() for x in candidates)
        raise ValueError('Multiple comics %s found.' % comics)
    else:
        raise ValueError('Comic %r not found.' % comicName)


def items():
    return get_scrapers()


_scrapers = None
def get_scrapers():
    """Find all comic scraper classes in the plugins directory.
    The result is cached.
    @return: list of _BasicScraper classes
    @rtype: list of _BasicScraper
    """
    global _scrapers
    if _scrapers is None:
        _scrapers = list(get_all_plugins(get_modules()))
        _scrapers.sort(key=lambda s: s.get_name())
        check_scrapers()
    return _scrapers


def check_scrapers():
    d = {}
    for s in _scrapers:
        name = s.get_name().lower()
        if name in d:
            name1 = s.get_name()
            name2 = d[name].get_name()
            raise ValueError('Duplicate scrapers %s and %s found' % (name1, name2))
        d[name] = s


def get_modules():
    """Find all valid modules in the plugins directory. A valid module
    must have a .py extension, and is importable.
    @return: all loaded valid modules
    @rtype: iterator of module
    """
    # load from the plugins folder
    folder = os.path.join(os.path.dirname(__file__), 'plugins')
    for filename in get_importable_modules(folder):
        try:
            module = load_module(filename)
            if module is not None:
                yield module
        except StandardError, msg:
            print "ERROR", msg


def get_importable_modules(folder):
    """Find all module files in the given folder that end witn '.py' and
    don't start with an underscore.
    @return module filenames
    @rtype: iterator of string
    """
    for fname in os.listdir(folder):
        if fname.endswith('.py') and not fname.startswith('_'):
            yield os.path.join(folder, fname)


def load_module(filename):
    """Load and return the module given by the filename.
    Other exceptions than ImportError are not catched.
    @return: loaded module or None on import errors
    @rtype: module or None
    """
    name = os.path.splitext(os.path.basename(filename))[0]
    modulename = "dosagelib.plugins.%s" % name
    __import__(modulename)
    return sys.modules[modulename]


def get_all_plugins(modules):
    """Find all scrapers in all modules.
    @param modules: the modules to search
    @ptype modules: iterator of modules
    @return: found scrapers
    @rytpe: iterator of class objects
    """
    for module in modules:
        for plugin in get_plugins(module):
            yield plugin


def get_plugins(module):
    """Return all subclasses of _BasicScraper in the module.
    If the module defines __all__, only those entries will be searched,
    otherwise all objects not starting with '_' will be searched.
    """
    try:
        names = module.__all__
    except AttributeError:
        names = [x for x in vars(module) if not x.startswith('_')]
    for name in names:
        try:
            obj = getattr(module, name)
        except AttributeError:
            continue
        try:
            if issubclass(obj, _BasicScraper):
                yield obj
        except TypeError:
            continue

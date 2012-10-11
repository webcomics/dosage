# -*- coding: iso-8859-1 -*-

import os
import sys

def get_modules(folder, importprefix):
    """Find all valid modules in the plugins directory. A valid module
    must have a .py extension, and is importable.
    @return: all loaded valid modules
    @rtype: iterator of module
    """
    for filename in get_importable_modules(folder):
        try:
            module = load_module(filename, importprefix)
            if module is not None:
                yield module
        except StandardError, msg:
            print "ERROR: could not load module %s: %s" % (filename, msg)


def get_importable_modules(folder):
    """Find all module files in the given folder that end witn '.py' and
    don't start with an underscore.
    @return module filenames
    @rtype: iterator of string
    """
    for fname in sorted(os.listdir(folder)):
        if fname.endswith('.py') and not fname.startswith('_'):
            yield os.path.join(folder, fname)


def load_module(filename, importprefix):
    """Load and return the module given by the filename.
    Other exceptions than ImportError are not catched.
    @return: loaded module or None on import errors
    @rtype: module or None
    """
    name = os.path.splitext(os.path.basename(filename))[0]
    modulename = "%s%s" % (importprefix, name)
    __import__(modulename)
    return sys.modules[modulename]


def get_plugins(modules, classobj):
    """Find all scrapers in all modules.
    @param modules: the modules to search
    @ptype modules: iterator of modules
    @return: found scrapers
    @rytpe: iterator of class objects
    """
    for module in modules:
        for plugin in get_module_plugins(module, classobj):
            yield plugin


def get_module_plugins(module, classobj):
    """Return all subclasses of _BasicScraper in the module.
    If the module defines __all__, only those entries will be searched,
    otherwise all objects not starting with '_' will be searched.
    """
    try:
        names = module.__all__
    except AttributeError:
        names = [x for x in vars(module) if not x.startswith('_')]
    for name in sorted(names):
        try:
            obj = getattr(module, name)
        except AttributeError:
            continue
        try:
            if issubclass(obj, classobj):
                yield obj
        except TypeError:
            continue

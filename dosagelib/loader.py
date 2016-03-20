# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2016 Tobias Gruetzmacher

"""
Functions to load plugin modules.

Example usage:
    modules = loader.get_modules('plugins')
    plugins = loader.get_plugins(modules, PluginClass)
"""

from __future__ import absolute_import, division, print_function
import pkgutil
import importlib
from .output import out


def get_modules(folder):
    """Find (and import) all valid modules in the given submodule of this file.
    @return: all loaded valid modules
    @rtype: iterator of module
    """
    mod = importlib.import_module(".." + folder, __name__)
    prefix = mod.__name__ + "."
    modules = [m[1] for m in pkgutil.iter_modules(mod.__path__, prefix)]

    # special handling for PyInstaller
    importers = map(pkgutil.get_importer, mod.__path__)
    toc = set()
    for i in importers:
        if hasattr(i, 'toc'):
            toc |= i.toc
    for elm in toc:
        if elm.startswith(prefix):
            modules.append(elm)

    for name in modules:
        try:
            yield importlib.import_module(name)
        except ImportError as msg:
            out.error("could not load module %s: %s" % (name, msg))


def get_plugins(modules, classobj):
    """Find all class objects in all modules.
    @param modules: the modules to search
    @ptype modules: iterator of modules
    @return: found classes
    @rytpe: iterator of class objects
    """
    for module in modules:
        for plugin in get_module_plugins(module, classobj):
            yield plugin


def get_module_plugins(module, classobj):
    """Return all subclasses of a class in the module.
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
            if issubclass(obj, classobj):
                yield obj
        except TypeError:
            continue

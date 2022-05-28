# SPDX-License-Identifier: MIT
# Copyright (C) 2012-2014 Bastian Kleineidam
# Copyright (C) 2016-2020 Tobias Gruetzmacher
"""
Functions to load plugin modules.

Example usage:
    for module in loader.get_plugin_modules():
        plugins.extend(loader.get_module_plugins(module, PluginClass))
"""
import importlib
import pkgutil
import sys

from .plugins import (__name__ as plugin_package, __path__ as plugin_path)
from .output import out


def get_plugin_modules():
    """Find (and import) all valid modules in the "plugins" package.
    @return: all loaded valid modules
    @rtype: iterator of module
    """
    prefix = plugin_package + "."
    modules = {m[1] for m in pkgutil.iter_modules(plugin_path, prefix)}

    for elm in _get_all_modules_pyinstaller():
        if elm.startswith(prefix):
            modules.add(elm)

    for name in modules:
        try:
            yield importlib.import_module(name)
        except ImportError as msg:
            out.error("could not load module %s: %s" % (name, msg))


def _get_all_modules_pyinstaller():
    # Special handling for PyInstaller
    toc = set()
    importers = pkgutil.iter_importers(__package__)
    for i in importers:
        if hasattr(i, 'toc'):
            toc |= i.toc
    return toc


def get_plugin_modules_from_dir(path, prefix='user_'):
    """Load and import a directory of python files as if they were part of the
    "plugins" package. (Mostly "stolen" from
    https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly)
    """
    modules = []
    for f in path.glob('*.py'):
        name = plugin_package + "." + prefix + f.stem
        # FIXME: Drop str() when this is Python 3.6+
        spec = importlib.util.spec_from_file_location(name, str(f))
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
        modules.append(module)
    return modules


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

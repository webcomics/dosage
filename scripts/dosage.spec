# SPDX-License-Identifier: MIT
# Copyright (C) 2017-2020 Tobias Gruetzmacher

# Idea from
# https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Setuptools-Entry-Point,
# but with importlib
def Entrypoint(group, name, **kwargs):
    import re
    try:
        from importlib.metadata import entry_points
    except ImportError:
        from importlib_metadata import entry_points

    # get the entry point
    eps = entry_points()[group]
    ep = next(ep for ep in eps if ep.name == name)
    module, attr = re.split(r'\s*:\s*', ep.value, 1)

    # script name must not be a valid module name to avoid name clashes on import
    script_path = os.path.join(workpath, name + '-script.py')
    print("creating script for entry point", group, name)
    with open(script_path, 'w') as fh:
        print("import sys", file=fh)
        print("import", module, file=fh)
        print("sys.exit(%s.%s())" % (module, attr), file=fh)

    return Analysis(
        [script_path] + kwargs.get('scripts', []),
        **kwargs
    )


a = Entrypoint('console_scripts', 'dosage')

a.binaries = [x for x in a.binaries if not x[1].lower().startswith(r'c:\windows')]

pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='dosage',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=True)

# vim: set ft=python:

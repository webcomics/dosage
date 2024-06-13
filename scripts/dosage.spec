# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: © 2017 Tobias Gruetzmacher

import re
from importlib import metadata

# Idea from
# https://github.com/pyinstaller/pyinstaller/wiki/Recipe-Setuptools-Entry-Point,
# but with importlib
def entrypoint(group, name, **kwargs):
    # get the entry point
    eps = metadata.entry_points()
    if 'select' in dir(eps):
        # modern
        ep = eps.select(group=group)[name]
    else:
        # legacy (pre-3.10)
        ep = next(ep for ep in eps[group] if ep.name == name)
    module, attr = re.split(r'\s*:\s*', ep.value, maxsplit=1)

    # script name must not be a valid module name to avoid name clashes on import
    script_path = os.path.join(workpath, name + '-script.py')
    print("creating script for entry point", group, name)
    with open(script_path, mode='w', encoding='utf-8') as fh:
        print("import sys", file=fh)
        print("import", module, file=fh)
        print(f"sys.exit({module}.{attr}())", file=fh)

    return Analysis(
        [script_path] + kwargs.get('scripts', []),
        **kwargs
    )


a = entrypoint('console_scripts', 'dosage')

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

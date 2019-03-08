# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['../dosage'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.binaries = [x for x in a.binaries if not x[1].lower().startswith(r'c:\windows')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
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

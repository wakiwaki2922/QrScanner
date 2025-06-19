# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

# Thu thập dữ liệu và thư viện động cho pyzbar
pyzbar_datas = collect_data_files('pyzbar')
pyzbar_binaries = collect_dynamic_libs('pyzbar')

# Thêm icon và manifest vào resources
added_files = [
    ('icon.ico', '.'),  # Copy icon.ico vào thư mục gốc của exe
    ('QRScanner.manifest', '.'),  # Copy manifest
]

a = Analysis(
    ['qr_scanner_app.py'],
    pathex=[],
    binaries=pyzbar_binaries,
    datas=pyzbar_datas + added_files,
    hiddenimports=['pyzbar', 'pyzbar.pyzbar'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter', 'matplotlib', 'numpy.f2py', 'scipy', 'unittest', 
        'email', 'http', 'urllib3', 'xml', 'pydoc', 'doctest',
        'argparse', 'logging.handlers', 'multiprocessing.spawn',
        'sqlite3', 'ssl', 'bz2', 'lzma', '_hashlib', '_ssl',
        'test', 'tests', 'distutils'
    ],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='QRScanner',
    debug=False,
    bootloader_ignore_signals=False,
    strip=True,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version_info.txt',
    icon='icon.ico',
) 
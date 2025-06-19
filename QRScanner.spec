# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_dynamic_libs

# Thu thập thư viện pyzbar
pyzbar_datas = collect_data_files('pyzbar')
pyzbar_binaries = collect_dynamic_libs('pyzbar')

a = Analysis(
    ['qr_scanner_app.py'],
    pathex=[],
    binaries=pyzbar_binaries,
    datas=pyzbar_datas,
    hiddenimports=['pyzbar'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
) 
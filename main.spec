# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, get_deps_all, hookspath, runtime_hooks
import sys
import os

# 取得 Kivy 相關的隱藏導入和數據文件
kivy_deps = get_deps_minimal()

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=kivy_deps['hiddenimports'] + [
        'kivy.core.window.window_sdl2',
        'kivy.core.image.img_tex',
        'kivy.core.image.img_dds',
        'kivy.core.text.text_layout',
        'kivy.core.audio.audio_sdl2',
        'kivy.core.clipboard.clipboard_sdl2',
    ],
    hookspath=hookspath(),
    hooksconfig={},
    runtime_hooks=runtime_hooks(),
    excludes=[
        'kivy.core.camera',
        'kivy.core.spelling',
        'kivy.core.video',
        'kivy.input.providers.mouse',
        'kivy.input.providers.mtdev',
        'kivy.input.providers.hidinput',
        'kivy.input.providers.linuxwacom',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# 根據平台設置不同的參數
if sys.platform == 'win32':
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
        name='main',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
    )
elif sys.platform == 'darwin':
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        name='main',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
    )
else:  # Linux
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        name='main',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        upx_exclude=[],
        runtime_tmpdir=None,
        console=False,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
    )
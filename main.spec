# -*- mode: python ; coding: utf-8 -*-
import sys
import os
import glob

# 只在 Windows 平台導入 kivy_deps
if sys.platform == 'win32':
    try:
        from kivy_deps import sdl2, glew
    except ImportError:
        print("Warning: kivy_deps not found, building without Windows dependencies")
        sdl2 = None
        glew = None
else:
    sdl2 = None
    glew = None

# 導入 Kivy 工具
try:
    from kivy.tools.packaging.pyinstaller_hooks import get_deps_minimal, get_deps_all, hookspath, runtime_hooks
    kivy_deps = get_deps_minimal()
    kivy_hiddenimports = kivy_deps['hiddenimports']
    kivy_hookspath = hookspath()
    kivy_runtime_hooks = runtime_hooks()
except ImportError:
    print("Warning: Kivy packaging tools not found, using basic configuration")
    kivy_hiddenimports = []
    kivy_hookspath = []
    kivy_runtime_hooks = []

# 動態查找資料檔案
data_files = []
for pattern in ['*.txt', '*.json', '*.csv', '*.yaml', '*.yml']:
    for file in glob.glob(pattern):
        data_files.append((file, '.'))
        print(f"Found data file: {file}")

# 如果沒有找到任何資料檔案，添加一個警告
if not data_files:
    print("Warning: No data files found matching common patterns")

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=data_files,
    hiddenimports=kivy_hiddenimports + [
        'kivy.core.window.window_sdl2',
        'kivy.core.window.window_x11',
        'kivy.core.image.img_tex',
        'kivy.core.image.img_dds',
        'kivy.core.text.text_layout',
        'kivy.core.audio.audio_sdl2',
        'kivy.core.clipboard.clipboard_sdl2',
        'kivy.input.providers.mouse',
        'kivy.input.providers.mtdev',
        'kivy.input.providers.hidinput',
        'kivy.input.postproc.calibration',
        'kivy.input.postproc.dejitter',
        'kivy.input.postproc.doubletap',
        'kivy.input.postproc.ignorelist',
        'kivy.input.postproc.retaintouch',
        'kivy.input.postproc.tripletap',
    ],
    hookspath=kivy_hookspath,
    hooksconfig={},
    runtime_hooks=kivy_runtime_hooks,
    excludes=[
        'kivy.core.camera',
        'kivy.core.spelling',
        'kivy.core.video',
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
    # Windows 特定設置
    binaries_to_add = []
    if sdl2 and glew:
        binaries_to_add = [Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)]

    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
        *binaries_to_add,
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
    # macOS 特定設置 - 使用 mock GL backend
    os.environ['KIVY_GL_BACKEND'] = 'mock'
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
    # Linux 特定設置
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
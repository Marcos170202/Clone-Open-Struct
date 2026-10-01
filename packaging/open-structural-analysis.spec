# Especificação do PyInstaller para gerar o executável do Open Structural Analysis.
# Uso, a partir da raiz do repositório:  pyinstaller packaging/open-structural-analysis.spec
import os

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

hiddenimports = (
    collect_submodules("osa")
    + collect_submodules("Pynite")
    + collect_submodules("pyvistaqt")
)
datas = (
    collect_data_files("osa", includes=["data/*.json", "resources/icons/*.svg"])
    + collect_data_files("pyvista")
    + collect_data_files("Pynite")
)

a = Analysis(
    ["launcher.py"],
    pathex=[os.path.join(SPECPATH, "..")],
    datas=datas,
    hiddenimports=hiddenimports,
    excludes=["tkinter", "IPython", "pytest"],
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="OpenStructuralAnalysis",
    console=False,
)
coll = COLLECT(exe, a.binaries, a.datas, name="OpenStructuralAnalysis")

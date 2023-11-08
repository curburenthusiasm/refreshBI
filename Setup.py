from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["pyautogui", "time", "logging", "pywinauto"],
    "include_files": ["C:/Users/rfoley/PycharmProjects/refreshBI/venv/Lib/site-packages/pyautogui/_init_.py"]
}

setup(
    name = "RefreshBI",
    version = "0.3",
    description = "A script to refresh PowerBI",
    executables = [Executable("main.py")]
)

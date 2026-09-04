import os
import shutil
import time
import sys


def is_admin():
    try:
        # Check for Linux/macOS
        if hasattr(os, 'getuid'):
            return os.getuid() == 0
        
        # Check for Windows
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False

if is_admin():
    print("starting setup")
    time.sleep(2)
else:
    print("rerun the setup as admin")
    time.sleep(5)
    sys.exit(0)

file_path = input("Please enter the path to the file you want to add to PATH: ")

answer = input(
    "Welcome to Path Installer, select your system\n 1. windows\n 2. linux\n 3. custom\n 4. darwin/macOS\n")



if answer in ("custom", "3"):
    manual_setup = input("Did you already run manualpath_SETUP.py? (y/n)")

    if manual_setup in("no", "n"):
        print("Please run manualpath_SETUP.py first to make custom install")

    else:
            with open("pathloc.txt", "r", encoding="utf-8") as file:
            content = file.read()
            time.sleep(1)
            shutil.copy(file_path, content)

if answer in ("windows", "1"):
    shutil.copy(file_path, "C:\\Windows\\System32")
if answer in ("linux", "2"):
    shutil.copy(file_path, "/local/usr/bin/")
if answer in ("darwin", "4"):
    shutil.copy(file_path, "/usr/local/bin/")
if answer not in ("darwin", "4", "linux", "2", "windows", "1"):
    print("unspported file/system")
    time.sleep(3)

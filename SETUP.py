import shutil
import os
import time
import sys

#yeah this admin function was taken out from a stack overflow thing


def is_admin():
    try:
        
        if hasattr(os, 'getuid'):
            return os.getuid() == 0
        
        
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

    



path = input("enter your system for path isntallation\n 1.windows\n 2.linux\n 3.darwin/macOS\n 4.custom\n please enter the number of your chioce (1-4)\n")
if path == "1":
    path = "C:\\Windows\\System32"
if path in("2", "3"):
    path = "/local/usr/bin/"
if path == "4":
    path = input("enter the path of your system:\n")

script_dir = os.path.dirname(os.path.abspath(__file__))
path_installer = os.path.join(script_dir, "path_installer.py")
pathloc = os.path.join(script_dir, "pathloc.txt")

shutil.copy(path_installer, path)


fp = open(
    'pathloc.txt', 'w')
fp.write(path)
fp.close()
time.sleep(1)

with open(pathloc, "r", encoding="utf-8") as file:
    content = file.read()

time.sleep(1)

alsothistoolonpath = input("do you want to also add this tool to your path? (y/n)")

if alsothistoolonpath in("y", "Y"):
    shutil.copy(path_installer, path)
if alsothistoolonpath in("n", "N"):
    print("ok :(")
    time.sleep(2)
sys.exit(0)
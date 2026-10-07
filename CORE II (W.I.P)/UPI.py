import os
import time
import json
from pathlib import Path
import sys

path = Path("pathloc.txt")
linux_mac = "/usr/local/bin"
windows = "C:\\Windows\\System32"
custom = ""


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
    time.sleep(1.5)
else:
    print("rerun the setup as admin")
    time.sleep(5)
    sys.exit(0)

def create_pathloc():
    answer_pathloc = input("please select your os: \n 1.linux \n 2.windows \n 3.custom \n >")
    if answer_pathloc == "1":
        path.write_text(linux_mac)
    elif answer_pathloc == "2":
        path.write_text(windows)
    elif answer_pathloc == "3":
        custom = input("please write the PATH folder of your system")
        path.write_text(custom)
    elif answer_pathloc:
        print("bro just read please")
    

def start():
    if path.is_file():
        print("PATHLOC was found, starting UPI..")
    else:
          answer_start = input("pathloc wasnt found, do you wanna create it? (y/n)\n")
          # sorry we ran out of budget so please dont type in capitals
          if answer_start.lower() == "y":
                create_pathloc()
          elif answer_start.lower() == "n":
                print("ok :(")
                sys.exit()


start()
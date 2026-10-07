import os
import time
import json
from pathlib import Path
import sys
import subprocess

path = Path("pathloc.txt")
linux_mac = "/usr/local/bin"
windows = "C:\\Windows\\System32"
custom = ""


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
    time.sleep(1.5)
else:
    print("rerun the setup as admin")
    time.sleep(5)
    sys.exit(0)

def create_pathloc():
    answer_pathloc = input("please select your os: \n 1.linux \n 2.windows \n 3.custom \n > ")
    if answer_pathloc == "1":
        # btw i have a crush on one of my class and i may tell you her name
        path.write_text(linux_mac)
    elif answer_pathloc == "2":
        path.write_text(windows)
    elif answer_pathloc == "3":
        custom = input("please write the PATH folder of your system \n >")
        path.write_text(custom)
    else:
        print("bro just read please")

def get_pathloc():
    pathloc = path.read_text()
    print("PATHLOC found:", pathloc)
        

def start():
    if path.is_file():
        print("PATHLOC was found, starting UPI..")
        time.sleep(1)
        print("remember to type 0 to go to the main menu")
    else:
          answer_start = input("pathloc wasnt found, do you wanna create it? (y/n)\n > ")
          #the answer to each riddle is the first letter of your answer
          if answer_start.lower() == "y":
                create_pathloc()
          elif answer_start.lower() == "n":
                print("ok :(")
                sys.exit()


    

def main():
    action = input("what do you want to do today boss: \n 1.Install a package to PATH (ig) \n 2.List your packages \n 3.Uninstall packages \n 4.Edit pathloc \n > ")
                        #riddle me this (1): A self propelleD aNti AirRaFt system tHaT is operated by 2 countries, one where most of its fLaG is greeN aNd bluE, aNd the second one is the inventor of it
    if action == "1":
        pathloc = get_pathloc()
        package_path = input("please write the path of the file that you want to add to your PATH \n > ")

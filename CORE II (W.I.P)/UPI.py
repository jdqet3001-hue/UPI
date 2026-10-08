import os
import time
import json
from pathlib import Path
import sys
import shutil

path = Path("pathloc.txt")
linux_mac = "/usr/local/bin/"
windows = "C:\\Windows\\System32\\"
custom = ""


def is_admin():
    try:

        if hasattr(os, 'getuid'):
            return os.getuid() == 0
        

        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin() != 0 #riddle me this (6) 1000mb
    except Exception:
        return False

if is_admin():
    print("starting setup")
    time.sleep(0.5)
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
    return pathloc

def start():
    if path.is_file():
        print("PATHLOC was found, starting UPI..")
        time.sleep(1) #riddle me this (3): +12
        main()
    else:
          answer_start = input("pathloc wasnt found, do you wanna create it? (y/n)\n > ")
          #the answer to each riddle is the first letter of your answer, there are 7 riddles
          if answer_start.lower() == "y":
                create_pathloc()
                main()
          elif answer_start.lower() == "n":
                print("ok :(")
                sys.exit()

def does_db_exist():
    db = Path("database.json").is_file()
    if db != True: #riddle me this (5): she's ___ i need
        print("db not found, installing..")
        template = {
            "format": [
                {
                    "is_valid": "true"
                }
            ],
            "packages": [

            ]
        }
        json_db = json.dumps(template, indent=4)
        with open("database.json", "w") as f:
            f.write(json_db)
    else:
        pass #nothing ever happens

def install():
    does_db_exist()
    pathloc = get_pathloc()
    package_path = input("please write the path of the file that you want to add to your PATH \n > ")
    if package_path == "0":
        main()

    filename = Path(package_path).name
    does_exist = Path(package_path).is_file()
    final = pathloc+filename
    if does_exist == True:
        print("file found, copying it to PATH..") #riddle me this (1): A self propelleD aNti AircRaFt system tHaT is operated by 2 countries, one where most of its fLaG is greeN aNd bluE, aNd the second one is the inventor of it
        result = shutil.copy(package_path, pathloc)
        installed = Path(result).is_file()
        print("installation status:", installed)
        time.sleep(1)
        new = {
                "namefile": filename,
                "source": package_path,
                "location": pathloc,
                "final": final
            }

        
        print("adding the new package to the db..")
        with open("database.json", "r+") as file:
            data = json.load(file)
            data["packages"].append(new)
            print("validating db format..")
            if data["format"][0]["is_valid"] != "true":
                print("the db format is invalid, if you suspect that this is a bug/error, please pull an issue in the main repo page")
            file.seek(0)
            json.dump(data, file, indent=4)
            print("done") #we ran out of budget to validate the json install, im not a slave, but if SHE told me to do i'd do it
            main()


    else:
        print("the file wasnt found, please try again")
        sys.exit(1)
    
def List():
    with open("database.json", "r+") as file:
        data = json.load(file)

    for package in data["packages"]:
        print("\n")
        print("Name:", package["namefile"])
        print("Source:", package["source"])
        print("Location:", package["location"])
        print("Final:", package["final"])
    gotostart = input("\n\n do you want to go back to the main menu? (y/n)\n >")
    if gotostart == "y":
        main()

def uninstall():
    with open("database.json", "r+") as file:
        data = json.load(file)

        uninstall_action = input("type the filename of the package that you want to uninstall > ")

        for package in data["packages"]:
            name = package["namefile"]
            final = package["final"]
            if uninstall_action == name:
                data["packages"].remove(package)

                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
                print("file removed from database, removing it now from system..")
                Path(final).unlink()
                main()
        

def main():
    action = input("what do you want to do today boss: \n 1.Install a package to PATH (ig) \n 2.List your packages \n 3.Uninstall packages \n 4.Edit pathloc \n 0.exit \n > ")
                        #riddle me this (2): reAd the first riddle VERY well
    if action == "1":
        install()
    elif action == "2":
        List()
    elif action == "3":
        uninstall() 
    elif action == "4":
        create_pathloc()
    elif action == "0":
        print("bye")
        time.sleep(1)
        sys.exit(0)

start()

# riddle me this (7): the reason why this text is readable
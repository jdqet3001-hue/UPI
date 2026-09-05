import os
import shutil
import time
import sys
import json


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

with open("systems.json", "r", encoding="utf-8") as systems:
    systemsconfig = json.load(systems)



system = input("enter your system as number:\n1. Windows\n2. Linux\n3. MacOS\n4. PATHLOC\n>  ")
time.sleep(1)
packet_path = (systemsconfig[system])
if system not in ("1", "2", "3", "4"):
    print("unknown input, press enter to exit.")
    if input() == "":
        sys.exit(0)

print(f"succefully configurated packet_path: {packet_path}")

time.sleep(3)

#json packet demo

packet_og_path,packet_name = input("enter the path of the file that you want to install to path and its name\n>  ").split()
if packet_path == "pathloc.txt":
    with open("pathloc.txt", "r") as pathloc:
        pathlocontent = pathloc.read()
        packet_path = pathlocontent


destination = os.path.join(packet_path, packet_name)

shutil.copy(packet_og_path, destination)

new_packet = packet_path,packet_name

json_add = {
    "PATH": {
        "source": packet_og_path,
        "location": packet_path,
        "name": packet_name
    }
}
with open("packets.json", "r", encoding="utf-8") as packets:
    packet_config = json.load(packets)


packet_config[packet_name] = {
    "source": packet_og_path,
    "location": packet_path,
    "name": packet_name
}

with open("packets.json", "w", encoding="utf-8") as packets:
    json.dump(packet_config, packets, indent=4)
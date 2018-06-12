from pathlib import Path
import re
from shutil import copyfile
from configparser import ConfigParser
import sys
import os

allowed_names = ["SmartSteamEmu.ini","steam_emu.ini","ALI213.ini","Origins.ini","steam_api.ini","stp-steam.ini","rev.ini","CPY.ini"]
ini_settings = {"SmartSteamEmu":"PersonaName ","Settings":"UserName","Settings":"PlayerName","UserName":"Name","Globals":"PersonaName","steamclient":"PlayerName","Emulator":"SteamUser","Settings":"username"}

def find_files(directory):
    files = []
    pathlist = Path(directory).glob('**/*.ini')
    for path in pathlist:
        if (extract_basename(path)) in allowed_names:
            files.append(path)
    return files

def extract_basename(path):
    basename = re.search(r'[^\\/]+(?=[\\/]?$)', str(path))
    if basename:
        return basename.group(0)

def backup_and_change(file_paths,username):
    for win_path in file_paths:
        path = str(win_path)
        if not(Path(path.join(".bak")).exists()):
            print("backing up file to %s"%(path.join(".bak")))
            copyfile(path,path.join(".bak"))
        change_username(path,username)

def change_username(path,username):
    config = ConfigParser()
    config.read(path)
    for key,item in ini_settings.items():
        if key in config:
            if item in config[key]:
                print("changing %s to %s in %s"%(config[key][item],username,path))
                config[key][item] = username
    with open(path, 'w') as configfile:
        config.write(configfile)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        path = os.path.dirname(sys.argv[0])
        username = sys.argv[1]
    else:
        path = os.path.dirname(sys.argv[0])
        username = input("Username ->")
    backup_and_change(find_files(path),username)
from pathlib import Path
import re
from shutil import copyfile 

allowed_names = ["SmartSteamEmu.ini","steam_emu.ini","ALI213.ini","Origins.ini","steam_api.ini","stp-steam.ini","rev.ini","CPY.ini"]

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

def backup_files(file_paths):
    for win_path in file_paths:
        path = str(win_path)
        copyfile(path,path+".bak")
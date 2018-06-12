from pathlib import Path
import re

allowed_names = ["SmartSteamEmu.ini","steam_emu.ini","ALI213.ini","Origins.ini","steam_api.ini","stp-steam.ini","rev.ini","CPY.ini"]

def find_files(directory):
    pathlist = Path(directory).glob('**/*.ini')
    for path in pathlist:
        if (extract_basename(path)) in allowed_names:
            print(path)

def extract_basename(path):
    basename = re.search(r'[^\\/]+(?=[\\/]?$)', str(path))
    if basename:
        return basename.group(0)
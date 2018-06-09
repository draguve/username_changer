from pathlib import Path
import re

def find_files(directory):
    pathlist = Path(directory).glob('**/*.ini')
    for path in pathlist:
        print(extract_basename(path))

def extract_basename(path):
    basename = re.search(r'[^\\/]+(?=[\\/]?$)', str(path))
    if basename:
        return basename.group(0)
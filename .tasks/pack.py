import argparse
from pathlib import Path
import shutil
import os
import logging

parser = argparse.ArgumentParser("GLOX Packager")
parser.add_argument("file", help="file changed")
parser.add_argument("--output", "-o", default=".", help="Output path")
parser.add_argument("--verbose", "-v", action="store_true", help="Enable verbose output.")

args = parser.parse_args()
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Find manifest [Content_Types].xml to determin folder of Shape
manifest = "[Content_Types].xml"
dir = Path(args.file).parent
base_dir = None
while base_dir is None:
    for file in dir.iterdir():
        if file.name == manifest:
            base_dir = dir
            break
    logger.debug(str(dir.name))
    dir = dir.parent

if not base_dir:
    exit(0)

outpath = Path(args.output).expanduser().resolve()
if not outpath.exists():
    os.makedirs(str(outpath))

filename = str(outpath.joinpath(Path(base_dir.name+".glox")))
shutil.make_archive(str(outpath.joinpath(Path(base_dir.name+".glox"))), 'zip', str(base_dir))

shutil.move(filename+".zip", filename)
logging.info(f"{filename} exported.")

    
    



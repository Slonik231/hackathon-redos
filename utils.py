from pathlib import Path
import os, subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd() + "/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

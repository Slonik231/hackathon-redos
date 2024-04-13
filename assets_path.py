from pathlib import Path
import os

def relative_to_assets(path: str) -> Path:
    return Path(os.path.dirname(__file__)) / Path("assets/frame0") / Path(path)

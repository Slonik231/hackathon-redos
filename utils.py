import tkinter as tk
import subprocess
import pwd

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)
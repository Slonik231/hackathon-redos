import os
import sys

app_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(app_path)

import gui

def main():
    gui.main()

if __name__ == "__main__":
    main()
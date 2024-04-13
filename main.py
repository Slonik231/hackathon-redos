import tkinter as tk
from gui import GUI
import os
from tkinter import messagebox

if __name__ == "__main__":
    if os.getuid() != 0:
        messagebox.showwarning("Недостаточно прав", "Данная программа доступна только для root пользователя!")
        exit()
    window = tk.Tk()
    app = GUI(window)
    window.mainloop()

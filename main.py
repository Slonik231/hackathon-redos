import tkinter as tk
from gui import KioskManagerApp

if __name__ == "__main__":
    if os.getuid() != 0:
        messagebox.showwarning("Недостаточно прав", "Данная программа доступна только для root пользователя!")
    else:
        root = tk.Tk()
        app = KioskManagerApp(root)
        root.mainloop()
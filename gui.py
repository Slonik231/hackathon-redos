from pathlib import Path
import os, subprocess, pwd
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, BooleanVar
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import config
from utils import relative_to_assets
from dialogs import DialogApps, DialogUsers


class KioskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Киоск-менеджер")
        self.root.geometry("1000x660")
        self.root.configure(bg="#FFFFFF")

        self.canvas = tk.Canvas(
            self.root,
            bg="#FFFFFF",
            height=660,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        self.create_widgets()

    def create_widgets(self):
        # Добавьте здесь создание всех виджетов и их настройку, например:

        # Поле ввода имени пользователя
        self.entry_user = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_user.place(
            x=654.0,
            y=158.0,
            width=188.0,
            height=46.0
        )

        # Кнопка для выбора имени пользователя
        button_dialog_users = tk.Button(
            image=tk.PhotoImage(file=relative_to_assets("button_dialog_users.png")),
            borderwidth=0,
            highlightthickness=0,
            command=lambda: DialogUsers(self.root, self.entry_user),
            relief="flat"
        )
        button_dialog_users.place(x=871.0, y=163.0, width=38.0, height=38.0)

        # ... и так далее для остальных виджетов

    def kiosk_on_clicked(self):
        user = self.entry_user.get()
        apps = self.entry_apps.get()
        timeout = self.entry_timeout.get()
        firejail = self.entry_firejail.get()

        command = f"kiosk-mode-on -u {user} -a {apps} -t {timeout}"

        if firejail:
            command += f' -f="{firejail}"'

        if self.var_blockbtn.get():
            command += ' -b'

        if self.var_autohide.get():
            command += ' -i'

        if self.var_quiet.get():
            command += ' -q'

        result = run_command(command)

        if result == "":
            messagebox.showinfo("Успех", "Команда выполнена успешно")
        else:
            messagebox.showerror("Ошибка", f"Киоск мод уже настроен для данного пользователя\n\n{result}")

def main():
    if os.getuid() != 0:
        messagebox.showwarning("Недостаточно прав", "Данная программа доступна только для root пользователя!")
        return

    root = tk.Tk()
    app = KioskManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()



# if os.getuid() != 0:
#     messagebox.showwarning("Недостаточно прав", "Данная программа доступна только для root пользователя!")
#     exit()

# window = Tk()
# window.title("Киоск-менеджер")
# window.geometry("1000x660")
# window.configure(bg = "#FFFFFF")

# canvas = Canvas(
#     window,
#     bg = "#FFFFFF",
#     height = 660,
#     width = 1000,
#     bd = 0,
#     highlightthickness = 0,
#     relief = "ridge"
# )

# canvas.place(x = 0, y = 0)
# canvas.create_rectangle(
#     498.0,
#     0.0,
#     998.0,
#     660.0,
#     fill="#F0F0F0",
#     outline="")

# entry_banner = PhotoImage(
#     file=relative_to_assets("input_user.png"))
# entry_bg_1 = canvas.create_image(
#     748.0,
#     182.0,
#     image=entry_banner
# )
# input_user = Entry(
#     bd=0,
#     bg="#FFFFFF",
#     fg="#000716",
#     highlightthickness=0
# )
# input_user.place(
#     x=654.0,
#     y=158.0,
#     width=188.0,
#     height=46.0
# )

# button_banner = PhotoImage(
#     file=relative_to_assets("kiosk_on.png"))

# def kiosk_on_clicked():
#     user = input_user.get()
#     apps = input_apps.get()
#     timeout = inpurt_timeout.get()
#     firejail = input_firejail.get()

#     if not user or not apps:
#         messagebox.showwarning("Предупреждение", "Пожалуйста, проверьте введенные данные")
#         return

#     command = f"kiosk-mode-on -u {user} -a {apps} -t {timeout}"

#     if firejail:
#         command += f' -f="{firejail}"'

#     if var1.get():
#         command += ' -b'

#     if var2.get():
#         command += ' -i'

#     if var3.get():
#         command += ' -q'

#     try:
#         output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
#         messagebox.showinfo("Успех", "Команда выполнена успешно")
#     except subprocess.CalledProcessError as e:
#         messagebox.showerror("Ошибка", f"Киоск мод уже настроен для данного пользователя\n\n{str(e)}")


# kiosk_on = tk.Button(
#     image=button_banner,
#     borderwidth=0,
#     highlightthickness=0,
#     command=kiosk_on_clicked,
#     relief="flat"
# )
# kiosk_on.place(
#     x=630.0,
#     y=485.0,
#     width=236.0,
#     height=48.0
# )

# canvas.create_text(
#     649.0,
#     293.0,
#     anchor="nw",
#     text="Время(мин)",
#     fill="#3F3131",
#     font=("Inter ExtraLight", 16 * -1)
# )

# canvas.create_text(
#     649.0,
#     215.0,
#     anchor="nw",
#     text="Приложения",
#     fill="#3F3131",
#     font=("Inter ExtraLight", 16 * -1)
# )

# canvas.create_text(
#     649.0,
#     371.0,
#     anchor="nw",
#     text="Firejail (опционально)",
#     fill="#3F3131",
#     font=("Inter ExtraLight", 16 * -1)
# )

# entry_background_lines = PhotoImage(
#     file=relative_to_assets("input_apps.png"))
# entry_bg_2 = canvas.create_image(
#     748.0,
#     260.0,
#     image=entry_background_lines
# )
# input_apps = Entry(
#     bd=0,
#     bg="#FFFFFF",
#     fg="#000716",
#     highlightthickness=0
# )
# input_apps.place(
#     x=654.0,
#     y=236.0,
#     width=188.0,
#     height=46.0
# )

# entry_image_3 = PhotoImage(
#     file=relative_to_assets("inpurt_timeout.png"))
# entry_bg_3 = canvas.create_image(
#     748.0,
#     338.0,
#     image=entry_image_3
# )
# inpurt_timeout = Entry(
#     bd=0,
#     bg="#FFFFFF",
#     fg="#000716",
#     highlightthickness=0
# )
# inpurt_timeout.place(
#     x=654.0,
#     y=314.0,
#     width=188.0,
#     height=46.0
# )

# canvas.create_text(
#     649.0,
#     137.0,
#     anchor="nw",
#     text="Имя пользователя",
#     fill="#3F3131",
#     font=("Inter ExtraLight", 16 * -1)
# )

# button_background_lines = PhotoImage(
#     file=relative_to_assets("button_support.png"))
# button_support = Button(
#     image=button_background_lines,
#     borderwidth=0,
#     highlightthickness=0,
#     relief="flat"
# )
# button_support.place(
#     x=888.0,
#     y=637.0,
#     width=107.0,
#     height=17.0
# )

# canvas.create_text(
#     631.0,
#     78.0,
#     anchor="nw",
#     text="Быстрая настройка",
#     fill="#3F3131",
#     font=("Inter Medium", 24 * -1)
# )

# image_banner = PhotoImage(
#     file=relative_to_assets("banner.png"))
# banner = canvas.create_image(
#     249.0,
#     330.0,
#     image=image_banner
# )



# button_image_3 = tk.PhotoImage(file=relative_to_assets("button_dialog_apps.png"))
# button_dialog_apps = tk.Button(
#     image=button_image_3,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: DialogApps(window, input_apps),
#     relief="flat"
# )
# button_dialog_apps.place(x=871.0, y=241.0, width=38.0, height=38.0)



# button_image_4 = tk.PhotoImage(file=relative_to_assets("button_dialog_users.png"))
# button_dialog_users = tk.Button(
#     image=button_image_4,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: DialogUsers(window, input_user),
#     relief="flat"
# )
# button_dialog_users.place(x=871.0, y=163.0, width=38.0, height=38.0)

# image_background_lines = PhotoImage(
#     file=relative_to_assets("background_lines.png"))
# background_lines = canvas.create_image(
#     771.0,
#     495.0,
#     image=image_background_lines
# )

# entry_image_firejail = PhotoImage(
#     file=relative_to_assets("input_firejail.png"))
# entry_bg_firejail = canvas.create_image(
#     748.0,
#     416.0,
#     image=entry_image_firejail
# )
# input_firejail = Entry(
#     bd=0,
#     bg="#FFFFFF",
#     fg="#000716",
#     highlightthickness=0
# )
# input_firejail.place(
#     x=654.0,
#     y=392.0,
#     width=188.0,
#     height=46.0
# )

# var1 = BooleanVar()
# var2 = BooleanVar()
# var3 = BooleanVar()

# # Create checkboxes
# check1 = tk.Checkbutton(
#     text="Blockbtn?",
#     variable=var1,
#     onvalue=True,
#     offvalue=False,
#     bg="#F0F0F0",
#     selectcolor="#F0F0F0",
#     activebackground="#F0F0F0"
# )
# check2 = tk.Checkbutton(
#     text="Autohide?",
#     variable=var2,
#     onvalue=True,
#     offvalue=False,
#     bg="#F0F0F0",
#     selectcolor="#F0F0F0",
#     activebackground="#F0F0F0"
# )
# check3 = tk.Checkbutton(
#     text="Quiet?",
#     variable=var3,
#     onvalue=True,
#     offvalue=False,
#     bg="#F0F0F0",
#     selectcolor="#F0F0F0",
#     activebackground="#F0F0F0"
# )

# # Place checkboxes on the canvas
# check1.place(x=600, y=450)
# check2.place(x=710, y=450)
# check3.place(x=820, y=450)

# window.resizable(False, False)
# window.mainloop()

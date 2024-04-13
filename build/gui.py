from pathlib import Path
import os, subprocess, pwd
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd() + "/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

if os.getuid() != 0:
    messagebox.showwarning("Недостаточно прав", "Данная программа доступна только для root пользователя!")
    exit()

window = Tk()

window.geometry("1000x660")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 660,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    498.0,
    0.0,
    998.0,
    660.0,
    fill="#F0F0F0",
    outline="")

entry_banner = PhotoImage(
    file=relative_to_assets("input_user.png"))
entry_bg_1 = canvas.create_image(
    748.0,
    182.0,
    image=entry_banner
)
input_user = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
input_user.place(
    x=654.0,
    y=158.0,
    width=188.0,
    height=46.0
)

button_banner = PhotoImage(
    file=relative_to_assets("kiosk_on.png"))

def kiosk_on_clicked():
    user = input_user.get()
    apps = input_apps.get()
    timeout = inpurt_timeout.get()

    if not user or not apps:
        messagebox.showwarning("Предупреждение", "Пожалуйста, проверьте введенные данные")
        return

    command = f"kiosk-mode-on -u {user} -a {apps} -t {timeout}"
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        messagebox.showinfo("Успех", "Команда выполнена успешно")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Ошибка", f"Киоск мод уже настроен для данного пользователя\n\n{str(e)}")

kiosk_on = tk.Button(
    image=button_banner,
    borderwidth=0,
    highlightthickness=0,
    command=kiosk_on_clicked,
    relief="flat"
)
kiosk_on.place(
    x=630.0,
    y=440.0,
    width=236.0,
    height=48.0
)

canvas.create_text(
    649.0,
    293.0,
    anchor="nw",
    text="Время(мин)",
    fill="#3F3131",
    font=("Inter ExtraLight", 16 * -1)
)

canvas.create_text(
    649.0,
    215.0,
    anchor="nw",
    text="Приложения",
    fill="#3F3131",
    font=("Inter ExtraLight", 16 * -1)
)

entry_background_lines = PhotoImage(
    file=relative_to_assets("input_apps.png"))
entry_bg_2 = canvas.create_image(
    748.0,
    260.0,
    image=entry_background_lines
)
input_apps = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
input_apps.place(
    x=654.0,
    y=236.0,
    width=188.0,
    height=46.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("inpurt_timeout.png"))
entry_bg_3 = canvas.create_image(
    748.0,
    338.0,
    image=entry_image_3
)
inpurt_timeout = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
inpurt_timeout.place(
    x=654.0,
    y=314.0,
    width=188.0,
    height=46.0
)

canvas.create_text(
    649.0,
    137.0,
    anchor="nw",
    text="Имя пользователя",
    fill="#3F3131",
    font=("Inter ExtraLight", 16 * -1)
)

button_background_lines = PhotoImage(
    file=relative_to_assets("button_support.png"))
button_support = Button(
    image=button_background_lines,
    borderwidth=0,
    highlightthickness=0,
    relief="flat"
)
button_support.place(
    x=888.0,
    y=637.0,
    width=107.0,
    height=17.0
)

canvas.create_text(
    631.0,
    78.0,
    anchor="nw",
    text="Быстрая настройка",
    fill="#3F3131",
    font=("Inter Medium", 24 * -1)
)

image_banner = PhotoImage(
    file=relative_to_assets("banner.png"))
banner = canvas.create_image(
    249.0,
    330.0,
    image=image_banner
)

class DialogApps(Dialog):
    def __init__(self, parent, entry_field):
        self.entry_field = entry_field
        super().__init__(parent)

    def body(self, master):
        # Create a Listbox
        self.listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)

        # Execute the bash script and capture its output
        output = subprocess.check_output("for app in /usr/share/applications/*.desktop; do echo \"${app:24:-8}\"; done", shell=True).decode().strip().split('\n')

        # Populate the Listbox with the output of the bash script
        for item in output:
            self.listbox.insert(tk.END, item)

        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Создание фрагметы для кнопок ниже
        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # Кнопка Подтвердить
        confirm_button = tk.Button(button_frame, text="Подтвердить", command=self.apply)
        confirm_button.pack(side=tk.RIGHT, padx=10)

        # Кнопка Отмена
        cancel_button = tk.Button(button_frame, text="Отменить", command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10)

    def apply(self):
        selected_items = [self.listbox.get(i) for i in self.listbox.curselection()]
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(0, ', '.join(selected_items))
        self.destroy()

    def buttonbox(self):
        return tk.Frame(self)

button_image_3 = tk.PhotoImage(file=relative_to_assets("button_dialog_apps.png"))
button_dialog_apps = tk.Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: DialogApps(window, input_apps),
    relief="flat"
)
button_dialog_apps.place(x=871.0, y=241.0, width=38.0, height=38.0)

class DialogUsers(Dialog):
    def __init__(self, parent, entry_field):
        self.entry_field = entry_field
        super().__init__(parent)

    def body(self, master):
        # Create a Listbox
        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE)

        # Get a list of all users in the system
        users = pwd.getpwall()

        # Filter out the users with an ID less than or equal to 999
        filtered_users = [user for user in users if user.pw_uid > 999]

        # Populate the Listbox with the remaining users
        for user in filtered_users:
            self.listbox.insert(tk.END, user.pw_name)

        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a frame for the buttons
        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # Create a Confirm button
        confirm_button = tk.Button(button_frame, text="Подтвердить", command=self.apply)
        confirm_button.pack(side=tk.RIGHT, padx=10)

        # Create a Cancel button
        cancel_button = tk.Button(button_frame, text="Отменить", command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10)

    def apply(self):
        # Get selected item
        selected_item = self.listbox.get(self.listbox.curselection())
        # Insert selected item into the entry field
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(0, selected_item)
        # Close the dialog
        self.destroy()

    def buttonbox(self):
        # Return an empty frame to remove the default buttons
        return tk.Frame(self)

button_image_4 = tk.PhotoImage(file=relative_to_assets("button_dialog_users.png"))
button_dialog_users = tk.Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: DialogUsers(window, input_user),
    relief="flat"
)
button_dialog_users.place(x=871.0, y=163.0, width=38.0, height=38.0)

image_background_lines = PhotoImage(
    file=relative_to_assets("background_lines.png"))
background_lines = canvas.create_image(
    771.0,
    495.0,
    image=image_background_lines
)

entry_image_firejail = PhotoImage(
    file=relative_to_assets("input_firejail.png"))
entry_bg_firejail = canvas.create_image(
    748.0,
    392.0,
    image=entry_image_firejail
)
input_firejail = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
input_firejail.place(
    x=654.0,
    y=392.0,
    width=188.0,
    height=46.0
)

window.resizable(False, False)
window.mainloop()

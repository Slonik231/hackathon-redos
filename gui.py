import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
from assets_path import relative_to_assets
from dialogs import DialogApps, DialogUsers
from utils import execute_command

class GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Киоск-менеджер")
        self.window.geometry("1000x660")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

        # Создание tk.Canvas
        self.canvas = tk.Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 660,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            498.0,
            0.0,
            998.0,
            660.0,
            fill="#F0F0F0",
            outline="")

        self.entry_banner = tk.PhotoImage(
            file=relative_to_assets("input_user.png"))
        self.entry_bg_1 = self.canvas.create_image(
            748.0,
            182.0,
            image=self.entry_banner
        )
        self.input_user = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.input_user.place(
            x=654.0,
            y=158.0,
            width=188.0,
            height=46.0
        )

        self.button_banner = tk.PhotoImage(
            file=relative_to_assets("kiosk_on.png"))


        self.kiosk_on = tk.Button(
            image=self.button_banner,
            borderwidth=0,
            highlightthickness=0,
            command=self.kiosk_on_clicked,
            relief="flat"
        )
        self.kiosk_on.place(
            x=630.0,
            y=485.0,
            width=236.0,
            height=48.0
        )

        self.canvas.create_text(
            649.0,
            293.0,
            anchor="nw",
            text="Время(мин)",
            fill="#3F3131",
            font=("Inter ExtraLight", 16 * -1)
        )

        self.canvas.create_text(
            649.0,
            215.0,
            anchor="nw",
            text="Приложения",
            fill="#3F3131",
            font=("Inter ExtraLight", 16 * -1)
        )

        self.canvas.create_text(
            649.0,
            371.0,
            anchor="nw",
            text="Firejail (опционально)",
            fill="#3F3131",
            font=("Inter ExtraLight", 16 * -1)
        )

        self.entry_background_lines = tk.PhotoImage(
            file=relative_to_assets("input_apps.png"))
        self.entry_bg_2 = self.canvas.create_image(
            748.0,
            260.0,
            image=self.entry_background_lines
        )
        self.input_apps = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.input_apps.place(
            x=654.0,
            y=236.0,
            width=188.0,
            height=46.0
        )

        self.entry_image_3 = tk.PhotoImage(
            file=relative_to_assets("inpurt_timeout.png"))
        self.entry_bg_3 = self.canvas.create_image(
            748.0,
            338.0,
            image=self.entry_image_3
        )
        self.inpurt_timeout = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.inpurt_timeout.place(
            x=654.0,
            y=314.0,
            width=188.0,
            height=46.0
        )

        self.canvas.create_text(
            649.0,
            137.0,
            anchor="nw",
            text="Имя пользователя",
            fill="#3F3131",
            font=("Inter ExtraLight", 16 * -1)
        )

        self.button_background_lines = tk.PhotoImage(
            file=relative_to_assets("button_support.png"))
        self.button_support =tk.Button(
            image=self.button_background_lines,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_support.place(
            x=888.0,
            y=637.0,
            width=107.0,
            height=17.0
        )

        self.canvas.create_text(
            631.0,
            78.0,
            anchor="nw",
            text="Быстрая настройка",
            fill="#3F3131",
            font=("Inter Medium", 24 * -1)
        )

        self.image_banner = tk.PhotoImage(
            file=relative_to_assets("banner.png"))
        self.banner = self.canvas.create_image(
            249.0,
            330.0,
            image=self.image_banner
        )

        self.button_image_3 = tk.PhotoImage(file=relative_to_assets("button_dialog_apps.png"))
        self.button_dialog_apps = tk.Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: DialogApps(self.window, self.input_apps),
            relief="flat"
        )
        self.button_dialog_apps.place(x=871.0, y=241.0, width=38.0, height=38.0)
        self.button_image_4 = tk.PhotoImage(file=relative_to_assets("button_dialog_users.png"))
        self.button_dialog_users = tk.Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: DialogUsers(self.window, self.input_user),
            relief="flat"
        )
        self.button_dialog_users.place(x=871.0, y=163.0, width=38.0, height=38.0)

        self.image_background_lines = tk.PhotoImage(
            file=relative_to_assets("background_lines.png"))
        self.background_lines = self.canvas.create_image(
            771.0,
            495.0,
            image=self.image_background_lines
        )

        self.entry_image_firejail = tk.PhotoImage(
            file=relative_to_assets("input_firejail.png"))
        self.entry_bg_firejail = self.canvas.create_image(
            748.0,
            416.0,
            image=self.entry_image_firejail
        )
        self.input_firejail = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.input_firejail.place(
            x=654.0,
            y=392.0,
            width=188.0,
            height=46.0
        )

        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()

        # Create checkboxes
        self.check1 = tk.Checkbutton(
            text="Blockbtn?",
            variable=self.var1,
            onvalue=True,
            offvalue=False,
            bg="#F0F0F0",
            selectcolor="#F0F0F0",
            activebackground="#F0F0F0"
        )
        self.check2 = tk.Checkbutton(
            text="Autohide?",
            variable=self.var2,
            onvalue=True,
            offvalue=False,
            bg="#F0F0F0",
            selectcolor="#F0F0F0",
            activebackground="#F0F0F0"
        )
        self.check3 = tk.Checkbutton(
            text="Quiet?",
            variable=self.var3,
            onvalue=True,
            offvalue=False,
            bg="#F0F0F0",
            selectcolor="#F0F0F0",
            activebackground="#F0F0F0"
        )

        # Place checkboxes on the canvas
        self.check1.place(x=600, y=450)
        self.check2.place(x=710, y=450)
        self.check3.place(x=820, y=450)

    def kiosk_on_clicked(self):
        user = self.input_user.get()
        apps = self.input_apps.get()
        timeout = self.inpurt_timeout.get()
        firejail = self.input_firejail.get()

        command = f"kiosk-mode-on -u {user} -a {apps} -t {timeout}"

        if firejail:
            command += f' -f="{firejail}"'

        if self.var1.get():
            command += ' -b'

        if self.var2.get():
            command += ' -i'

        if self.var3.get():
            command += ' -q'

        try:
            output = execute_command(command)
            tk.messagebox.showinfo("Успех", "Команда выполнена успешно")
        except Exception as e:
            tk.messagebox.showerror("Ошибка", f"Киоск мод уже настроен для данного пользователя\n\n{str(e)}")

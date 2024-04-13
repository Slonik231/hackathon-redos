import tkinter as tk
from tkinter import messagebox
from utils import relative_to_assets
from dialogs import DialogApps, DialogUsers

class KioskManagerApp:
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
        self.canvas.create_rectangle(
            498.0,
            0.0,
            998.0,
            660.0,
            fill="#F0F0F0",
            outline=""
        )

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

        self.button_kiosk_on = tk.Button(
            image=tk.PhotoImage(file=relative_to_assets("kiosk_on.png")),
            borderwidth=0,
            highlightthickness=0,
            command=self.kiosk_on_clicked,
            relief="flat"
        )
        self.button_kiosk_on.place(
            x=630.0,
            y=485.0,
            width=236.0,
            height=48.0
        )

        self.entry_apps = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_apps.place(
            x=654.0,
            y=236.0,
            width=188.0,
            height=46.0
        )

        self.entry_timeout = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_timeout.place(
            x=654.0,
            y=314.0,
            width=188.0,
            height=46.0
        )

        self.entry_firejail = tk.Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_firejail.place(
            x=654.0,
            y=392.0,
            width=188.0,
            height=46.0
        )

        self.var1 = tk.BooleanVar()
        self.var2 = tk.BooleanVar()
        self.var3 = tk.BooleanVar()

        self.check1 = tk.Checkbutton(
            text="Blockbtn?",
            variable=self.var1,
            onvalue=True,
            offvalue=False,
            bg="#F0F0F0",
            selectcolor="#F0F0F0",
            activebackground="#F0F0F0"
        )
        self.check1.place(x=600, y=450)

        self.check2 = tk.Checkbutton(
            text="Autohide?",
            variable=self.var2,
            onvalue=True,
            offvalue=False,
            bg="#F0F0F0",
            selectcolor="#F0F0F0",
            activebackground="#F0F0F0"
        )
        self.check2.place(x=710, y=450)

        self.check3 = tk.Checkbutton(
            text="Quiet?",
            variable=self.var3,
            onvalue=True,
            offvalue=False,
            bg="#F0F0F0",
            selectcolor="#F0F0F0",
            activebackground="#F0F0F0"
        )
        self.check3.place(x=820, y=450)

        self.create_widgets()

    def create_widgets(self):
        # Создание остальных виджетов
        pass

    def kiosk_on_clicked(self):
        user = self.entry_user.get()
        apps = self.entry_apps.get()
        timeout = self.entry_timeout.get()
        firejail = self.entry_firejail.get()

        if not user or not apps:
            messagebox.showwarning("Предупреждение", "Пожалуйста, проверьте введенные данные")
            return

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
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            messagebox.showinfo("Успех", "Команда выполнена успешно")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Ошибка", f"Киоск мод уже настроен для данного пользователя\n\n{str(e)}")

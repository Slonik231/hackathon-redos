import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import Dialog
import subprocess
import pwd

class DialogApps(Dialog):
    def __init__(self, parent, entry_field):
        self.entry_field = entry_field
        super().__init__(parent)

    def body(self, master):
        self.listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)

        output = subprocess.check_output("for app in /usr/share/applications/*.desktop; do echo \"${app:24:-8}\"; done", shell=True).decode().strip().split('\n')

        for item in output:
            self.listbox.insert(tk.END, item)

        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        confirm_button = tk.Button(button_frame, text="Подтвердить", command=self.apply)
        confirm_button.pack(side=tk.RIGHT, padx=10)

        cancel_button = tk.Button(button_frame, text="Отменить", command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10)

    def apply(self):
        selected_items = [self.listbox.get(i) for i in self.listbox.curselection()]
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(0, ', '.join(selected_items))
        self.destroy()

    def buttonbox(self):
        return tk.Frame(self)

class DialogUsers(Dialog):
    def __init__(self, parent, entry_field):
        self.entry_field = entry_field
        super().__init__(parent)

    def body(self, master):
        self.listbox = tk.Listbox(master, selectmode=tk.SINGLE)

        users = pwd.getpwall()
        filtered_users = [user for user in users if user.pw_uid > 999]

        for user in filtered_users:
            self.listbox.insert(tk.END, user.pw_name)

        self.listbox.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        button_frame = tk.Frame(master)
        button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        confirm_button = tk.Button(button_frame, text="Подтвердить", command=self.apply)
        confirm_button.pack(side=tk.RIGHT, padx=10)

        cancel_button = tk.Button(button_frame, text="Отменить", command=self.cancel)
        cancel_button.pack(side=tk.RIGHT, padx=10)

    def apply(self):
        selected_item = self.listbox.get(self.listbox.curselection())
        self.entry_field.delete(0, tk.END)
        self.entry_field.insert(0, selected_item)
        self.destroy()

    def buttonbox(self):
        return tk.Frame(self)

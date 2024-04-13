import tkinter as tk
from tkinter import simpledialog

class DialogApps(simpledialog.Dialog):
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

class DialogUsers(simpledialog.Dialog):
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
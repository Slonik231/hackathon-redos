from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(os.getcwd() + "/build/assets/frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    748.0,
    182.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=654.0,
    y=158.0,
    width=188.0,
    height=46.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=630.0,
    y=392.0,
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

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    748.0,
    260.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=654.0,
    y=236.0,
    width=188.0,
    height=46.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    748.0,
    338.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
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

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
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

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    249.0,
    330.0,
    image=image_image_1
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=871.0,
    y=241.0,
    width=38.0,
    height=38.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=871.0,
    y=163.0,
    width=38.0,
    height=38.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    771.0,
    495.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\4Code\Python\reboot\Python-Project\python\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1133x744")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 744,
    width = 1133,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    431.0,
    48.0,
    1081.0,
    698.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    656.0,
    85.0,
    anchor="nw",
    text="BÁO CÁO THỐNG KÊ",
    fill="#1E1E1E",
    font=("Inter SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()

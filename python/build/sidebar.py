
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk

class App(Tk):
    def __init__(self):
        super().__init__()
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.geometry("1133x744")
        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=744,
            width=1133,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            379.0,
            745.0,
            fill="#161F80",
            outline="")

        self.canvas.create_text(
            35.0,
            41.0,
            anchor="nw",
            text="ỨNG DỤNG QUẢN LÝ NHÂN SỰ",
            fill="#FFFFFF",
            font=("Inter SemiBold", 20 * -1)
        )

        self.contentFrame = tk.Frame(self, width=650, height=650, bg="white") 
        self.contentFrame.place(x=440, y=10)
        self.open_find_btn2()

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            bg="#161F80",
            activebackground="#161F80",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_cam_btn1(),
            relief="flat",
            cursor="hand2"
        )
        self.button_1.place(
            x=35.0,
            y=172.0,
            width=304.0,
            height=24.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            bg="#161F80",
            activebackground="#161F80",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_find_btn2(),
            relief="flat",
            cursor="hand2"
        )
        self.button_2.place(
            x=35.0,
            y=211.0,
            width=304.0,
            height=24.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            bg="#161F80",
            activebackground="#161F80",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_new_btn3(),
            relief="flat",
            cursor="hand2"
        )
        self.button_3.place(
            x=35.0,
            y=250.0,
            width=304.0,
            height=24.0
        )

        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            bg="#161F80",
            activebackground="#161F80",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_edit_btn4(),
            relief="flat",
            cursor="hand2"
        )
        self.button_4.place(
            x=35.0,
            y=289.0,
            width=304.0,
            height=24.0
        )

        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            bg="#161F80",
            activebackground="#161F80",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_history_btn5(),
            relief="flat",
            cursor="hand2"
        )
        self.button_5.place(
            x=35.0,
            y=328.0,
            width=304.0,
            height=24.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            bg="#161F80",
            activebackground="#161F80",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.open_schedule_btn6(),
            relief="flat",
            cursor="hand2"
        )
        self.button_6.place(
            x=35.0,
            y=367.0,
            width=304.0,
            height=24.0
        )

        self.resizable(False,False)

    def open_cam_btn1(self):
        from cam import Cam
        self.clean_content()
        self.cam = Cam(self.contentFrame) 
        self.cam.place(x=0,y=0,width=650,height=650)

    def open_find_btn2(self):
        from find import Find
        self.clean_content()
        self.find = Find(self.contentFrame) 
        self.find.place(x=0,y=0,width=650,height=650)

    def open_new_btn3(self):
        from new import New
        self.clean_content()
        self.new = New(self.contentFrame)
        self.new.place(x=0,y=0,width=650,height=650)
        
    def open_edit_btn4(self):
        from edit import Edit
        self.clean_content()
        self.edit = Edit(self.contentFrame)
        self.edit.place(x=0,y=0,width=650,height=650)

    def open_history_btn5(self):
        from history import History
        self.clean_content()
        self.history = History(self.contentFrame)
        self.history.place(x=0,y=0,width=650,height=650)

    def open_schedule_btn6(self):
        from schedule import Schedule
        self.clean_content()
        self.schedule = Schedule(self.contentFrame)
        self.schedule.place(x=0,y=0,width=650,height=650)


    def clean_content(self):
        if self.contentFrame.winfo_children():
            for widget in self.contentFrame.winfo_children():
                widget.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, messagebox, END
from tkcalendar import DateEntry
from tkinter.messagebox import askyesno
import duty, staff

class Edit(ttk.Frame):

    def __init__(self, frame):
        super().__init__(frame)
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame2")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 650,
            width = 650,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge",
            background="#fff"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            20.0,
            48.0,
            1081.0,
            698.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            207.0,
            65.0,
            anchor="nw",
            text="CHỈNH SỬA THÔNG TIN",
            fill="#1E1E1E",
            font=("Inter SemiBold", 20 * -1)
        )

        self.canvas.create_rectangle(
            123.0,  # 554
            99.0,
            574.0,
            260.0,
            fill="#fff",
            outline=""
        )
        # ==========================================================================================
        self.entry_image_5 = PhotoImage(
            file=relative_to_assets("entry_4.png"))
        self.entry_bg_5 = self.canvas.create_image(
            300.0,
            120.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=104.0,
            y=106.0,
            width=310.0,
            height=26.0
        )
        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.find_staff(self.entry_5.get()),
            relief="flat"
        )
        self.button_3.place(
            x=466.0,
            y=105.0,
            width=80.0,
            height=30.0
        )

        self.canvas.create_text(
            136.0,  # 567
            169.0,
            anchor="nw",
            text="Mã cá nhân",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            386,
            179.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0,
        )
        self.entry_1.place(
            x=260,
            y=165.0,
            width=253.0,
            height=28.0
        )

        self.entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            386,
            214.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=260.0,
            y=200.0,
            width=253.0,
            height=28.0
        )

        self.canvas.create_text(
            136.0,
            204.0,
            anchor="nw",
            text="Họ và tên",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        options = duty.select_all()
        self.entry_image_3 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            386,
            249.0,
            image=self.entry_image_3
        )
        self.entry_3 = ttk.Combobox(
            self,
            state="readonly",
            values=options,
        )
        self.entry_3.place(
            x=260,
            y=235.0,
            width=253.0,
            height=28.0
        )

        self.canvas.create_text(
            136.0,
            239.0,
            anchor="nw",
            text="Chức vụ",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file=relative_to_assets("entry_3.png"))
        self.entry_bg_4 = self.canvas.create_image(
            386,
            284.0,
            image=self.entry_image_3
        )
        self.entry_4 = DateEntry(
            self,
            state="readonly"
        )
        self.entry_4.place(
            x=260,
            y=270.0,
            width=253.0,
            height=28.0
        )

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_1.place(
            x=250.0,
            y=319.0,
            width=70.0,
            height=30.0
        )
        self.canvas.create_text(
            136.0,
            274.0,
            anchor="nw",
            text="Ngày sinh",
            fill="#000000",
            font=("Inter SemiBold", 15 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            relief="flat"
        )
        self.button_2.place(
            x=335.0,
            y=319.0,
            width=70.0,
            height=30.0
        )

        #right
        self.canvas.create_rectangle(
            527.0,
            149.0,
            529.0,
            359.0,
            fill="#000000",
            outline="")

        #bot
        self.canvas.create_rectangle(
            123.0,
            358.0,
            527.0,
            360.0,
            fill="#000000",
            outline="")

        #left
        self.canvas.create_rectangle(
            123.0,
            149.0,
            125.0,
            358.0,
            fill="#000000",
            outline="")

        #top
        self.canvas.create_rectangle(
            123.0,
            148.0,
            527.0,
            150.0,
            fill="#000000",
            outline="")
        # ======================================================================================

    def find_staff(self,input):
        if input in staff.select_id():
            print(input)
            self.entry_1.delete(0, END)
            self.entry_1.insert(0, input)
            self.entry_2.insert(0, staff.select_one_name(input))
            self.button_1.config(command=lambda: self.update_data())
            self.button_2.config(command=lambda: self.delete())

        else:
            messagebox.showerror("Lỗi","Không tìm thấy nhân viên")
            self.entry_5.delete(0, END)

    def update_data(self):
        answer = askyesno(title="Confirm insert",
                        message='Bạn chắc chắn chứ ?')

        if answer:
            if self.entry_1.get() == '' or self.entry_2.get() == '' or self.entry_4.get() == '':

                messagebox.showerror(
                    'Invalid input', 'Thông tin không được để trống')
                return
            if not self.entry_1.get().isdigit():
                messagebox.showerror(
                    'Invalid input', 'Mã cá nhân phải là số')
                return
            try:
                staff.update(
                    self.entry_1.get(), self.entry_2.get(),self.entry_4.get(), duty.select_name(self.entry_3.get())),
            except ValueError:
                messagebox.showerror(
                    'ERROR ⚠', 'Mã trùng')
                return
            messagebox.showinfo('Done!!!', "Đã sửa thành công")

            self.entry_1.delete(0, END)
            self.entry_2.delete(0, END)
            self.button_1.config(command=self.empty)
            self.button_2.config(command=self.empty)

    def delete(self):
        answer = askyesno(title="Confirm insert",
                        message='Bạn chắc chắn muốn xóa ?')
        
        if answer:
            try:
                staff.delete(self.entry_1.get())
            except ValueError:
                messagebox.showerror(
                    'ERROR ⚠', 'Đã xảy ra lỗi hãy thử lại')
                return
            messagebox.showinfo('Done!!!', "Đã xóa thành công")
            self.entry_1.delete(0, END)
            self.entry_2.delete(0, END)
            self.button_1.config(command=self.empty)
            self.button_2.config(command=self.empty)

    
    def empty(self):
        print("")

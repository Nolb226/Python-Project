from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, ttk, END, messagebox
from tkcalendar import DateEntry
import tkinter.font as tkFont
import staff, checkin, checkout

class History(ttk.Frame):
    def __init__(self, frame):
        super().__init__(frame)

        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r".\assets\frame4")


        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)
        
        self.canvas = Canvas(
            self,
            bg = "#FFFFFF",
            height = 650,
            width = 650,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            431.0,
            48.0,
            1081.0,
            698.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            200.0,
            65.0,
            anchor="nw",
            text="LỊCH SỬ CHẤM CÔNG",
            fill="#1E1E1E",
            font=("Inter SemiBold", 20 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            250.0,
            120.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self,
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=54.0,
            y=106.0,
            width=310.0,
            height=26.0
        )

        self.entry_2 = DateEntry(
            self,
            state="readonly"
        )
        self.entry_2.place(
            x=450.0,
            y=105.0,
            width=80.0,
            height=30.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.set_data_table(self.entry_1.get(), self.entry_2.get(), self.type),
            relief="flat"
        )
        self.button_3.place(
            x=530.0,
            y=105.0,
            width=60.0,
            height=30.0
        )

        self.hisTable = ttk.Treeview()
        self.style = ttk.Style()
        self.style.configure("myStyle.Treeview", font=('Calibri', 14), rowheight=30) # Modify the font of the body
        self.style.configure("myStyle.Treeview.Heading", font=('Calibri', 16,'bold')) # Modify the font of the headings
        self.style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])
        self.set_table(1)

        self.font_style = tkFont.Font(family="Helvetica", size=12, weight="normal") 

        self.type = 1

        # Nút Checkin
        self.in_button = Button(
            self, text="Check in", command=lambda: self.set_table(1), font=self.font_style)
        self.in_button.place(x=0,y=610, width=300, height=40)

        # Nút Checkout
        self.out_button = Button(
            self, text="Check out", command=lambda: self.set_table(2), font=self.font_style)
        self.out_button.place(x=305, y=610, width=300, height=40)

    def set_table(self, type):
        
        self.set_heading_table(type)
        vsb = ttk.Scrollbar(self, orient="vertical", command=self.hisTable.yview)
        vsb.place(x=622,y=150,height=500)
        self.hisTable.configure(yscrollcommand=vsb.set)
        for i in range(len(self.columns)):
            self.hisTable.heading(i, text=self.columns[i])
            self.hisTable.column(i, width=200, anchor='center')
        self.set_data_table("","",type)
    
    def set_heading_table(self, type):
        self.hisTable.place_forget()
        if type == 1:
            self.columns = ('Mã nhân viên','Tên nhân viên','Check In')
            self.hisTable = ttk.Treeview(self, columns=self.columns, show="headings", style="myStyle.Treeview")
        else:
            self.columns = ('Mã nhân viên','Tên nhân viên','Check Out')
            self.hisTable = ttk.Treeview(self, columns=self.columns, show="headings", style="myStyle.Treeview")


    def set_data_table(self, code, date, type):
        self.type = type
        if self.hisTable.get_children():
            self.hisTable.delete(*self.hisTable.get_children())
        data = None
        if type == 1:
            if code == "" and date == "" :
                data = checkin.select("","")
            elif code == "" or date == "" :
                if code != "" :
                    data = checkin.select_by_id(code)
                else:
                    formatted_date = self.format_date(date)
                    data = checkin.select_by_date(formatted_date)
            else:
                formatted_date = self.format_date(date)
                data = checkin.select(code,formatted_date)
        else:
            if code == "" and date == "" :
                data = checkout.select("","")
            elif code == "" or date == "" :
                if code != "" :
                    data = checkout.select_by_id(code)
                else:
                    formatted_date = self.format_date(date)
                    data = checkout.select_by_date(formatted_date)
            else:
                formatted_date = self.format_date(date)
                data = checkout.select(code,formatted_date)
        for row in data:
            self.hisTable.insert('','end',values=(row[0], staff.search2(row[0])[1], row[1]))
        self.hisTable.place(x=0,y=150, height=455)

    def format_date(self,date):
        # Chuyển đổi thành đối tượng datetime
        date_object = date.split("/")
        # Chuyển đổi thành chuỗi với định dạng "dd/mm/yyyy"
        formatted_date = "{}{}-{}-{}".format(20,date_object[2],date_object[0],date_object[1])
        return formatted_date
        

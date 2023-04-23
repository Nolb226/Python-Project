import cv2
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import face_recognition
import os
from tkcalendar import DateEntry
from playsound import playsound
import datetime
import encoding
import checkin
import checkout
import staff


class App:

    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.geometry('1050x480+300+50')

        # Khởi tạo camera
        self.video_capture = cv2.VideoCapture(0)

        # Tạo một label để hiển thị hình ảnh
        self.label = tk.Label(window)
        self.label.place(x=0, y=0)

        # Tạo 1 frame chứa các nút chức năng và hiển thị kết quả
        self.resultFrame = tk.Frame(window, width=400, height=480)
        self.resultFrame.place(x=650, y=0)

        # Nút cập nhật
        self.update_button = tk.Button(
            self.resultFrame, text="Refresh", command=self.encode)
        self.update_button.place(x=330, y=5, relwidth=0.15, height=30)

        # Nút để chụp ảnh
        self.cap_button = tk.Button(
            self.resultFrame, text="Capture", command=self.capture)
        self.cap_button.place(x=330, y=40, relwidth=0.15, height=30)

        # Nút Checkin
        self.in_button = tk.Button(
            self.resultFrame, text="Check in", command=lambda: self.check(1))
        self.in_button.place(x=330, y=75, relwidth=0.15, height=30)

        # Nút Checkout
        self.out_button = tk.Button(
            self.resultFrame, text="Check out", command=lambda: self.check(2))
        self.out_button.place(x=330, y=110, relwidth=0.15, height=30)

        # Nút xem lịch sử
        self.quit_button = tk.Button(
            self.resultFrame, text="History", command=self.history)
        self.quit_button.place(x=330, y=145, relwidth=0.15, height=30)

        # Đăng ký
        # prettier-ignore
        self.border = LabelFrame(self.resultFrame, bd=2, bg="black")
        # self.border.pack(pady=10)
        self.border.place(x=330, y=180, relwidth=0.15, height=30)
        self.open_signup_form = Button(self.border, text="Đăng ký", width=8,
                                       bg="white", fg="black", activebackground="green", activeforeground="black", 
                                       command=lambda: self.open_popup(window))
        self.open_signup_form.pack()

        # Nút để thoát ứng dụng
        self.quit_button = tk.Button(
            self.resultFrame, text="Quit", command=self.quit)
        self.quit_button.place(x=330, y=215, relwidth=0.15, height=30)

        # Khởi tạo font
        self.myFont = tkFont.Font(family='Helvetica', size=12, weight='bold')

        # Ô input để nhập mã nv đăng ký khuôn mặt (lưu ý chỉ được đk khi nv đó đã có trong db)
        self.inputValue = StringVar("")
        self.inputId = Entry(
            self.resultFrame, textvariable=self.inputValue, justify="center", font=self.myFont)
        self.inputId.place(x=35, y=5, relwidth=0.65, relheight=0.05)

        # Label hiển thị thời gian
        self.timeLabel = tk.Label(window)
        self.display_time()
        self.timeLabel.place(x=0, y=0)

        # Các label hiển thị kết quả
        self.photo = ImageTk.PhotoImage(Image.open("icon/done.png"))
        self.photo2 = ImageTk.PhotoImage(Image.open("icon/close.png"))
        self.photo3 = ImageTk.PhotoImage(Image.open("icon/wait.png"))
        self.resultImage = tk.Label(self.resultFrame)
        self.resultImage.place(x=65, y=180)

        self.resultId = tk.Label(self.resultFrame, font=self.myFont)
        self.resultId.place(x=65, y=120, width=200, height=30)
        self.resultName = tk.Label(self.resultFrame, font=self.myFont)
        self.resultName.place(x=65, y=150, width=200, height=30)

        #Frame hiển thị lịch sử chấm công
        self.historyFrame = tk.Frame(self.resultFrame)

        # Lấy mã hóa của các khuôn mặt tron dataset
        self.encode()

        # Update hình ảnh lên label
        self.update()

    def update(self):
        # Đọc hình ảnh từ camera
        ret, frame = self.video_capture.read()

        # Lấy kích thước khung hình
        height, width, _ = frame.shape

        # Tính toán tâm của hình oval
        center_x = int(width / 2)
        center_y = int(height / 2)

        # Tính toán bán kính theo chiều dài và rộng của hình oval
        radius_x = int(width / 4.5)
        radius_y = int(height / 3)

        # Vẽ hình oval trên khung hình
        cv2.ellipse(frame, (center_x, center_y), (radius_x, radius_y), 0, 0, 360, (0, 255, 0), thickness=2)

        if ret:
            # Chuyển đổi hình ảnh từ OpenCV sang PIL để hiển thị trên tkinter
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = Image.fromarray(img)
            imgtk = ImageTk.PhotoImage(image=pil_img)

            # Hiển thị hình ảnh lên tkinter
            self.label.config(image=imgtk)
            self.label.image = imgtk

        # Lặp lại việc cập nhật sau 15ms
        self.label.after(15, self.update)

    def display_time(self):
        time = datetime.datetime.now().strftime('%H:%M:%S')
        self.timeLabel.config(text=time)
        self.timeLabel.after(1000, self.display_time)

    def quit(self):
        self.video_capture.release()
        self.window.quit()

    def capture(self):
        if self.inputValue.get() in staff.select_id():
            ret, frame = self.video_capture.read()
            staffCode = self.inputValue.get()
            index = encoding.get_number_of_paths(staffCode)+1
            if ret:
                pathName = "dataset/{}".format(staffCode)
                if not os.path.exists(pathName):
                    os.makedirs(pathName)
                cv2.imwrite("{}/{}-{}.jpg".format(pathName,
                            staffCode, index), frame)
                index += 1
        else:
            self.notice(0)

    def encode(self):
        self.resultName.config(text="Please, wait...", anchor="center")
        self.resultImage.config(image=self.photo3)
        self.data = encoding.get_encodings()
        self.id = encoding.get_staff_id()
        self.resultFrame.after(2000, self.clean)

    def check(self, type):
        self.historyFrame.place_forget()
        ret, frame = self.video_capture.read()
        if ret:
            # Tìm các khuôn mặt trong hình ảnh
            face_location = face_recognition.face_locations(frame)
            try :
                face_encoding = face_recognition.face_encodings(
                    frame, face_location)[0]
            except:
                self.notice(0)
            # So sánh với hình ảnh có sẵn
            for i in range(len(self.data)):
                match = face_recognition.face_distance(
                    [self.data[i]], face_encoding)[0]
                same = False
                code = ""
                print(match)
                print(self.id[i])
                if match < 0.4:
                    same = True
                    code = self.id[i]
                    break
            if same == True:
                now = datetime.datetime.now()
                result = staff.search(code)
                self.resultId.config(text="ID: " + result[0], anchor='w')
                self.resultName.config(text="Tên: " + result[1], anchor='w')
                self.notice(1)
                if type == 1:
                    # Đưa dữ liệu vào database
                    a = checkin.Checkin(code, now)
                    a.insert()
                else:
                    # Đưa dữ liệu vào database
                    a = checkout.Checkout(code, now)
                    a.insert()
            else:
                self.notice(0)

    def clean(self):
        self.resultImage.configure(image="")
        self.resultId.configure(text="")
        self.resultName.configure(text="")
        self.inputValue.set("")

    def notice(self, status):
        if status == 1:
            self.resultImage.config(image=self.photo)
            playsound("mp3.2\\Pleasetry-again2.mp3")
        else:
            self.resultImage.config(image=self.photo2)
            playsound("mp3\\Pleasetry-again.mp3")
        # Xóa hình ảnh sau khi hiển thị
        self.resultFrame.after(2000, self.clean)

    def open_popup(self, window):
        from tkinter import ttk

        top = Toplevel(window)
        top.geometry("260x260")
        top.resizable(FALSE, FALSE)
        from gui import SignUpForm
        frame = SignUpForm(top)
        frame.pack(fill=BOTH, expand=TRUE)

    def history(self):

        self.historyFrame.place(x = 35, y = 40,relwidth=0.65, height=500)

        self.dateEntry = DateEntry(self.historyFrame)
        self.filtButton = Button(self.historyFrame, text="Filter", 
                                 command=lambda: self.updateTreeview(self.dateEntry.get(),1))
        self.in_button = Button(self.historyFrame, text="In", 
                                command=lambda: self.updateTreeview(self.dateEntry.get(),1))
        self.out_button = Button(self.historyFrame, text="Out", 
                                 command=lambda: self.updateTreeview(self.dateEntry.get(),0))
        self.columns = ('ID', 'Time')
        self.table = ttk.Treeview(self.historyFrame, columns=self.columns, show='headings')

        # Thiết lập các thuộc tính cho bảng
        for col in self.columns:
            self.table.column(col, width=100)
            self.table.heading(col, text=col.title())

        self.updateTreeview("",1)

        self.dateEntry.place(x = 0, y = 0, relwidth=0.7, height=30)
        self.filtButton.place(relx= 0.75, y = 0, relwidth=0.25, height=30)
        self.table.place(x = 0, y = 35, relwidth=1, height=350)
        self.in_button.place(x= 0, y = 390, relwidth=0.48,height=30)
        self.out_button.place(relx= 0.52, y = 390, relwidth=0.48,height=30)


    def updateTreeview(self, date, type):
        if self.table.get_children():
            self.table.delete(*self.table.get_children())
        formatted_date = ""
        if date != "":
            # Chuyển đổi thành đối tượng datetime
            date_object = date.split("/")
            # Chuyển đổi thành chuỗi với định dạng "dd/mm/yyyy"
            formatted_date = "{}{}-{}-{}".format(20,date_object[2],date_object[0],date_object[1])
        if type == 1:
            data = checkin.select(formatted_date)
        else:
            data = checkout.select(formatted_date)
        
         # Thêm dữ liệu vào bảng
        for row in data:
            self.table.insert('', 'end', values=row)


# Khởi tạo ứng dụng
App(tk.Tk(), "Camera Feed")
tk.mainloop()

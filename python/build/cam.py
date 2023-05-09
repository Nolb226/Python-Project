import cv2
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import face_recognition
import os
from tkcalendar import DateEntry
import tkinter.simpledialog as sd
import datetime
import encoding
import checkin
import checkout
import staff


class Cam(ttk.Frame):

    def __init__(self, window):
        super().__init__(window)
        # Khởi tạo camera
        self.video_capture = cv2.VideoCapture(0)

        # Tạo một label để hiển thị hình ảnh
        self.label = tk.Label(window)
        self.label.place(x=0, y=0, width=650, height=480)

        # Tạo 1 frame chứa các nút chức năng và hiển thị kết quả
        self.resultFrame = tk.Frame(window, width=650, height=170)
        self.resultFrame.place(x=0, y=480)

        self.font_style = tkFont.Font(family="Helvetica", size=12, weight="normal") 

        # Nút Checkin
        self.in_button = tk.Button(
            self.resultFrame, text="Check in", command=lambda: self.check(1), font=self.font_style)
        
        # Nút Checkout
        self.out_button = tk.Button(
            self.resultFrame, text="Check out", command=lambda: self.check(2), font=self.font_style)
        
         # Nút đăng ký
        self.signUp_button = tk.Button(
            self.resultFrame, text="Đăng ký", command=lambda:self.show_message(),font=self.font_style)
        
        # Nút cập nhật
        self.update_button = tk.Button(
            self.resultFrame, text="Cập nhật", command=self.encode, font=self.font_style)
        
        # Nút để chụp ảnh
        self.cap_button = tk.Button(
            self.resultFrame, text="Capture", command=self.capture, font=self.font_style)
        
        # Nút quay lại
        self.back_button = tk.Button(
            self.resultFrame, text="Back", command=lambda:self.time_keeping(), font=self.font_style)
        
        # Khởi tạo font
        self.myFont = tkFont.Font(family='Helvetica', size=12, weight='bold')

        # Label hiển thị thời gian
        self.timeLabel = tk.Label(window)
        self.display_time()
        self.timeLabel.place(x=0, y=0)

        self.resultId = tk.Label(self.resultFrame, font=self.myFont)
        self.resultId.place(x=0, y=50, relwidth=1, height=30)
        self.resultName = tk.Label(self.resultFrame, font=self.myFont)
        self.resultName.place(x=0, y=80,  relwidth=1, height=30)
        self.resultNotice = tk.Label(self.resultFrame, font=self.myFont)
        self.resultNotice.place(x=0, y=110,  relwidth=1, height=30)

        self.time_keeping()

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
        ret, frame = self.video_capture.read()
        staffCode = self.inputValue
        index = encoding.get_number_of_paths(staffCode)+1
        if ret:
            pathName = "build/dataset/{}".format(staffCode)
            if not os.path.exists(pathName):
                os.makedirs(pathName)
            cv2.imwrite("{}/{}-{}.jpg".format(pathName,
                        staffCode, index), frame)
            index += 1
        self.resultNotice.config(text="Chụp thành công", anchor="center")
        self.resultNotice.after(2000, lambda: self.resultNotice.configure(text=""))

    def encode(self):
        self.resultName.config(text="Please, wait...", anchor="center")
        self.data = encoding.get_encodings()
        self.id = encoding.get_staff_id()
        self.resultFrame.after(2000, self.clean)

    def check(self, type):
        ret, frame = self.video_capture.read()
        same = False
        if ret:
            # Tìm các khuôn mặt trong hình ảnh
            face_location = face_recognition.face_locations(frame)
            try :
                face_encoding = face_recognition.face_encodings(
                    frame, face_location)[0]
            except:
                self.notice()
            # So sánh với hình ảnh có sẵn
            for i in range(len(self.data)):
                match = face_recognition.face_distance(
                    [self.data[i]], face_encoding)[0]
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
                self.resultId.config(text="ID: " + result[0], anchor='center')
                self.resultName.config(text="Tên: " + result[1], anchor='center')
                self.resultNotice.config(text="Nhận diện thành công", anchor='center', fg="#085F00")
                self.notice()
                if type == 1:
                    # Đưa dữ liệu vào database
                    a = checkin.Checkin(code, now)
                    a.insert()
                else:
                    # Đưa dữ liệu vào database
                    a = checkout.Checkout(code, now)
                    a.insert()
            else:
                self.resultNotice.config(text="Không thể nhận diện, hãy thử lại", anchor='center', fg="#C70000")
                self.notice()

    def clean(self):
        self.resultId.configure(text="")
        self.resultName.configure(text="")
        self.resultNotice.configure(text="")
        self.inputValue = None

    def notice(self):
        # Xóa hình ảnh sau khi hiển thị
        self.resultFrame.after(2000, self.clean)


    def time_keeping(self):
        self.clean()
        self.update_button.place_forget()
        self.cap_button.place_forget()
        self.back_button.place_forget()
        self.in_button.place(x=5,y=5, width=200, height=40)
        self.out_button.place(x=225, y=5, width=200, height=40)
        self.signUp_button.place(x=445, y=5, width=200, height=40)

    def sign_up(self): 
        self.in_button.place_forget()
        self.out_button.place_forget()
        self.signUp_button.place_forget()
        self.update_button.place(x=5,y=5, width=200, height=40)
        self.cap_button.place(x=225, y=5, width=200, height=40)
        self.back_button.place(x=445, y=5, width=200, height=40)
    
    def show_message(self):
        self.inputValue = sd.askstring("", "Nhập mã nhân viên:")
        if self.inputValue is not None:
            if self.inputValue in staff.select_id():
                self.sign_up()
                result = staff.search(self.inputValue)
                self.resultId.config(text="ID: " + result[0], anchor='center')
                self.resultName.config(text="Tên: " + result[1], anchor='center')
            else:
                messagebox.showerror("Lỗi","Không tìm thấy nhân viên")

# Khởi tạo ứng dụng
if __name__ == "__main__":
    Cam(tk.Tk(), "Camera Feed")
    tk.mainloop()

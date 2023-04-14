import cv2
from tkinter import * 
from PIL import ImageTk, Image
import tkinter as tk
import face_recognition
import os
from playsound import playsound
import datetime
import encoding
import checkin, checkout

class App:

    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.geometry('1000x480+300+50')

        # Khởi tạo camera
        self.video_capture = cv2.VideoCapture(0)

        # Tạo một label để hiển thị hình ảnh
        self.label = tk.Label(window)
        self.label.place(x = 0, y = 0)

        # Tạo 1 frame chứa các nút chức năng và hiển thị kết quả
        self.resultFrame = tk.Frame(window, width=350, height=480, bg ='green')
        self.resultFrame.place(x = 650, y = 0)

        # Nút để chụp ảnh
        self.cap_button = tk.Button(
            self.resultFrame, text="Capture", command=self.capture)
        self.cap_button.place(x = 7, y = 440, relwidth=0.3, height=40)

        # Nút Checkin
        self.in_button = tk.Button(
            self.resultFrame, text="Check in", command=self.check_in)
        self.in_button.place(x = 124, y = 440, relwidth=0.3, height=40)

        # Nút Checkout
        self.out_button = tk.Button(
            self.resultFrame, text="Check out", command=self.check_out)
        self.out_button.place(x = 241, y = 440, relwidth=0.3, height=40)

        # Thêm nút để thoát ứng dụng
        self.quit_button = tk.Button(window, text="Quit", command=self.quit)
        # self.quit_button.place(x = 970, y = 0)

        #Ô input để đăng ký khuôn mặt
        self.inputValue = StringVar()
        self.inputId = Entry(self.resultFrame, width=650, textvariable=self.inputValue)
        self.inputId.place(x = 0, y = 0)

        #Label hiển thị thời gian
        self.timeLabel = tk.Label(window)
        self.display_time()
        self.timeLabel.place(x = 0, y = 0)

        self.data = encoding.get_encodings()
        self.id = encoding.get_staff_id()

        # Update hình ảnh lên label
        self.update()

    def update(self):
        # Đọc hình ảnh từ camera
        ret, frame = self.video_capture.read()

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
        staffCode = self.inputValue.get()
        index = encoding.get_number_of_paths(staffCode)+1
        if ret:
            pathName = "dataset/{}".format(staffCode)
            if not os.path.exists(pathName):
                os.makedirs(pathName)
            cv2.imwrite("{}/{}-{}.jpg".format(pathName,
                        staffCode, index), frame)
            index += 1

    def check_in(self):
        ret, frame = self.video_capture.read()
        if ret:
            # Tìm các khuôn mặt trong hình ảnh
            face_location = face_recognition.face_locations(frame)
            face_encoding = face_recognition.face_encodings(frame, face_location)[0]
            # So sánh với hình ảnh có sẵn
            for i in range(len(self.data)):
                match = face_recognition.face_distance([self.data[i]], face_encoding)[0]
                same = False
                code = ""
                print(match)
                if match < 0.4:
                    same = True
                    code = self.id[i]
                    break
            if same == True:
                # Lấy ngày giờ hiện tại dưới dạng chuỗi
                now = datetime.datetime.now()
                current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                # Đưa dữ liệu vào database
                a = checkin.Checkin(code, now)
                a.insert()
                playsound("mp3.2\\Pleasetry-again2.mp3")
                print("Thank you for check in {} {}".format(code,current_date_time))
            else:
                playsound("mp3\\Pleasetry-again.mp3")
                print("Please, try again")

    def check_out(self):
        ret, frame = self.video_capture.read()
        if ret:
            # Tìm các khuôn mặt trong hình ảnh
            face_location = face_recognition.face_locations(frame)
            face_encoding = face_recognition.face_encodings(frame, face_location)[0]
            # So sánh với hình ảnh có sẵn
            for i in range(len(self.data)):
                match = face_recognition.face_distance([self.data[i]], face_encoding)[0]
                same = False
                code = ""
                print(match)
                if match < 0.4:
                    same = True
                    code = self.id[i]
                    break
            if same == True:
                # Lấy ngày giờ hiện tại dưới dạng chuỗi
                now = datetime.datetime.now()
                current_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
                # Đưa dữ liệu vào database
                a = checkout.Checkout(code, now)
                a.insert()
                playsound("mp3.2\\Pleasetry-again2.mp3")
                print("Thank you for check out {} {}".format(code,current_date_time))
            else:
                playsound("mp3\\Pleasetry-again.mp3")
                print("Please, try again")
    


# Khởi tạo ứng dụng
App(tk.Tk(), "Camera Feed")
tk.mainloop()

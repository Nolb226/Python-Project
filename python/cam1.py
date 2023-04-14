import tkinter as tk
from PIL import ImageTk, Image
import cv2
import face_recognition

# Khởi tạo cửa sổ tkinter
root = tk.Tk()
root.title("Face Recognition")

# Khởi tạo đối tượng OpenCV VideoCapture để lấy hình ảnh từ camera
cap = cv2.VideoCapture(0)

# Định nghĩa hàm cập nhật hình ảnh từ camera
def update_frame():
    # Đọc hình ảnh từ camera
    ret, frame = cap.read()

    # Chuyển đổi hình ảnh từ OpenCV sang PIL để hiển thị trên tkinter
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=pil_img)

    # Hiển thị hình ảnh lên tkinter
    label.config(image=imgtk)
    label.image = imgtk

    # Nhận diện khuôn mặt
    face_locations = face_recognition.face_locations(frame)
    for (top, right, bottom, left) in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        print(top, right, bottom, left)

    # Lặp lại cập nhật hình ảnh từ camera sau một khoảng thời gian nhất định
    label.after(15, update_frame)

# Khởi tạo label để hiển thị hình ảnh
label = tk.Label(root)
label.pack()

# Bắt đầu cập nhật hình ảnh từ camera
update_frame()

# Khởi chạy ứng dụng tkinter
root.mainloop()

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()
from PIL import Image, ImageTk
import tkinter as tk

# Khởi tạo cửa sổ tkinter
root = tk.Tk()

# Load ảnh
image = Image.open("icon/done.png")

# Thay đổi kích thước ảnh
image = image.resize((200, 200))

# Chuyển đổi ảnh thành định dạng có thể sử dụng được bởi Tkinter
photo = ImageTk.PhotoImage(image)

# Tạo label
label = tk.Label(root, image=photo)

# Hiển thị label
label.pack()

# Khởi chạy vòng lặp sự kiện Tkinter
root.mainloop()
from imutils import paths
import face_recognition
import os
import cv2

# lấy paths của images trong dataset
def get_path():
    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images("build/dataset"))
    return imagePaths

def get_number_of_paths(id):
    imagePaths = list(paths.list_images("build/dataset/{}".format(id)))
    return len(imagePaths)

# khởi tạo list chứa known encodings và known names (để các test images so sánh)
# chứa encodings và tên của các images trong dataset
# viết 2 hàm trả về list chứa encoding và staffid
def get_encodings(): 
    imagePaths = get_path()
    knownEncodings = []

    # duyệt qua các image paths
    for (i, imagePath) in enumerate(imagePaths):

        # load image bằng OpenCV và chuyển từ BGR to RGB (dlib cần)
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb, model="hog")    
        encodings = face_recognition.face_encodings(rgb, boxes)  
        for encoding in encodings:
            # lưu encoding vào list
            knownEncodings.append(encoding)
        # Nếu muốn xử lí mỗi hình ảnh chỉ lấy 1 khuôn mặt
        # knownEncodings.append(encodings[0])
    return knownEncodings

def get_staff_id():
    staffIds = []
    imagePaths = get_path()

    for (i, imagePath) in enumerate(imagePaths):
        # Lấy tên của file ảnh
        fileName = imagePath.split(os.path.sep)[2]
        staffId = fileName.split("-")[0]
        staffIds.append(staffId)
    return staffIds


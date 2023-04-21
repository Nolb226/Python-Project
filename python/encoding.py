from imutils import paths
import face_recognition
import os
import cv2

# lấy paths của images trong dataset
def get_path():
    print("[INFO] quantifying faces...")
    imagePaths = list(paths.list_images("dataset"))
    return imagePaths

def get_number_of_paths(id):
    imagePaths = list(paths.list_images("dataset/{}".format(id)))
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

        # Đối với từng image phải thực hiện detect face, trích xuất face ROI và chuyển về encoding
        # trả về array of bboxes of faces, dùng dlib như bài face detection đó
        # model="cnn" chính xác hơn nhưng chậm hơn, "hog" nhanh hơn nhưng kém chính xác hơn
        boxes = face_recognition.face_locations(rgb, model="hog")    

        # tính the facial embedding for the face
        # sẽ tính encodings cho mỗi face phát hiện được trong ảnh (có thể có nhiều faces)
        # Để lý tưởng trong ảnh nên chỉ có một mặt người của mình thôi
        encodings = face_recognition.face_encodings(rgb, boxes)  

        # duyệt qua các encodings
        # Trong ảnh có thể có nhiều faces, mà ở đây chỉ có 1 tên
        # Nên chắc chắn trong dataset ban đầu ảnh chỉ có một mặt người thôi nhé
        # Lý tưởng nhất mỗi ảnh có 1 face và có 1 encoding thôi
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


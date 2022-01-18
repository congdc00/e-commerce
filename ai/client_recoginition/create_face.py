from all_lib import *
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(device)
mtcnn = MTCNN(margin=20, keep_all = True, post_process=False, device= device)
count = 50 # Đếm số lượng ảnh
leap = 1  # bước nhảy: lấy 1 ảnh sau mỗi leap frame
video_cap = cv2.VideoCapture(0)
video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
img_path = '../../data/face_img'
label_face = input('Tên của bạn là gì: ')
face_path = os.path.join(img_path, label_face)
print(face_path)
while video_cap.isOpened() and count:
    isSuccess, frame = video_cap.read()
    # xác định lại xem có đúng thu được 1 frame từ camera không
    if mtcnn(frame) is not None and leap%2 : # nếu có box nào đó tồn tại
        # Đặt tên theo định dạng 2021-07-03-22-39-2216.jpg
        path = str(face_path + '/{}.jpg'.format(str(datetime.now())[:-7].replace(":","-").replace(" ","-") + str(count)))
        # Nhận diện và lưu ảnh
        face_img = mtcnn(frame,save_path = path)
        count -= 1
    leap +=1
    cv2.imshow('Face_detection', frame)
    # Đặt nút tắt
    if cv2.waitKey(1)&0xFF == ord('q'):
        break
video_cap.release()
cv2.destroyAllWindows()
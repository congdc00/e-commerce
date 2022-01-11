import os
from datetime import datetime

import streamlit as st
import cv2
import torch
from facenet_pytorch.models.mtcnn import MTCNN

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
mtcnn = MTCNN(margin=20, keep_all = True, post_process=False, device= device)
count = 50 # Đếm số lượng ảnh
leap = 1  # bước nhảy: lấy 1 ảnh sau mỗi leap frame


st.sidebar.button("Trang chủ")
st.sidebar.button("Đăng ký tài khoản")
st.header("Đăng ký")

# Bước 1
st.subheader("Bước 1: Điền thông tin người dùng")
label_face = st.text_input("Tên của bạn là")
img_path = '../../data/face_img'
face_path = os.path.join(img_path, label_face)

#buoc 2
st.subheader("Bước 2: Đăng ký khuôn mặt")
btnShowCam = st.button("Face ID")

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)
count = 50 # Đếm số lượng ảnh
leap = 1  # bước nhảy: lấy 1 ảnh sau mỗi leap frame
while btnShowCam:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # xác định lại xem có đúng thu được 1 frame từ camera không
    if mtcnn(frame) is not None and leap%2 : # nếu có box nào đó tồn tại
        # Đặt tên theo định dạng 2021-07-03-22-39-2216.jpg
        path = str(face_path + '/{}.jpg'.format(str(datetime.now())[:-7].replace(":","-").replace(" ","-") + str(count)))
        # Nhận diện và lưu ảnh
        face_img = mtcnn(frame,save_path = path)
        count -= 1

    FRAME_WINDOW.image(frame)
    leap +=1


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


st.subheader("Bước 2: Đăng ký khuôn mặt")

btnShowCam = st.button("Face ID")

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

while btnShowCam:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)



from datetime import datetime
import os

import torch
import cv2
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render
from facenet_pytorch.models.mtcnn import MTCNN

from.forms import RegistrationForm
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    Data = {'form': form}
    return render(request, 'register.html', Data)

def infomation(request):
    return render(request, 'infomation.html')

def drone_delivery(request):
    return render(request, 'drone_delivery.html')

def stream():
    video_cap = cv2.VideoCapture(0)
    video_cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video_cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    device =  torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    mtcnn = MTCNN(margin=20, keep_all=False, select_largest = True, post_process=False, device = device)
    count = 50 # Đếm số lượng ảnh
    leap = 1  # bước nhảy: lấy 1 ảnh sau mỗi leap frame
    img_path = '../../data/new_face'
    label_face = 'khachhangmoi'
    face_path = os.path.join(img_path, label_face)

    while count:
        ret, frame = video_cap.read()
        if mtcnn(frame) is not None and leap%2 : # nếu có box nào đó tồn tại
            # Đặt tên theo định dạng 2021-07-03-22-39-2216.jpg
            path = str(face_path + '/{}.jpg'.format(str(datetime.now())[:-7].replace(":","-").replace(" ","-") + str(count)))
            # Nhận diện và lưu ảnh
            face_img = mtcnn(frame,save_path = path)
            count -= 1
        leap +=1
        if not ret:
            print("Error: failed to capture image")
            break

        cv2.imwrite('livestream.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('livestream.jpg', 'rb').read() + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')



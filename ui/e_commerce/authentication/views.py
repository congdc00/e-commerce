from datetime import datetime
import os

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin

import torch
import cv2
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from facenet_pytorch.models.mtcnn import MTCNN

from.forms import RegistrationForm,UpdatePersonalForm, UpdateAddressForm, UpdateAccountForm
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

def information(request):
    return render(request, 'information.html')

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

def update_personal(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(User, pk=pk)

    # pass the object as instance in form
    form = UpdatePersonalForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/info/information/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_personal.html", context)

def update_address(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(User, pk=pk)

    # pass the object as instance in form
    form = UpdateAddressForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/info/information/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_address.html", context)

def update_account(request, pk):
    # dictionary for initial data with
    # field names as keys
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(User, pk=pk)

    # pass the object as instance in form
    form = UpdateAccountForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/info/information/")

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_account.html", context)

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('information')

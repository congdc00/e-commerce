from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('infomation/', views.infomation, name = 'infomation'),
    path('drone_delivery/', views.drone_delivery, name = 'drone_delivery'),
    path('create_face/', views.video_feed, name="create_face"),
]

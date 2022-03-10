from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('information/', views.information, name = 'information'),
    path('information/<int:pk>/', views.update_personal, name = 'update_personal'),
    path('information/address/<int:pk>/', views.update_address, name = 'update_address'),
    path('information/account/<int:pk>/', views.update_account, name = 'update_account'),
    path('information/bank/<int:pk>/', views.update_bank, name = 'update_bank'),
    path('information/change_password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('drone_delivery/', views.drone_delivery, name = 'drone_delivery'),
    path('create_face/', views.video_feed, name="create_face"),
]

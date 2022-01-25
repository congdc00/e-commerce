from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.product, name ='product'),
    path('addcart',views.addcart, name='addcart')
]

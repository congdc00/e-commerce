from django.urls import path
from . import views
from django. contrib.auth import views as auth_views


urlpatterns = [
    path('', views.ProductListView.as_view(), name = 'home'),
    path('contact/', views.contact, name = 'contact'),
    path('<int:pk>/', views.product, name = 'product'),
    path('login/',auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('logout/',auth_views.LogoutView.as_view(next_page='/'),name='logout'),
]

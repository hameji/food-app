from django.contrib.auth import views as authentication_views
from django.urls import path

from . import  views as user_views

app_name = 'user'
urlpatterns = [
    path('', user_views.index, name='index'),
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name ='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name ='logout'),
    path('password_change/', authentication_views.PasswordChangeView.as_view(), name ='change_password'),
    path('profile/', user_views.profilepage, name='profile'),
]
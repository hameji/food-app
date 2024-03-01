from django.contrib.auth import views as authentication_views
from django.urls import path

from . import views as user_views

app_name = 'user'
urlpatterns = [
    path('', user_views.index, name='index'),
    path('register/', user_views.register, name='register'),
    path('register/done/', user_views.register_done, name='register_done'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name ='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), {'next_page': '/'}, name ='logout'),
    path('password_change/', authentication_views.PasswordChangeView.as_view(), name ='password_change'),
    path('password_change/done/', authentication_views.PasswordChangeDoneView.as_view(), name ='password_change_done'),
    path('password_reset/', authentication_views.PasswordResetView.as_view(), name ='password_reset'),
    path('password_reset/done/', authentication_views.PasswordResetDoneView.as_view(), name ='password_reset_done'),
    path('password_reset/<uidb64>/<token>/', authentication_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name ='password_reset_confirm'),
    path('password_reset/complete/', authentication_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"), name ='password_reset_complete'),
    path('profile/', user_views.profilepage, name='profile'),
]


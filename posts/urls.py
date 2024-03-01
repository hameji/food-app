from django.contrib.auth import views as authentication_views
from django.urls import path

from . import views as posts_views

app_name = 'posts'
urlpatterns = [
    path('create/', posts_views.post_create, name='create'),
]


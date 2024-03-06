from django.contrib.auth import views as authentication_views
from django.urls import path

from . import views as posts_views

app_name = 'posts'
urlpatterns = [
    path('', posts_views.index, name='index'),
    path('feed/', posts_views.feed, name='feed'),
    path('like/', posts_views.like_post, name='like'),
    path('create/', posts_views.post_create, name='create'),
]


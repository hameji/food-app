from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from portfolio import views as portfolio_views
from movies.views import MovieViewSet, ActionViewSet, CommedyViewSet
from social import views as social_views
from musics import views as music_views
from ecom import views as ecom_views
from pdf import views as pdf_views
from facebook_crawler import views as crawler_view
from calorieTracker import views as tracker_view

# REST api
router = routers.SimpleRouter()
router.register('movies', MovieViewSet)
router.register('action', ActionViewSet)
router.register('commedy', CommedyViewSet)

urlpatterns = [ # dynamic path
    path('admin/', admin.site.urls),

    ## Original Apps
    # giants_sholder
    path('giants_sholder/', include('giants_sholder.urls')),


    # portfolio
    path('', portfolio_views.index, name='index'),
    # REST api(movie)
    path('', include(router.urls)),
    # social
    path('social/', social_views.index, name='social_top'),
    # facebook_crawler
    path('crawler/', crawler_view.index, name='crawler_top'),
    path('crawler/delete', crawler_view.clear, name='crawler_delete'),
    # calorie_tracker
    path('calorieTracker/', tracker_view.index, name='tracker'),
    path('calorieTracker/<int:id>/', tracker_view.delete_consume, name='tracker_delete'),
    # Music
    path('musics/', music_views.music_list, name='music_list'),
    # food
    path('food/', include('food.urls')),
    # pdf
    path('pdf/', pdf_views.list, name='pdf_list'),
    path('pdf/input', pdf_views.input, name='pdf_input'),
    path('pdf/<int:id>', pdf_views.resume, name='pdf_resume'),
    # E commer
    path('ecom/', ecom_views.shop, name='shop'),
    path('ecom/<int:id>', ecom_views.product_detail, name='detail'),
    path('ecom/checkout', ecom_views.checkout, name='checkout'),
    # User
    path('users/', include('users.urls')),
    # User
    path('posts/', include('posts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as authentication_views
from django.urls import path, include
from rest_framework import routers

from portfolio import views as portfolio_views
from movies.views import MovieViewSet, ActionViewSet, CommedyViewSet
from bic import views as bic_views
from users import views as user_views
from musics import views as music_views
from ecom import views as ecom_views

# REST api
router = routers.SimpleRouter()
router.register('movies', MovieViewSet)
router.register('action', ActionViewSet)
router.register('commedy', CommedyViewSet)

urlpatterns = [ # dynamic path
    path('admin/', admin.site.urls),
    path('', portfolio_views.index, name='index'),
    # REST api(movie)
    path('', include(router.urls)),
    # BIC
    path('bic/', bic_views.bic_forum, name='bic_forum'),
    # Music
    path('musics/', music_views.music_list, name='music_list'),
    # food
    path('food/', include('food.urls')),
    # E commer
    path('ecom/', ecom_views.shop, name='shop'),
    path('ecom/<int:id>', ecom_views.product_detail, name='detail'),
    path('ecom/checkout', ecom_views.checkout, name='checkout'),
    # User
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name ='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name ='logout'),
    path('profile/', user_views.profilepage, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
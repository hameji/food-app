from django.urls import path

from . import views as giants_sholder_views

app_name = 'giants_sholder'
urlpatterns = [ # dynamic path
    path('', giants_sholder_views.index, name='index'),
]
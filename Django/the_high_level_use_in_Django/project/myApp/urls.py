from django.urls import re_path
from . import views

app_name = 'app'
urlpatterns = [
    re_path('^index/$', views.index, name='index'),
    re_path('^upfile/$', views.upfile, name='upfile'),
    re_path('^savefile/$', views.savefile, name='savefile'),
]
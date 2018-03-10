from django.urls import re_path
from . import views

app_name = 'app'
urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^students/$', views.students),
    re_path(r'^good/(\d+)/$', views.good, name='good'),
    re_path(r'^main/$', views.main, name='main'),
    re_path(r'^postfile', views.postfile, name='postfile'),
    re_path(r'^showinfo', views.showinfo, name='showinfo'),
]
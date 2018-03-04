from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.welcome),
    re_path(r'^students/&',views.students),
]
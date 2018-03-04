from django.urls import re_path,path
from . import views

urlpatterns=[
    re_path(r'^$',views.index),
    re_path(r'^(\d+)/$',views.detail),
    re_path(r'^grades/$',views.grades),
    re_path(r'^students/$',views.students),
    re_path(r'^grades/(\d+)/$',views.gradesStudents),
]
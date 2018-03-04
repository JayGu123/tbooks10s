from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.welcome),

    re_path(r'^students/$',views.students),
    re_path(r'^students2/$',views.students2),
    re_path(r'^stu\w+/(\d+)/$',views.stupage),
    re_path(r'^studentsearch/$',views.studentsearch),
    #re_path(r'^addstudents/$',views.addstudents),
    #re_path(r'^addstudents2/$',views.addstudents2),
]
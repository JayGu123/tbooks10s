from django.urls import re_path
from . import views

app_name='myApp'
urlpatterns=[
    re_path(r'^$',views.home,name='home'),
    re_path(r'^attributes/$',views.attributes),
    re_path(r'^get1/$',views.get1),
    re_path(r'^get2/$',views.get2),
    re_path(r'^showregister/$', views.showregister),
    re_path(r'^showregister/register/$',views.register),
    re_path(r'^showresponse/$',views.showresponse),
]
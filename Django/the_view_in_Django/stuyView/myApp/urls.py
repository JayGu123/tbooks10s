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
    re_path('^cookietest/$',views.cookietest),
    re_path('^redirect1/$',views.redirect1),
    re_path('^redirect2/$',views.redirect2),
    re_path('^index/$',views.index),
    re_path('^login/$',views.login),
    re_path('^showindex/$',views.showindex),
    re_path('^quit/$', views.quit),

]
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
   url(r'^$', views.Home, name='home'),
   url(r'^gifter/', views.Gifter, name='gifter'),
   url(r'^my_challenge/', views.My_Challenge, name='my_challenge'),
   url(r'^my_profile/', views.My_Profile, name='my_profile'),
]
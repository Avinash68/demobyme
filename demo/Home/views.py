from django.shortcuts import render, get_object_or_404, render_to_response, redirect

from django.views.generic import TemplateView
from django.views import generic
import services

from rest_framework.response import Response
from rest_framework import status
from pip._vendor.cachecontrol.serialize import Serializer
from rest_framework import generics
from django.contrib.gis.serializers.geojson import Serializer
from .serializers import *
from django.template import RequestContext
import requests

# Create your views here.

# class Home(generics.CreateAPIView):
#     serializer_class =  PostSerializer
#     def get_queryset(self):
#         queryset=Postservice.objects.all()
#         return queryset

def Home(request):
        return render(request,"base.html" )

#     def Save(request):
#           print "hiii"
#           print request.method
#           if request.method == "POST":
#               
#               email = request.POST.get('email')
#               password = request.POST.get('password')
#              
#               print "email is",email
#               print "password is",password
#               payload = {"emailid": email,"password": password,}
# 
#               r = requests.post("http://192.168.1.129:8063/rest-auth/login/", data=payload)
# 
#               print r.text
#               return render(request, "gifter_home.html")

def Gifter(request):
        return render(request,"Home/gifter_home.html" )

# class Gifter(generic.TemplateView):
#     def get(self,request):
#         print("in get view")
#         object_list = services.get_location()
#         print("location list", object_list)
#         return render(request,'Home/gifter_home.html',{'object_list':object_list})   
        

def My_Challenge(request):
    return render(request,"Home/my_challenge.html" )

def My_Profile(request):
    return render(request,"Home/my_profile.html" )
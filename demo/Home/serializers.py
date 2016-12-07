from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class PostSerializer(serializers.Serializer):
    print "in seriealizer"
    
    
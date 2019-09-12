from .models import Notif
from rest_framework import generics,viewsets
from .serializers import NotifSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.


class NotifView(viewsets.ModelViewSet):
    queryset = Notif.objects.all()
    serializer_class = NotifSerializer
    

    
    
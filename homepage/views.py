from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Homepage
from .serializers import HomepageSerializer


class HomepageView(viewsets.ModelViewSet):
    queryset = Homepage.objects.all()
    serializer_class = HomepageSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


'''class EventsView(viewsets.ModelViewSet):
    queryset=Events.objects.all()
    serializer_class=EventsSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
'''

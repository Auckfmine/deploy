from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Cantine
from .serializers import CantineSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User



"""class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)"""


class CantineView(viewsets.ModelViewSet):
    queryset = Cantine.objects.all()
    serializer_class = CantineSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        author = get_object_or_404(User, username=self.request.user)
        return serializer.save(user=author)

from django.shortcuts import render
from rest_framework import viewsets
from .models import reclamation
from .serializers import reclamationSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication





class ReclamationView(viewsets.ModelViewSet):
    queryset=reclamation.objects.all()
    serializer_class=reclamationSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        author = get_object_or_404(User, username=self.request.user)
        return serializer.save(user=author)

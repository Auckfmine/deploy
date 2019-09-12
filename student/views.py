from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Student
from.serializers import ArticleSerializer
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class ArticleView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        author = get_object_or_404(User, username=self.request.user)
        return serializer.save(parent=author)

from rest_framework.views import APIView
from rest_framework import generics
from.models import Notes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import NoteSerializer


class NotesViews(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    #permission_classes = (IsAuthenticated, )


# Create your views here.

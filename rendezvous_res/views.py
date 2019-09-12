from .models import Rv
from rest_framework import generics,viewsets
from .serializers import RvSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

# Create your views here.


class Rv_View(viewsets.ModelViewSet):
    queryset = Rv.objects.all()
    serializer_class = RvSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        author = get_object_or_404(User, username=self.request.user)
        return serializer.save(Rv_user=author)
    """

class Rv_View(APIView):

    #Retrieve, update or delete a instance.

    def get_object(self, pk):
        try:
            return Rv.objects.get(pk=pk)
        except Rv.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        rv = self.get_object(pk)
        serializer = RvSerializer(rv)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        rv = self.get_object(pk)
        serializer = RvSerializer(rv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        rv = self.get_object(pk)
        rv.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """

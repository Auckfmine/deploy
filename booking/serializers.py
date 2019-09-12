from rest_framework import serializers
from .models import Cantine
try:
    from django.contrib.auth import get_user_model
except ImportError: # django < 1.5
    from django.contrib.auth.models import User



"""class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')"""


class CantineSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField( read_only=True)

    class Meta :
        model=Cantine
        fields =('id','user','meals','date')

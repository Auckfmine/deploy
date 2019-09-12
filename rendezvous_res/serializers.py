from .models import Rv
from rest_framework import serializers
from django.contrib.auth.models import User




class RvSerializer(serializers.ModelSerializer):
    Rv_user = serializers.PrimaryKeyRelatedField( read_only=True)
    class Meta:
        model = Rv
        fields ='__all__'
        extra_kwargs = {'Rv_available_date': {'read_only': True},
                        'Rv_admin_comment':{'read_only': True}}
        

   



from rest_framework import serializers
from .models import reclamation




class reclamationSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField( read_only=True)
    class Meta :
        model=reclamation
        fields =('id','user','title','msg','time')

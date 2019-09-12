from .models import paiement
from django.contrib.auth.models import User
from .models import paiement
from rest_framework import serializers





class PaiementSerializer(serializers.ModelSerializer):
    class Meta :
        model=paiement
        fields =('id','user','paye','date','valid_until')

from rest_framework import serializers
from .models import Homepage


class HomepageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homepage
        fields = '__all__'


'''class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('id', 'title', 'description', 'date', 'img',)
'''

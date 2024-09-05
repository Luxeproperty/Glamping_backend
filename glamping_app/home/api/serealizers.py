from rest_framework import serializers
from home.models import *

class AddPodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pods
        fields = '__all__'
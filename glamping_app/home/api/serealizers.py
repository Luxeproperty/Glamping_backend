from rest_framework import serializers
from home.models import *

class AddPodImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PodImages
        fields = '__all__'


class AddPodSerializer(serializers.ModelSerializer):
    images = AddPodImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pods
        fields = '__all__'
        
        
class ContactSerializer(serializers.Serializer):
    
    class Meta:
        model = Contact
        fields = '__all__'

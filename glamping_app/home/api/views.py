from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response

from home.api.serealizers import AddPodSerializer, AddPodImageSerializer
from home.models import Pods
from home.api.permissions import IsAdminOrReadOnly

# Create your views here.

class PodListView(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, *args, **kwargs):
        pods = Pods.objects.all()
        serializer = AddPodSerializer(pods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = AddPodSerializer(data=request.data)
        
        if serializer.is_valid():
            pod = serializer.save()
            
            image_serializer = AddPodImageSerializer(data=request.data)
            if image_serializer.is_valid():
                images = image_serializer.validated_data.get('images')
                
                for image in images:
                    Pods.objects.create(pod=pod, image=image)
                
                return Response(serializer.data, status=201)
            
            else:
                pod.delete()
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class PodDetailView(APIView):
    
    permission_classes = [IsAdminOrReadOnly]
    
    def get(self, request, pk, *args, **kwargs):
        pod = Pods.objects.get(pk=pk)
        serializer = AddPodSerializer(pod)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, *args, **kwargs):
        pod = Pods.objects.get(pk=pk)
        serializer = AddPodSerializer(instance=pod, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        pod = Pods.objects.get(pk=pk)
        pod.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

        
        
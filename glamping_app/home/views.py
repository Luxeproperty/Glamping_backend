from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from home.models import Pods

# Create your views here.

class AddPod(View):
    def get(self, request):
        model = Pods
        return render(request, 'add_pod.html', {'model': model})
        
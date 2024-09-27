from django.contrib import admin
from .models import Pods, PodImages
# Register your models here.

admin.site.register(Pods)
admin.site.register(PodImages)

class PodAdmin(admin.ModelAdmin):
    list_display = ('name')
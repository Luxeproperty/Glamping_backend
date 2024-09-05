from django.contrib import admin
from .models import Pods
# Register your models here.

admin.site.register(Pods)

class PodAdmin(admin.ModelAdmin):
    list_display = ('name')
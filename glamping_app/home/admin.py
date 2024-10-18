from django.contrib import admin
from .models import Pods, PodImages, Contact
# Register your models here.

admin.site.register(Pods)
admin.site.register(PodImages)
admin.site.register(Contact)

class PodAdmin(admin.ModelAdmin):
    list_display = ('name')
from django.db import models

# Create your models here.

# Model for pods

class Pods(models.Model):
    
    name = models.CharField(max_length=200, blank=False, null=False)
    max_occupancy = models.IntegerField(default=1, null=False, blank=False)
    beds = models.IntegerField(default=0, null=False, blank=False)
    couches = models.IntegerField(default=0, null=False, blank=True)
    washrooms = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    gallery_images = models.ImageField(upload_to="pod_images/", null=True, blank=True)
    description = models.TextField()
    facilitiess = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name
    
    
    
from django.db import models
import os

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# Model for pods

def upload_to_podcast_images(instance, filename):
    # Use the original file name to store the image
    return f"pod_images/{filename}"

    
class Pods(models.Model):
    
    name = models.CharField(max_length=200, blank=False, null=False)
    max_occupancy = models.IntegerField(default=1, null=False, blank=False)
    beds = models.IntegerField(default=0, null=False, blank=False)
    couches = models.IntegerField(default=0, null=False, blank=True)
    washrooms = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    description = models.TextField()
    facilitiess = models.TextField()
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    
    def __str__(self):
        return self.name
    

class PodImages(models.Model):
 
    pod = models.ForeignKey(Pods, on_delete=models.CASCADE, related_name="images", null=True, blank=True)  # Foreign key to Pods model
    image = models.ImageField(upload_to="pod_images/", null=True, blank=True) 
    image_name = models.CharField(max_length=255, blank=True)
    
    def save(self, *args, **kwargs):
        # Save the original file name to `image_name`
        if self.image:
            self.image_name = os.path.basename(self.image.name)
        super().save(*args, **kwargs)  # Call the "real" save() method

    def __str__(self):
        return f"{self.pod.name} - {self.image_name}"
      

class Contact(models.Model):
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = PhoneNumberField(region="GB")
    message = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.message}"

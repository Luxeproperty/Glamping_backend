# Generated by Django 5.1 on 2024-09-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_remove_pods_gallery_images_podimages"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="podimages",
            name="pod",
        ),
        migrations.AddField(
            model_name="pods",
            name="pod_images",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="pod_images", to="home.podimages"
            ),
        ),
    ]

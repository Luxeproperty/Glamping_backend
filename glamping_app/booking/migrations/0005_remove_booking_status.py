# Generated by Django 5.1 on 2024-09-01 10:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("booking", "0004_alter_guestdetails_email"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="status",
        ),
    ]

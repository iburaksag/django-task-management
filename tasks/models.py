from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    battery_size = models.IntegerField()
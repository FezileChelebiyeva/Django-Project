from django.db import models

# Create your models here.

class Studens(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    group = models.TextField(blank=True)
    age = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    scholarship = models.BooleanField(default=False)

    
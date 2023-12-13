from django.db import models
from django.urls import reverse
# Create your models here.

class Studens(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    group = models.TextField(blank=True)
    age = models.IntegerField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    scholarship = models.BooleanField(null=True)
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, null=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    



class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    
    def get_absolute_url(self):
       return reverse('category', kwargs={'cat_id': self.pk})

    def __str__(self):
        return self.name


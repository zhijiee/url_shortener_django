from django.db import models

# Create your models here.

'''
Create Database Model for URL Mapping here
'''
class UrlMapping(models.Model):
    url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_created', )
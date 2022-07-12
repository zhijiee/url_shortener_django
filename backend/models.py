from django.db import models

# Create your models here.

'''
Create Database Model for URL Mapping here
'''
class UrlMapping(models.Model):
    original_url = models.CharField(max_length=256)
    hash = models.CharField(max_length=10)
    date_created = models.DateTimeField('creation date')
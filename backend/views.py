from django.shortcuts import render
from django.http import HttpResponse

from .models import UrlMapping
from .serializers import UrlSerializer
from rest_framework import generics

import pyshorteners


# Create your views here.
def shorten(request, url):
    shorterner = pyshorteners.Shortener()
    shortened_url = shorterner.chilpit.short(url)
    return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')


class UrlListCreate(generics.ListCreateAPIView):
    queryset = UrlMapping.objects.all()
    serializer_class = UrlSerializer
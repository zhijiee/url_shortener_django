from django.shortcuts import render
from django.http import HttpResponse

from .models import UrlMapping
from .serializers import UrlSerializer
from rest_framework import generics

from .models import UrlMapping
from .serializers import UrlSerializer


# Create your views here.
class UrlListCreate(generics.ListCreateAPIView):
    """ View created using Django Generics
    For testing purposes
    """
    queryset = UrlMapping.objects.all()
    serializer_class = UrlSerializer
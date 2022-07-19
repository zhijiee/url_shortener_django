from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status

import json

from .models import UrlMapping
from .serializers import UrlSerializer
from .service import get_random_hash, load_url


# Create your views here.
class UrlListCreate(generics.ListCreateAPIView):
    """ View created using Django Generics
    For testing purposes
    """
    queryset = UrlMapping.objects.all()
    serializer_class = UrlSerializer


@api_view(['POST'])
def shorten_url(request) -> HttpResponse:
    """ Generate a random hash and store it with the URL

    Returns a HTTP Response
    """
    data = json.loads(request.body)
    data['hash'] = get_random_hash()

    shortened_url = request.build_absolute_uri(
        reverse('redirect', args=[data['hash']]))
    print(shortened_url)

    serializer = UrlSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        response = HttpResponse(
            f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')
        response.status_code = status.HTTP_201_CREATED
    else:
        response = HttpResponse(f'Failed to save Shorted URL!')
        response.status_code = status.HTTP_400_BAD_REQUEST
    return response


def redirect_hash(request, hash):
    url = load_url(hash).url
    return redirect(url)

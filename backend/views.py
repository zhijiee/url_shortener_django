from tabnanny import check
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.core.validators import URLValidator

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status

import json

from .models import UrlMapping
from .serializers import UrlSerializer
from .service import get_random_hash, load_url, check_url, convert


# Create your views here.
class UrlListCreate(generics.ListCreateAPIView):
    """ View created using Django Generics
    For testing purposes
    """
    queryset = UrlMapping.objects.all()
    serializer_class = UrlSerializer


@api_view(['POST'])
def shorten_url(request) -> JsonResponse:
    """ Generate a random hash and store it with the URL

    Returns a HTTP Response
    """

    # Prepare for serialization
    data = json.loads(request.body)
    data['hash'] = get_random_hash()
    data['url'] = convert(data['url'])

    serializer = UrlSerializer(data=data)
    if check_url(data['url']) and serializer.is_valid():
        serializer.save()
        # Generate the URL to be returned
        shortened_url = request.build_absolute_uri(
            reverse('redirect', args=[data['hash']]))
        response = JsonResponse({'message': shortened_url},
                                status=status.HTTP_201_CREATED)
    else:
        response = JsonResponse({'message': serializer.errors},
                                status=status.HTTP_400_BAD_REQUEST)
    return response


def redirect_hash(request, hash):
    url = load_url(hash).url
    return redirect(url)

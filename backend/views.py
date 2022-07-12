from django.shortcuts import render
from django.http import HttpResponse
import pyshorteners


# Create your views here.
def shorten(request, url):
    shorterner = pyshorteners.Shortener()
    shortened_url = shorterner.chilpit.short(url)
    return HttpResponse(f'Shortened URL: <a href="{shortened_url}">{shortened_url}</a>')

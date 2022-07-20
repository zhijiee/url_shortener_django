import random
import string

from tokenize import String
from xml.dom import ValidationErr
from xmlrpc.client import Boolean
from django.core.validators import URLValidator

from .models import UrlMapping


def convert(url):
    if url.startswith('https://www.'):
        return 'https://' + url[len('http://www.'):]
    if url.startswith('www.'):
        return 'https://' + url[len('www.'):]
    if not url.startswith('http://'):
        return 'https://' + url
    return url


def check_url(url) -> bool:
    val = URLValidator()
    try:
        val(url)
    except ValidationErr as e:
        print(e)
        return False
    return True


def get_random_hash() -> String:
    '''
    Generates a random hash
    '''
    random_hash = ''.join(random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits
    )for _ in range(7))
    return random_hash


def load_url(url_hash) -> String:
    '''
    Retrieve original URL with hash
    '''
    return UrlMapping.objects.get(hash=url_hash)

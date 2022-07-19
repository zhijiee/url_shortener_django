import random
import string
from tokenize import String
from django.utils import timezone

from .models import UrlMapping


def get_random_hash() -> String:
    '''
    Generates a random hash
    '''
    random_hash = ''.join(random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    return random_hash


def load_url(url_hash) -> String:
    '''
    Retrieve original URL with hash
    '''
    return UrlMapping.objects.get(hash=url_hash)

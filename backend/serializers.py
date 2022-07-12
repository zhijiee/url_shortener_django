from rest_framework import serializers
from .models import UrlMapping

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrlMapping
        fields = ('id', 'original_url', 'hash', 'date_created')
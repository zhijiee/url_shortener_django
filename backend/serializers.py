from rest_framework import serializers
from .models import UrlMapping


class UrlSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.CharField(
        required=False, allow_blank=True, max_length=100)

    class Meta:
        model = UrlMapping
        fields = ('id', 'url', 'hash', 'date_created')

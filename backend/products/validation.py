from rest_framework import serializers

from .models import Product


def validate_name(value):
    qs = Product.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(
            f'{value} is already a product exist')
    return qs

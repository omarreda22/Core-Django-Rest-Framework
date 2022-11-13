from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'id', 'content', 'price', 'sell', 'discount']

    def get_discount(self, obj):
        # obj.id
        # obj.user
        return obj.get_discount()

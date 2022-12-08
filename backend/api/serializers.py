from rest_framework import serializers
from rest_framework.reverse import reverse

from products.models import Product
from products.validation import validate_name


class ProductSerializer(serializers.ModelSerializer):
    discount = serializers.SerializerMethodField(read_only=True)
    url_one = serializers.SerializerMethodField(read_only=True)
    url_good = serializers.SerializerMethodField(read_only=True)
    url_better = serializers.HyperlinkedIdentityField(
        view_name='products:generics_get_one',
        lookup_field='pk'
    )
    # email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validate_name])
    name_source = serializers.CharField(source='name', read_only=True)
    name_source2 = serializers.CharField(
        source='name', read_only=True)

    # set email for user
    # user = serializers.SerializerMethodField(read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    # email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Product
        fields = [
            # 'user',
            'email',
            'url_one',
            'url_good',
            'url_better',
            'name',
            'id',
            'content',
            'price',
            'sell',
            'discount',
            'name_source',
            'name_source2',
        ]

    # def get_user(self, obj):
    #     request = self.context.get('request')
    #     obj = request.user
    #     # print(request)
    #     # print(obj.user)
    #     # print(request.user)
    #     # print(obj)
    #     # print('oanr')
    #     return obj.id
    # Url

    def get_url_one(self, obj):
        return f'products/viewsets/prooducts/{obj.pk}'

    def get_url_good(self, obj):
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse('products:generics_get_one', kwargs={'pk': obj.pk}, request=request)

    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     # omar = validated_data.pop('omar')
    #     obj = super().create(validated_data)
    #     # print(email, omar, obj)
    #     return obj

    def get_discount(self, obj):
        # obj.id
        # obj.user
        return obj.get_discount()

    # validation

    # def validate_name(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     # qs = Product.objects.filter(user=user, name__iexact=value)
    #     # print(user)
    #     # value meaning Input field
    #     qs = Product.objects.filter(name__iexact=value)
    #     # exact -> capital different about small
    #     # iexact -> Two the same
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a exist')
    #     return value


# 1- Custom Validation
# 2- Put User Field
# 3. When user post user=user
# 4. user only see thir posts
# 5. Custom QuerySet
# 6. Mixin For QuerySet

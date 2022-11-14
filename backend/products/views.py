from django.shortcuts import render

from rest_framework import generics, mixins

from .models import Product
from api.serializers import ProductSerializer


# [ Get List - Post - Detial - Updata - Delete]

# Generics List View only -> RetrieveAPIView
class GenericsGETListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


generic_list_api = GenericsGETListProduct.as_view()


# Generics POST -> CreateAPIView
class GenericPOSTProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # import -> serializer.save(user=self.request.user)
        # print(serializer.validated_data)
        title = serializer.validated_data.get('name')
        content = serializer.validated_data.get('content')
        if content is None:
            content = 'Created By Default!'
        serializer.save(content=content)
        print(serializer.validated_data)


generic_post_product = GenericPOSTProduct.as_view()


# Generics GET one product-> RetrieveAPIView
class GenericsGETOneProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


get_one_product_view = GenericsGETOneProductDetail.as_view()


# Generic Update -> UpdateAPIView
class GenericUpdateProduct(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.name


generic_update = GenericUpdateProduct.as_view()


# Generic Delete -> DestoryAPIVIEW
class GenericDeleteProduct(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destory(self, instance):
        super().perform_destory(instance)


generic_delete = GenericDeleteProduct.as_view()


# Generics GET PUT DELETE -> RetrieveUpdateDestroyAPIView
class GenericGPD(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.name

    def perform_destory(self, instance):
        super().perform_destory(instance)


generic_GPD = GenericGPD.as_view()


# Generics List and Create -> ListCreateAPIVIEW
class GenerivListAndCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save()


generic_list_and_create = GenerivListAndCreate.as_view()


##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################

# Mixins
# all in one mixin
# we can divide it to pieces every piece alone
# can use perform in mixins to handle data

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):  # HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.name

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def perform_destory(self, instance):
        super().perform_destory(instance)

    # def post(): #HTTP -> post


product_mixin_view = ProductMixinView.as_view()

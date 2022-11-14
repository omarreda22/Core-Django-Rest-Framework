import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from .serializers import ProductSerializer


def api_first(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    print(model_data)
    data = {}
    if model_data:
        # data['name'] = model_data.name
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        # OR
        data = model_to_dict(model_data)
    return JsonResponse(data)


@api_view(['GET'])
def api_home_test(request):
    model_data = Product.objects.all().order_by("?")
    serializ = ProductSerializer(
        model_data, many=True).data  # turn model to json data
    return Response(serializ)


@api_view(['POST'])
def api_post_data(request):
    serialize = ProductSerializer(data=request.data)
    if serialize.is_valid(raise_exception=True):
        data = serialize.save()
        print(serialize.data)
        return Response(serialize.data)
    # return Response({"Message": "not good data"}, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def api_edit_and_delete(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'GET':
        serialize = ProductSerializer(product).data
        return Response(serialize)

    elif request.method == 'PUT':
        serialize = ProductSerializer(product, request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)

    elif request.method == 'DELETE':
        product.delete()
        return redirect('/api_home/')


# same view for pk and pk None
# contain all methods [ get - post - put - delete ]
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def all_methods(request, pk=None, *args, **kwargs):
    method = request.method
    if pk is None:
        if method == 'GET':
            qs = Product.objects.all()
            serialize = ProductSerializer(qs, many=True).data
            return Response(serialize)
        if method == 'POST':
            serialize = ProductSerializer(data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data)
    else:
        qs = get_object_or_404(Product, pk=pk)
        if method == 'GET':
            serialize = ProductSerializer(qs).data
            return Response(serialize)
        if method == 'PUT':
            serialize = ProductSerializer(qs, request.data)
            if serialize.is_valid():
                serialize.save()
                return Response(serialize.data)
        if method == 'DELETE':
            qs.delete()
            qs = Product.objects.all()
            serialize = ProductSerializer(qs, many=True).data
            return Response(serialize)
            # return redirect('api:all_methods')

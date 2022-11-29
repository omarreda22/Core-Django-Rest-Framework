from rest_framework import viewsets, mixins

from api.serializers import ProductSerializer
from ..models import Product

# all you need to one place list or retrieve
# url
# url/pk
# cfe don't use viewsite alot because does't give full control
# he love have all control and know every url what do exactly
# cfe use generic view


class ProductViewSet(viewsets.ModelViewSet):
    """
    In this model
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial UPdate
    delete -> destroy 
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'name'


# list and retrieve only
class ViewListOrRetrieveOnlyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

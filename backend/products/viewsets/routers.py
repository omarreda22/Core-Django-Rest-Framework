from rest_framework.routers import DefaultRouter

from .viewset import (
    ProductViewSet,
    ViewListOrRetrieveOnlyViewSet
)


router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
# products/viewset/products
# products/viewset/products/name_of_product
router.register('list_and_retrieve',
                ViewListOrRetrieveOnlyViewSet, basename='list_and_retrieve')

urlpatterns = router.urls

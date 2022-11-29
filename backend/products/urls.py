from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views
from .viewsets.viewset import ProductViewSet

app_name = 'products'

"""
if routers in same url page
router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
path('viewsets/', include(router.urls))
"""
router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('generics_get_one_product/<int:pk>/',
         views.get_one_product_view, name='generics_get_one'),
    path('generic_post/', views.generic_post_product, name='generic_post'),
    path('list_view/', views.generic_list_api, name='list_view'),
    path('list_and_create/', views.generic_list_and_create, name='list_and_create'),
    path('generic_update/<int:pk>/', views.generic_update),
    path('generic_delete/<int:pk>/', views.generic_delete),
    path('generic_gpd/<int:pk>/', views.generic_GPD),
    ########################################################
    ########################################################
    ########################################################
    path('mixins/', views.product_mixin_view),
    path('mixins/<int:pk>/', views.product_mixin_view),
    #######################################################
    #######################################################
    # Token for authentications
    path('token/', obtain_auth_token),
    #######################################################
    #######################################################
    # ViewSet and Router
    # products/viewset/products/ ~ name_of_product
    # path('viewsets/', include('products.viewset.routers')),
    path('viewsets/', include(router.urls))
]

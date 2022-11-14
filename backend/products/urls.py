from django.urls import path

from . import views

app_name = 'products'

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
]

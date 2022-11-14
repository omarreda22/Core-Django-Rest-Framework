from django.urls import path

from .views import (
    api_first,
    api_home_test,
    api_post_data,
    api_edit_and_delete,
    all_methods,
)

app_name = 'api'

urlpatterns = [
    path('api/', api_first),
    path('api_home/', api_home_test, name='home'),
    path('api_post/', api_post_data),
    path('api_edit_and_delete/<int:id>/', api_edit_and_delete),
    path('all_methods/', all_methods, name='all_methods'),
    path('all_methods/<int:pk>/', all_methods)
]

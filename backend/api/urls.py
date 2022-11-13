from django.urls import path

from .views import (
    api_first,
    api_home_test,
    api_post_data,
    api_edit_and_delete,
)

app_name = 'api'

urlpatterns = [
    path('api/', api_first),
    path('api_home/', api_home_test),
    path('api_post/', api_post_data),
    path('api_edit_and_delete/<int:id>/', api_edit_and_delete)
]

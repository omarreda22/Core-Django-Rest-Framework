from django.urls import path

from .views import (
    api_first,
)

app_name = 'api'

urlpatterns = [
    path('api', api_first)
]

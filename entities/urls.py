from django.urls import path
from .views import EntityAPI

urlpatterns = [
    path('api/entities/', EntityAPI.as_view())
]
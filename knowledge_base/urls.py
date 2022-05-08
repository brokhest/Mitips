from django.urls import path
from .views import CarTypeAPI, AttributeAPI


urlpatterns = [
    path('api/types/', CarTypeAPI.as_view()),
    path('api/types/<int:pk>', CarTypeAPI.as_view()),
    path('api/attributes/', AttributeAPI.as_view())
]
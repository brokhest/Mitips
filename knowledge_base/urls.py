from django.urls import path
from .views import CarTypeAPI, AttributeAPI, StAttributeAPI, Integrity


urlpatterns = [
    path('api/types/', CarTypeAPI.as_view()),
    path('api/types/<str:name>', CarTypeAPI.as_view()),
    path('api/car_attributes/', AttributeAPI.as_view()),
    path('api/car_attributes/<str:name>', AttributeAPI.as_view()),
    path('api/attributes/', StAttributeAPI.as_view()),
    path('api/attributes/<str:name>', StAttributeAPI.as_view()),
    path('api/integrity/', Integrity.as_view())
]
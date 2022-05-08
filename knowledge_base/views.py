from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import CarType, CharAttribute, IntAttribute, BoolAttribute
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


# Create your views here.

def add_int_atr(request):
    car_type = request.data.get("name")



class CarTypeAPI(APIView):

    @staticmethod
    def get(request):
        data = []
        for type in CarType.objects.all():
            record = {
                "name": type.name
            }
            data.append(record)
        return JsonResponse(data, safe=False)

    @staticmethod
    def post(request):
        car_type = CarType(name=request.data.get("name"))
        car_type.save()
        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    def put(request, pk):
        car_type = get_object_or_404(CarType.objects.all(), pk=pk)
        car_type.name = request.data.get("name")
        car_type.save()
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, pk):
        car_type = get_object_or_404(CarType.objects.all(), pk=pk)
        car_type.delete()
        return Response(status=status.HTTP_200_OK)


class AttributeAPI(APIView):

    @staticmethod
    def get(request):
        car_type = get_object_or_404(CarType.objects.all(), name=request.data.get("car type"))
        data = []
        for atr in car_type.int_attrs.all():
            record = {
                "name": atr.name,
                "low value": atr.low_value,
                "high_value": atr.high_value
            }
            data.append(record)
        for atr in car_type.char_attrs.all():
            record = {
                "name": atr.name,
                "values": atr.values,
            }
            data.append(record)
        for atr in car_type.bool_attrs.all():
            record = {
                "name": atr.name,
                "values": atr.value,
            }
            data.append(record)
        return JsonResponse(data, safe=False)
from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import CarType, CharAttribute, IntAttribute, BoolAttribute,\
    StBoolAttribute, StCharAttribute, StIntAttribute
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


class StAttributeAPI(APIView):

    @staticmethod
    def get(request):
        data = []
        for atr in StIntAttribute.objects.all():
            record = {
                "name": atr.name,
                "low value": atr.low_value,
                "high_value": atr.high_value
            }
            data.append(record)
        for atr in StCharAttribute.objects.all():
            record = {
                "name": atr.name,
                "values": atr.values,
            }
            data.append(record)
        for atr in StBoolAttribute.objects.all():
            record = {
                "name": atr.name,
                "values": atr.value,
            }
            data.append(record)
        return JsonResponse(data, safe=False)

    @staticmethod
    def post(request):
        type = request.data.get("attr type")
        if type == "int":
            attribute = StIntAttribute(name=request.data.get("name"), low_value=int(request.data.get("low value")),
                                       high_value=int(request.data.get("high value")))
        elif type == "char":
            attribute = StCharAttribute(name=request.data.get("name"), values=request.data.get("values"))
        elif type == "bool":
            attribute = StBoolAttribute(name=request.data.get("name"), values=request.data.get("values"))
        attribute.save()
        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    def put(request, name):
        type = request.data.get("attr type")
        if type == "int":
            attribute = get_object_or_404(StIntAttribute.objects.all(), name=name)
            attribute.name = request.data.get("name")
            attribute.low_value = request.data.get("low value")
            attribute.high_value = request.data.get("high value")
        elif type == "char":
            attribute = get_object_or_404(StCharAttribute.objects.all(), name=name)
            attribute.name = request.data.get("name")
            attribute.values = request.data.get("values")
        elif type == "bool":
            attribute = get_object_or_404(StBoolAttribute.objects.all(), name=name)
            attribute.name = request.data.get("name")
            attribute.value = request.data.get("values")
        attribute.save()
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, name):
        type = request.data.get("attr type")
        if type == "int":
            attribute = get_object_or_404(StIntAttribute.objects.all(), name=name)
        elif type == "char":
            attribute = get_object_or_404(StCharAttribute.objects.all(), name=name)
        elif type == "bool":
            attribute = get_object_or_404(StBoolAttribute.objects.all(), name=name)
        attribute.delete()
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
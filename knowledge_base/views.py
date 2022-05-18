from django.shortcuts import render
from rest_framework import status
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import CarType, CharAttribute, FloatAttribute, BoolAttribute,\
    StBoolAttribute, StCharAttribute, StFloatAttribute, StAttribute
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .check import *


# Create your views here.

def add_int_atr(request):
    car_type = request.data.get("name")


class Integrity(APIView):

    @staticmethod
    def get(request):
        data = []
        for attr in StBoolAttribute.objects.all():
            if attr.value == ", ":
                record = {
                    "attribute": attr.name
                }
                data.append(record)
        for attr in StCharAttribute.objects.all():
            if attr.values == ",":
                record = {
                    "attribute": attr.name
                }
                data.append(record)
        for attr in StFloatAttribute.objects.all():
            if attr.low_value == attr.high_value == 0:
                record = {
                    "attribute": attr.name
                }
                data.append(record)
        for car in CarType.objects.all():
            if not (car.float_attrs.all().exists() + car.char_attrs.all().exists() + car.bool_attrs.all().exists()):
                record = {
                    "car type": car.name
                }
                data.append(record)
            else:
                for attr in car.float_attrs.all():
                    if attr.low_value == attr.high_value == 0:
                        record = {
                            "car type": car.name,
                            "attribute": attr.name
                        }
                        data.append(record)
                for attr in car.bool_attrs.all():
                    if attr.value == ",":
                        record = {
                            "car type": car.name,
                            "attribute": attr.name
                        }
                        data.append(record)
                for attr in car.char_attrs.all():
                    if attr.values == ", ":
                        record = {
                            "car type": car.name,
                            "attribute": attr.name
                        }
                        data.append(record)
        if len(data) == 0:
            return Response(status=status.HTTP_200_OK)
        return JsonResponse(data, safe=False)


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
    def put(request, name):
        car_type = get_object_or_404(CarType.objects.all(), name=name)
        car_type.name = request.data.get("name")
        car_type.save()
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, name):
        car_type = get_object_or_404(CarType.objects.all(), name=name)
        car_type.delete()
        return Response(status=status.HTTP_200_OK)


class StAttributeAPI(APIView):

    @staticmethod
    def get(request):
        data = []
        for atr in StFloatAttribute.objects.all():
            record = {
                "name": atr.name,
                "type": "float",
                "low value": atr.low_value,
                "high_value": atr.high_value
            }
            data.append(record)
        for atr in StCharAttribute.objects.all():
            record = {
                "name": atr.name,
                "type": "char",
                "values": atr.values,
            }
            data.append(record)
        for atr in StBoolAttribute.objects.all():
            record = {
                "name": atr.name,
                "type": "bool",
                "values": atr.value,
            }
            data.append(record)
        return JsonResponse(data, safe=False)

    @staticmethod
    def post(request):
        type = request.data.get("attr type")
        if type == "float":
            attribute = StFloatAttribute(name=request.data.get("name"), low_value=float(request.data.get("low value")),
                                         high_value=float(request.data.get("high value")))
        elif type == "char":
            attribute = StCharAttribute(name=request.data.get("name"), values=request.data.get("values")+",")
        elif type == "bool":
            attribute = StBoolAttribute(name=request.data.get("name"), value=request.data.get("value")+", ")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        attribute.save()
        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    def put(request, name):
        type = request.data.get("attr type")
        if type == "float":
            attribute = get_object_or_404(StFloatAttribute.objects.all(), name=name)
            if "new type" in request.data:
                change_type(attribute, request)
                changed = True
            else:
                change_name(attribute, type, request.data.get("name"))
                attribute.name = request.data.get("name")
                change_float(attribute, request.data.get("low value"), request.data.get("high value"))
                attribute.low_value = request.data.get("low value")
                attribute.high_value = request.data.get("high value")
        elif type == "char":
            attribute = get_object_or_404(StCharAttribute.objects.all(), name=name)
            if "new type" in request.data:
                change_type(attribute, request)
                changed = True
            else:
                change_name(attribute, type, request.data.get("name"))
                attribute.name = request.data.get("name")
                change_char(attribute, request.data.get("values")+",")
                attribute.values = request.data.get("values") + ","
        elif type == "bool":
            attribute = get_object_or_404(StBoolAttribute.objects.all(), name=name)
            if "new type" in request.data:
                change_type(attribute, request)
                changed = True
            else:
                change_name(attribute, type, request.data.get("name"))
                attribute.name = request.data.get("name")
                change_bool(attribute, request.data.get("value")+",")
                attribute.value = request.data.get("value") + ","
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if not changed:
            attribute.save()
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def delete(request, name):
        type = request.data.get("attr type")
        if type == "float":
            attribute = get_object_or_404(StFloatAttribute.objects.all(), name=name)
        elif type == "char":
            attribute = get_object_or_404(StCharAttribute.objects.all(), name=name)
        elif type == "bool":
            attribute = get_object_or_404(StBoolAttribute.objects.all(), name=name)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        attribute.delete()
        return Response(status=status.HTTP_200_OK)


class AttributeAPI(APIView):

    @staticmethod
    def get(request):
        car_type = get_object_or_404(CarType.objects.all(), name=request.data.get("car type"))
        data = []
        for atr in car_type.float_attrs.all():
            record = {
                "name": atr.name,
                "type": "float",
                "low value": atr.low_value,
                "high_value": atr.high_value
            }
            data.append(record)
        for atr in car_type.char_attrs.all():
            record = {
                "name": atr.name,
                "type": "char",
                "values": atr.values,
            }
            data.append(record)
        for atr in car_type.bool_attrs.all():
            record = {
                "name": atr.name,
                "type": "bool",
                "value": atr.value,
            }
            data.append(record)
        return JsonResponse(data, safe=False)

    @staticmethod
    def post(request):
        car_type = get_object_or_404(CarType.objects.all(), name=request.data.get("car type"))
        type = request.data.get("attr type")
        if type == "float":
            attribute = FloatAttribute(name=request.data.get("name"), low_value=request.data.get("low value"),
                                       high_value=request.data.get("high value"), car_type=car_type)
            result = check(get_object_or_404(StFloatAttribute.objects.all(), name=request.data.get("name")),
                           attribute, "float")
        elif type == "char":
            attribute = CharAttribute(name=request.data.get("name"), values=request.data.get("values") + ", ", car_type=car_type)
            result = check(get_object_or_404(StCharAttribute.objects.all(), name=request.data.get("name")),
                           attribute, "char")
        elif type == "bool":
            attribute = BoolAttribute(name=request.data.get("name"), value=request.data.get("value") + ", ", car_type=car_type)
            result = check(get_object_or_404(StBoolAttribute.objects.all(), name=request.data.get("name")),
                           attribute, "bool")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if result:
            attribute.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

    @staticmethod
    def put(request, name):
        car_type = get_object_or_404(CarType.objects.all(), name=request.data.get("car type"))
        type = request.data.get("attr type")
        if type == "float":
            attribute = get_object_or_404(car_type.float_attrs.all(), name=name)
            attribute.low_value = request.data.get("low value")
            attribute.high_value = request.data.get("high value")
            result = check(get_object_or_404(StFloatAttribute.objects.all(), name=name),
                           attribute, "float")
        elif type == "char":
            attribute = get_object_or_404(car_type.char_attrs.all(), name=name)
            attribute.values = request.data.get("values") + ", "
            result = check(get_object_or_404(StCharAttribute.objects.all(), name=name),
                           attribute, "char")
        elif type == "bool":
            attribute = get_object_or_404(car_type.bool_attrs.all(), name=name)
            attribute.value = request.data.get("value") + ", "
            result = check(get_object_or_404(StBoolAttribute.objects.all(), name=name),
                           attribute, "bool")
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if result:
            attribute.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_409_CONFLICT)

    @staticmethod
    def delete(request, name):
        car_type = get_object_or_404(CarType.objects.all(), name=request.data.get("car type"))
        type = request.data.get("attr type")
        if type == "float":
            attribute = get_object_or_404(car_type.float_attrs.all(), name=name)
        elif type == "char":
            attribute = get_object_or_404(car_type.char_attrs.all(), name=name)
        elif type == "bool":
            attribute = get_object_or_404(car_type.bool_attrs.all(), name=name)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        attribute.delete()
        return Response(status=status.HTTP_200_OK)

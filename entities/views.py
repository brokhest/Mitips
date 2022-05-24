from django.shortcuts import render
from rest_framework.views import APIView
from .models import Entity
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse
from .analizer import analyze
# Create your views here.


class EntityAPI(APIView):

    @staticmethod
    def get(request):
        data = []
        for entity in Entity.objects.all():
            response = {
                "name": entity.name,
                "data": entity.description,
                "car type": entity.car_type
            }
            data.append(response)
        return JsonResponse(data=data, safe=False)

    @staticmethod
    def post(request):
        # entity = Entity(name=request.data.get("name"), description=request.data.get("data"))
        entity = Entity(description=request.data)
        data = analyze(entity)
        if data == 0:
            return Response(data={
                "result": "no valid attributes given"
            })
        if data == 1:
            return Response(data={
                "result": "no matches"
            })
        if data == 2:
            return Response(data={
                "result": "integrity is not kept"
            })
        entity.save()
        return Response(data=data, status=status.HTTP_201_CREATED)


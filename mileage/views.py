from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.response import Response


# DRF FBV 방식
@api_view()
def hello_world_drf(request):
    return Response({'msg': 'hello_world!!!'})


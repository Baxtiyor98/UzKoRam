from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from app.serializer import *


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['get']


class MurojatView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Murojat.objects.all()
    serializer_class = MurojatSerializer

class YuridikView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Yuridik.objects.all()
    serializer_class = YuridikSerializer


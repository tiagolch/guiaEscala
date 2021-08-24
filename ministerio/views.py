from django.shortcuts import render
from rest_framework import viewsets
from .models import Ministerio, Funcao
from .serializers import MinisterioSerializer, FuncaoSerializer


class MinisterioViewSet(viewsets.ModelViewSet):
    queryset = Ministerio.objects.all()
    serializer_class = MinisterioSerializer


class FuncaoViewSet(viewsets.ModelViewSet):
    queryset = Funcao.objects.all()
    serializer_class = FuncaoSerializer
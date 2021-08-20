from django.shortcuts import render
from rest_framework import viewsets
from .models import Escala, Evento
from .serializers import EscalaSerializer, EventoSerializer


class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    


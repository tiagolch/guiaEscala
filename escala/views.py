from django.shortcuts import render,redirect, get_object_or_404
# from django.contrib.auth.models import User
from account.models import User
from rest_framework import viewsets
from .models import Escala, Evento
from .serializers import EscalaSerializer, EventoSerializer


class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    
def MinhaEscalaView(request):
    usuario = get_object_or_404(User, pk=request.user.id)
    resultado = Escala.objects.filter(nome=usuario)

    context = {
        'escala': resultado,
    }
    return render(request, 'minhaescala.html', context)

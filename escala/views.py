from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from datetime import date, timedelta
from account.models import User
from rest_framework import viewsets

from ministerio.models import Ministerio
from .models import Escala, Evento
from .serializers import EscalaSerializer, EventoSerializer


class EscalaViewSet(viewsets.ModelViewSet):
    queryset = Escala.objects.all()
    serializer_class = EscalaSerializer


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

    
@login_required() 
def MinhaEscalaView(request):
    usuario = get_object_or_404(User, pk=request.user.id)
    hoje = date.today()
    if usuario:
        resultado = Escala.objects.filter(nome=usuario, data__month=str(hoje.month))

        context = {
            'escala': resultado,
        }
        return render(request, 'minhaescala.html', context)


@login_required() 
def EscalaView(request):
    busca = request.GET.get('buscar')
    if busca:
        result = Escala.objects.filter(nome__icontains=busca, funcao__icontains=busca)
        paginator = Paginator(result, 50)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        result = {
            'core': posts
        }
    hoje = date.today()
    resultado = Escala.objects.filter(data__month=str(hoje.month))
    print([resultado])


    context = {
        'escala': resultado,
    }
    return render(request, 'escala.html', context)

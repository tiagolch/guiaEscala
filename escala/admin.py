import django
from django.contrib import admin
from django.contrib import auth
from django.http import request
from .models import Evento, Escala, MinhaEscala


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = [
        'nome_evento',
        'getUltima_alteracao'
    ]
    search_fields = [
        'nome_evento',
        'getUltima_alteracao',
    ]


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = [
        'responsavel',
        'datas',
        'funcao',
        'evento'
    ]
    list_filter = [
        'funcao',
        'evento',
        'data',
        'nome'
    ]
    autocomplete_fields = [
        'nome',
        'funcao',
        'evento',
    ]


@admin.register(MinhaEscala)
class MinhaEscalaAdmin(admin.ModelAdmin):
    list_display = [
        'datas',
        'funcao',
        'evento'
    ]
    list_filter = [
        'evento',
        'data',
    ]
    autocomplete_fields = [
        'nome',
        'funcao',
        'evento',
    ]
    ordering = ['data']

    def get_queryset(self, request):
        user = request.user
        qs = super(MinhaEscalaAdmin, self).get_queryset(request)
        qs = qs.filter(nome=user)
        return qs
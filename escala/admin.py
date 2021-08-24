from django.contrib import admin
from .models import Evento, Escala


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome_evento',
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
    search_fields = [
        'nome',
        'evento',
        'funcao'
    ]

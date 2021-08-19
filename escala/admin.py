from django.contrib import admin
from .models import Evento, Escala


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome_evento',
                    'ultima_alteracao'
                    ]


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['nome',
                    'datas',
                    'funcao',
                    'evento'
                    ]
